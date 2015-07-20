# -*- coding:utf-8 -*-
from PyQt5.QtCore import QRect, QObject


class Brush(QObject):
    def mousePress(self, painter, pos):
        return self.mouseMove(painter, pos, pos)

    def mouseMove(self, painter, pos, lastPos):
        rad = painter.pen().width() // 2 + 1
        boundingRect = QRect(lastPos, pos).normalized().adjusted(-rad, -rad, +rad, +rad)
        painter.drawLine(lastPos, pos)
        # painter.restore()
        return boundingRect

    def mouseRelease(self, painter, pos, lastPos):
        return QRect(0, 0, 0, 0)
