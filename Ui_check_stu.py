# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学业\研究生\研一\数据库系统与原理\check_stu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_check_stu(object):
    def setupUi(self, check_stu):
        check_stu.setObjectName("check_stu")
        check_stu.resize(572, 269)
        self.show_table = QtWidgets.QTableWidget(check_stu)
        self.show_table.setGeometry(QtCore.QRect(10, 60, 451, 192))
        self.show_table.setObjectName("show_table")
        self.show_table.setColumnCount(0)
        self.show_table.setRowCount(0)
        self.widget = QtWidgets.QWidget(check_stu)
        self.widget.setGeometry(QtCore.QRect(10, 20, 551, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.student_id_input = QtWidgets.QLineEdit(self.widget)
        self.student_id_input.setObjectName("student_id_input")
        self.horizontalLayout.addWidget(self.student_id_input)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.project_combox = QtWidgets.QComboBox(self.widget)
        self.project_combox.setObjectName("project_combox")
        self.project_combox.addItem("")
        self.project_combox.addItem("")
        self.horizontalLayout.addWidget(self.project_combox)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.date_box = QtWidgets.QSpinBox(self.widget)
        self.date_box.setObjectName("date_box")
        self.horizontalLayout.addWidget(self.date_box)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.widget1 = QtWidgets.QWidget(check_stu)
        self.widget1.setGeometry(QtCore.QRect(470, 180, 95, 65))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_button = QtWidgets.QPushButton(self.widget1)
        self.check_button.setObjectName("check_button")
        self.verticalLayout.addWidget(self.check_button)
        self.return_button = QtWidgets.QPushButton(self.widget1)
        self.return_button.setObjectName("return_button")
        self.verticalLayout.addWidget(self.return_button)

        self.retranslateUi(check_stu)
        QtCore.QMetaObject.connectSlotsByName(check_stu)

    def retranslateUi(self, check_stu):
        _translate = QtCore.QCoreApplication.translate
        check_stu.setWindowTitle(_translate("check_stu", "Form"))
        self.label.setText(_translate("check_stu", "查询学号"))
        self.label_4.setText(_translate("check_stu", "的"))
        self.project_combox.setItemText(0, _translate("check_stu", "健康打卡"))
        self.project_combox.setItemText(1, _translate("check_stu", "核酸检测"))
        self.label_2.setText(_translate("check_stu", "在"))
        self.label_3.setText(_translate("check_stu", "天内的情况"))
        self.check_button.setText(_translate("check_stu", "查询"))
        self.return_button.setText(_translate("check_stu", "返回"))