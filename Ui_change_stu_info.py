# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学业\研究生\研一\数据库系统与原理\change_stu_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_change_stu_info(object):
    def setupUi(self, change_stu_info):
        change_stu_info.setObjectName("change_stu_info")
        change_stu_info.resize(366, 137)
        self.widget = QtWidgets.QWidget(change_stu_info)
        self.widget.setGeometry(QtCore.QRect(30, 20, 313, 98))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.student_id_input = QtWidgets.QLineEdit(self.widget)
        self.student_id_input.setObjectName("student_id_input")
        self.horizontalLayout.addWidget(self.student_id_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.project_combox = QtWidgets.QComboBox(self.widget)
        self.project_combox.setObjectName("project_combox")
        self.project_combox.addItem("")
        self.project_combox.addItem("")
        self.project_combox.addItem("")
        self.project_combox.addItem("")
        self.horizontalLayout_2.addWidget(self.project_combox)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.change_result_input = QtWidgets.QLineEdit(self.widget)
        self.change_result_input.setObjectName("change_result_input")
        self.horizontalLayout_2.addWidget(self.change_result_input)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.commit_button = QtWidgets.QPushButton(self.widget)
        self.commit_button.setObjectName("commit_button")
        self.horizontalLayout_3.addWidget(self.commit_button)
        self.return_button = QtWidgets.QPushButton(self.widget)
        self.return_button.setObjectName("return_button")
        self.horizontalLayout_3.addWidget(self.return_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(change_stu_info)
        QtCore.QMetaObject.connectSlotsByName(change_stu_info)

    def retranslateUi(self, change_stu_info):
        _translate = QtCore.QCoreApplication.translate
        change_stu_info.setWindowTitle(_translate("change_stu_info", "更改学生信息"))
        self.label.setText(_translate("change_stu_info", "修改学号为"))
        self.label_2.setText(_translate("change_stu_info", "的"))
        self.project_combox.setItemText(0, _translate("change_stu_info", "姓名"))
        self.project_combox.setItemText(1, _translate("change_stu_info", "居住地"))
        self.project_combox.setItemText(2, _translate("change_stu_info", "电话"))
        self.project_combox.setItemText(3, _translate("change_stu_info", "所属学院"))
        self.label_3.setText(_translate("change_stu_info", "为"))
        self.commit_button.setText(_translate("change_stu_info", "确认"))
        self.return_button.setText(_translate("change_stu_info", "返回"))
