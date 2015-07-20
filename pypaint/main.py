# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from .mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
