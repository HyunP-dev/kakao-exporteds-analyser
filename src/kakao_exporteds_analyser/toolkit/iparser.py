import datetime
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import NewType

Header = NewType("Header", str)
# Event = NewType("Event", str)


@dataclass
class Message:
    timestamp: datetime.datetime
    nickname: str
    content: str

@dataclass
class Event:
    timestamp: datetime.datetime
    nickname: str | None
    content: str

class IParser(ABC):
    @staticmethod
    @abstractmethod
    def parse(text: str):
        pass
