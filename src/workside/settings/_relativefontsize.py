"""RelativeFontSize subclasses FontSize to provide a size relative to the
present viewport."""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import QRect, QRectF, QSize, QSizeF
from PySide6.QtGui import QPainter, QFont
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.core import maybe
from worktoy.parsing import maybeType, extractArg
from worktoy.stringtools import stringList
from worktoy.typetools import CallMeMaybe

from workside.settings import FontSize

ic.configureOutput(includeContext=True)


class RelativeFontSize(FontSize):
  """RelativeFontSize subclasses FontSize to provide a size relative to the
  present viewport. By default, a scale multiplier of 30 is used such that
  an instance with base size 12 will have actual size 12 on a viewport of
  360 pixels on its longest dimension.
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, size: int = None, scale: float | int = None) -> None:
    _size360 = maybe(size, 12)
    if isinstance(_size360, (int, float)):
      self._size360 = int(_size360)
    else:
      raise TypeError
    _scale = maybe(scale, 30)
    if isinstance(_scale, (int, float)):
      self._scale = _scale
    else:
      raise TypeError
    FontSize.__init__(self, _size360)

  def viewPort2Font(self, font: QFont, viewPort: QRectF) -> QFont:
    """Adjusts font size of the given painter relative to viewport"""
    width = viewPort.width()
    height = viewPort.height()
    font.setPointSize(int(max(width, height) / self._scale))
    return font

  def applyPainter(self, painter: QPainter) -> QPainter:
    """Adjusts font size of the given painter relative to viewport"""
    painter.setFont(self.viewPort2Font(painter.font(), painter.viewport()))
    return painter

  def applyWidget(self, widget: QWidget) -> QWidget:
    """Adjusts font size of the given widget relative to viewport"""
    viewPort = widget.visibleRegion().boundingRect().toRectF()
    widget.setFont(self.viewPort2Font(widget.font(), viewPort))
    return widget
