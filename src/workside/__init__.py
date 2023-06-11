"""NEW SCRIPT"""
#  Copyright (c) 2023 Asger Jon Vistisen
#  MIT Licence
from __future__ import annotations

from icecream import ic

from ._corewidget import CoreWidget
from ._label import Label
from ._listwidget import ListedWidget
from ._logwidget import LogWidget

from ._basewindow import BaseWindow
from ._layoutwindow import LayoutWindow
from ._inputwindow import InputWindow
from ._mainwindow import MainWindow

ic.configureOutput(includeContext=True)
