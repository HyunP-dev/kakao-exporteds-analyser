from __future__ import annotations

import os
from collections import Counter
from operator import attrgetter

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from kakao_exporteds_analyser.model.chatlogsmodel import ChatLogsModel
from kakao_exporteds_analyser.toolkit.parser import *
from kakao_exporteds_analyser.widget.detailview import DetailView
from kakao_exporteds_analyser.widget.filterwidget import *


class MainHeader(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("KakaoTalk Openchat Analyser")
        self.setObjectName("MainHeader")
        self.setMaximumHeight(48)

class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MenuBar")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setMaximumHeight(32)
        self.setLayout(QHBoxLayout())
        self.layout().addWidget(QPushButton("로그 불러오기"))
        self.layout().setContentsMargins(8, 2, 2, 2)
        self.layout().addItem(QSpacerItem(0, 0, hData=QSizePolicy.Policy.Expanding))
        

class MainWindow(QMainWindow):#
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().setContentsMargins(0,0,0,0)
        central_widget.layout().setSpacing(0)

        central_widget.layout().addWidget(MainHeader())
        central_widget.layout().addWidget(MenuBar())

        self.setCentralWidget(central_widget)

        main_splitter = QSplitter()
        central_widget.layout().addWidget(main_splitter)
        main_splitter.addWidget(left_tabs := QTabWidget())
        main_splitter.addWidget(center_splitter := QSplitter(Qt.Orientation.Vertical))
        main_splitter.addWidget(right_tabs := QTabWidget())
        main_splitter.setSizes([250, 800, 400])

        self.setStatusBar(QStatusBar())
        self.statusBar().addWidget(status_label := QLabel("  총 레코드 수:  "))
        self.status_label = status_label

        self.logs = []
        self.chat_view = QTreeView()
        self.chat_view.setUniformRowHeights(True)
        self.chat_view.setRootIsDecorated(False)
        self.chat_view.setModel(ChatLogsModel([]))

        upper_tabs = QTabWidget()
        upper_tabs.addTab(self.chat_view, "대화내역")
        center_splitter.addWidget(upper_tabs)

        lower_tabs = QTabWidget()
        lower_tabs.setStyleSheet("QTabWidget QWidget { border: none; }")
        lower_tabs.addTab(preview := QPlainTextEdit(), "미리보기")
        self.preview = preview
        self.preview.setReadOnly(True)

        center_splitter.addWidget(lower_tabs)

        center_splitter.setSizes([600, 360])

        users_view = QTreeView()
        users_view.setUniformRowHeights(True)
        users_view.setRootIsDecorated(False)
        self.users_view = users_view
        left_tabs.addTab(self.users_view, "대화상대")

        self.detail_view = DetailView()
        right_tabs.addTab(self.detail_view, "상세정보")

        self.chat_view.doubleClicked.connect(self.on_chat_view_doubleClicked)
        self.users_view.doubleClicked.connect(self.on_users_view_doubleClicked)
        self.users_view.setEditTriggers(self.users_view.EditTrigger.NoEditTriggers)

        self.detail_view.manager_view.doubleClicked.connect(self.on_event_doubleClicked)
        self.detail_view.inout_view.doubleClicked.connect(self.on_event_doubleClicked)

        self.load_chats()

    def load_chats(self):
        with open("KakaoTalkChats.txt") as f:
            text = f.read()

        self.logs = list(Parser.parse(text))
        logs = self.logs

        self.chat_view.setModel(ChatLogsModel(logs))

        users_model = QStandardItemModel()
        users_model.setHorizontalHeaderLabels(["닉네임", "메시지 수"])

        counter = Counter([log.nickname for log in logs if isinstance(log, Message)])
        for nickname, count in counter.most_common():
            users_model.appendRow([QStandardItem(nickname), QStandardItem(str(count))])

        self.users_view.setModel(users_model)
        self.status_label.setText(f"  총 레코드 수: {len(logs)}  ")

    @Slot(QModelIndex)
    def on_chat_view_doubleClicked(self, index: QModelIndex):
        timestamp_index = index.model().index(index.row(), 0)
        nickname_index = index.model().index(index.row(), 1)
        content_index = index.model().index(index.row(), 2)
        nickname = nickname_index.data(Qt.ItemDataRole.DisplayRole)
        timestamp = timestamp_index.data(Qt.ItemDataRole.DisplayRole)
        content = content_index.data(Qt.ItemDataRole.DisplayRole)
        self.detail_view.open(self.logs, nickname)

        self.preview.setPlainText(f"""
【 전송 시각 】
{timestamp}

【 보낸이 】
{nickname}

【 메시지 전문 】
{self.logs[index.row()].content}
""".strip())
        

    @Slot(QModelIndex)
    def on_users_view_doubleClicked(self, index: QModelIndex):
        nickname_index = index.model().index(index.row(), 0)
        nickname = nickname_index.data(Qt.ItemDataRole.DisplayRole)
        self.detail_view.open(self.logs, nickname)

    @Slot(QModelIndex)
    def on_event_doubleClicked(self, index: QModelIndex):
        idx = index.model().index(index.row(), 0).data(Qt.ItemDataRole.UserRole)
        log = self.logs[idx]
        self.chat_view.setCurrentIndex(self.chat_view.model().index(idx, 0))
        self.preview.setPlainText(f"""
【 전송 시각 】
{log.timestamp}

【 보낸이 】


【 메시지 전문 】
{log.content}
        """.strip())


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(0xf7, 0xf7, 0xf7))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Base, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Highlight, QColor(0x48, 0x77, 0xd7))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
    
    app.setPalette(palette)
    with open(os.path.dirname(__file__) + "/style/light.qss") as f:
        app.setStyleSheet(f.read())
    form = MainWindow()
    form.showMaximized()
    app.exec()
