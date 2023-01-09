import sys
import os
from PyQt5.QtGui import QGuiApplication
from PyQt5.QQmlApplicationEngine import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow


# 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

QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
sys.exit(app.exec())