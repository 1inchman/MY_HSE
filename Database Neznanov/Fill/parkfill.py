# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector

# import json
#
# with open("park.json") as file:
#     data = json.load(file)
#
# df = pd.DataFrame(columns=('distr', 'address', 'flagw', 'flacg', 'flags', 'latitude', 'longitude', 'name'))
#
#
# for i in range(len(data)):
#     layer = data[i]
#     layer = layer['Cells']
#     if isinstance(layer['geoData']['coordinates'][0][0][0], (int, float)):
#         df.loc[i] = [layer['District'][0], layer['Location'], layer['HasWater'], layer['HasPlayground'],
#                      layer['HasSportground'], layer['geoData']['coordinates'][0][0][0],
#                      layer['geoData']['coordinates'][0][0][1], layer['CommonName']]
#     else:
#         df.loc[i] = [layer['District'][0], layer['Location'], layer['HasWater'], layer['HasPlayground'],
#                      layer['HasSportground'], layer['geoData']['coordinates'][0][0][0][0],
#                      layer['geoData']['coordinates'][0][0][0][1], layer['CommonName']]
#
# print df.head()
#
# # writer = pd.ExcelWriter('parksxl.xls')
# # df.to_excel(writer, 'parksxl')
# df.to_csv('parks.csv', sep=',', encoding='utf-8')

data = pd.read_csv('parks.csv')

data['flagw'] = data['flagw'].str.replace('да', '1')
data['flagw'] = data['flagw'].str.replace('нет', '0')
data['flacg'] = data['flacg'].str.replace('да', '1')
data['flacg'] = data['flacg'].str.replace('нет', '0')
data['flags'] = data['flags'].str.replace('да', '1')
data['flags'] = data['flags'].str.replace('нет', '0')
data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')

cycles = len(data)
cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO park "
         "(distid, fullname, address, flagwater, flagchildarea, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s)")
for i in range(1, cycles, 1):
    selectquery = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectquery)
    st = cursor.fetchall()
    st = st[0][0]
    data_query = (st, data['name'][i], data['address'][i], data['flagw'][i], data['flacg'][i], float(data['latitude'][i]), float(data['longitude'][i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()



