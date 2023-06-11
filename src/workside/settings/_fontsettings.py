"""FontSettings is an abstract class allowing for adjusting the settings
relating to fonts"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from abc import abstractmethod

from PySide6.QtGui import QFont, QPainter
from PySide6.QtWidgets import QWidget
from icecream import ic

ic.configureOutput(includeContext=True)


class FontSettings:
  """FontSettings is an abstract class allowing for adjusting the settings
  relating to fonts
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, *args, **kwargs) -> None:
    pass

  @abstractmethod
  def applyFont(self, font: QFont) -> QFont:
    """Applies self to given font"""

  def applyPainter(self, painter: QPainter) -> QPainter:
    """Applies self to given painter"""
    painter.setFont(self.applyFont(painter.font()))
    return painter

  def applyWidget(self, widget: QWidget) -> QWidget:
    """Applies self to given widget"""
    widget.setFont(self.applyFont(widget.font()))
    return widget
