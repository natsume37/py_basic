from openpyxl import Workbook

# 新建工作簿
wb = Workbook()
# 选择默认的工作表
sheet = wb.active
# 给工作表重命名
sheet.title = '考勤统计表'

data = [
  ['姓名', '出勤天数', '迟到次数'],
  ['小贝', 20, 5],
  ['闻闻', 22, 0]
]

# 写入多行数据
for row in data:
  sheet.append(row)

# 保存 Excel 文件
wb.save('考勤统计.xlsx')