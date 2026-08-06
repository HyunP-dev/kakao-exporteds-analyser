from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kakao_exporteds_analyser.toolkit.iparser import Event


class LabeledWidget(QWidget):
    def __init__(self, text, widget, parent=None):
        super().__init__()

        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.layout().addWidget(QLabel(text))
        self.layout().addWidget(widget)


class DetailView(QSplitter):
    def __init__(self, parent=None):
        super().__init__()
        self.setOrientation(Qt.Orientation.Vertical)

        self.summary_view = QTreeView()

        self.manager_view = QTreeView()
        self.manager_view.setRootIsDecorated(False)

        self.inout_view = QTreeView()
        self.inout_view.setRootIsDecorated(False)

        self.addWidget(LabeledWidget("개요", self.summary_view))
        self.addWidget(LabeledWidget("부방장 이력", self.manager_view))
        self.addWidget(LabeledWidget("입장·퇴장·강퇴 이력", self.inout_view))

    def open(self, logs: list, nickname: str):
        manager_model = QStandardItemModel()
        manager_model.setHorizontalHeaderLabels(["시각", "구분"])

        inout_model = QStandardItemModel()
        inout_model.setHorizontalHeaderLabels(["시각", "구분"])

        for log in logs:
            if not (hasattr(log, "nickname") and log.nickname == nickname):
                continue

            if "Event" in str(type(log)):
                print(log)

                if log.content.endswith("님이 들어왔습니다."):
                    inout_model.appendRow(
                        [
                            QStandardItem(log.timestamp.strftime("%Y-%m-%d %p %I:%M")),
                            QStandardItem("입장"),
                        ]
                    )
                if log.content.endswith("님이 나갔습니다."):
                    inout_model.appendRow(
                        [
                            QStandardItem(log.timestamp.strftime("%Y-%m-%d %p %I:%M")),
                            QStandardItem("퇴장"),
                        ]
                    )
                if log.content.endswith("님을 내보냈습니다."):
                    inout_model.appendRow(
                        [
                            QStandardItem(log.timestamp.strftime("%Y-%m-%d %p %I:%M")),
                            QStandardItem("강퇴"),
                        ]
                    )
                if log.content.endswith("님이 부방장이 되었습니다."):
                    manager_model.appendRow(
                        [
                            QStandardItem(log.timestamp.strftime("%Y-%m-%d %p %I:%M")),
                            QStandardItem("부방장 임명"),
                        ]
                    )
                if log.content.endswith("님이 부방장에서 해제되었습니다."):
                    manager_model.appendRow(
                        [
                            QStandardItem(log.timestamp.strftime("%Y-%m-%d %p %I:%M")),
                            QStandardItem("부방장 해제"),
                        ]
                    )
        self.inout_view.setModel(inout_model)
        self.manager_view.setModel(manager_model)
