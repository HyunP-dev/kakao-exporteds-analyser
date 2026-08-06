import datetime
import re

from .iparser import *


TIMESTAMP_REGEX_STR = r"\d{4}년 \d+월 \d+일 오[전후] \d+:\d+"

with open("KakaoTalkChats.txt") as f:
    lines = f.read().splitlines()



class Parser(IParser):
    def parse(text: str):
        lines = text.splitlines()

        logs = []
        is_logging = False
        for line in lines:
            #  삭제된 메시지
            if line == "메시지가 삭제되었습니다.":
                print(Event("메시지가 삭제되었습니다."))
                continue

            #  단순 날짜 표기
            # if re.fullmatch(TIMESTAMP_REGEX_STR, line):
            #     print(line)
            #     continue
        
            #  로그 시작
            if re.match("^" + TIMESTAMP_REGEX_STR + ", ", line):
                if is_logging:
                    is_logging = False
                    message = Message(timestamp, nickname, message_content)
                    logs.append(message)
        
        
                timestamp, content = line.split(", ", maxsplit=1)
                timestamp = timestamp.replace("오전", "AM").replace("오후", "PM")
                timestamp = datetime.datetime.strptime(timestamp, "%Y년 %m월 %d일 %p %I:%M")
        
                if line.endswith("님이 들어왔습니다."):
                    nickname = content.split("님이 ")[0]
                    print(timestamp, nickname)
                    continue

                if line.endswith("님이 나갔습니다."):
                    nickname = content.split("님이 ")[0]
                    print(timestamp, nickname, "퇴장")
                    continue

                if line.endswith("님을 내보냈습니다."):
                    nickname = content.split("님을 ")[0]
                    print(timestamp, nickname, "강퇴")
                    continue

                if line.endswith("님이 부방장이 되었습니다."):
                    nickname = content.split("님이 부방장")[0]
                    print(timestamp, nickname, "부방장")
                    continue

                if line.endswith("님이 부방장에서 해제되었습니다."):
                    nickname = content.split("님이 부방장")[0]
                    print(timestamp, nickname, "부방장 해제")
                    continue

                if " : " in content:
                    is_logging = True
                    nickname, message_content = content.split(" : ", maxsplit=1)
        
        
            #  로그 진행 중
            if not re.match("^" + TIMESTAMP_REGEX_STR + ", ", line) and is_logging:
                message_content += "\n" + line
                continue

        if is_logging:
            is_logging = False
            message = Message(timestamp, nickname, message_content)
            logs.append(message)
        
        yield from logs
        
        