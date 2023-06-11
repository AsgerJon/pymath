"""The math module showcases how Python can implement various mathematical
operations"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

import os
import sys
import time
from typing import Any, NoReturn

from PySide6.QtWidgets import QApplication
from icecream import ic

from workside import MainWindow

ic.configureOutput(includeContext=True)


def tester00() -> NoReturn:
  """Hello world!"""
  for item in ['hello world', Any, NoReturn, os, sys, MainWindow,
               QApplication, time]:
    print(item)


def tester01() -> NoReturn:
  """MainWindow"""

  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.quit()
  sys.exit(app.exec())


if __name__ == '__main__':
  print('Started at: %s' % time.ctime())
  tester01()
  print('Ended at: %s' % time.ctime())
