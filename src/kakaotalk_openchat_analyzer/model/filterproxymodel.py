import bisect

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import datetime

from kakaotalk_openchat_analyzer.model.chatlogsmodel import ChatLogsModel


class FilterProxyModel(QSortFilterProxyModel):
    def __init__(self):
        super().__init__()

        self.start = datetime.datetime.min
        self.end = datetime.datetime.max
        self.keyword = ""

        self.start_i = 0
        self.end_i = None

    def setFilterTimeRange(self, start=None, end=None):
        logs = self.sourceModel().logs

        if start:
            self.start = start
            self.start_i = bisect.bisect_left(
                logs, 
                start, 
                key=lambda log: log.timestamp if log.timestamp else datetime.datetime.min
            )

        if end:
            self.end = end
            self.end_i = bisect.bisect_right(
                logs, 
                end, 
                key=lambda log: log.timestamp if log.timestamp else datetime.datetime.max
            ) - 1

        self.invalidateFilter()

    def setFilterKeyword(self, keyword):
        self.keyword = keyword

        self.invalidateFilter()

    
    def filterAcceptsRow(self, source_row: int, source_parent: QModelIndex | QPersistentModelIndex) -> bool:
        logs = self.sourceModel().logs
        log = logs[source_row]

        if self.end_i is None:
            self.end_i = len(logs) - 1

        if not (self.start_i <= source_row <= self.end_i):
            return False

        return not (self.keyword and self.keyword not in log.content)