# -*- coding:utf-8 -*-
import os
from PyQt5.QtWidgets import (
    QMainWindow, QScrollArea,
    QFileDialog, QColorDialog,
    QMessageBox,
)
from .paintarea import PaintArea
from .newimagedialog import NewImageDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("pypaint")

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction("New").triggered.connect(self.newImage)
        fileMenu.addAction("Open...").triggered.connect(self.openImage)
        fileMenu.addAction("Save As...").triggered.connect(self.saveAs)

        brushMenu = menubar.addMenu('Brush')
        brushMenu.addAction('Color').triggered.connect(self.showColorDialog)

        self.paintArea = PaintArea(self)
        scrollArea = QScrollArea()
        # scrollArea.setBackgroundRole(QPalette.Dark)
        scrollArea.setWidget(self.paintArea)
        self.setCentralWidget(scrollArea)
        self.resize(600, 500)

    def newImage(self):
        (width, height), ok = NewImageDialog.getSize(self)
        if ok:
            self.paintArea.newImage(width, height)
            self.paintArea.adjustSize()

    def openImage(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image File")
        if filename:
            if not self.paintArea.openImage(filename):
                QMessageBox.information(self, "pypaint", "Cannot load {}.".format(filename))
            self.paintArea.adjustSize()

    def saveAs(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save As", "")
        if not filename:
            return False
        else:
            root, ext = os.path.splitext(filename)
            if not ext:
                ext = ".png"
                filename += ext
            return self.paintArea.saveImage(filename, ext[1:])

    def showColorDialog(self):
        color = QColorDialog().getColor()
        if color.isValid():
            self.paintArea.color = color
