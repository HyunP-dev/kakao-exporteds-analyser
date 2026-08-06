from __future__ import annotations

from collections import Counter
from operator import attrgetter

import pandas as pd
import plotly.express as px
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# from toolkit.legacy_parser import *
from kakao_exporteds_analyser.model.chatlogsmodel import ChatLogsModel
from kakao_exporteds_analyser.toolkit.parser import *
from kakao_exporteds_analyser.widget.detailview import DetailView


class SendersViewItem(QTreeWidgetItem):
    def __lt__(self, other: SendersViewItem):
        return int(self.text(1)) < int(other.text(1))


# class MainWindow(QMainWindow, design.mainform.Ui_MainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)

#         self.htmls = {}
#         self.loadAction.triggered.connect(self.load)
#         self.resultCmbBox.currentTextChanged.connect(
#             lambda text: self.resultView.setHtml(self.htmls[text])
#         )

#     def load(self):
#         path, _ = QFileDialog.getOpenFileName(None, "파일 선택", "", "All Files (*)")
#         print(path)
#         if not path:
#             return
#         self.chatsView.clear()
#         self.sendersView.clear()

#         model = self.chatsView.model()
#         with open(path, encoding="utf-8-sig") as f:
#             text = f.read()


#         # messages = []
#         # nicknames = Counter()
#         # for data in Parser.parse(text):
#         #     match data:
#         #         # case data if isinstance(data, datetime.date) or isinstance(data, str):
#         #         #     item = QTreeWidgetItem()
#         #         #     item.setText(0, str(data))
#         #         #     self.chatsView.addTopLevelItem(item)
#         #         #     item.setFirstColumnSpanned(True)
#         #         case Message():
#         #             item = QTreeWidgetItem()
#         #             nicknames[data.nickname] += 1
#         #             item.setText(1, data.nickname)
#         #             item.setText(0, data.timestamp.strftime("%Y-%m-%d %p %I:%M"))
#         #             item.setText(2, data.content.replace("\n", " "))
#         #             self.chatsView.addTopLevelItem(item)
#         #             messages.append(data)
#         #         case Event():
#         #             item = QTreeWidgetItem()
#         #             if data.timestamp:
#         #                 item.setText(0, data.timestamp.strftime("%Y-%m-%d %p %I:%M"))
#         #             item.setText(2, data.content.replace("\n", " "))
#         #             self.chatsView.addTopLevelItem(item)


#         # for nickname in nicknames:
#         #     item = SendersViewItem()
#         #     item.setText(0, nickname)
#         #     item.setText(1, nicknames.get(nickname).__str__())
#         #     self.sendersView.addTopLevelItem(item)

#         df = pd.DataFrame(messages)
#         htmls = {
#             "채팅방의 활성 시간 분석 결과": px.histogram(
#                 df.timestamp, x="timestamp"
#             ).to_html(include_plotlyjs="cdn"),
#             "유저별 활동 시간 분석 결과": px.histogram(
#                 df.groupby("nickname")
#                 .timestamp.apply(lambda series: series.map(attrgetter("hour")))
#                 .to_frame()
#                 .reset_index(),
#                 color="nickname",
#                 x="timestamp",
#             ).to_html(include_plotlyjs="cdn"),
#             "대화 수 상위 10명의 대화 비율 분석 결과": px.pie(
#                 df.value_counts("nickname").nlargest(10).to_frame().reset_index(),
#                 "nickname",
#                 "count",
#                 title="대화 수 상위 10명의 대화 비율",
#             ).to_html(include_plotlyjs="cdn"),
#         }
#         self.htmls = htmls

#         self.resultView.setHtml(htmls[self.resultCmbBox.currentText()])


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.logs = []
        self.chat_view = QTreeView()
        self.chat_view.setUniformRowHeights(True)
        self.chat_view.setRootIsDecorated(False)
        self.chat_view.setModel(ChatLogsModel([]))


        users_dock = QDockWidget("대화상대", self)
        users_view = QTreeView()
        users_view.setUniformRowHeights(True)
        users_view.setRootIsDecorated(False)
        users_dock.setWidget(users_view)
        self.users_view = users_view

        detail_dock = QDockWidget("상세정보", self)
        self.detail_view = DetailView()
        detail_dock.setWidget(self.detail_view)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, users_dock)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, detail_dock)

        self.chat_view.doubleClicked.connect(self.on_chat_view_doubleClicked)
        self.setCentralWidget(self.chat_view)

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
        for (nickname, count) in counter.most_common():
            users_model.appendRow([QStandardItem(nickname), QStandardItem(str(count))])

        self.users_view.setModel(users_model)
        

    @Slot(QModelIndex)
    def on_chat_view_doubleClicked(self, index: QModelIndex):
        nickname_index = index.model().index(index.row(), 1)
        nickname = nickname_index.data(Qt.ItemDataRole.DisplayRole)
        self.detail_view.open(self.logs, nickname)


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("Fusion")
    form = MainWindow()
    form.show()
    app.exec()
