# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学业\研究生\研一\数据库系统与原理\add_new_stu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_add_new_stu(object):
    def setupUi(self, add_new_stu):
        add_new_stu.setObjectName("add_new_stu")
        add_new_stu.resize(283, 245)
        self.widget = QtWidgets.QWidget(add_new_stu)
        self.widget.setGeometry(QtCore.QRect(20, 20, 242, 205))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.sname_input = QtWidgets.QLineEdit(self.widget)
        self.sname_input.setObjectName("sname_input")
        self.gridLayout.addWidget(self.sname_input, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.sid_input = QtWidgets.QLineEdit(self.widget)
        self.sid_input.setObjectName("sid_input")
        self.gridLayout.addWidget(self.sid_input, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.apartment_combox = QtWidgets.QComboBox(self.widget)
        self.apartment_combox.setObjectName("apartment_combox")
        self.apartment_combox.addItem("")
        self.apartment_combox.addItem("")
        self.gridLayout.addWidget(self.apartment_combox, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.tel_input = QtWidgets.QLineEdit(self.widget)
        self.tel_input.setObjectName("tel_input")
        self.gridLayout.addWidget(self.tel_input, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.department_combox = QtWidgets.QComboBox(self.widget)
        self.department_combox.setObjectName("department_combox")
        self.gridLayout.addWidget(self.department_combox, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.commit_button = QtWidgets.QPushButton(self.widget)
        self.commit_button.setObjectName("commit_button")
        self.horizontalLayout.addWidget(self.commit_button)
        self.cancel_botton = QtWidgets.QPushButton(self.widget)
        self.cancel_botton.setObjectName("cancel_botton")
        self.horizontalLayout.addWidget(self.cancel_botton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(add_new_stu)
        QtCore.QMetaObject.connectSlotsByName(add_new_stu)

    def retranslateUi(self, add_new_stu):
        _translate = QtCore.QCoreApplication.translate
        add_new_stu.setWindowTitle(_translate("add_new_stu", "Form"))
        self.label.setText(_translate("add_new_stu", "添加新的学生信息"))
        self.label_2.setText(_translate("add_new_stu", "姓名"))
        self.label_3.setText(_translate("add_new_stu", "学号"))
        self.label_4.setText(_translate("add_new_stu", "居住地"))
        self.apartment_combox.setItemText(0, _translate("add_new_stu", "创新港"))
        self.apartment_combox.setItemText(1, _translate("add_new_stu", "兴庆"))
        self.label_5.setText(_translate("add_new_stu", "电话"))
        self.label_6.setText(_translate("add_new_stu", "所属院系"))
        self.commit_button.setText(_translate("add_new_stu", "确认"))
        self.cancel_botton.setText(_translate("add_new_stu", "取消"))
