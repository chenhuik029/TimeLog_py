# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '04_Admin_Mode_01.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin_Mode_1(object):
    def setupUi(self, Admin_Mode_1):
        Admin_Mode_1.setObjectName("Admin_Mode_1")
        Admin_Mode_1.resize(1022, 835)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Admin_Mode_1.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(Admin_Mode_1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.centralwidget)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_title.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_instruction = QtWidgets.QFrame(self.centralwidget)
        self.frame_instruction.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_instruction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_instruction.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_instruction.setObjectName("frame_instruction")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_instruction)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_instruction = QtWidgets.QLabel(self.frame_instruction)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_instruction.setFont(font)
        self.label_instruction.setObjectName("label_instruction")
        self.verticalLayout_3.addWidget(self.label_instruction)
        self.verticalLayout.addWidget(self.frame_instruction)
        self.frame_input = QtWidgets.QFrame(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 233, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame_input.setPalette(palette)
        self.frame_input.setStyleSheet("b")
        self.frame_input.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_input.setObjectName("frame_input")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_input)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_input)
        self.frame.setMinimumSize(QtCore.QSize(350, 0))
        self.frame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(30)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_emp_name = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_emp_name.setFont(font)
        self.label_emp_name.setObjectName("label_emp_name")
        self.verticalLayout_4.addWidget(self.label_emp_name)
        self.label_emp_id = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_emp_id.setFont(font)
        self.label_emp_id.setObjectName("label_emp_id")
        self.verticalLayout_4.addWidget(self.label_emp_id)
        self.label_card_id = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_card_id.setFont(font)
        self.label_card_id.setObjectName("label_card_id")
        self.verticalLayout_4.addWidget(self.label_card_id)
        self.label_emp_sal = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_emp_sal.setFont(font)
        self.label_emp_sal.setObjectName("label_emp_sal")
        self.verticalLayout_4.addWidget(self.label_emp_sal)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_input)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setSpacing(30)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_emp_name = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_emp_name.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_emp_name.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_emp_name.setFont(font)
        self.lineEdit_emp_name.setAutoFillBackground(False)
        self.lineEdit_emp_name.setObjectName("lineEdit_emp_name")
        self.verticalLayout_5.addWidget(self.lineEdit_emp_name)
        self.lineEdit_emp_id = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_emp_id.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_emp_id.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_emp_id.setFont(font)
        self.lineEdit_emp_id.setObjectName("lineEdit_emp_id")
        self.verticalLayout_5.addWidget(self.lineEdit_emp_id)
        self.lineEdit_card_id = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_card_id.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_card_id.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_card_id.setFont(font)
        self.lineEdit_card_id.setObjectName("lineEdit_card_id")
        self.verticalLayout_5.addWidget(self.lineEdit_card_id)
        self.lineEdit_emp_sal = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_emp_sal.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_emp_sal.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_emp_sal.setFont(font)
        self.lineEdit_emp_sal.setObjectName("lineEdit_emp_sal")
        self.verticalLayout_5.addWidget(self.lineEdit_emp_sal)
        self.comboBox_emp_stat = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_emp_stat.setMinimumSize(QtCore.QSize(200, 30))
        self.comboBox_emp_stat.setObjectName("comboBox_emp_stat")
        self.comboBox_emp_stat.addItem("")
        self.comboBox_emp_stat.addItem("")
        self.verticalLayout_5.addWidget(self.comboBox_emp_stat)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_input)
        self.frame_button = QtWidgets.QFrame(self.centralwidget)
        self.frame_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button.setObjectName("frame_button")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_button)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_cancel = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setAutoFillBackground(False)
        self.pushButton_cancel.setStyleSheet("background: #f0f0f0")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_button)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background: #f0f0f0")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_button)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.EmployeeDataBase_Table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmployeeDataBase_Table.sizePolicy().hasHeightForWidth())
        self.EmployeeDataBase_Table.setSizePolicy(sizePolicy)
        self.EmployeeDataBase_Table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EmployeeDataBase_Table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EmployeeDataBase_Table.setLineWidth(1)
        self.EmployeeDataBase_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.EmployeeDataBase_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.EmployeeDataBase_Table.setObjectName("EmployeeDataBase_Table")
        self.EmployeeDataBase_Table.setColumnCount(7)
        self.EmployeeDataBase_Table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(0, item)
        self.EmployeeDataBase_Table.setColumnWidth(0, 30)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(1, item)
        self.EmployeeDataBase_Table.setColumnWidth(1, 270)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(2, item)
        self.EmployeeDataBase_Table.setColumnWidth(2, 200)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(3, item)
        self.EmployeeDataBase_Table.setColumnWidth(3, 100)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(4, item)
        self.EmployeeDataBase_Table.setColumnWidth(4, 100)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(5, item)
        self.EmployeeDataBase_Table.setColumnWidth(5, 150)
        item = QtWidgets.QTableWidgetItem()
        self.EmployeeDataBase_Table.setHorizontalHeaderItem(6, item)
        self.EmployeeDataBase_Table.setColumnWidth(6, 100)
        self.EmployeeDataBase_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.EmployeeDataBase_Table.horizontalHeader().setMinimumSectionSize(39)
        self.EmployeeDataBase_Table.horizontalHeader().setSortIndicatorShown(True)
        self.EmployeeDataBase_Table.horizontalHeader().setStretchLastSection(False)
        self.EmployeeDataBase_Table.verticalHeader().setVisible(False)
        self.EmployeeDataBase_Table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.EmployeeDataBase_Table)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        Admin_Mode_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Admin_Mode_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1022, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuNavigate = QtWidgets.QMenu(self.menubar)
        self.menuNavigate.setObjectName("menuNavigate")
        Admin_Mode_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Admin_Mode_1)
        self.statusbar.setObjectName("statusbar")
        Admin_Mode_1.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(Admin_Mode_1)
        self.actionExit.setObjectName("actionExit")
        self.actionBack = QtWidgets.QAction(Admin_Mode_1)
        self.actionBack.setObjectName("actionBack")
        self.menuFile.addAction(self.actionExit)
        self.menuNavigate.addAction(self.actionBack)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuNavigate.menuAction())

        self.retranslateUi(Admin_Mode_1)
        QtCore.QMetaObject.connectSlotsByName(Admin_Mode_1)

    def retranslateUi(self, Admin_Mode_1):
        _translate = QtCore.QCoreApplication.translate
        Admin_Mode_1.setWindowTitle(_translate("Admin_Mode_1", "Attendance Recorder System - Admin Mode (Add Employee ID)"))
        self.label_title.setText(_translate("Admin_Mode_1", "Administrator Mode"))
        self.label_instruction.setText(_translate("Admin_Mode_1", "Add Employee ID"))
        self.label_emp_name.setText(_translate("Admin_Mode_1", "Employee Name:\n"
"(Last Name, First Name)"))
        self.label_emp_id.setText(_translate("Admin_Mode_1", "Employee ID: \n"
"(For Manual Entry)"))
        self.label_card_id.setText(_translate("Admin_Mode_1", "Card ID: \n"
"(Please Tap Designated Card at Card Reader\n"
" to retrieve Card ID)"))
        self.label_emp_sal.setText(_translate("Admin_Mode_1", "Employee Salary:\n"
" (For Salary Disbursement Usage)"))
        self.label_2.setText(_translate("Admin_Mode_1", "Employment Status:"))
        self.lineEdit_emp_name.setPlaceholderText(_translate("Admin_Mode_1", "Employee Name..."))
        self.lineEdit_emp_id.setPlaceholderText(_translate("Admin_Mode_1", "Employee ID..."))
        self.lineEdit_card_id.setPlaceholderText(_translate("Admin_Mode_1", "Please tap RFID Card on Card Reader for Card ID..."))
        self.lineEdit_emp_sal.setPlaceholderText(_translate("Admin_Mode_1", "Employee salary..."))
        self.comboBox_emp_stat.setItemText(0, _translate("Admin_Mode_1", "Active"))
        self.comboBox_emp_stat.setItemText(1, _translate("Admin_Mode_1", "Inactive"))
        self.pushButton_cancel.setText(_translate("Admin_Mode_1", "Back"))
        self.pushButton_2.setText(_translate("Admin_Mode_1", "Apply"))
        self.label.setText(_translate("Admin_Mode_1", "Employee Database"))
        self.EmployeeDataBase_Table.setSortingEnabled(True)
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(0)
        item.setText(_translate("Admin_Mode_1", "ID"))
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(1)
        item.setText(_translate("Admin_Mode_1", "Employee Name"))
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(2)
        item.setText(_translate("Admin_Mode_1", "Employee ID"))
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(3)
        item.setText(_translate("Admin_Mode_1", "Card ID"))
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(4)
        item.setText(_translate("Admin_Mode_1", "Salary"))
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(5)
        item.setText(_translate("Admin_Mode_1", "Employee Status"))
        item = self.EmployeeDataBase_Table.horizontalHeaderItem(6)
        item.setText(_translate("Admin_Mode_1", "Date Joined"))
        self.menuFile.setTitle(_translate("Admin_Mode_1", "File"))
        self.menuNavigate.setTitle(_translate("Admin_Mode_1", "Navigate"))
        self.actionExit.setText(_translate("Admin_Mode_1", "Exit"))
        self.actionBack.setText(_translate("Admin_Mode_1", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin_Mode_1 = QtWidgets.QMainWindow()
    ui = Ui_Admin_Mode_1()
    ui.setupUi(Admin_Mode_1)
    Admin_Mode_1.show()
    sys.exit(app.exec_())