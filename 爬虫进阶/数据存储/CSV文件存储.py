# coding : utf-8
# 夏目&青一
# @name:CSV文件存储
# @time: 2023/3/6  9:45
import csv

with open('./data/CSV_text.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['011', 'xiaohua', 19])
