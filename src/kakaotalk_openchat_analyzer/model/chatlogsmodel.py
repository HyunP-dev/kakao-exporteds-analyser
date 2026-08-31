from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from ..toolkit.parser import *


class ChatLogsModel(QAbstractTableModel):
    HEADERS = ("보낸 시간", "닉네임", "메시지")

    class Role:
        EntryRole = Qt.ItemDataRole.UserRole + 1


    def __init__(self, logs: list[Message | Event]):
        super().__init__()
        self.logs = logs

    def rowCount(self, parent):
        return len(self.logs)

    def columnCount(self, parent):
        return len(self.HEADERS)

    def data(self, index: QModelIndex, role):
        if role == Qt.ItemDataRole.DisplayRole:
            log = self.logs[index.row()]
            match log:
                case Message():
                    return (
                        log.timestamp.strftime("%Y-%m-%d %p %I:%M"),
                        log.nickname,
                        log.content.replace("\n", " "),
                    )[index.column()]
                case Event():
                    return (
                        log.timestamp.strftime("%Y-%m-%d %p %I:%M")
                        if log.timestamp
                        else "",
                        "",
                        log.content.replace("\n", " "),
                    )[index.column()]

        if role == ChatLogsModel.Role.EntryRole:
            return self.logs[index.row()]


    def headerData(self, section, orientation, role):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
        ):
            return self.HEADERS[section]
