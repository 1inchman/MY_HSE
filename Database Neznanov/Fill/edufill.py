# -*- coding: utf-8 -*-

import json
import numpy as np
import pandas as pd
import mysql.connector
import re

# with open("/Users/oneinchman/Downloads/edu.json") as file:
#     data = json.load(file)
#
# df = pd.DataFrame(columns=('distr', 'address', 'phone', 'fullname', 'form', 'head', 'latitude', 'longitude'))
#
#
# for i in range(len(data)):
#     layer = data[i]
#     layer = layer['Cells']
#
#     # if type(layer['EducationPrograms']) == type(None):
#     #     layer['EducationPrograms'] = 'Null'
#     # else:
#     #     layer['EducationPrograms'] = layer['EducationPrograms'].encode('utf8')
#
#     if i == 720:
#         df.loc[i] = [layer['InstitutionsAddresses'][0]['District'],
#                      layer['LegalAddress'],
#                      layer['InstitutionsAddresses'][0]['PublicPhone'][0]['PublicPhone'],
#                      layer['FullName'],
#                      layer['LegalOrganization'],
#                      layer['ChiefName'],
#                      None,
#                      None]
#         continue
#
#
#     if isinstance(layer['geoData']['coordinates'][0][0][0], (int, float)):
#         df.loc[i] = [layer['InstitutionsAddresses'][0]['District'],
#                      layer['LegalAddress'],
#                      layer['InstitutionsAddresses'][0]['PublicPhone'][0]['PublicPhone'],
#                      layer['FullName'],
#                      layer['LegalOrganization'],
#                      layer['ChiefName'],
#                      layer['geoData']['coordinates'][0][0][0],
#                      layer['geoData']['coordinates'][0][0][1]]
#     else:
#         df.loc[i] = [layer['InstitutionsAddresses'][0]['District'],
#                      layer['LegalAddress'],
#                      layer['InstitutionsAddresses'][0]['PublicPhone'][0]['PublicPhone'],
#                      layer['FullName'],
#                      layer['LegalOrganization'],
#                      layer['ChiefName'],
#                      layer['geoData']['coordinates'][0][0][0][0],
#                      layer['geoData']['coordinates'][0][0][0][1]]
#
# print df.head()
#
# df.to_csv('edu.csv', sep=',', encoding='utf-8')

data = pd.read_csv('edu.csv')
data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')

fullname = list(data['fullname'])
types = []
for i in range(len(fullname)):

    if re.search(r'Школа', fullname[i]) != None or re.search(r'школа', fullname[i]) != None:
        types.append('Школа')
        continue

    elif re.search(r'Гимназия', fullname[i]) != None or re.search(r'гимназия', fullname[i]) != None:
        types.append('Гимназия')
        continue
    elif re.search(r'Лицей', fullname[i]) != None or re.search(r'лицей', fullname[i]) != None:
        types.append('Лицей')
    elif re.search(r'Колледж', fullname[i]) != None or re.search(r'колледж', fullname[i]) != None:
        types.append('Колледж')
        continue
    else:
        types.append('Учреждение дополнительного образования')
        continue


data['latitude'].fillna(0., inplace=True)
data['longitude'].fillna(0., inplace=True)


# print data.head()
#
cycles = len(data)
cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO eduplace "
         "(distid, fullname, address, phonenumber, placetype, form, head, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
for i in range(1, cycles, 1):
    selectquery = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectquery)
    st = cursor.fetchall()
    print st, data['distr'][i]
    print (st, data['address'][i], data['phone'][i], data['fullname'][i],
                  data['form'][i], data['head'][i], float(data['latitude'][i]), float(data['longitude'][i]))
    st = st[0][0]

    data_query = (st, data['fullname'][i], data['address'][i], data['phone'][i], types[i],
                  data['form'][i], data['head'][i], float(data['latitude'][i]), float(data['longitude'][i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()


