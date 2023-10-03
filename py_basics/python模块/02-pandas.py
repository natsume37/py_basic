# coding:utf-8
# USER: 冷不丁
# @FILE_NAME: pandas
# @TIME: 2023/9/22 22:58

import pandas as pd

# print(pd.Series([2, 3, 4, 5, 6], index=[3,4,7,3,6]))

# print(pd.Series({'a': 2, 'b': 4, 'c': 6, 'd': 8}))

# s1 = pd.Series({'辣条': 14, '面包': 7, '可乐': 8, '烤肠': 10})
# s2 = pd.Series({'辣条': 20, '烤肠': 6, '可乐': 13, '面包': 3})
# print(s1 + s2)

# s1 = pd.Series({'辣条': 14, '面包': 7, '可乐': 8, '烤肠': 10})
# s2 = pd.Series({'辣条': 20, '面包': 3, '雪碧': 13, '泡面': 6})
# print(s1.add(s2, fill_value=0))  # fill_value 为数据缺失时的默认值

# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)
#
# df = pd.DataFrame({'辣条': [14, 20], '面包': [7, 3], '可乐': [8, 13], '烤肠': [10, 6]})
# print(df)

# data = {
#   '辣条': [14, 20],
#   '面包': [7, 3],
#   '可乐': [8, 13],
#   '烤肠': [10, 6]
# }
# df = pd.DataFrame(data, index=['2020-01-01', '2020-01-02'])
# print(df)

# df = pd.DataFrame({'辣条': [14, 20], '面包': [7, 3], '可乐': [8, 13], '烤肠': [10, 6]})
#
# print(df['可乐'])

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# data = {
#     '辣条': [14, 20],
#     '面包': [7, 3],
#     '可乐': [8, 13],
#     '烤肠': [10, 6]
# }
# df = pd.DataFrame(data, index=['2020-01-01', '2020-01-02'])
#
# # 新增
# df["新增列"] = [12, 18]
#
# # 删除
# df.drop("面包",axis=1, inplace=True)
#
# # 改
# df['烤肠'] = [99,33]
#
# # 查
# print(df[["烤肠", "辣条"]])
#
# print(df)

# data = {
#   '辣条': [14, 20, 12, 15, 17],
#   '面包': [7, 3, 8, 3, 9],
#   '可乐': [8, 13, 23, 12, 19],
#   '烤肠': [10, 6, 21, 24, 18]
# }
# df = pd.DataFrame(data, index=['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'])
# print(df.iloc[:3])

# df = pd.read_csv("data/数据.csv")
# grouped = df.groupby("团队").sum()
# data = grouped.loc[grouped["第一季度"] < grouped["总和"].mean(), "第一季度"]
# print(data)


df = pd.read_csv('https://media-zip1.baydn.com/storage_media_zip/srfeae/dc3fa2c70032c4f4dfd7d878d79eb4da.41767dfc9dd1646b2a9f71527db2125f.csv')

df["评分"] = df["评分"].str.replace("分","").astype('float')
df["评分"].fillna(df['评分'].mean().round(1),inplace=True)
print(df.head(10))
