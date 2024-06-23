import re
from typing import NewType

Header = NewType("Header", str)


def parse_header(line: str) -> Header | None:
    header = re.findall(r"\[.*\]\ \[오[전후] \d{1,2}:\d{1,2}\]\ ", line)
    return Header(header[0][:-1]) if header else None


def parse_nickname(header: Header) -> str:
    return re.split(r" \[오[전후] \d{1,2}:\d{1,2}\]", header)[0][1:-1]


def parse_timestamp(header: Header) -> str:
    return re.findall(r"\[오[전후] \d{1,2}:\d{1,2}\]", header)[0][1:-1]
