# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector
# import json
#
# with open("/Users/oneinchman/Downloads/Лыжные трассы города Москвы.json") as file:
#     dt = json.load(file)
#
# data = pd.DataFrame(columns=('distr', 'address', 'phone', 'hasrent', 'hastoilet', 'latitude', 'longitude'))
#
# for i in range(len(dt)):
#     layer = dt[i]
#     layer = layer['Cells']
#
#     data.loc[i] = [layer['District'],
#                  layer['Address'],
#                  layer['HelpPhone'],
#                  layer['ObjectHasEquipmentRental'],
#                  layer['ObjectHasToilet'],
#                  layer['SportZoneLatitudeWGS84'],
#                  layer['SportZoneLongitudeWGS84']]
# print data.head()
#
#
# data.to_csv('skitrack.csv', sep=',', encoding='utf-8')

data = pd.read_csv('skitrack.csv')

data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')
data['hasrent'] = data['hasrent'].str.replace('нет', '0')
data['hasrent'] = data['hasrent'].str.replace('да', '1')
data['hastoilet'] = data['hastoilet'].str.replace('нет', '0')
data['hastoilet'] = data['hastoilet'].str.replace('да', '1')

cycles = len(data)
cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO skitrack "
         "(distid, address, phonenumber, flagwc, flagrent, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s)")
for i in range(1, cycles, 1):
    selectquery = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectquery)
    st = cursor.fetchall()
    print st, data['distr'][i]
    st = st[0][0]
    try:
        data_query = (st, data['address'][i], data['phone'][i], data['hastoilet'][i],
                      data['hasrent'][i], float(data['latitude'][i]), float(data['longitude'][i]))
        cursor.execute(query, data_query)
        cnx.commit()
    except:
        continue

cursor.close()
cnx.close()