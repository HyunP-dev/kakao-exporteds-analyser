from __future__ import annotations
from collections import Counter
from operator import attrgetter
from tkinter import filedialog

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

import pandas as pd
import plotly.express as px

from toolkit.parser import *
import design.mainform


class SendersViewItem(QTreeWidgetItem):
    def __lt__(self, other: SendersViewItem):
        return int(self.text(1)) < int(other.text(1))


class MainWindow(QMainWindow, design.mainform.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.htmls = {}
        self.loadAction.triggered.connect(self.load)
        self.resultCmbBox.currentTextChanged.connect(lambda text: self.resultView.setHtml(self.htmls[text]))

    def load(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        self.chatsView.clear()
        self.sendersView.clear()

        model = self.chatsView.model()
        with open(path, encoding="UTF-8") as f:
            lines = list(map(lambda line: line[:-1], f.readlines()))

        messages = []
        nicknames = Counter()
        for data in iterate(lines[3:]):
            match data:
                case data if isinstance(data, datetime.date) or isinstance(data, str):
                    item = QTreeWidgetItem()
                    item.setText(0, str(data))
                    self.chatsView.addTopLevelItem(item)
                    item.setFirstColumnSpanned(True)
                case Message():
                    item = QTreeWidgetItem()
                    nicknames[data.nickname] += 1
                    item.setText(0, data.nickname)
                    item.setText(1, data.timestamp.strftime("%p %I:%M"))
                    item.setText(2, data.content.replace("\n", " "))
                    self.chatsView.addTopLevelItem(item)
                    messages.append(data)
        
        for nickname in nicknames:
            item = SendersViewItem()
            item.setText(0, nickname)
            item.setText(1, nicknames.get(nickname).__str__())
            self.sendersView.addTopLevelItem(item)

        df = pd.DataFrame(messages)
        htmls = {
            "채팅방의 활성 시간 분석 결과": px.histogram(df.timestamp, x="timestamp").to_html(include_plotlyjs='cdn'),
            "유저별 활동 시간 분석 결과": px.histogram(df.groupby("nickname").timestamp.apply(lambda series: series.map(attrgetter("hour"))).to_frame().reset_index(), color="nickname", x="timestamp").to_html(include_plotlyjs='cdn'),
            "대화 수 상위 10명의 대화 비율 분석 결과": px.pie(df.value_counts("nickname").nlargest(10).to_frame().reset_index(), "nickname", "count", title="대화 수 상위 10명의 대화 비율").to_html(include_plotlyjs='cdn')
        }
        self.htmls = htmls

        self.resultView.setHtml(htmls[self.resultCmbBox.currentText()])


if __name__ == "__main__":
    app = QApplication()
    form = MainWindow()
    form.show()
    app.exec()
