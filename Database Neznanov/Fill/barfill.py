# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector

data = pd.read_csv('bar.csv', header=0, names=['lat', 'lon', 'id', 'number', 'globid', 'name',
                                               'isnet', 'opercom', 'admarea', 'distr', 'address', 'phone',
                                               'seats', 'socpriv', 'latitude', 'longitude'])

data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')
data['isnet'] = data['isnet'].str.replace('нет', '0')
data['isnet'] = data['isnet'].str.replace('да', '1')
print data.head()

cycles = len(data)
cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO bar "
         "(distid, fullname, address, phonenumber, sitsnum, isnet, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
for i in range(1, cycles, 1):
    selectquery = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectquery)
    st = cursor.fetchall()
    print st, data['distr'][i]
    st = st[0][0]
    data_query = (st, data['name'][i], data['address'][i], data['phone'][i], int(data['seats'][i]),
                  int(data['isnet'][i]), float(data['latitude'][i]), float(data['longitude'][i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()
