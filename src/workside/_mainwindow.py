"""MainWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from typing import NoReturn

from workside import InputWindow, LogWidget


class MainWindow(InputWindow):
  """MainWindow
  #  Copyright (c) 2023 Asger Jon Vistisen
  #  MIT Licence"""

  def __init__(self, ) -> None:
    InputWindow.__init__(self)
    self.setMinimumWidth(640)
    self.setMinimumHeight(480)
    self._logWidget = None

  def _createLogWidget(self) -> NoReturn:
    """Creator-function for the log widget"""
    self._logWidget = LogWidget()

  def _getLogWidget(self) -> LogWidget:
    """Getter-function for the log widget"""
    if self._logWidget is None:
      self._createLogWidget()
      return self._getLogWidget()
    if isinstance(self._logWidget, LogWidget):
      return self._logWidget
    raise TypeError

  def setupWidgets(self) -> NoReturn:
    """Sets up the widgets"""
    self.getBaseLayout().addWidget(self._getLogWidget(), 0, 0)
