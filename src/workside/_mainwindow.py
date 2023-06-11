"""MainWindow"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import time
from typing import NoReturn

from icecream import ic

from workside import InputWindow, LogWidget

ic.configureOutput(includeContext=True)


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
    self.getBaseWidget().setLayout(self.getBaseLayout())
    self.setCentralWidget(self.getBaseWidget())

  def tellMe(self, msg: str) -> NoReturn:
    """Takes a log"""
    self._getLogWidget().tellMe(msg)

  def show(self, ) -> NoReturn:
    """Implementation"""
    self.setupWidgets()
    InputWindow.show(self)

  def debugFunc01(self) -> NoReturn:
    """omg"""

  def debugFunc02(self) -> NoReturn:
    """fuck you"""

  def debugFunc03(self) -> NoReturn:
    """omg"""

  def debugFunc04(self) -> NoReturn:
    """omg"""
