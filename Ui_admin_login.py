# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学业\研究生\研一\数据库系统与原理\admin_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_login(object):
    def setupUi(self, admin_login):
        admin_login.setObjectName("admin_login")
        admin_login.resize(371, 250)
        self.widget = QtWidgets.QWidget(admin_login)
        self.widget.setGeometry(QtCore.QRect(50, 70, 252, 57))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.uname_input = QtWidgets.QLineEdit(self.widget)
        self.uname_input.setObjectName("uname_input")
        self.gridLayout.addWidget(self.uname_input, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pwd_input = QtWidgets.QLineEdit(self.widget)
        self.pwd_input.setObjectName("pwd_input")
        self.gridLayout.addWidget(self.pwd_input, 1, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(admin_login)
        self.widget1.setGeometry(QtCore.QRect(80, 180, 195, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_button = QtWidgets.QPushButton(self.widget1)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.cancel_button = QtWidgets.QPushButton(self.widget1)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)

        self.retranslateUi(admin_login)
        QtCore.QMetaObject.connectSlotsByName(admin_login)

    def retranslateUi(self, admin_login):
        _translate = QtCore.QCoreApplication.translate
        admin_login.setWindowTitle(_translate("admin_login", "Form"))
        self.label.setText(_translate("admin_login", "用户名"))
        self.label_2.setText(_translate("admin_login", "密码"))
        self.login_button.setText(_translate("admin_login", "确定"))
        self.cancel_button.setText(_translate("admin_login", "取消"))
