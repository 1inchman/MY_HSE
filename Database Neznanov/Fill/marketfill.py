# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector


data = pd.read_csv('market.csv', header=0, names=['id', 'number', 'globid', 'name', 'admarea', 'distr',
                                                  'address', 'mancomp', 'mancompaddr', 'kind', 'extra', 'geotype',
                                                  'latitude', 'longitude'])
data = data.drop(['id', 'number', 'globid', 'name', 'admarea', 'mancomp', 'mancompaddr', 'geotype', 'extra'], axis=1)
data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')


cycles = len(data)
cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO market "
         "(distid, address, kind, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s)")
for i in range(1, cycles, 1):
    selectquery = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectquery)
    st = cursor.fetchall()
    st = st[0][0]
    data_query = (st, data['address'][i], data['kind'][i], float(data['latitude'][i]), float(data['longitude'][i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()
