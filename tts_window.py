# App window setup.

# PyQt Tools.
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPainterPath, QRegion

# Setup window.
Form, Window = uic.loadUiType('ui\\TextToSpeechWindow.ui')

app = QApplication([])

window = Window()

form = Form()
form.setupUi(window)

# Remove window title bar.
window.setWindowFlag(Qt.FramelessWindowHint)

# Make rounded edges in window.
round_radius = 10.0

round_path = QPainterPath()
round_path.addRoundedRect(QRectF(window.rect()), round_radius, round_radius)

window_mask = QRegion(round_path.toFillPolygon().toPolygon())

window.setMask(window_mask)

# Window close, hide/show logic.
form.CloseWindow.clicked.connect(lambda: exit(0))
form.HideWindow.clicked.connect(lambda: window.showMinimized())

