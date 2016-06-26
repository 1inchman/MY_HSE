# coding=utf-8


from PyQt4 import QtCore, QtGui, QtSql
import sys
import math


class main(QtGui.QDialog):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.setMinimumWidth(700)

        self.db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.db.setDatabaseName('DBproj')
        self.db.setUserName('root')
        self.db.setPassword('hiKNMsBw1')
        self.db.open()

        self.buttnames = [u'Отчет №1: кол-ва обр учр-ий и парков по районам',
                          u'Отчет №2: все типы учреждений по районам',
                          u'Отчет №3: количество всех учреждений по районам',
                          u'Отчет №4: парки в районах с населением < 79000 человек',
                          u'Отчет №5: все учреждения в радиусе 2км от точки', u'Добавить запись',
                          u'Удалить запись', u'Обновить запись']
        self.buttons = []
        for nm in self.buttnames:
            self.buttons.append(QtGui.QPushButton(nm))

        self.layout = QtGui.QVBoxLayout()
        self.table = QtGui.QTableView()
        self.layout.addWidget(self.table)
        for b in self.buttons:
            self.layout.addWidget(b)

        self.butslay1 = QtGui.QHBoxLayout()
        self.buts1rownames = [u'Районы', u'Трассы', u'Рынки', u'Парки']
        self.buts1row = []
        for nm in self.buts1rownames:
            self.buts1row.append(QtGui.QPushButton(nm))
        for b in self.buts1row:
            self.butslay1.addWidget(b)
        self.layout.addLayout(self.butslay1)

        self.butslay2 = QtGui.QHBoxLayout()
        self.buts2rownames = [u'Вай-фай точки', u'Обр. учр-ия', u'Бары', u'Травмпункты']
        self.buts2row = []
        for nm in self.buts2rownames:
            self.buts2row.append(QtGui.QPushButton(nm))
        for b in self.buts2row:
            self.butslay2.addWidget(b)
        self.layout.addLayout(self.butslay2)

        self.setLayout(self.layout)

        QtCore.QObject.connect(self.buttons[0], QtCore.SIGNAL("clicked()"), self.query1)
        QtCore.QObject.connect(self.buttons[1], QtCore.SIGNAL("clicked()"), self.query2)
        QtCore.QObject.connect(self.buttons[2], QtCore.SIGNAL("clicked()"), self.query3)
        QtCore.QObject.connect(self.buttons[3], QtCore.SIGNAL("clicked()"), self.query4)
        QtCore.QObject.connect(self.buttons[4], QtCore.SIGNAL("clicked()"), self.query5)
        QtCore.QObject.connect(self.buttons[5], QtCore.SIGNAL("clicked()"), self.addrecord)
        QtCore.QObject.connect(self.buttons[6], QtCore.SIGNAL("clicked()"), self.delrecord)
        QtCore.QObject.connect(self.buttons[7], QtCore.SIGNAL("clicked()"), self.updrecord)

        QtCore.QObject.connect(self.buts1row[0], QtCore.SIGNAL("clicked()"), self.showdist)
        QtCore.QObject.connect(self.buts1row[1], QtCore.SIGNAL("clicked()"), self.showski)
        QtCore.QObject.connect(self.buts1row[2], QtCore.SIGNAL("clicked()"), self.showmark)
        QtCore.QObject.connect(self.buts1row[3], QtCore.SIGNAL("clicked()"), self.showpark)

        QtCore.QObject.connect(self.buts2row[0], QtCore.SIGNAL("clicked()"), self.showwifi)
        QtCore.QObject.connect(self.buts2row[1], QtCore.SIGNAL("clicked()"), self.showedu)
        QtCore.QObject.connect(self.buts2row[2], QtCore.SIGNAL("clicked()"), self.showbar)
        QtCore.QObject.connect(self.buts2row[3], QtCore.SIGNAL("clicked()"), self.showfrac)

    def showdist(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from district")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showski(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from skitrack ")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showmark(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from market")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showpark(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from park")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showwifi(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from wifispot")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showedu(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from eduplace")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showbar(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from bar")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def showfrac(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("select * from fracture")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def addrecord(self):
        self.newwind = addWindow()
        self.newwind.show()

    def delrecord(self):
        self.delwind = delWindow()
        self.delwind.show()

    def updrecord(self):
        self.updwind = updWindow()
        self.updwind.show()

    def query1(self):
        model = QtSql.QSqlRelationalTableModel()

        query = QtSql.QSqlQuery("SELECT DISTINCT t1.distname AS district, count( distinct t2.id) AS number_of_eduplaces, count( distinct t3.id) AS number_of_parks "
"FROM "
"district t1 INNER JOIN eduplace t2 ON (t1.id=t2.distid) "
"INNER JOIN park t3 ON (t1.id=t3.distid) "
"GROUP BY t1.distname "
"ORDER BY count( distinct t2.id) desc, count( distinct t3.id) desc")
        model.setQuery(query)
        model.setHeaderData(0, QtCore.Qt.Horizontal, u'Район')
        model.setHeaderData(1, QtCore.Qt.Horizontal, u'Количество учебных заведений')
        model.setHeaderData(2, QtCore.Qt.Horizontal, u'Количество парков')
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.show()

    def query2(self):
        model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("(select district.distName, 'Skitrack' as Type, skitrack.address from district join skitrack on district.id=skitrack.distid) "
                    "union (select district.distName, 'Park' as Type,park.fullname from district join park on district.id=park.distid) "
                    "union (select district.distName, 'Wi-fi spot' AS Type, wifispot.spotname from wifispot join district on wifispot.distid = district.id) "
                    "union "
                    "(select district.distName, 'Bar' as Type, bar.fullname from bar join district on bar.distid = district.id) "
                    "union "
                    "(select district.distName, 'Fracture clinic' as Type, fracture.fullname from fracture join district on fracture.distid = district.id) "
                    "union "
                    "SELECT district.distName, 'Edu. place' AS Type, eduplace.fullname from eduplace JOIN district ON eduplace.distid = district.id "
                    "union "
                    "SELECT district.distName, 'Market place' AS type, market.address from market JOIN district ON market.distid = district.id "
                    "ORDER BY type, distName")
        print query.lastError().text()
        model.setQuery(query)
        model.setHeaderData(0, QtCore.Qt.Horizontal, u'Район')
        model.setHeaderData(1, QtCore.Qt.Horizontal, u'Тип места')
        model.setHeaderData(2, QtCore.Qt.Horizontal, u'Наименование или адрес')
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        # self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()


    def query3(self):
        model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("SELECT district.distName, 'park' AS type, COUNT(park.fullname) FROM park JOIN district ON park.distid = district.id "
                    "GROUP BY type, district.distName "
                    "UNION "
                    "SELECT district.distName, 'wifispot' AS type, COUNT(wifispot.spotname) FROM wifispot JOIN district ON wifispot.distid = district.id "
                    "GROUP BY type, district.distName "
                    "UNION "
                    "SELECT district.distName, 'skitrack' AS type, COUNT(skitrack.address) FROM skitrack JOIN district ON skitrack.distid = district.id "
                    "GROUP BY type, district.distName "
                    "UNION "
                    "SELECT district.distName, 'bar' AS type, COUNT(bar.fullname) FROM bar JOIN district ON bar.distid = district.id "
                    "GROUP BY type, district.distName "
                    "UNION "
                    "SELECT district.distName, 'fracture' AS type, COUNT(fracture.fullname) FROM fracture JOIN district ON fracture.distid = district.id "
                    "GROUP BY type, district.distName "
                    "UNION "
                    "SELECT district.distName, 'education' AS type, COUNT(eduplace.fullname) FROM eduplace JOIN district ON eduplace.distid = district.id "
                    "GROUP BY type, district.distName "
                    "UNION "
                    "SELECT district.distName, 'market' AS type, COUNT(market.address) FROM market JOIN district ON market.distid = district.id "
                    "GROUP BY type, district.distName")
        model.setQuery(query)
        model.setHeaderData(0, QtCore.Qt.Horizontal, u'Район')
        model.setHeaderData(1, QtCore.Qt.Horizontal, u'Тип места')
        model.setHeaderData(2, QtCore.Qt.Horizontal, u'Количество')
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        # self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def query4(self):
        model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("SELECT district.distName, park.fullname, park.address, park.flagwater, park.flagchildarea "
"FROM "
"park join district on district.id=park.distid "
"WHERE park.distid IN (SELECT id FROM district WHERE population < 790000)")
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()

    def query5(self):
        model = QtSql.QSqlRelationalTableModel()
        query = QtSql.QSqlQuery()
        query.exec_("SELECT district.distName, 'Park' AS type, park.fullname,6378137*ACOS(SIN(55.806701*3.14/180)*SIN(park.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(park.longitude*3.14/180)*COS(park.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"park JOIN district ON park.distid = district.id "
"HAVING distance < 2000 "
"UNION ALL "
"SELECT district.distName, 'Wifi spot' AS type, wifispot.spotname, 6378137*ACOS(SIN(55.806701*3.14/180)*SIN(wifispot.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(wifispot.longitude*3.14/180)*COS(wifispot.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"wifispot JOIN district ON wifispot.distid = district.id "
"HAVING distance < 2000 "
"UNION ALL "
"SELECT district.distName, 'Ski track' AS type, skitrack.address, 6378137*ACOS(SIN(55.806701*3.14/180)*SIN(skitrack.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(skitrack.longitude*3.14/180)*COS(skitrack.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"skitrack JOIN district ON skitrack.distid = district.id "
"HAVING "
"distance < 2000 "
"UNION ALL "
"SELECT district.distName, 'Bar' AS type, bar.fullname, 6378137*ACOS(SIN(55.806701*3.14/180)*SIN(bar.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(bar.longitude*3.14/180)*COS(bar.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"bar JOIN district ON bar.distid = district.id "
"HAVING "
"distance < 2000 "
"UNION ALL "
"SELECT district.distName, 'Fracture clinic' AS type, fracture.fullname, 6378137*ACOS(SIN(55.806701*3.14/180)*SIN(fracture.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(fracture.longitude*3.14/180)*COS(fracture.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"fracture JOIN district ON fracture.distid = district.id "
"HAVING "
"distance < 2000 "
"UNION ALL "
"SELECT district.distName, 'Edu. place' AS type, eduplace.fullname, 6378137*ACOS(SIN(55.806701*3.14/180)*SIN(eduplace.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(eduplace.longitude*3.14/180)*COS(eduplace.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"eduplace JOIN district ON eduplace.distid = district.id "
"HAVING "
"distance < 2000 "
"UNION ALL "
"SELECT district.distName, 'Market place' AS type, market.address, 6378137*ACOS(SIN(55.806701*3.14/180)*SIN(market.longitude*3.14/180)+COS(55.806701*3.14/180)*COS(market.longitude*3.14/180)*COS(market.lattitude*3.14/180 - 37.541618*3.14/180)) AS distance "
"FROM "
"market JOIN district ON market.distid = district.id "
"HAVING "
"distance < 2000 "
"ORDER BY distance, distName"
)
        model.setQuery(query)
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnHidden(model.fieldIndex('id'), True)
        self.table.show()



class addWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(addWindow, self).__init__(parent)
        self.setMinimumWidth(900)
        self.flag = False
        self.layout = QtGui.QVBoxLayout()
        self.chbutton = QtGui.QPushButton(u'Выбрать таблицу')
        self.addbutton = QtGui.QPushButton(u'Добавить данные')
        self.choosedistbox = QtGui.QComboBox()
        self.choosedistbox.addItem(u'Район')
        self.choosedistbox.addItems([u'Рынок', u'Лыжная трасса', u'Wi-fi точка', u'Образовательное учр-ие',
                                     u'Бар', u'Травмпункт', u'Парк'])
        self.distlabel = QtGui.QLabel(u'Выберите таблицу')
        self.layout.addWidget(self.distlabel)
        self.layout.addWidget(self.choosedistbox)
        self.layout.addWidget(self.chbutton)
        self.layout.addWidget(self.addbutton)
        self.setLayout(self.layout)
        QtCore.QObject.connect(self.chbutton, QtCore.SIGNAL("clicked()"), self.placetextboxes)
        QtCore.QObject.connect(self.addbutton, QtCore.SIGNAL("clicked()"), self.dataadd)

    def placetextboxes(self):
        if self.flag==True:
            def clearLayout(layout):
                while layout.count():
                    child = layout.takeAt(0)
                    child.widget().deleteLater()

            clearLayout(self.textlay)
            clearLayout(self.lablelay)

        curtext = self.choosedistbox.currentText()
        if curtext == u'Парк':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Адрес', u'Наименование', u'Есть водоем?', u'Есть детплощадка?', u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Район':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование', u'Площадь', u'Население']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Рынок':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Адрес', u'Вид', u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Лыжная трасса':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Адрес', u'Телефон', u'Есть прокат?', u'Есть туалет?', u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Wi-fi точка':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Имя точки', u'Радиус', u'Открытая/закрытая\nсеть', u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Образовательное учр-ие':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Наименование', u'Адрес', u'Номер телефона', u'Тип заведения', u'О-П форма',
                    u'Глава', u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)

            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Наименование', u'Адрес', u'Телефон', u'Кол-во мест', u'Сетевой? (1/0)',
                    u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Травмпункт':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Наименование', u'Адрес', u'Телефон', u'Глава', u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        # if curtext == u'Расстояния бар-травмпункт':
        #     self.lablelay = QtGui.QHBoxLayout()
        #     self.textlay = QtGui.QHBoxLayout()
        #     text = [u'Название бара', u'Название травмпункта', u'Расстояние']
        #     self.labels = []
        #     self.texteds = []
        #     for tx in text:
        #         self.labels.append(QtGui.QLabel(tx))
        #         tmp = QtGui.QTextEdit()
        #         tmp.setFixedHeight(20)
        #         self.texteds.append(tmp)
        #     for l in self.labels:
        #         self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
        #     for t in self.texteds:
        #         self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
        #     self.layout.addLayout(self.lablelay)
        #     self.layout.addLayout(self.textlay)
        #     self.setLayout(self.layout)
        if curtext == u'Бар':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Район', u'Наименование', u'Адрес', u'Номер телефона', u'Количество мест', u'Сетевой? (1/0)',
                    u'Долгота', u'Широта']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        self.flag = True


    def dataadd(self):

        row = []
        for text in self.texteds:
            fromtexted = unicode(text.toPlainText())
            if fromtexted == '':
                row.append(QtCore.QVariant())
            else:
                row.append(fromtexted)

        curtext = self.choosedistbox.currentText()
        if curtext == u'Парк':
            query = QtSql.QSqlQuery()
            query.prepare("insert into park (distid, fullname, address, flagwater, flagchildarea, lattitude, longitude) "
                          "values (:dist, :name, :addr, :water, :child, :lat, :lon)")
            distToidQuery = QtSql.QSqlQuery("select id from district where distName = %s" % row[0])
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()
            query.bindValue(':dist', distid[0])
            query.bindValue(':name', row[2])
            query.bindValue(':addr', row[1])
            query.bindValue(':water', row[3])
            query.bindValue(':child', row[4])
            query.bindValue(':lat', row[5])
            query.bindValue(':lon', row[6])
            b = query.exec_()
        if curtext == u'Район':
            query = QtSql.QSqlQuery()
            query.prepare("insert into district (area, distName, population) values (:ni, :nd, :np)")
            query.bindValue(':ni', row[1])
            query.bindValue(':nd', row[0])
            query.bindValue(':np', row[2])
            b = query.exec_()
        if curtext == u'Рынок':
            query = QtSql.QSqlQuery()
            query.prepare(
                "insert into market (distid, address, kind, lattitude, longitude) "
                "values (:dist, :addr, :kind, :lat, :lon)")
            distToidQuery = QtSql.QSqlQuery("select id from district where distName = %s" % row[0])
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()
            query.bindValue(':dist', distid[0])
            query.bindValue(':addr', row[1])
            query.bindValue(':kind', row[2])
            query.bindValue(':lat', row[3])
            query.bindValue(':lon', row[4])
            b = query.exec_()
        if curtext == u'Лыжная трасса':
            query = QtSql.QSqlQuery()
            query.prepare(
                "insert into skitrack (distid, address, phonenumber, flagwc, flagrent, lattitude, longitude) "
                "values (:dist, :addr, :phone, :wc, :rent, :lat, :lon)")
            distToidQuery = QtSql.QSqlQuery("select id from district where distName = %s" % row[0])
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()
            query.bindValue(':dist', distid[0])
            query.bindValue(':addr', row[1])
            query.bindValue(':phone', row[2])
            query.bindValue(':rent', row[3])
            query.bindValue(':wc', row[4])
            query.bindValue(':lat', row[5])
            query.bindValue(':lon', row[6])
            b = query.exec_()
        if curtext == u'Wi-fi точка':
            distToidQuery = QtSql.QSqlQuery()
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()

            tmpskidist = 100000000
            tmpskiid = QtCore.QVariant()
            tmpparkdist = 100000000
            tmpparkid = QtCore.QVariant()
            selectSkitrack = QtSql.QSqlQuery()
            selectSkitrack.prepare("SELECT id, lattitude, longitude from skitrack where distid = :id")
            selectSkitrack.bindValue(':id', distid)
            selectSkitrack.exec_()
            while selectSkitrack.next():
                if 6378137 * math.acos(math.cos(math.radians(selectSkitrack.value(1).toFloat()[0])) * math.cos(
                        math.radians(float(row[5]))) * math.cos(math.radians(selectSkitrack.value(2).toFloat()[0]) -
                                                                              math.radians(float(row[4]))) +
                                                       math.sin(math.radians(selectSkitrack.value(1).toFloat()[0])) * math.sin(
                                                   math.radians(float(row[5])))) <= tmpskidist:
                    tmpskiid = 6378137 * math.acos(math.cos(math.radians(selectSkitrack.value(1).toFloat()[0])) * math.cos(
                        math.radians(float(row[5]))) * math.cos(math.radians(selectSkitrack.value(2).toFloat()[0]) -
                                                                              math.radians(float(row[4]))) +
                                                       math.sin(math.radians(selectSkitrack.value(1).toFloat()[0])) * math.sin(
                                                   math.radians(float(row[5]))))
            selectPark = QtSql.QSqlQuery()
            selectPark.prepare("SELECT id, lattitude, longitude from park where distid = :id")
            selectPark.bindValue(':id', distid)
            selectPark.exec_()
            while selectPark.next():
                if 6378137 * math.acos(math.cos(math.radians(selectPark.value(1).toFloat()[0])) * math.cos(
                        math.radians(float(row[5]))) * math.cos(math.radians(selectPark.value(2).toFloat()[0]) -
                                                                        math.radians(float(row[4]))) +
                                                       math.sin(
                                                           math.radians(selectPark.value(1).toFloat()[0])) * math.sin(
                                                   math.radians(float(row[5])))) <= tmpparkdist:
                    tmpparkid = 6378137 * math.acos(math.cos(math.radians(selectPark.value(1).toFloat()[0])) * math.cos(
                        math.radians(float(row[5]))) * math.cos(math.radians(selectPark.value(2).toFloat()[0]) -
                                                                math.radians(float(row[4]))) +
                                                   math.sin(math.radians(selectPark.value(1).toFloat()[0])) * math.sin(
                                                       math.radians(float(row[5]))))

            query = QtSql.QSqlQuery()
            query.prepare(
                "insert into wifispot (distid, parkid, skitrackid, spotname, zone, privacy, lattitude, longitude) "
                "values (:dist, :parkid, :skiid, :name, :zone, :priv, :lat, :lon)")
            query.bindValue(':dist', distid[0])
            query.bindValue(':parkid', tmpparkid)
            query.bindValue(':skiid', tmpskiid)
            query.bindValue(':name', row[1])
            query.bindValue(':zone', row[2])
            query.bindValue(':priv', row[3])
            query.bindValue(':lat', row[5])
            query.bindValue(':lon', row[4])
            b = query.exec_()
        if curtext == u'Образовательное учр-ие':
            query.prepare(
                "insert into eduplace (distid, fullname, address, phonenumber, placetype, form, head, lattitude, longitude) "
                "values (:dist, :name, :addr, :phone, :type, :form, :head, :lat, :lon)")
            distToidQuery = QtSql.QSqlQuery("select id from district where distName = %s" % row[0])
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()
            query.bindValue(':dist', distid[0])
            query.bindValue(':name', row[1])
            query.bindValue(':addr', row[2])
            query.bindValue(':phone', row[3])
            query.bindValue(':type', row[4])
            query.bindValue(':form', row[5])
            query.bindValue(':head', row[6])
            query.bindValue(':lat', row[7])
            query.bindValue(':lon', row[8])
            b = query.exec_()
        if curtext == u'Бар':
            query.prepare(
                "insert into bar (distid, fullname, address, phonenumber, sitsnum, isnet, lattitude, longitude) "
                "values (:dist, :name, :addr, :phone, :sits, :isnet, :lat, :lon)")
            distToidQuery = QtSql.QSqlQuery("select id from district where distName = %s" % row[0])
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()
            query.bindValue(':dist', distid[0])
            query.bindValue(':name', row[1])
            query.bindValue(':addr', row[2])
            query.bindValue(':phone', row[3])
            query.bindValue(':sits', row[4])
            query.bindValue(':isnet', row[5])
            query.bindValue(':lat', row[6])
            query.bindValue(':lon', row[7])
            b = query.exec_()
        if curtext == u'Травмпункт':
            query.prepare(
                "insert into fracture (distid, fullname, address, phonenumber, head, lattitude, longitude) "
                "values (:dist, :name, :addr, :phone, :head, :lat, :lon)")
            distToidQuery = QtSql.QSqlQuery("select id from district where distName = %s" % row[0])
            distToidQuery.prepare("select id from district where distName = :name")
            distToidQuery.bindValue(':name', row[0])
            distToidQuery.exec_()
            distToidQuery.next()
            distid = distToidQuery.value(0).toInt()
            query.bindValue(':dist', distid[0])
            query.bindValue(':name', row[1])
            query.bindValue(':addr', row[2])
            query.bindValue(':phone', row[3])
            query.bindValue(':head', row[4])
            query.bindValue(':lat', row[5])
            query.bindValue(':lon', row[6])
            b = query.exec_()


        if b == False:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)

            msg.setText(u"Ошибка добавления")
            msg.setInformativeText(query.lastError().text())
            msg.setWindowTitle(u'Ошибка')
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
        else:
            label = QtGui.QLabel(u'Запрос выполнен успешно')
            layout = QtGui.QHBoxLayout()
            layout.addWidget(label, QtCore.Qt.AlignCenter)
            self.layout.addLayout(layout)
            self.setLayout(self.layout)

class delWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(delWindow, self).__init__(parent)
        self.setMinimumWidth(900)
        self.flag = False
        self.layout = QtGui.QVBoxLayout()
        self.chbutton = QtGui.QPushButton(u'Выбрать таблицу')
        self.addbutton = QtGui.QPushButton(u'Удалить данные')
        self.choosedistbox = QtGui.QComboBox()
        self.choosedistbox.addItem(u'Район')
        self.choosedistbox.addItems([u'Рынок', u'Лыжная трасса', u'Wi-fi точка', u'Образовательное учр-ие',
                                     u'Бар', u'Травмпункт', u'Парк'])
        self.distlabel = QtGui.QLabel(u'Выберите таблицу')
        self.layout.addWidget(self.distlabel)
        self.layout.addWidget(self.choosedistbox)
        self.layout.addWidget(self.chbutton)
        self.layout.addWidget(self.addbutton)
        self.setLayout(self.layout)
        QtCore.QObject.connect(self.chbutton, QtCore.SIGNAL("clicked()"), self.placetextboxes)
        QtCore.QObject.connect(self.addbutton, QtCore.SIGNAL("clicked()"), self.datadel)

    def placetextboxes(self):
        if self.flag==True:
            def clearLayout(layout):
                while layout.count():
                    child = layout.takeAt(0)
                    child.widget().deleteLater()

            clearLayout(self.textlay)
            clearLayout(self.lablelay)

        curtext = self.choosedistbox.currentText()
        if curtext == u'Парк':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Адрес', u'Наименование']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Район':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Рынок':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Адрес']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Лыжная трасса':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Адрес']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Wi-fi точка':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Имя точки']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Образовательное учр-ие':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование', u'Тип заведения']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)

        if curtext == u'Травмпункт':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Бар':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        self.flag = True


    def datadel(self):

        row = []
        for text in self.texteds:
            fromtexted = unicode(text.toPlainText())
            if fromtexted == '':
                row.append(QtCore.QVariant())
            else:
                row.append(fromtexted)

        curtext = self.choosedistbox.currentText()
        if curtext == u'Парк':
            query = QtSql.QSqlQuery()
            if type(row[0]) == type(QtCore.QVariant()) and type(row[1]) != type(QtCore.QVariant()):
                query.prepare("delete from park where fullname = :name")
                query.bindValue(':name', row[1])
                b = query.exec_()
            elif type(row[1]) == type(QtCore.QVariant()) and type(row[0]) != type(QtCore.QVariant()):
                query.prepare("delete from park where address = :name")
                query.bindValue(':name', row[0])
                b = query.exec_()
            else:
                query.prepare("delete from park where address = :adr and fullname = :name")
                query.bindValue(':name', row[1])
                query.bindValue(':adr', row[0])
                b = query.exec_()

        if curtext == u'Район':
            query = QtSql.QSqlQuery()
            query.prepare("delete from district where distName = :ni")
            query.bindValue(':ni', row[0])
            b = query.exec_()
        if curtext == u'Рынок':
            query = QtSql.QSqlQuery()
            query.prepare(
                "delete from market where address = :adr")
            query.bindValue(':adr', row[0])
            b = query.exec_()
        if curtext == u'Лыжная трасса':
            query = QtSql.QSqlQuery()
            query.prepare("delete from skitrack where address = :adr")
            query.bindValue(':adr', row[0])
            b = query.exec_()
        if curtext == u'Wi-fi точка':

            query = QtSql.QSqlQuery()
            query.prepare("delete from wifispot where spotname = :name")
            query.bindValue(':name', row[0])
            b = query.exec_()
        if curtext == u'Образовательное учр-ие':
            query = QtSql.QSqlQuery()
            if type(row[0]) == type(QtCore.QVariant()) and type(row[1]) != type(QtCore.QVariant()):
                query.prepare("delete from eduplace where placetype = :type")
                query.bindValue(':type', row[1])
                b = query.exec_()
            elif type(row[1]) == type(QtCore.QVariant()) and type(row[0]) != type(QtCore.QVariant()):
                query.prepare("delete from eduplace where fullname = :name")
                query.bindValue(':name', row[0])
                b = query.exec_()
            else:
                query.prepare("delete from eduplace where fullname = :adr and placetype = :name")
                query.bindValue(':name', row[1])
                query.bindValue(':adr', row[0])
                b = query.exec_()
        if curtext == u'Бар':
            query.prepare("delete from bar where fullname = :name")
            query.bindValue(':name', row[0])
            b = query.exec_()
        if curtext == u'Травмпункт':
            query.prepare("delete from fracture where fullname = :name")
            query.bindValue(':name', row[0])
            b = query.exec_()


        if b == False:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)

            msg.setText(u"Ошибка удаления")
            msg.setInformativeText(query.lastError().text())
            msg.setWindowTitle(u'Ошибка')
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
        else:
            label = QtGui.QLabel(u'Количество измененных строк: '+ str(query.numRowsAffected()))
            layout = QtGui.QHBoxLayout()
            layout.addWidget(label, QtCore.Qt.AlignCenter)
            self.layout.addLayout(layout)
            self.setLayout(self.layout)

class updWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(updWindow, self).__init__(parent)
        self.setMinimumWidth(900)
        self.flag = False
        self.layout = QtGui.QVBoxLayout()
        self.chbutton = QtGui.QPushButton(u'Выбрать таблицу')
        self.addbutton = QtGui.QPushButton(u'Изменить данные')
        self.choosedistbox = QtGui.QComboBox()
        self.choosedistbox.addItem(u'Район')
        self.choosedistbox.addItems([u'Рынок', u'Лыжная трасса', u'Wi-fi точка', u'Образовательное учр-ие',
                                     u'Бар', u'Травмпункт', u'Парк'])
        self.distlabel = QtGui.QLabel(u'Выберите таблицу')
        self.layout.addWidget(self.distlabel)
        self.layout.addWidget(self.choosedistbox)
        self.layout.addWidget(self.chbutton)
        self.layout.addWidget(self.addbutton)
        self.setLayout(self.layout)
        QtCore.QObject.connect(self.chbutton, QtCore.SIGNAL("clicked()"), self.placetextboxes)
        QtCore.QObject.connect(self.addbutton, QtCore.SIGNAL("clicked()"), self.dataupd)

    def placetextboxes(self):
        if self.flag==True:
            def clearLayout(layout):
                while layout.count():
                    child = layout.takeAt(0)
                    child.widget().deleteLater()

            clearLayout(self.textlay)
            clearLayout(self.lablelay)

        curtext = self.choosedistbox.currentText()
        if curtext == u'Парк':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Адрес', u'Наименование', u'Есть водоем?', u'Есть детплощадка?', u'Долгота', u'Широта',
                    u'Найти по наименованию']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Район':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование', u'Площадь', u'Население', u'Найти по наименованию']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Рынок':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Адрес', u'Вид', u'Долгота', u'Широта', u'Поиск по адресу']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Лыжная трасса':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Адрес', u'Телефон', u'Есть прокат?', u'Есть туалет?', u'Долгота', u'Широта', u'Поиск по адресу']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Wi-fi точка':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Имя точки', u'Радиус', u'Открытая/закрытая\nсеть', u'Долгота', u'Широта', u'Поиск по имени точки']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Образовательное учр-ие':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование', u'Адрес', u'Номер телефона', u'Тип заведения', u'О-П форма',
                    u'Глава', u'Долгота', u'Широта', u'Поиск по наименованию']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Травмпункт':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование', u'Адрес', u'Телефон', u'Глава', u'Долгота', u'Широта', u'Поиск по наименованию']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        if curtext == u'Бар':
            self.lablelay = QtGui.QHBoxLayout()
            self.textlay = QtGui.QHBoxLayout()
            text = [u'Наименование', u'Адрес', u'Номер телефона', u'Количество мест', u'Сетевой? (1/0)',
                    u'Долгота', u'Широта', u'Поиск по наиманованию']
            self.labels = []
            self.texteds = []
            for tx in text:
                self.labels.append(QtGui.QLabel(tx))
                tmp = QtGui.QTextEdit()
                tmp.setFixedHeight(20)
                self.texteds.append(tmp)
            for l in self.labels:
                self.lablelay.addWidget(l, QtCore.Qt.AlignLeft)
            for t in self.texteds:
                self.textlay.addWidget(t, QtCore.Qt.AlignLeft)
            self.layout.addLayout(self.lablelay)
            self.layout.addLayout(self.textlay)
            self.setLayout(self.layout)
        self.flag = True


    def dataupd(self):

        row = []
        for text in self.texteds:
            fromtexted = unicode(text.toPlainText())
            if fromtexted == '':
                row.append(QtCore.QVariant())
            else:
                row.append(fromtexted)

        curtext = self.choosedistbox.currentText()
        if curtext == u'Парк':
            query = QtSql.QSqlQuery()
            query.prepare("update park set fullname = :name, address = :adr, flagwater = :water, flagchildarea = :child, lattitude = :lat, longitude = :lon where fullname = :cond")
            query.bindValue(':cond', row[6])
            query.bindValue(':name', row[1])
            query.bindValue(':adr', row[0])
            query.bindValue(':water', row[2])
            query.bindValue(':child', row[3])
            query.bindValue(':lat', row[4])
            query.bindValue(':lon', row[5])
            b = query.exec_()
        if curtext == u'Район':
            query = QtSql.QSqlQuery()
            query.prepare("update district set area = :area, distName = :name, population = :pop where distName = :cond")
            query.bindValue(':area', row[1])
            query.bindValue(':name', row[0])
            query.bindValue(':pop', row[2])
            query.bindValue(':cond', row[3])
            b = query.exec_()
        if curtext == u'Рынок':
            query = QtSql.QSqlQuery()
            query.prepare("update market set address = :adr, kind = :kind, lattitude = :lat, longitude = :lon where address = :cond")
            query.bindValue(':adr', row[0])
            query.bindValue(':kind', row[1])
            query.bindValue(':lat', row[3])
            query.bindValue(':lon', row[2])
            query.bindValue(':cond', row[4])
            b = query.exec_()
        if curtext == u'Лыжная трасса':
            query = QtSql.QSqlQuery()
            query.prepare("update skitrack set address = :adr, phonenumber = :num, flagwc = :wc, flagrent = :rent, lattitude = :lat, longitude = :lon where address = :cond")
            query.bindValue(':adr', row[0])
            query.bindValue(':num', row[1])
            query.bindValue(':rent', row[2])
            query.bindValue(':wc', row[3])
            query.bindValue(':lat', row[5])
            query.bindValue(':lon', row[4])
            query.bindValue(':cond', row[6])
            b = query.exec_()
        if curtext == u'Wi-fi точка':
            query = QtSql.QSqlQuery()
            query.prepare("update wifispot set spotname = :name, zone = :zone, privacy = :priv, lattitude = :lat, longitude = :lon where spotname = :cond")
            query.bindValue(':name', row[0])
            query.bindValue(':zone', row[1])
            query.bindValue(':priv', row[2])
            query.bindValue(':lat', row[4])
            query.bindValue(':lon', row[3])
            query.bindValue(':cond', row[5])
            b = query.exec_()
        if curtext == u'Образовательное учр-ие':
            query = QtSql.QSqlQuery()
            query.prepare("update eduplace set fullname = :name, address = :adr, phonenumber = :num, placetype = :type, form = :form,"
                          "head = :head, lattitude = :lat, longitude = :lon where fullname = :cond")
            query.bindValue(':name', row[0])
            query.bindValue(':adr', row[1])
            query.bindValue(':num', row[2])
            query.bindValue(':type', row[3])
            query.bindValue(':form', row[4])
            query.bindValue(':head', row[5])
            query.bindValue(':lat', row[7])
            query.bindValue(':lon', row[6])
            query.bindValue(':cond', row[8])
            b = query.exec_()
        if curtext == u'Бар':
            query = QtSql.QSqlQuery()
            query.prepare("update bar set fullname = :name, address = :adr, phonenumber = :num, sitsnum = :sits, isnet = :net, lattitude = :lat, longitude = :lon where fullname = :cond")
            query.bindValue(':name', row[0])
            query.bindValue(':adr', row[1])
            query.bindValue(':num', row[2])
            query.bindValue(':sits', row[3])
            query.bindValue(':net', row[4])
            query.bindValue(':lat', row[6])
            query.bindValue(':lon', row[5])
            query.bindValue(':cond', row[7])
            b = query.exec_()
        if curtext == u'Травмпункт':
            query = QtSql.QSqlQuery()
            query.prepare("update fracture set fullname = :name, address = :adr, phonenumber = :num, head = :head, lattitude = :lat, longitude = :lon where fullname = :cond")
            query.bindValue(':name', row[0])
            query.bindValue(':adr', row[1])
            query.bindValue(':num', row[2])
            query.bindValue(':head', row[3])
            query.bindValue(':lat', row[5])
            query.bindValue(':lon', row[4])
            query.bindValue(':cond', row[6])
            b = query.exec_()


        if b == False:
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)

            msg.setText(u"Ошибка обновления")
            msg.setInformativeText(query.lastError().text())
            msg.setWindowTitle(u'Ошибка')
            msg.setStandardButtons(QtGui.QMessageBox.Ok)
            msg.exec_()
        else:
            label = QtGui.QLabel(u'Количество измененных строк: '+ str(query.numRowsAffected()))
            layout = QtGui.QHBoxLayout()
            layout.addWidget(label, QtCore.Qt.AlignCenter)
            self.layout.addLayout(layout)
            self.setLayout(self.layout)

App = QtGui.QApplication(sys.argv)
Prim = main()
Prim.show()
sys.exit(App.exec_())
