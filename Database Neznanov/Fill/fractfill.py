# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector
import math

# import json
#
# with open("/Users/oneinchman/Downloads/Травматологические пункты.json") as file:
#     data = json.load(file)
#
# df = pd.DataFrame(columns=('distr', 'address', 'name', 'phone', 'head', 'latitude', 'longitude'))
#
#
# for i in range(len(data)):
#     layer = data[i]
#     layer = layer['Cells']
#
#     try:
#         df.loc[i] = [layer['ObjectAddress'][0]['District'],
#                      layer['ObjectAddress'][0]['Address'],
#                      layer['ShortName'],
#                      layer['ChiefPhone'][0]['ChiefPhone'][0],
#                      layer['ChiefName'],
#                      layer['geoData']['coordinates'][0][0],
#                      layer['geoData']['coordinates'][0][1]]
#     except:
#         print 'exception'
#
#
# print df.head()
#
# # writer = pd.ExcelWriter('parksxl.xls')
# # df.to_excel(writer, 'parksxl')
# df.to_csv('fracture.csv', sep=',', encoding='utf-8')

data = pd.read_csv('fracture.csv')

data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')

print data.head()

cycles = len(data)

cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO fracture "
         "(distid, barid, fullname, address, phonenumber, head, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

for i in range(1, cycles, 1):
    selectquery = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectquery)
    st = cursor.fetchall()
    st = st[0][0]
    selectcoords = ("SELECT id, lattitude, longitude from bar")
    cursor.execute(selectcoords)
    for aidi, lat, long in cursor:
        tmpid = aidi
        if 6378137 * math.acos(math.cos(math.radians(lat)) * math.cos(math.radians(data['latitude'][i])) * math.cos(
                        math.radians(long) -
                        math.radians(data['longitude'][i])) +
                                               math.sin(math.radians(lat)) * math.sin(
                                           math.radians(data['latitude'][i]))) <= 10000:
            break

    try:
        dump = cursor.fetchall()
    except:
        print 'exception'
    data_query = (st, tmpid, data['name'][i], data['address'][i], data['phone'][i], data['head'][i], float(data['latitude'][i]),
                  float(data['longitude'][i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()
