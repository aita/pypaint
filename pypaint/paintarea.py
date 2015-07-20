# -*- coding:utf-8 -*-
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QImage, QColor
from PyQt5.QtWidgets import QWidget
from .brush import Brush


class PaintArea(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StaticContents)
        self.setAttribute(Qt.WA_NoSystemBackground)

        self.newImage(400, 400)

        self.lastPos = None
        self.color = QColor()
        self.thickness = 3
        self.brush = Brush()

    def newImage(self, width, height):
        image = QImage(width, height, QImage.Format_RGB32)
        image.fill(Qt.white)
        self.setImage(image)

    def openImage(self, filename):
        image = QImage()
        if not image.load(filename):
            return False
        self.setImage(image)
        return True

    def setImage(self, image):
        self.image = image.convertToFormat(QImage.Format_RGB32)
        self.update()
        self.updateGeometry()

    def saveImage(self, filename, format):
        return self.image.save(filename, format)

    def sizeHint(self):
        return self.image.size()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(QPoint(0, 0), self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            painter = QPainter(self.image)
            self.setupPainter(painter)
            rect = self.brush.mousePress(painter, event.pos())
            self.update(rect)
            self.lastPos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.lastPos:
            painter = QPainter(self.image)
            self.setupPainter(painter)
            rect = self.brush.mouseMove(painter, event.pos(), self.lastPos)
            self.update(rect)
            self.lastPos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.lastPos:
            painter = QPainter(self.image)
            self.setupPainter(painter)
            rect = self.brush.mouseRelease(painter, event.pos(), self.lastPos)
            self.update(rect)
            self.lastPos = None

    def setupPainter(self, painter):
        painter.setRenderHint(QPainter.Antialiasing, False)
        painter.setPen(QPen(self.color, self.thickness, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
