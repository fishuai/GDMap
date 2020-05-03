from Map.models import AMapInfo
import pymysql
import xlrd

from xlutils.copy import copy


def getLocation():
    lng_list = list(AMapInfo.objects.values('lng'))
    lng_key_list = []
    for lng_dict in lng_list:
        lng_key_list.append(list(lng_dict.values()))

    lat_list = list(AMapInfo.objects.values('lat'))
    lat_key_list = []
    for lat_dict in lat_list:
        lat_key_list.append(list(lat_dict.values()))

    location = []

    for i in range(len(lng_key_list)):
        lng = lng_key_list[i][0]
        lat = lat_key_list[i][0]
        location.append([lng, lat])

    return location


def getIsOpen():
    is_open_list = list(AMapInfo.objects.values('is_open'))
    is_open_key_list = []
    for is_open_dict in is_open_list:
        is_open_key_list.append(list(is_open_dict.values()))

    is_open = []
    for i in range(len(is_open_key_list)):
        is_open.append(is_open_key_list[i][0])

    return is_open


def getOtherInfo():
    name_list = list(AMapInfo.objects.values('name'))
    name = []
    for name_dict in name_list:
        name.append(list(name_dict.values()))

    open_time_list = list(AMapInfo.objects.values('open_time'))
    open_time = []
    for open_time_dict in open_time_list:
        open_time.append(list(open_time_dict.values()))

    note_list = list(AMapInfo.objects.values('note'))
    note = []
    for note_dict in note_list:
        note.append(list(note_dict.values()))

    return name, open_time, note


def changeDataBaseById(id):
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='gp1djangotemplate',
        port=3306,
        charset='utf8',
    )
    cursor = db.cursor()
    # cursor.execute('''select convert(int,'123')''')
    cursor.execute("SELECT is_open FROM map_amapinfo WHERE id=%s" % id) + 0
    oldstate = cursor.fetchall()[0][0]
    # print("旧状态：", oldstate)
    newstate = (oldstate + 1) % 2
    cursor.execute("UPDATE map_amapinfo SET is_open=%s WHERE id=%s" % (newstate, id))
    # print("新状态：", newstate)
    cursor.execute('''select * from map_amapinfo''')
    cursor.close()
    db.commit()
    db.close()
    print("修改database完毕")


def changeExcelById(id):
    ExcelFile = xlrd.open_workbook(r'G:\PycharmProject\DjangoTemplate\Map\mapinfo\dataset\map_info.xlsx')
    sheet = ExcelFile.sheet_by_index(0)
    oldstate = sheet.cell(id, 3).value
    # print(oldstate)
    if oldstate == "是":
        newstate = "否"
    elif oldstate == "否":
        newstate = "是"
    # print(newstate)

    wb = copy(ExcelFile)
    ws = wb.get_sheet(0)
    ws.write(id, 3, newstate)

    wb.save('G:\PycharmProject\DjangoTemplate\Map\mapinfo\dataset\map_info.xlsx')  # 保存文件

    print("修改excel完毕")
