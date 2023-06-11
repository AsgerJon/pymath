"""FontSize represents resizing of fonts"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import Never
from warnings import warn

from PySide6.QtGui import QFont, QPainter
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from icecream import ic
from worktoy.core import maybe
from worktoy.waitaminute import ReadOnlyError

ic.configureOutput(includeContext=True)


class FontSize:
  """FontSize represents resizing of fonts.
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, size: int = None) -> None:
    size = maybe(size, 12)
    if isinstance(size, int):
      self._baseSize = size
    else:
      raise TypeError

  def _getBaseSize(self) -> int:
    """Getter-function for base font size."""
    if isinstance(self._baseSize, int):
      return self._baseSize
    raise TypeError

  def _noAcc(self, *_) -> Never:
    """Illegal setter/deleter"""
    raise ReadOnlyError('_baseSize')

  def applyFont(self, font: QFont) -> QFont:
    """Applies self to given font"""
    font.setPointSize(self._baseSize)
    return font

  size = property(_getBaseSize, _noAcc, _noAcc)
