from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class FilterRack(QFrame):
    def __init__(self):
        super().__init__()

        # self.setFrameShape(QFrame.Shape.StyledPanel)
        # self.setFrameShadow(QFrame.Shadow.Plain)
        self.setMinimumSize(QSize(32, 32))

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(QCheckBox())
        self.layout().addWidget(QLabel("날짜 필터"))
        self.layout().addItem(QSpacerItem(1, 1, hData=QSizePolicy.Policy.Expanding))


class FilterHeader(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(QLabel("필터"))
        self.layout().addItem(QSpacerItem(1, 1, hData=QSizePolicy.Policy.Expanding))
        self.layout().addWidget(QPushButton("날짜 필터"))
        self.layout().addWidget(QPushButton("키워드 필터"))
        self.layout().addWidget(QPushButton("유저 필터"))
        self.layout().setContentsMargins(0,0,0,0)


class FilterWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)

        
        self.layout().addWidget(FilterHeader())

        self.racks_layout = QVBoxLayout()
        self.racks_area = QScrollArea()
        

        self.racks_view = QWidget()
        self.racks_area.setWidget(self.racks_view)
        self.racks_area.setWidgetResizable(True)
        self.racks_view.setLayout(self.racks_layout)


        self.layout().addWidget(self.racks_area)

        self.racks_layout.addWidget(FilterRack())
        self.racks_layout.addWidget(FilterRack())
        self.racks_layout.setContentsMargins(0, 0, 0, 0)
        self.racks_layout.setSpacing(0)

        self.racks_layout.addItem(QSpacerItem(1, 1, vData=QSizePolicy.Policy.Expanding))
