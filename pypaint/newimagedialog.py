# -*- coding:utf-8 -*-
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QDialog, QGridLayout, QLabel, QSpinBox, QDialogButtonBox



class NewImageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(250, 100)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel("width"), 1, 1)
        grid.addWidget(QLabel("height"), 2, 1)

        self.widthEdit = QSpinBox()
        self.widthEdit.setMaximum(10000)
        self.widthEdit.setValue(400)
        grid.addWidget(self.widthEdit, 1, 2)

        self.heightEdit = QSpinBox()
        self.heightEdit.setMaximum(10000)
        self.heightEdit.setValue(400)
        grid.addWidget(self.heightEdit, 2, 2)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        grid.addWidget(buttons, 3, 2)

    def size(self):
        return self.widthEdit.value(), self.heightEdit.value()

    @classmethod
    def getSize(cls, parent=None):
        dialog = cls(parent)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            return dialog.size(), True
        return (None, None), False
