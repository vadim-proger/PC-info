# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("PC info")
        Dialog.resize(749, 638)
        Dialog.setStyleSheet("background-color:#0419d6")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(310, 90, 121, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: #fff;\n"
"    background-color: #1e2026;\n"
"    border: none;\n"
"    font: 75 11pt \"Ubuntu Mono\";\n"
"}\n"
"QPushButton:hover{\n"
"    color: #f7ff9c;\n"
"    background-color: #291ac9;\n"
"}\n"
"QPushButton:pressed{\n"
"    color: #ffc757;\n"
"    background-color: #2354cf;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(10, 20, 731, 21))
        self.comboBox.setStyleSheet("color: #fff;\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"background-color: #14098f;\n"
"border: none;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 200, 731, 431))
        self.textBrowser.setStyleSheet("color:#fff;")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PC info"))
        self.pushButton.setText(_translate("Dialog", "Get info"))
        self.comboBox.setItemText(0, _translate("Dialog", "Host_info"))
        self.comboBox.setItemText(1, _translate("Dialog", "CPU"))
        self.comboBox.setItemText(2, _translate("Dialog", "Memory"))
        self.comboBox.setItemText(3, _translate("Dialog", "Distribution"))
        self.comboBox.setItemText(4, _translate("Dialog", "Core"))
        self.comboBox.setItemText(5, _translate("Dialog", "Architecture"))
        self.comboBox.setItemText(6, _translate("Dialog", "Disk space"))
        self.comboBox.setItemText(7, _translate("Dialog", "USB"))
        self.comboBox.setItemText(8, _translate("Dialog", "Network interfaces"))
        self.comboBox.setItemText(9, _translate("Dialog", "GPU"))
        self.comboBox.setItemText(10, _translate("Dialog", "Audio"))
