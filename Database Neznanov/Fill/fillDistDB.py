# coding=utf-8
import numpy as np
import pandas as pd
import mysql.connector


data = pd.read_csv('/Users/oneinchman/Desktop/BD project/district.csv', names=['#', 'name', 'mun', 'adm', 'area', 'pop'
                                                                               , 'popdens', 'livarea', 'areaperm'])
data = data.drop(['#', 'mun', 'adm', 'popdens', 'livarea', 'areaperm'], axis=1)
data['area'] = data['area'].str.replace(',', '.')
pop = np.array(data['pop'], dtype='int_')
area = np.array(data['area'], dtype='float')
cycles = len(data)


cnx = mysql.connector.connect(user='root', password='hiKNMsBw1', host='localhost', database='DBproj')
cursor = cnx.cursor()
query = ("INSERT INTO district "
         "(area, distName, population) "
         "VALUES (%s, %s, %s)")
for i in range(1, cycles, 1):
    data_query = (float(area[i]), data['name'][i], int(pop[i]))
    cursor.execute(query, data_query)
    cnx.commit()

cursor.close()
cnx.close()
