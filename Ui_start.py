# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学业\研究生\研一\数据库系统与原理\start.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_START(object):
    def setupUi(self, START):
        START.setObjectName("START")
        START.resize(408, 260)
        self.OK = QtWidgets.QPushButton(START)
        self.OK.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.OK.setObjectName("OK")
        self.widget = QtWidgets.QWidget(START)
        self.widget.setGeometry(QtCore.QRect(100, 50, 191, 82))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(START)
        QtCore.QMetaObject.connectSlotsByName(START)

    def retranslateUi(self, START):
        _translate = QtCore.QCoreApplication.translate
        START.setWindowTitle(_translate("START", "START"))
        self.OK.setText(_translate("START", "OK"))
        self.label.setText(_translate("START", "选择身份"))
        self.comboBox.setItemText(0, _translate("START", "学生"))
        self.comboBox.setItemText(1, _translate("START", "管理员"))