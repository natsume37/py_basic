import re

print(re.findall('.+', 'abc\ndef\nghi'))  # ['abc', 'def', 'ghi']
print(re.findall('.+', 'abc\ndef\nghi', flags=re.DOTALL))  # ['abc\ndef\nghi']

# flags属性
# flags=re.DOTALL   让.匹配所有字符（正常情况下.不能匹配\n换行符）
# python的正则表达式在处理（）的时候有些许区别  （？:）
# 手机号脱敏

