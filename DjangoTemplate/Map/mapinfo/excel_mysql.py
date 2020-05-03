import xlrd
from datetime import date, datetime
import pymysql
import xlrd

from xlrd import xldate_as_tuple
import datetime

db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    db='gp1djangotemplate',
    port=3306,
    charset='utf8'
)
cursor = db.cursor()
ExcelFile = xlrd.open_workbook(r'G:\PycharmProject\DjangoTemplate\Map\mapinfo\dataset\map_info.xlsx')
sheet = ExcelFile.sheet_by_index(0)

for i in range(1, sheet.nrows):
    name = sheet.cell(i, 0).value
    lng = sheet.cell(i, 1).value
    lat = sheet.cell(i, 2).value
    is_open = 1 if sheet.cell(i, 3).value == "是" else 0
    time_value = ""
    if sheet.cell(i, 4).ctype==3:
        date = xldate_as_tuple(sheet.cell(i,4).value, 0)
        time_value = datetime.datetime(*date).date()
    open_time = time_value if time_value else 0
    note = sheet.cell(i, 5).value.encode('UTF-8') if sheet.cell(i, 5).value else "无备注"
    cursor.execute("insert into map_amapinfo(name,lng, lat, is_open,open_time,note) values (%s,%s,%s,%s,%s,%s)",
                   (name,lng, lat, is_open, open_time, note))

cursor.close()
db.commit()
db.close()

# 重新建立数据库连接`
db = pymysql.connect(
    host='localhost',
    user='root',
    passwd='123456',
    db='gp1djangotemplate',
    port=3306,
    charset='utf8'
)
cursor = db.cursor()
# 查询数据库并打印内容
cursor.execute('''select * from map_amapinfo''')
results = cursor.fetchall()
for row in results:
    print(row)
# 关闭
cursor.close()
db.commit()
db.close()
