# App window setup.

# PyQt Tools.
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainterPath, QRegion

# Better exit.
from sys import exit as _sys_exit

# Logs.
from tts_logs import *


# Tools loading logs.
logger.info('Libraries loaded.')

# Setup window.
Form, Window = uic.loadUiType('ui\\TextToSpeechWindow.ui')

app = QApplication([])

window = Window()

form = Form()
form.setupUi(window)

logger.info('Window setup was successfully!')

# Remove window title bar.
window.setWindowFlag(Qt.FramelessWindowHint)

logger.info('Window title bar removed.')

# Make rounded edges in window.
round_radius = 10.0

round_path = QPainterPath()
round_path.addRoundedRect(QRectF(window.rect()), round_radius, round_radius)

window_mask = QRegion(round_path.toFillPolygon().toPolygon())

window.setMask(window_mask)

logger.info('Window rounding edges was successfully!')

# Window close, hide/show logic.
form.CloseWindow.clicked.connect(lambda: [logger.info('Window closed.'), _sys_exit(0)])
form.HideWindow.clicked.connect(lambda: [logger.info('Window minimized.'), window.showMinimized()])

logger.info('Window close/hide/show logic connected!')

