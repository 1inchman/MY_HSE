# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector
import math

data = pd.read_csv('fracture.csv')

data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')

print data.head()

cycles = len(data)

cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cnx2 = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()
internalcursor = cnx2.cursor()

for i in range(1, cycles, 1):
    getFracIdquery = ("SELECT id FROM fracture WHERE fullname='%s'" % data['name'][i])
    cursor.execute(getFracIdquery)
    fracID = cursor.fetchall()
    fracID = fracID[0][0]
    selectcoords = ("SELECT id, lattitude, longitude from bar")
    cursor.execute(selectcoords)
    dists = []
    for aidi, lat, long in cursor:
        tmpdist = 6378137 * math.acos(math.cos(math.radians(lat)) * math.cos(math.radians(data['latitude'][i])) * math.cos(
                        math.radians(long) -
                        math.radians(data['longitude'][i])) +
                                               math.sin(math.radians(lat)) * math.sin(
                                           math.radians(data['latitude'][i])))
        if tmpdist <= 10000:
            insertDistQuery = "INSERT INTO fracbardist (barid, fracid, distance) VALUES (%s, %s, %s)"
            insertData = (aidi, fracID, tmpdist)
            internalcursor.execute(insertDistQuery, insertData)
            cnx2.commit()
            continue


cursor.close()
cnx.close()
