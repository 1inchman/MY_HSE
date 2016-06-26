# -*- coding: utf-8 -*-

import pandas as pd
import mysql.connector
import math

data = pd.read_csv('wifi.csv', header=0, names=['1', '2', '3', '4', '5', '6', 'name', '7', 'distr', '8', '9',
                                               'zone', '10', 'privacy', '11', '13', '14', '12', 'longitude',
                                               'latitude'])

data['distr'] = data['distr'].str.replace('район ', '')
data['distr'] = data['distr'].str.replace(' район', '')
data['distr'] = data['distr'].str.replace('район', '')
data['distr'] = data['distr'].str.replace('поселение ', '')


cycles = len(data)
cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()

query = ("INSERT INTO wifispot "
         "(distid, parkid, skitrackid, spotname, zone, privacy, lattitude, longitude) "
         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
flag = False
for i in range(1, cycles, 1):
    selectDistId = ("SELECT id from district where distName = '%s'" % data['distr'][i])
    cursor.execute(selectDistId)
    distId = cursor.fetchall()
    distId = distId[0][0]
    selectSkitrack = ("SELECT id, lattitude, longitude from skitrack where distid = '%s'" % distId)
    cursor.execute(selectSkitrack)
    tmpskidist = 100000000
    tmpskiid = None
    for aidi, lat, long in cursor:

        if 6378137*math.acos(math.cos(math.radians(lat))*math.cos(math.radians(data['latitude'][i]))*math.cos(math.radians(long) -
                             math.radians(data['longitude'][i]))+
                             math.sin(math.radians(lat))*math.sin(math.radians(data['latitude'][i]))) <= tmpskidist:
            tmpskidist = 6378137*math.acos(math.cos(math.radians(lat))*math.cos(math.radians(data['latitude'][i]))*math.cos(math.radians(long) -
                             math.radians(data['longitude'][i]))+
                             math.sin(math.radians(lat))*math.sin(math.radians(data['latitude'][i])))
            tmpskiid = aidi

    selectPark = ("SELECT id, lattitude, longitude from park where distid = '%s'" % distId)
    cursor.execute(selectPark)
    tmpparkdist = 100000000
    tmpparkid = None
    for aidi, lat, long in cursor:

        if 6378137 * math.acos(math.cos(math.radians(lat)) * math.cos(math.radians(data['latitude'][i])) * math.cos(
                        math.radians(long) -
                        math.radians(data['longitude'][i])) +
                                               math.sin(math.radians(lat)) * math.sin(
                                           math.radians(data['latitude'][i]))) <= tmpparkdist:
            tmpparkdist = 6378137 * math.acos(
                math.cos(math.radians(lat)) * math.cos(math.radians(data['latitude'][i])) * math.cos(
                    math.radians(long) -
                    math.radians(data['longitude'][i])) +
                math.sin(math.radians(lat)) * math.sin(math.radians(data['latitude'][i])))
            tmpparkid = aidi
    data_query = (distId, tmpparkid, tmpskiid, data['name'][i], int(data['zone'][i]), data['privacy'][i], float(data['latitude'][i]),
                  float(data['longitude'][i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()
