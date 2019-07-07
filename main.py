# -*-coding: utf8-*
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout, \
    QTextEdit, QLabel, QPushButton, QDateTimeEdit, QCheckBox, QLineEdit, QTableWidget, QTimeEdit, QTableWidgetItem
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import re
import xml.etree.ElementTree as  xml
import hashlib
from my_style import *
import datetime
import time
import os

# Разрешенеие окна
WIDTH = 1400
HEIGHT = 700


def get_hash_md5(filename):
    """Получить хэш сумму файла"""
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


class Main_Window(QMainWindow):
    """Главное окно"""

    def __init__(self):
        super().__init__()
        q = QDesktopWidget().availableGeometry()  # Работать с окнами экрана
        r_w, r_h = q.width(), q.height()  # Размеры окна
        self.setGeometry(r_w / 2 - WIDTH / 2, r_h / 2 - HEIGHT / 2, WIDTH, HEIGHT)  # Установить окно по центру

        self.tabs = QTabWidget()
        self.tab1 = File_Readme()
        self.tabs.addTab(self.tab1, "1-ый этап")
        self.setCentralWidget(self.tabs)
        self.setStyleSheet(style_2)


class File_Readme(QWidget):
    """Окно 1-ый этап"""

    def __init__(self):
        super().__init__()
        self.box_1 = QHBoxLayout()
        self.box_2 = QHBoxLayout()

        self.box_button = QVBoxLayout()
        self.box_main = QVBoxLayout()

        #
        self.text_readme = QTextEdit()

        # Таблица
        self.table_widget = QTableWidget()

        # Титул
        self.titul_1 = QLabel('Путь к файлу: ')
        self.titul_2 = QLabel(r'Содержимое install.txt\install_patch.txt')
        self.box_1.addWidget(self.titul_2)
        self.box_1.addStretch(1)

        # Кнопки
        self.but_form = QPushButton('Сформировать')
        self.but_form.setDisabled(True)
        self.but_add = QPushButton('Добавить')
        self.but_add.setDisabled(True)
        self.but_remove = QPushButton('Удалить')
        self.but_remove.setDisabled(True)
        self.but_save = QPushButton('Сохранить')
        self.but_save.setDisabled(True)


        self.box_button.addWidget(self.but_form)
        self.box_button.addWidget(self.but_add)
        self.box_button.addWidget(self.but_remove)
        self.box_button.addWidget(self.but_save)


        self.box_2.addWidget(self.text_readme)
        self.box_2.addLayout(self.box_button)
        # clipboard=QApplication.clipboard() копирование в буфере

        self.box_main.addWidget(self.titul_1)
        self.box_main.addWidget(self.table_widget)
        self.box_main.addLayout(self.box_1)
        self.box_main.addLayout(self.box_2)

        self.setLayout(self.box_main)
        self.setAcceptDrops(True)

        self.but_form.clicked.connect(self.get_text)
        self.but_add.clicked.connect(self.record_append)
        self.but_remove.clicked.connect(self.record_remove)
        self.but_save.clicked.connect(self.create_xml_file)

        self.setStyleSheet(style_1)
        self.table_widget.setStyleSheet(style)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        global files
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            text_1 = f.split('/')
            self.titul_1.setText("Путь к файлу: .\{}\n \{}\{}".format(text_1[-3], text_1[-2], text_1[-1]))
        self.but_form.setDisabled(False)

    def get_text(self):
        """Получить текст по файлу, который перетащили"""
        print(files)

        itog_text = ''
        itog_list = []
        line_count = 0
        with open(files[0]) as file:
            for line in file:
                line_count += 1
                itog_text += line
                itog_list.append(line.strip('\n'))
        print(line_count)
        self.text_readme.setText(itog_text)
        list_label = []
        if line_count > 2:
            number_val = re.findall(r'[0-99][.]\s?.+', itog_text)
            for value in number_val:
                list_label.append(value)

        self.table_widget.clear()
        labels = ["Пункт", "Комментария", 'Время выполнения', '+/-']
        self.table_widget.setColumnCount(len(labels))
        self.table_widget.setHorizontalHeaderLabels(labels)
        self.table_widget.setSortingEnabled(True)
        self.table_widget.setGridStyle(QtCore.Qt.NoPen)
        row = 0
        for r in list_label:
            time = QtCore.QTime()
            punkt = QtWidgets.QTextEdit(r)
            punkt.setStyleSheet(style_1)
            punkt.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
            comment = QtWidgets.QTextEdit()
            comment.setStyleSheet(style_1)
            # date_1 = QtWidgets.QTimeEdit()
            # date_1.setTime(time.currentTime())
            # cell_widget = QtWidgets.QWidget()
            chbk = QtWidgets.QCheckBox(parent=self.table_widget)
            chbk.setStyleSheet(style_1)
            chbk.clicked.connect(self.onStateChanged)

            # lay_out = QtWidgets.QHBoxLayout(cell_widget)
            # lay_out.addWidget(chbk)
            # lay_out.setAlignment(QtCore.Qt.AlignCenter)
            # lay_out.setContentsMargins(0, 0, 0, 0)
            # cell_widget.setLayout(lay_out)
            # text='Не выполнялась'
            self.table_widget.setRowCount(row + 1)
            self.table_widget.setCellWidget(row, 0, punkt)
            self.table_widget.setCellWidget(row, 1, comment)
            self.table_widget.setItem(row, 2, QTableWidgetItem('Не выполнялась'))
            self.table_widget.setCellWidget(row, 3, chbk)
            self.table_widget.setRowHeight(row, 100)
            self.table_widget.resizeColumnsToContents()
            self.table_widget.setColumnWidth(0, 500)
            row = row + 1
            self.but_add.setDisabled(False)
            self.but_remove.setDisabled(False)
            self.but_save.setDisabled(False)

    def create_xml_file(self):
        """Создаем XML файл"""

        print(self.table_widget)
        n = self.table_widget.rowCount()
        m = self.table_widget.columnCount()
        a = [[0] * m for i in range(n)]
        label = []
        # for k in range(m):
        #     text1 = self.table_widget.takeHorizontalHeaderItem(k).text()
        #     label.append(text1)
        for i in range(n):
            for j in range(m):
                if self.table_widget.cellWidget(i, j) == None:
                    text = self.table_widget.item(i, j).text()
                    a[i][j] = text
                else:
                    text = self.table_widget.cellWidget(i, j)
                    a[i][j] = text
        a.insert(0, label)

        # for i in a:
        #     print(i)
        print(a)
        global xml_list
        xml_list = []
        for i in a[1:]:
            xml_list_i = []
            for l in i:
                print(l)
                if 'QCheckBox' in l.__str__():
                    xml_list_i.append(l.checkState())
                elif 'QTextEdit' in l.__str__():
                    xml_list_i.append(l.toPlainText())
                else:
                    xml_list_i.append(l)
            xml_list.append(xml_list_i)

        # Получение хэш-суммы файла
        hash_file = get_hash_md5(files[0])

        # Создание xml файла
        root = xml.Element("InstallFile")
        k = 0
        for i in xml_list:
            print(i)
            k += 1
            appt = xml.Element("InstallRecord")
            item = xml.SubElement(appt, "item")
            item.text = i[0]

            comments = xml.SubElement(appt, "comments")
            comments.text = i[1]

            time_sysdate = xml.SubElement(appt, "time")
            time_sysdate.text = i[2]

            choice_option = xml.SubElement(appt, "choice_option")
            choice_option.text = str(i[3])

            root.append(appt)

        appt = xml.Element("HashAmount")
        hashAmount = xml.SubElement(appt, 'value')
        hashAmount.text = hash_file
        root.append(appt)
        k = []
        for i in files:
            k = i.split('/')
        text_path = '/'.join(k[0:-1])
        print(text_path)
        tree = xml.ElementTree(root)
        tree.write('{}/record.xml'.format(text_path))

    def record_append(self):
        """Добавляем запись"""
        # time = QtCore.QTime()
        punkt = QtWidgets.QTextEdit()
        punkt.setStyleSheet(style_1)
        comment = QtWidgets.QTextEdit()
        comment.setStyleSheet(style_1)
        # date_1 = QtWidgets.QTimeEdit()
        # date_1.setTime(time.currentTime())
        #chbk = QtWidgets.QCheckBox()
        row = self.table_widget.rowCount()
        chbk = QtWidgets.QCheckBox(parent=self.table_widget)
        chbk.setStyleSheet(style_1)
        chbk.clicked.connect(self.onStateChanged)
        self.table_widget.setRowCount(row + 1)
        self.table_widget.setCellWidget(row, 0, punkt)
        self.table_widget.setCellWidget(row, 1, comment)
        # self.table_widget.setCellWidget(row, 2, date_1)
        self.table_widget.setItem(row, 2, QTableWidgetItem('Не выполнялась'))
        self.table_widget.setCellWidget(row, 3, chbk)
        self.table_widget.setRowHeight(row, 100)
        self.table_widget.resizeColumnsToContents()
        self.table_widget.setColumnWidth(0, 500)
        row = row + 1

    def record_remove(self):
        row = set(index.row() for index in self.table_widget.selectedIndexes())
        for i in reversed(list(row)):
            self.table_widget.removeRow(int(i))


    def onStateChanged(self):
        """Действие при активации чекбокса"""

        now = datetime.datetime.now()
        date_1 = now.strftime("%d.%m.%Y")
        date_ne_pars = now.strftime("%H:%M:%S")

        chbk = self.sender()
        print(chbk.parent())
        ix = self.table_widget.indexAt(chbk.pos())
        print(ix.row(), ix.column() + 1, chbk.isChecked())
        if chbk.isChecked():
            time = QtCore.QTime()
            print(time.currentTime())
            type(time.currentTime())

            self.table_widget.setItem(ix.row(), ix.column() - 1, QTableWidgetItem(date_ne_pars))
            chbk.setDisabled(True)
        else:
            self.table_widget.setItem(ix.row(), ix.column() - 1, QTableWidgetItem('Не выполнилось'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_w = Main_Window()
    main_w.show()
    sys.exit(app.exec_())
