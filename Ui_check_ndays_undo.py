# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\学业\研究生\研一\数据库系统与原理\check_ndays_undo.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_check_ndays_undo(object):
    def setupUi(self, check_ndays_undo):
        check_ndays_undo.setObjectName("check_ndays_undo")
        check_ndays_undo.resize(530, 285)
        self.widget = QtWidgets.QWidget(check_ndays_undo)
        self.widget.setGeometry(QtCore.QRect(10, 10, 511, 264))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.n_day_box = QtWidgets.QSpinBox(self.widget)
        self.n_day_box.setObjectName("n_day_box")
        self.horizontalLayout.addWidget(self.n_day_box)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.project_combox = QtWidgets.QComboBox(self.widget)
        self.project_combox.setObjectName("project_combox")
        self.project_combox.addItem("")
        self.project_combox.addItem("")
        self.horizontalLayout.addWidget(self.project_combox)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.show_table = QtWidgets.QTableWidget(self.widget)
        self.show_table.setObjectName("show_table")
        self.show_table.setColumnCount(0)
        self.show_table.setRowCount(0)
        self.verticalLayout.addWidget(self.show_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.check_button = QtWidgets.QPushButton(self.widget)
        self.check_button.setObjectName("check_button")
        self.horizontalLayout_2.addWidget(self.check_button)
        self.return_button = QtWidgets.QPushButton(self.widget)
        self.return_button.setObjectName("return_button")
        self.horizontalLayout_2.addWidget(self.return_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(check_ndays_undo)
        QtCore.QMetaObject.connectSlotsByName(check_ndays_undo)

    def retranslateUi(self, check_ndays_undo):
        _translate = QtCore.QCoreApplication.translate
        check_ndays_undo.setWindowTitle(_translate("check_ndays_undo", "统计连续多日未完成的同学信息"))
        self.label.setText(_translate("check_ndays_undo", "连续"))
        self.label_2.setText(_translate("check_ndays_undo", "天未完成"))
        self.project_combox.setItemText(0, _translate("check_ndays_undo", "健康打卡"))
        self.project_combox.setItemText(1, _translate("check_ndays_undo", "核酸检测"))
        self.label_3.setText(_translate("check_ndays_undo", "的同学信息"))
        self.check_button.setText(_translate("check_ndays_undo", "确认"))
        self.return_button.setText(_translate("check_ndays_undo", "返回"))
