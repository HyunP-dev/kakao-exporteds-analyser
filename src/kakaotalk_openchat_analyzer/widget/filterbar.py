from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class DateTimeEdit(QDateTimeEdit):
    def __init__(self):
        super().__init__()
        self.setDisplayFormat("yyyy년 MM월 dd일 AP hh시 mm분")


class FilterBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())
        self.layout().setContentsMargins(8, 5, 2, 0)

        self.layout().addWidget(QLabel("범위"))
        self.layout().addWidget(startEdit := DateTimeEdit())
        self.layout().addWidget(QLabel(" ~ "))
        self.layout().addWidget(endEdit := DateTimeEdit())
        self.layout().addWidget(QLabel("    검색어"))
        self.layout().addWidget(keywordEdit := QLineEdit())

        self.startEdit = startEdit
        self.endEdit = endEdit
        self.keywordEdit = keywordEdit
        