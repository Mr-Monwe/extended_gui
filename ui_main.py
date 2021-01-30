# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 503)
        MainWindow.setStyleSheet("background-color:none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tlwg Typo")
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet("QFrame{\n"
                                 "    background-color : rgb(92, 53, 102);\n"
                                 "    color : rgb(220, 220, 220);\n"
                                 "    border-radius: 10px;\n"
                                 "}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dropdown = QtWidgets.QComboBox(self.frame)
        self.dropdown.setGeometry(QtCore.QRect(220, 210, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.dropdown.setFont(font)
        self.dropdown.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dropdown.setStyleSheet("background-color: rgb(98, 114, 164);\n"
                                    "color: rgb(238, 238, 236); ")
        self.dropdown.setObjectName("dropdown")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.dropdown.addItem("")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 110, 731, 71))
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK SC")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(254, 121, 199);\n"
                                 "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.select = QtWidgets.QPushButton(self.frame)
        self.select.setGeometry(QtCore.QRect(350, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(11)
        self.select.setFont(font)
        self.select.setStyleSheet("background-color: rgb(98, 114, 164);\n"
                                  "color: rgb(238, 238, 236); ")
        self.select.setObjectName("select")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WSU Robotics Command Center"))
        self.dropdown.setCurrentText(_translate("MainWindow", "Main Competition"))
        self.dropdown.setItemText(0, _translate("MainWindow", "Main Competition"))
        self.dropdown.setItemText(1, _translate("MainWindow", "Lane Mode"))
        self.dropdown.setItemText(2, _translate("MainWindow", "Speed Mode"))
        self.dropdown.setItemText(3, _translate("MainWindow", "Obstacle Mode"))
        self.dropdown.setItemText(4, _translate("MainWindow", "Waypoint Mode"))
        self.dropdown.setItemText(5, _translate("MainWindow", "Init Param Server"))
        self.dropdown.setItemText(6, _translate("MainWindow", "Status Check"))
        self.dropdown.setItemText(7, _translate("MainWindow", "Kill All "))
        self.label.setText(_translate("MainWindow", "SELECT & LAUNCH A <strong>MODE</strong>"))
        self.select.setText(_translate("MainWindow", "Select"))
