import re
import datetime
from dataclasses import dataclass
from typing import NewType, Iterable, Generator

Header = NewType("Header", str)
Event = NewType("Event", str)

@dataclass
class Message(object):
    timestamp: datetime.datetime
    nickname: str
    content: str



def parse_header(line: str) -> Header | None:
    header = re.findall(r"\[.*\]\ \[오[전후] \d{1,2}:\d{1,2}\]\ ", line)
    return Header(header[0][:-1]) if header else None


def parse_nickname(header: Header) -> str:
    return re.split(r" \[오[전후] \d{1,2}:\d{1,2}\]", header)[0][1:-1]


def parse_timestamp(header: Header) -> str:
    return re.findall(r"\[오[전후] \d{1,2}:\d{1,2}\]", header)[0][1:-1]


def iterate(lines: Iterable[str]) -> Generator[Event | Message | datetime.date, None, None]:
    current_date = None
    buffer = None
    for line in lines:
        if line.startswith("----"):
            KOREAN_DATE_FORMAT = r"\d{4}년 \d{1,2}월 \d{1,2}일"
            date = map(int, re.findall(r"\d+", re.findall(KOREAN_DATE_FORMAT, line)[0]))
            date = datetime.date(*date)
            current_date = date
            if buffer:
                yield buffer
            yield current_date
            continue

        header = parse_header(line)
        if header is None and (line.endswith("님이 나갔습니다.") or line.endswith("부방장에서 해제되었습니다.") or line.endswith("들어왔습니다.")):
            if buffer:
                yield buffer
            yield Event(line)
            continue

        if header:
            if buffer is not None:
                yield buffer
            nickname = parse_nickname(header)
            timestamp = parse_timestamp(header).replace("오전", "AM").replace("오후", "PM")
            timestamp = datetime.datetime.strptime(f"{current_date} {timestamp}", "%Y-%m-%d %p %I:%M")
            msg = line[len(header) + 1:]
            buffer = Message(timestamp, nickname, msg)
            continue

        if header is None:
            buffer.content += "\n" + line
    if buffer:
        yield buffer
    