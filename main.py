from __future__ import annotations
from collections import Counter
from tkinter import filedialog

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

from toolkit.parser import *
import design.mainform


class SendersViewItem(QTreeWidgetItem):
    def __lt__(self, other: SendersViewItem):
        return int(self.text(1)) < int(other.text(1))


class MainWindow(QMainWindow, design.mainform.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loadAction.triggered.connect(self.load)

    def load(self):
        path = filedialog.askopenfilename()
        if not path:
            return
        self.chatsView.clear()
        self.sendersView.clear()

        with open(path, encoding="UTF-8") as f:
            lines = map(str.strip, f.readlines())
        nicknames = Counter()
        for line in lines:
            if line.startswith("----"):
                item = QTreeWidgetItem()
                item.setText(0, line)

                self.chatsView.addTopLevelItem(item)
                item.setFirstColumnSpanned(True)
                continue

            header = parse_header(line)
            if header:
                item = QTreeWidgetItem()
                nickname = parse_nickname(header)
                nicknames[nickname] += 1
                item.setText(0, nickname)
                item.setText(1, parse_timestamp(header))
                item.setText(2, line[len(header) + 1:])
                self.chatsView.addTopLevelItem(item)
        for nickname in nicknames:
            item = SendersViewItem()
            item.setText(0, nickname)
            item.setText(1, nicknames.get(nickname).__str__())
            self.sendersView.addTopLevelItem(item)


if __name__ == "__main__":
    app = QApplication()
    form = MainWindow()
    form.show()
    app.exec()
