import re

s = "abc123def456"
# 当你在字符串前加上 r 前缀时，Python 会将字符串中的反斜杠 \ 视为普通字符，而不是转义字符。
match = re.search(r"\d+", s)
if match:
    print(match.group(0))  # None（开头不是数字）
print(re.search(r"\d+", s))  # <Match '123'>
print(re.findall(r"\d+", s))  # ['123', '456']
