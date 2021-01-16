import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5 import QtWidgets, QtCore, QtGui
from UserInterface import Main_UI, Admin_Mode_login, Admin_Mode_0, Admin_Mode_1, Admin_Mode_2, Admin_Mode_3, Admin_Mode_4, Admin_Mode_5, Card_ID_Entry,Manual_ID_Entry
import function_DB
import function_log_inout
from function_log_inout import employee_verification
from function_msgbox import msg_box_ok, msg_box_ok_cancel, new_entry_get_text, new_drop_list, new_calender_get_date, msg_box_auto_close
import function_pdf
from datetime import date, datetime, timedelta
import string
import re
import numpy as np
from os import listdir
from os.path import isfile, join
import tkinter as tk
from tkinter import filedialog


# Main UI
class MainUI(QMainWindow, Main_UI.Ui_MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.manual_id_entry_ui = Manual_Id_Entry()
        self.card_id_scanning_ui = Card_ID_Scan()
        self.admin_mode_log_in_ui = Admin_Mode_Login()
        self.pushButton_ManID_Entry.clicked.connect(self.go_to_manual_id_entry)
        self.pushButton_CardID_Scan.clicked.connect(self.go_to_card_id_scanning)
        self.actionExit.triggered.connect(self.close_app)
        self.actionLog_In.triggered.connect(self.admin_mode_login)
        self.actionAbout.triggered.connect(self.about)

    def close_app(self):
        self.close()

    def admin_mode_login(self):
        self.close()
        self.admin_mode_log_in_ui.show()

    def go_to_manual_id_entry(self):
        self.close()
        self.manual_id_entry_ui.show()

    def go_to_card_id_scanning(self):
        self.close()
        self.card_id_scanning_ui.show()

    def about(self):
        msg_box_ok("<===== Attendace Recorder Version 1.0 =====>\n\n"
                   "Created by CH Corp.\n\n"
                   "Having trouble? \n"
                   "==> email to: chenhui_k029@hotmail.com")


# Manual ID Entry (Manual_ID_Entry)
class Manual_Id_Entry(QMainWindow, Manual_ID_Entry.Ui_Manual_Id_Entry):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_employee_name.setFocus()
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_Proceed.clicked.connect(self.manual_entry_submit)
        self.lineEdit_employee_id.returnPressed.connect(self.manual_entry_submit)
        self.lineEdit_employee_id.setEchoMode(QLineEdit.Password)

    def close_app(self):
        self.close()

    def navigate_back(self):
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()

    def manual_entry_submit(self):
        # Get input from UI
        employee_name = self.lineEdit_employee_name.displayText()
        employee_id = self.lineEdit_employee_id.text()
        print(f'name entered: {employee_name}')

        # Check input data
        if employee_id and employee_name:
            # Check entered employee information in database
            employee_check_result, verified_name, verified_name_id = employee_verification(employee_name=employee_name,
                                                                                           employee_id=employee_id)

            if employee_check_result:
                employee_log_in = function_log_inout.EmployeeLogInOut(verified_name, verified_name_id)
                employee_log_in.employee_log_in_out()

            else:
                msg_box_ok("Incorrect Name/ ID entry.\nPlease re-enter your name and employee ID.")

            self.lineEdit_employee_name.clear()
            self.lineEdit_employee_id.clear()
            self.lineEdit_employee_name.setFocus()

        else:
            msg_box_ok("Please enter both NAME and EMPLOYEE ID!")
            self.lineEdit_employee_name.setFocus()


# Card ID Scan (Card ID Entry)
class Card_ID_Scan(QMainWindow, Card_ID_Entry.Ui_Card_ID_Scanning):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.lineEdit_id_scan.returnPressed.connect(self.card_id_submit)
        self.lineEdit_id_scan.setEchoMode(QLineEdit.Password)

    def close_app(self):
        self.close()

    def navigate_back(self):
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()

    def card_id_submit(self):
        # Get input from UI
        card_id = self.lineEdit_id_scan.text()

        # Check input data
        if card_id:
            # Check entered employee information in database
            employee_check_result, verified_name, verified_id = employee_verification(card_id=card_id)

            if employee_check_result:
                employee_log_in = function_log_inout.EmployeeLogInOut(employee_name=verified_name,
                                                                      employee_id=verified_id)
                employee_log_in.employee_log_in_out()
            else:
                msg_box_auto_close("Invalid Card ID.\nPlease try again or contact Administrator.")

            self.lineEdit_id_scan.clear()
            self.lineEdit_id_scan.setFocus()

        else:
            msg_box_auto_close("Please scan your CARD ID!")
            self.lineEdit_id_scan.setFocus()


# Admin Mode log in Page
class Admin_Mode_Login(QMainWindow, Admin_Mode_login.Ui_Admin_Mode_LogIn):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.admin_mode_ui = Admin_Mode_Main()
        self.lineEdit_Admin_Username.setFocus()
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_Proceed.clicked.connect(self.admin_mode)
        self.lineEdit_Admin_Password.returnPressed.connect(self.admin_mode)
        self.lineEdit_Admin_Username.returnPressed.connect(self.admin_mode)

    def admin_mode(self):
        if self.lineEdit_Admin_Username.text() == "Admin" and self.lineEdit_Admin_Password.text() == "Admin":
            self.close()
            self.admin_mode_ui.show()
        else:
            msg_box_ok("Sorry!\n"
                       "Incorrect Admin Username or password entered!\n"
                       "Please try again!")
            self.lineEdit_Admin_Username.clear()
            self.lineEdit_Admin_Password.clear()
            self.lineEdit_Admin_Username.setFocus()

    def close_app(self):
        self.close()

    def navigate_back(self):
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()


# Admin Mode Main Page (Mode 0)
class Admin_Mode_Main(QMainWindow, Admin_Mode_0.Ui_Admin_Mode_0):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.am_add_employee_ui = Admin_M_Add_Employee()
        self.am_remove_employee_ui = Admin_M_Remove_Employee()
        self.am_edit_employee_ui = Admin_M_Edit_Employee()
        self.am_edit_time_log_ui = Admin_M_Edit_Timelog()
        self.am_print_time_log_ui = Admin_M_Print_Timesheet()
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_am1.clicked.connect(self.admin_mode_add_employee)
        self.pushButton_am5.clicked.connect(self.admin_mode_delete_employee)
        self.pushButton_am4.clicked.connect(self.admin_mode_edit_employee)
        self.pushButton_am3.clicked.connect(self.admin_mode_edit_timelog)
        self.pushButton_am2.clicked.connect(self.admin_mode_print_timelog)

    def close_app(self):
        self.close()

    def navigate_back(self):
        self.close()
        self.main_ui = MainUI()
        self.main_ui.show()

    def admin_mode_add_employee(self):
        self.close()
        self.am_add_employee_ui.load_read_data_to_emp_db_table()
        self.am_add_employee_ui.show()

    def admin_mode_delete_employee(self):
        self.close()
        self.am_remove_employee_ui.load_read_data_to_emp_db_table()
        self.am_remove_employee_ui.load_name_to_drop_down_list()
        self.am_remove_employee_ui.show()

    def admin_mode_edit_employee(self):
        self.close()
        self.am_edit_employee_ui.load_read_data_to_emp_db_table()
        self.am_edit_employee_ui.show()

    def admin_mode_edit_timelog(self):
        self.close()
        self.am_edit_time_log_ui.show()

    def admin_mode_print_timelog(self):
        self.close()
        self.am_print_time_log_ui.show()


# Admin Mode Add Employee (Mode 1)
class Admin_M_Add_Employee(QMainWindow, Admin_Mode_1.Ui_Admin_Mode_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.read_database = []
        self.error_msg = []
        self.no_of_read = 0
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_cancel.clicked.connect(self.navigate_back)
        self.pushButton_2.clicked.connect(self.employee_id_admission)

    # Load data from employee ID database and display to table
    def load_read_data_to_emp_db_table(self):
        self.read_database, self.no_of_read = load_employee_database_table(self.EmployeeDataBase_Table)

    # close apps
    def close_app(self):
        self.close()

    # navigate back
    def navigate_back(self):
        self.close()
        self.admin_mode_main_ui = Admin_Mode_Main()
        self.admin_mode_main_ui.show()

    # Add employee ID to database
    def employee_id_admission(self):

        # Reinitialize line edit background colour to white
        self.lineEdit_emp_name.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
        self.lineEdit_emp_id.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
        self.lineEdit_card_id.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
        self.lineEdit_emp_sal.setStyleSheet("QLineEdit{background-color: rgb(255, 255, 255);}")
        self.emp_id_add_err = False

        # Retrieve input from LineEdit
        employee_name = self.lineEdit_emp_name.displayText()
        employee_id = self.lineEdit_emp_id.displayText()
        employee_card_id = self.lineEdit_card_id.displayText()
        employee_salary = self.lineEdit_emp_sal.displayText()
        employee_status = self.comboBox_emp_stat.currentText()

        # To check for duplicate item in employee database versus user input from LineEdit
        for row_data in self.read_database:
            if employee_name == row_data[1]:
                self.emp_id_add_err = True
                self.error_msg.append(f'- Name "{employee_name}" is already in used.\n')
                # print(f'Name {employee_name} is already in used.')
                self.lineEdit_emp_name.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

            if employee_id == row_data[2]:
                self.emp_id_add_err = True
                self.error_msg.append(f'- Employee ID "{employee_id}" is already in used\n')
                # print(f'Employee ID: {employee_id} is already in used')
                self.lineEdit_emp_id.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

            if employee_card_id == row_data[3]:
                self.emp_id_add_err = True
                self.error_msg.append(f'- Employee Card ID "{employee_card_id}" is already in used\n')
                # print(f'Employee Card ID: {employee_card_id} is already in used')
                self.lineEdit_card_id.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

        # To check for empty string and invalid character in salary input Line Edit
        if employee_salary:
            try:
                float(employee_salary)
            except:
                self.error_msg.append("- Invalid Salary Input\n")
                # print("Invalid Salary Input")
                self.emp_id_add_err = True
                self.lineEdit_emp_sal.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")
        else:
            self.error_msg.append("- Employee salary is not entered\n")
            # print("Employee Salary is not entered")
            self.emp_id_add_err = True
            self.lineEdit_emp_sal.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

        # To check for empty string in Line Edit
        if not employee_name:
            self.emp_id_add_err = True
            self.error_msg.append("- Employee name is not entered\n")
            # print("Employee name is not entered")
            self.lineEdit_emp_name.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

        if not employee_id:
            self.emp_id_add_err = True
            self.error_msg.append("- Employee ID is not entered\n")
            self.lineEdit_emp_id.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

        if not employee_card_id:
            self.emp_id_add_err = True
            self.error_msg.append("- Employee card ID is not entered\n")
            self.lineEdit_card_id.setStyleSheet("QLineEdit{background-color: rgb(255, 10, 10);}")

        # If there is no error, proceed all new employee database
        if self.emp_id_add_err is False:
            round_employee_salary = round(float(employee_salary), 2)
            add_employee = function_DB.EmployeeDataBase(id=str(self.no_of_read+1),
                                                        employee_name=employee_name,
                                                        employee_id=employee_id,
                                                        card_id=employee_card_id,
                                                        employee_salary=str(round_employee_salary),
                                                        employee_stat=employee_status,
                                                        employee_join_date=date.today())
            add_employee.add_employee_to_database()

            # Reload latest data to current table
            reload_employee_database_table(self, self.EmployeeDataBase_Table)

            # Clear Line Edit Text
            self.lineEdit_emp_name.clear()
            self.lineEdit_emp_id.clear()
            self.lineEdit_card_id.clear()
            self.lineEdit_emp_sal.clear()

            # Added Succesful text
            msg_box_ok(f"Employee '{employee_name}' added succesfully!")
        else:
            # for error in self.error_msg:
            separator = "\n"
            msg_box_ok(f'Unable to proceed due to following error(s):\n \n {separator.join(self.error_msg)}')
            self.error_msg.clear()


# Admin Mode Remove Employee (Mode 2)
class Admin_M_Remove_Employee(QMainWindow, Admin_Mode_2.Ui_Admin_Mode_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.read_database = []
        self.no_of_read = 0
        self.clicked_row = 0
        # self.clicked_name = ""
        self.table_selected_name = ""
        self.selected_id_to_delete = 0
        self.selected_row = 0
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_cancel.clicked.connect(self.navigate_back)
        self.comboBox_emp_name.activated.connect(self.highlight_emp_db_table)
        self.EmployeeDataBase_Table.clicked.connect(self.check_table_click_row)
        self.pushButton_delete.clicked.connect(self.employee_id_delete)

    # close apps
    def close_app(self):
        self.close()

    # navigate back
    def navigate_back(self):
        self.close()
        self.admin_mode_main_ui = Admin_Mode_Main()
        self.admin_mode_main_ui.show()

    # Delete Employee
    def employee_id_delete(self):

        if self.selected_id_to_delete:
            msgbox_action = msg_box_ok_cancel(f"Confirm to delete employee data?")
            if msgbox_action:
                delete_database = function_DB.EmployeeDataBase(id=str(self.selected_id_to_delete))
                delete_database.delete_employee_from_database()
                deleted_row_id = int(self.selected_id_to_delete)
                update_id_employee_database = function_DB.EmployeeDataBase()
                for count in range(1, (self.no_of_read - deleted_row_id + 1)):
                    update_id_employee_database.edit_employee_database(deleted_row_id + count, 0, deleted_row_id + (count-1))
                reload_employee_database_table(self, self.EmployeeDataBase_Table)
                msg_box_ok(f"Selected employee deleted!")

        else:
            msg_box_ok("Please select an Employee Name to proceed !!\n\n(By Drop Down List / Select Name from Table)")

    # Load User Database to table
    def load_read_data_to_emp_db_table(self):
        self.read_database, self.no_of_read = load_employee_database_table(self.EmployeeDataBase_Table)

    # Load User Database to table
    def load_name_to_drop_down_list(self):
        # employee_name = ""
        self.comboBox_emp_name.clear()
        for row_data in self.read_database:
            self.comboBox_emp_name.addItem(row_data[1])

    # Get row index and highlight User Database in table when name in drop down list name was selected
    def highlight_emp_db_table(self):
        self.table_selected_name = self.comboBox_emp_name.currentText()
        items = self.EmployeeDataBase_Table.findItems(self.table_selected_name, QtCore.Qt.MatchContains)
        if items:
            self.selected_row = '\n'.join('%d' % (item.row()) for item in items)
        self.EmployeeDataBase_Table.selectRow(int(self.selected_row))

        # Set id/ name to be deleted for delete function "employee_id_delete"
        self.selected_id_to_delete = self.EmployeeDataBase_Table.item(int(self.selected_row), 0).text()

    # Get name when user directly click onto table
    def check_table_click_row(self):
        # Get clicked row
        self.clicked_row = self.EmployeeDataBase_Table.currentRow()

        # # Get name of column "1" for the any item in clicked row. (Not used in code)
        # self.clicked_name = self.EmployeeDataBase_Table.item(self.clicked_row, 1).text()

        # Set id/ name to be deleted for delete function "employee_id_delete"
        self.selected_id_to_delete = self.EmployeeDataBase_Table.item(self.clicked_row, 0).text()


# Admin Mode Edit Employee (Mode 3)
class Admin_M_Edit_Employee(QMainWindow, Admin_Mode_3.Ui_Admin_Mode_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.read_database = []
        self.error_msg = []
        self.clicked_record = []
        self.no_of_read = 0
        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_cancel.clicked.connect(self.navigate_back)
        self.pushButton_apply.clicked.connect(self.apply_edit_to_db)
        self.pushButton_search.clicked.connect(self.search_user_hide_unrelated)
        self.search_bar.returnPressed.connect(self.search_user_hide_unrelated)
        self.pushButton_clear.clicked.connect(self.search_user_unhide_all)
        self.EmployeeDataBase_Table.cellDoubleClicked.connect(self.edit_emp_db_table)

    # close apps
    def close_app(self):
        self.close()

    # navigate back
    def navigate_back(self):
        self.close()
        self.admin_mode_main_ui = Admin_Mode_Main()
        self.admin_mode_main_ui.show()

    # Load User Database to table
    def load_read_data_to_emp_db_table(self):
        self.read_database, self.no_of_read = load_employee_database_table(self.EmployeeDataBase_Table)

    # Search User based on search input bar
    def search_user_hide_unrelated(self):
        search_item = self.search_bar.displayText()
        search_item_nospace = (str(search_item).upper().translate({ord(c): None for c in string.whitespace}))
        if search_item_nospace:
            search_no_match = True
            for rowIndex in range(self.EmployeeDataBase_Table.rowCount()):
                row_name = self.EmployeeDataBase_Table.item(rowIndex, 1)
                row_emp_id = self.EmployeeDataBase_Table.item(rowIndex, 2)
                row_card_id = self.EmployeeDataBase_Table.item(rowIndex, 3)
                row_name_no_space = row_name.text().upper().translate({ord(c): None for c in string.whitespace})
                if search_item_nospace in row_name_no_space:
                    self.EmployeeDataBase_Table.setRowHidden(rowIndex, False)
                    search_no_match = False
                elif search_item_nospace in row_emp_id.text():
                    self.EmployeeDataBase_Table.setRowHidden(rowIndex, False)
                    search_no_match = False
                elif search_item_nospace in row_card_id.text():
                    self.EmployeeDataBase_Table.setRowHidden(rowIndex, False)
                    search_no_match = False
                else:
                    self.EmployeeDataBase_Table.setRowHidden(rowIndex, True)
            if search_no_match:
                msg_box_ok("Unable to find any match item!")
                self.search_user_unhide_all()
        else:
            msg_box_ok("No input to search!\n\nPlease type your input at search bar.")

    # Unhide all user in employee database table
    def search_user_unhide_all(self):
        for rowIndex in range(self.EmployeeDataBase_Table.rowCount()):
            self.EmployeeDataBase_Table.setRowHidden(rowIndex, False)
        self.search_bar.setText("")
        self.search_bar.setFocus()

    # To edit employee database table UI in admin mode.
    def edit_emp_db_table(self):
        clicked_row = self.EmployeeDataBase_Table.currentRow()
        clicked_column = self.EmployeeDataBase_Table.currentColumn()
        new_entry_edit = 0
        read_table_name = []
        read_table_id = []
        read_table_card_id = []
        read_status = []
        read_date = []
        cancel_edit = False
        # If only column name, emp_id, card_id, salary clicked.
        if 0 < clicked_column < 5:
            option_selected, new_entry_edit = new_entry_get_text()
            if option_selected:
                if new_entry_edit:
                    # Retrieve table data
                    for x in range(self.EmployeeDataBase_Table.rowCount()):
                        read_table_name.append((self.EmployeeDataBase_Table.item(x, 1).text()).upper())
                        read_table_id.append(self.EmployeeDataBase_Table.item(x, 2).text())
                        read_table_card_id.append(self.EmployeeDataBase_Table.item(x, 3).text())
                        read_status.append(self.EmployeeDataBase_Table.item(x, 4).text())
                        read_date.append(self.EmployeeDataBase_Table.item(x, 5).text())

                    # Check input versus existing data on table for not having duplicate value
                    if clicked_column == 1:
                        if str(new_entry_edit).upper() in read_table_name:
                            cancel_edit = True
                            msg_box_ok(f'- Name "{new_entry_edit}" is already in used.\nNo changes made.')

                    if clicked_column == 2:
                        try:
                            if str(new_entry_edit) in read_table_id:
                                cancel_edit = True
                                msg_box_ok(f'- Employee ID "{new_entry_edit}" is already in used\nNo changes made.')
                        except ValueError:
                            cancel_edit = True
                            msg_box_ok(f'- Invalid Input.\nPlease only input Integer/ numbers.')

                    if clicked_column == 3:
                        try:
                            if str(new_entry_edit) in read_table_card_id:
                                cancel_edit = True
                                msg_box_ok(f'- Employee ID "{new_entry_edit}" is already in used\nNo changes made.')
                        except ValueError:
                            cancel_edit = True
                            msg_box_ok(f'- Invalid Input.\nPlease only input Integer/ numbers.')

                    if clicked_column == 4:
                        try:
                            if float(new_entry_edit):
                                cancel_edit = False
                                new_entry_edit = str(float(new_entry_edit))
                        except ValueError:
                            cancel_edit = True
                            msg_box_ok(f'- Invalid Input.\nPlease only input Integer/ numbers.')

                else:
                    msg_box_ok("No Input detected.\nNo changes made.")

            else:
                cancel_edit = True

        # Use another UI for column 5
        elif clicked_column == 5:

            ok_selected, return_item = new_drop_list(["Active", "Inactive"])
            if ok_selected:
                cancel_edit = False
                new_entry_edit = return_item
            else:
                cancel_edit = True

        # Use another UI for column 6
        elif clicked_column == 6:

            ok_selected, return_item = new_calender_get_date()
            if ok_selected:
                cancel_edit = False
                new_entry_edit = str(return_item)
            else:
                cancel_edit = True

        else:
            cancel_edit = True

        # If changes are valid, update the table.
        if cancel_edit is False:
            self.EmployeeDataBase_Table.setItem(clicked_row, clicked_column, QtWidgets.QTableWidgetItem(new_entry_edit))
            self.clicked_record.append((clicked_row, clicked_column))

    # To update SQ Database
    def apply_edit_to_db(self):
        # Proceed if changes made
        if self.clicked_record:
            # To finalized change
            if msg_box_ok_cancel("Proceed to apply changes?"):
                edit_database = function_DB.EmployeeDataBase()
                print(self.clicked_record)
                for to_edit in self.clicked_record:
                    to_edit_data = self.EmployeeDataBase_Table.item(to_edit[0], to_edit[1]).text()
                    to_edit_data_id = int(self.EmployeeDataBase_Table.item(to_edit[0], 0).text())
                    edit_database.edit_employee_database(to_edit_data_id, to_edit[1], to_edit_data)

                reload_employee_database_table(self, self.EmployeeDataBase_Table)
                msg_box_ok("Changes made successful!")

        else:
            print(msg_box_ok("No changes made!"))


# Admin Mode Edit Employee time data (Mode 4)
class Admin_M_Edit_Timelog(QMainWindow, Admin_Mode_4.Ui_Admin_Mode_4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.setDisabled(True)
        self.pushButton_showtable.setDisabled(True)

        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_cancel.clicked.connect(self.navigate_back)
        self.pushButton_search.clicked.connect(self.load_time_log_db_drop_down_list)
        self.search_bar.returnPressed.connect(self.load_time_log_db_drop_down_list)
        self.comboBox.activated.connect(self.load_time_log_db_to_table)
        self.EmployeeTimeDataBase_Table.cellDoubleClicked.connect(self.entry_update_time_log_db_table)
        self.pushButton_recalculate.clicked.connect(self.recalculate_edited_timelog_to_table)
        self.pushButton_apply.clicked.connect(self.apply_changes_to_db)

        self.employee_name = ""
        self.employee_id = ""
        self.card_id = ""
        self.login_out_file_dir = ""
        self.verified_result = False

        self.time_db = []
        self.no_of_read = 0

        self.clicked_row = 0
        self.clicked_column = 0

        # Read Table Result and storage object
        self.read_table = []

        # Column id for timelog database
        self.db_column_id = 0
        self.db_column_date = 1
        self.db_column_timein = 2
        self.db_column_timeout = 3
        self.db_column_timesession = 4
        self.db_column_timeday = 5
        self.db_column_timemonth = 6

        # Column id for employee database
        self.db_emp_column_id = 0
        self.dp_emp_column_name = 1
        self.db_emp_column_id = 2
        self.dp_emp_column_card_id = 3
        self.db_emp_column_salary = 4
        self.dp_emp_column_status = 5
        self.dp_emp_column_join_date = 6

    # close apps
    def close_app(self):
        self.close()

    # navigate back
    def navigate_back(self):
        self.close()
        self.admin_mode_main_ui = Admin_Mode_Main()
        self.admin_mode_main_ui.show()

    # load time_log files to drop down list for given employee
    def load_time_log_db_drop_down_list(self):
        self.comboBox.setDisabled(True)
        self.pushButton_showtable.setDisabled(True)
        # self.EmployeeTimeDataBase_Table.clear()
        self.comboBox.clear()
        search_employee_db = self.search_bar.displayText()
        if search_employee_db:
            employee_check_result = False
            employee_database = function_DB.EmployeeDataBase()

            try:
                read_database, no_of_read = employee_database.read_employee_from_database()

                for x in range(no_of_read):
                    if (search_employee_db.upper() == read_database[x][self.dp_emp_column_name].upper() \
                            or search_employee_db == read_database[x][self.db_emp_column_id] \
                            or search_employee_db == read_database[x][self.dp_emp_column_card_id]):
                        employee_check_result = True
                        self.employee_name = read_database[x][1]
                        self.employee_id = read_database[x][2]
                        self.card_id = read_database[x][3]
                        break

                if employee_check_result:
                    self.login_out_file_dir = f'{self.employee_name.replace(" ", "")}_{self.employee_id}'
                    directory = f'.\TimeLogData\{self.login_out_file_dir}\\'
                    files = [f for f in listdir(directory) if isfile(join(directory, f))]
                    for file in files:
                        self.comboBox.addItem(file)

                    self.comboBox.setEnabled(True)
                    self.pushButton_showtable.setEnabled(True)
                    msg_box_ok("Please select time log database at drop down list.")
                else:
                    msg_box_ok("Invalid entry.\nPlease enter valid Employee Name/ ID/ Card ID.")

            except:
                msg_box_ok(f"Sorry!\n\nNo time log data available for {search_employee_db}.\nPlease login at least once for data to be available.")

        else:
            msg_box_ok("No input detected.\nPlease enter valid Employee Name/ ID/ Card ID.")

    # load time_log database to table
    def load_time_log_db_to_table(self):
        file_name = self.comboBox.currentText().split(".", 1)[0]
        self.time_db, self.no_of_read = load_time_log_db_table(self.EmployeeTimeDataBase_Table, self.login_out_file_dir, file_name)

    # Get New entry input on Time-log table
    def entry_update_time_log_db_table(self):
        self.clicked_row = self.EmployeeTimeDataBase_Table.currentRow()
        self.clicked_column = self.EmployeeTimeDataBase_Table.currentColumn()

        if self.clicked_column == self.db_column_timein or self.clicked_column == self.db_column_timeout:

            while True:
                new_entry_action, new_entry_text = new_entry_get_text()

                if new_entry_action:
                        if new_entry_text is not "":
                            # To check for correct entry input
                            pattern = re.compile("^[0-2][0-9]:[0-5][0-9]:[0-5][0-9]$")

                            if pattern.match(new_entry_text) is not None:
                                # To check the hour entry is not exceeding 23 hours, else datetime will not work

                                if int(new_entry_text.split(":", 1)[0]) < 24:

                                    # Verify user input
                                    self.verified_result = self.verify_user_new_entry(new_entry_text=new_entry_text)
                                    
                                    if self.verified_result:
                                        break

                                else:
                                    msg_box_ok("Invalid format input.\n"
                                               "\nPlease re-enter time as below:"
                                               "\n- Hours(2 digits, < 24 hours)"
                                               "\n- Minutes(2 digits, < 60 minutes)"
                                               "\n- Seconds(2 digits, < 60 seconds)")
                            else:
                                msg_box_ok("Invalid format input.\n"
                                           "\nPlease re-enter time as below:"
                                           "\n- Hours(2 digits):Minutes(2 digits):Seconds(2 digits)")
                        else:
                            msg_box_ok("No entry detected!\nNo change will be made!")
                else:
                    break

        elif self.clicked_column == 4 or self.clicked_column == 5 or self.clicked_column == 6:
            msg_box_ok("Data in this column is not editable."
                       "\nOnly \"Time In\" and \"Time Out\" can be edited."
                       "\nPlease click \"Re-Calculate\" to update the value for:"
                       "\n   a) Time Per Session"
                       "\n   b) Time Per Day"
                       "\n   c) Time Per Month")

    # Verify user input
    def verify_user_new_entry(self, new_entry_text):

        # Check edit cell date
        if self.clicked_row is not 0:
            previous_row_date = self.EmployeeTimeDataBase_Table.item(self.clicked_row - 1,
                                                                     self.db_column_date).text()
            previous_row_time = self.EmployeeTimeDataBase_Table.item(self.clicked_row - 1,
                                                                     self.db_column_timeout).text()
        else:
            previous_row_date = "1000-01-01"
            previous_row_time = "01:01:01"

        clicked_cell_date = self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.db_column_date).text()
        previous_cell_timein = self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.db_column_timein).text()

        if self.clicked_row == self.EmployeeTimeDataBase_Table.rowCount() - 1:
            next_row_date = "2999-12-31"
            next_row_time = "23:59:59"
            next_cell_timeout = "23:59:59"
        else:
            next_row_date = self.EmployeeTimeDataBase_Table.item(self.clicked_row + 1, self.db_column_date).text()
            next_row_time = self.EmployeeTimeDataBase_Table.item(self.clicked_row + 1, self.db_column_timein).text()
            next_cell_timeout = self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.db_column_timeout).text()

        # Convert text to time for comparison
        new_entry_time_obj = datetime.strptime(f'{clicked_cell_date} {new_entry_text}', '%Y-%m-%d %H:%M:%S')
        previous_row_timeout_obj = datetime.strptime(f'{previous_row_date} {previous_row_time}',
                                                     '%Y-%m-%d %H:%M:%S')

        next_row_timein_obj = datetime.strptime(f'{next_row_date} {next_row_time}', '%Y-%m-%d %H:%M:%S')
        previous_cell_timein_obj = datetime.strptime(f'{clicked_cell_date} {previous_cell_timein}',
                                                     '%Y-%m-%d %H:%M:%S')

        next_cell_timeout_obj = datetime.strptime(f'{clicked_cell_date} {next_cell_timeout}', '%Y-%m-%d %H:%M:%S')
        max_timeout_obj = datetime.strptime(f'{clicked_cell_date} 00:00:00', '%Y-%m-%d %H:%M:%S') + timedelta(days=1)

        # Check user input is correct
        # ----------------------------------------------------------------------------------------------------------------
        # If user editing time in

        if self.clicked_column == self.db_column_timein:
            if new_entry_time_obj.date() == previous_row_timeout_obj.date():
                if previous_row_timeout_obj <= new_entry_time_obj <= next_cell_timeout_obj:
                    self.EmployeeTimeDataBase_Table.setItem(self.clicked_row, self.clicked_column,
                                                            QtWidgets.QTableWidgetItem(new_entry_text))
                    self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.clicked_column).setBackground(
                        QtGui.QColor('cyan'))
                else:
                    self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.clicked_column).setBackground(
                        QtGui.QColor('red'))
                    msg_box_ok(f'The newly input time "{new_entry_time_obj}" must be:'
                               f'\n - later than previous same date time-out "{previous_row_timeout_obj}"'
                               f'\n - not later than same date time-out "{next_cell_timeout_obj}"')
            else:
                if new_entry_time_obj <= next_cell_timeout_obj:
                    self.EmployeeTimeDataBase_Table.setItem(self.clicked_row, self.clicked_column,
                                                            QtWidgets.QTableWidgetItem(new_entry_text))
                    self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.clicked_column).setBackground(
                        QtGui.QColor('cyan'))
                else:
                    msg_box_ok(f'The newly input time "{new_entry_time_obj}" must be:'
                               f'\n - not later than same date time-out "{next_cell_timeout_obj}"')

        elif self.clicked_column == self.db_column_timeout:
            if new_entry_time_obj.date() == next_row_timein_obj.date():
                if previous_cell_timein_obj <= new_entry_time_obj <= next_row_timein_obj:
                    self.EmployeeTimeDataBase_Table.setItem(self.clicked_row, self.clicked_column,
                                                            QtWidgets.QTableWidgetItem(new_entry_text))
                    self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.clicked_column).setBackground(
                        QtGui.QColor('cyan'))
                else:
                    self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.clicked_column).setBackground(
                        QtGui.QColor('red'))
                    msg_box_ok(f'The newly input time "{new_entry_time_obj}" must be:'
                               f'\n - later than previous same date time-in "{previous_cell_timein_obj}"'
                               f'\n - not later than next date time-in "{next_row_timein_obj}"')
            else:
                if max_timeout_obj >= new_entry_time_obj >= previous_cell_timein_obj:
                    self.EmployeeTimeDataBase_Table.setItem(self.clicked_row, self.clicked_column,
                                                            QtWidgets.QTableWidgetItem(new_entry_text))
                    self.EmployeeTimeDataBase_Table.item(self.clicked_row, self.clicked_column).setBackground(
                        QtGui.QColor('cyan'))
                else:
                    msg_box_ok(f'The newly input time "{new_entry_time_obj}" must be:'
                               f'\n - later than same date time-in "{previous_cell_timein_obj}"'
                               f'\n - No later than same date time out "{max_timeout_obj}"')

        return True

    # Re-calculate and load to table
    def recalculate_edited_timelog_to_table(self):

        self.read_table = self.read_all_employee_timelog_table()

        for row in range(len(self.read_table)):

            # To re-calculate time for each session per day
            # ----------------------------------------------------------------------------------------------------------------
            if self.read_table[row][self.db_column_timein] != "" and self.read_table[row][self.db_column_timeout] != "":

                date = self.read_table[row][self.db_column_date]
                # date_obj = datetime.strptime(f'{date} 23:59:59', '%Y-%m-%d %H:%M:%S').date()
                time_in = self.read_table[row][self.db_column_timein]
                time_in_obj = datetime.strptime(f'{date} {time_in}', '%Y-%m-%d %H:%M:%S')
                time_out = self.read_table[row][self.db_column_timeout]
                time_out_obj = datetime.strptime(f'{date} {time_out}', '%Y-%m-%d %H:%M:%S')

                new_time_per_session = function_log_inout.employee_time_per_session_calc(datetime_in=time_in_obj,
                                                                                         datetime_out=time_out_obj)
                # Save latest result to self.read_table
                self.read_table[row][self.db_column_timesession] = str(new_time_per_session)

                # upload re-calculated result to display table
                self.EmployeeTimeDataBase_Table.setItem(row, self.db_column_timesession, QtWidgets.QTableWidgetItem(str(new_time_per_session)))

            # To re-calculate time per day
            # ----------------------------------------------------------------------------------------------------------------
            if self.read_table[row][self.db_column_timesession] != "":

                if row == (len(self.read_table) - 1):
                    new_calculated_time_per_day = self.recalculation_time_per_day(row)

                    # Update re-calculated result to display table
                    self.EmployeeTimeDataBase_Table.setItem(row, self.db_column_timeday, QtWidgets.QTableWidgetItem(str(new_calculated_time_per_day)))

                    # # Update self.read_table
                    self.read_table[row][self.db_column_timeday] = str(new_calculated_time_per_day)

                elif self.read_table[row][self.db_column_date] != self.read_table[row + 1][self.db_column_date]:
                    new_calculated_time_per_day = self.recalculation_time_per_day(row)

                    # Update re-calculated result to display table
                    self.EmployeeTimeDataBase_Table.setItem(row, self.db_column_timeday, QtWidgets.QTableWidgetItem(str(new_calculated_time_per_day)))

                    # # Update self.read_table
                    self.read_table[row][self.db_column_timeday] = str(new_calculated_time_per_day)

            # To re-calculate time per month
            # ----------------------------------------------------------------------------------------------------------------

        if self.read_table[len(self.read_table)-1][self.db_column_timesession] != "":
            new_calculated_time_per_month = function_log_inout.employee_time_per_month_calc(time_log_db=self.read_table,
                                                                                            no_item_time_log_db=len(self.read_table))

            self.EmployeeTimeDataBase_Table.setItem(len(self.read_table)-1, self.db_column_timemonth,
                                                    QtWidgets.QTableWidgetItem(str(new_calculated_time_per_month)))
            self.read_table[len(self.read_table)-1][self.db_column_timemonth] = str(new_calculated_time_per_month)

            # Clear the time per month in previous row
            for row in range(len(self.read_table)-1):
                self.EmployeeTimeDataBase_Table.setItem(row, self.db_column_timemonth, QtWidgets.QTableWidgetItem(""))
                self.read_table[row][self.db_column_timemonth] = ""

    # Retrieve all data in display timelog table shown for re-calculation edited time
    def read_all_employee_timelog_table(self):

        read_table = []
        read_table_id = []
        read_table_date = []
        read_table_time_in = []
        read_table_time_out = []
        read_table_time_per_session = []
        read_table_time_per_day = []
        read_table_time_per_month = []

        for x in range(self.EmployeeTimeDataBase_Table.rowCount()):
            read_table_id.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_id).text())
            read_table_date.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_date).text())
            read_table_time_in.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timein).text())
            read_table_time_out.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timeout).text())
            read_table_time_per_session.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timesession).text())
            read_table_time_per_day.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timeday).text())
            read_table_time_per_month.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timemonth).text())

        read_table.extend((read_table_id, read_table_date, read_table_time_in,
                           read_table_time_out, read_table_time_per_session,
                           read_table_time_per_day, read_table_time_per_month))

        numpy_array = np.array(read_table)
        transpose = numpy_array.T
        read_table = transpose.tolist()

        return read_table

    # Algorithm for re-calculation per day
    def recalculation_time_per_day(self, current_row):

        new_time_per_session = datetime.strptime("00:00:00", '%H:%M:%S')

        for row_check in range(current_row + 1):
            new_session_time_obj = datetime.strptime(self.read_table[row_check][self.db_column_timesession], '%H:%M:%S')
            new_session_hour = new_session_time_obj.time().hour
            new_session_minute = new_session_time_obj.time().minute
            new_session_second = new_session_time_obj.time().second
            if self.read_table[row_check][self.db_column_date] == self.read_table[current_row][self.db_column_date]:
                new_time_per_session = new_time_per_session + timedelta(hours=new_session_hour,
                                                                        minutes=new_session_minute,
                                                                        seconds=new_session_second)
        return new_time_per_session.time()

    # Apply changes to database
    def apply_changes_to_db(self):

        if self.clicked_column != 0:

            self.recalculate_edited_timelog_to_table()
            update_multiple_column = function_DB.EmployeeLogInOut(self.login_out_file_dir, self.comboBox.currentText().split(".", 1)[0])

            for row in range(len(self.read_table)):
                update_multiple_column.edit_by_column(self.read_table[row][self.db_column_id],
                                                      str(self.read_table[row][self.db_column_date]),
                                                      str(self.read_table[row][self.db_column_timein]),
                                                      str(self.read_table[row][self.db_column_timeout]),
                                                      str(self.read_table[row][self.db_column_timesession]),
                                                      str(self.read_table[row][self.db_column_timeday]),
                                                      str(self.read_table[row][self.db_column_timemonth]))
            msg_box_ok("Changes made succesful.\n"
                       "Database was updated!\n\n"
                       "Click \"Back\" to navigate back to previous page.")

        else:
            msg_box_ok("No changes detected.\nNo changes to database.")


class Admin_M_Print_Timesheet(QMainWindow, Admin_Mode_5.Ui_Admin_Mode_5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.setDisabled(True)
        self.pushButton_showtable.setDisabled(True)

        self.actionExit.triggered.connect(self.close_app)
        self.actionBack.triggered.connect(self.navigate_back)
        self.pushButton_cancel.clicked.connect(self.navigate_back)

        self.pushButton_search.clicked.connect(self.load_time_log_db_drop_down_list)
        self.search_bar.returnPressed.connect(self.load_time_log_db_drop_down_list)
        self.comboBox.activated.connect(self.load_time_log_db_to_table)
        self.pushButton_print.clicked.connect(self.print_time_log_table)

        # Read Table Result and storage object
        self.read_table = []

        # Column id for timelog database
        self.db_column_id = 0
        self.db_column_date = 1
        self.db_column_timein = 2
        self.db_column_timeout = 3
        self.db_column_timesession = 4
        self.db_column_timeday = 5
        self.db_column_timemonth = 6

        # Column id for employee database
        self.db_emp_column_id = 0
        self.dp_emp_column_name = 1
        self.db_emp_column_id = 2
        self.dp_emp_column_card_id = 3
        self.db_emp_column_salary = 4
        self.dp_emp_column_status = 5
        self.dp_emp_column_join_date = 6

        self.employee_name = ""
        self.employee_id = ""
        self.card_id = ""
        self.employee_status = ""
        self.login_out_file_dir = ""
        self.verified_result = False

        self.time_db = []
        self.no_of_read = 0

    # close apps
    def close_app(self):
        self.close()

    # navigate back
    def navigate_back(self):
        self.close()
        self.admin_mode_main_ui = Admin_Mode_Main()
        self.admin_mode_main_ui.show()

    # load time_log files to drop down list for given employee
    def load_time_log_db_drop_down_list(self):

        self.comboBox.setDisabled(True)
        self.pushButton_showtable.setDisabled(True)
        self.comboBox.clear()

        search_employee_db = self.search_bar.displayText()

        if search_employee_db:
            employee_check_result = False
            employee_database = function_DB.EmployeeDataBase()
            try:
                read_database, no_of_read = employee_database.read_employee_from_database()

                for x in range(no_of_read):
                    if (search_employee_db.upper() == read_database[x][self.dp_emp_column_name].upper()
                            or search_employee_db == read_database[x][self.db_emp_column_id]
                            or search_employee_db == read_database[x][self.dp_emp_column_card_id]):
                        employee_check_result = True
                        self.employee_name = read_database[x][1]
                        self.employee_id = read_database[x][2]
                        self.card_id = read_database[x][3]
                        self.employee_status = read_database[x][5]
                        break

                if employee_check_result:
                    self.login_out_file_dir = f'{self.employee_name.replace(" ", "")}_{self.employee_id}'
                    directory = f'.\TimeLogData\{self.login_out_file_dir}\\'
                    files = [f for f in listdir(directory) if isfile(join(directory, f))]
                    for file in files:
                        self.comboBox.addItem(file)

                    self.comboBox.setEnabled(True)
                    self.pushButton_showtable.setEnabled(True)
                    msg_box_ok("Please select time log database at drop down list.")
                else:
                    msg_box_ok("Invalid entry.\nPlease enter valid Employee Name/ ID/ Card ID.")

            except:
                msg_box_ok(f"Sorry!\n\nNo time log data available for {search_employee_db}.\nPlease login at least once for data to be available.")
        else:
            msg_box_ok("No input detected.\nPlease enter valid Employee Name/ ID/ Card ID.")

    # load time_log database to table
    def load_time_log_db_to_table(self):
        file_name = self.comboBox.currentText().split(".", 1)[0]
        self.time_db, self.no_of_read = load_time_log_db_table(self.EmployeeTimeDataBase_Table, self.login_out_file_dir, file_name)

    # Print Time log data report
    def print_time_log_table(self):

        if self.no_of_read != 0 and self.search_bar.displayText() != "":
            # Ask for same directory
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askdirectory()

            if file_path:

                read_table = self.read_all_employee_timelog_table()
                month_year = self.comboBox.currentText()
                year = month_year[0:4]
                month = month_year[4:6]

                # Print report to pdf format
                title = "Time Log Report"
                pdf = function_pdf.PDF(title=title)
                pdf.set_title(title)
                pdf.set_author("Company_Time_Log")
                pdf.print_document(month, year, self.employee_name, self.employee_id, self.card_id, self.employee_status, read_table)

                if file_path[-1] != "/":
                    file_path = file_path + "/"

                try:
                    pdf.output(f"{file_path}timelog_{self.employee_name}{self.employee_id}_{year}{month}.pdf", 'F')
                    msg_box_ok(f'"timelog_{self.employee_name}{self.employee_id}_{year}{month}.pdf" printed and saved at directory:\n'
                               f'\n<{file_path}>')

                except PermissionError as error:
                    msg_box_ok(f'"timelog_{self.employee_name}{self.employee_id}_{year}{month}.pdf" is in used.\n\n'
                               f'Please close the file and retry again!')

            else:
                msg_box_ok(f"Path is not selected.\nTime log will not be print.")
        else:
            msg_box_ok(f"No time-log data chosen.\nPlease choose an option from combo box to print!")

    # Retrieve all data in display timelog table shown for re-calculation edited time
    def read_all_employee_timelog_table(self):

        read_table = []
        read_table_id = []
        read_table_date = []
        read_table_time_in = []
        read_table_time_out = []
        read_table_time_per_session = []
        read_table_time_per_day = []
        read_table_time_per_month = []

        for x in range(self.EmployeeTimeDataBase_Table.rowCount()):
            read_table_id.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_id).text())
            read_table_date.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_date).text())
            read_table_time_in.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timein).text())
            read_table_time_out.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timeout).text())
            read_table_time_per_session.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timesession).text())
            read_table_time_per_day.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timeday).text())
            read_table_time_per_month.append(self.EmployeeTimeDataBase_Table.item(x, self.db_column_timemonth).text())

        read_table.extend((read_table_id, read_table_date, read_table_time_in,
                           read_table_time_out, read_table_time_per_session,
                           read_table_time_per_day, read_table_time_per_month))

        numpy_array = np.array(read_table)
        transpose = numpy_array.T
        read_table = transpose.tolist()

        return read_table


# Reload Qt Table
def reload_employee_database_table(parent_current_ui, qt_table):
    old_sort = qt_table.horizontalHeader().sortIndicatorSection()
    old_order = qt_table.horizontalHeader().sortIndicatorOrder()
    qt_table.setSortingEnabled(False)
    parent_current_ui.load_read_data_to_emp_db_table()
    qt_table.sortItems(old_sort, old_order)
    qt_table.setSortingEnabled(True)


# # Load data from employee ID database and display to table
def load_employee_database_table(qt_table):
    read_emp_database = function_DB.EmployeeDataBase()
    read_database, no_of_read = read_emp_database.read_employee_from_database()
    numrows = 0
    qt_table.setRowCount(no_of_read)
    for x in read_database:
        qt_table.setItem(numrows, 0, QtWidgets.QTableWidgetItem(x[0]))
        qt_table.setItem(numrows, 1, QtWidgets.QTableWidgetItem(x[1]))
        qt_table.setItem(numrows, 2, QtWidgets.QTableWidgetItem(x[2]))
        qt_table.setItem(numrows, 3, QtWidgets.QTableWidgetItem(x[3]))
        qt_table.setItem(numrows, 4, QtWidgets.QTableWidgetItem(x[4]))
        qt_table.setItem(numrows, 5, QtWidgets.QTableWidgetItem(x[5]))
        qt_table.setItem(numrows, 6, QtWidgets.QTableWidgetItem(x[6]))
        numrows = numrows + 1
    return read_database, no_of_read


def load_time_log_db_table(qt_table, login_out_file_dir, login_out_file_name):
    time_database = function_DB.EmployeeLogInOut(login_out_file_dir, login_out_file_name)
    read_time_database, no_of_read_time_db = time_database.read_session()
    numrows = 0
    qt_table.setRowCount(no_of_read_time_db)
    for x in read_time_database:
        qt_table.setItem(numrows, 0, QtWidgets.QTableWidgetItem(x[0]))
        qt_table.setItem(numrows, 1, QtWidgets.QTableWidgetItem(x[1]))
        qt_table.setItem(numrows, 2, QtWidgets.QTableWidgetItem(x[2]))
        qt_table.setItem(numrows, 3, QtWidgets.QTableWidgetItem(x[3]))
        qt_table.setItem(numrows, 4, QtWidgets.QTableWidgetItem(x[4]))
        qt_table.setItem(numrows, 5, QtWidgets.QTableWidgetItem(x[5]))
        qt_table.setItem(numrows, 6, QtWidgets.QTableWidgetItem(x[6]))
        numrows = numrows + 1
    return read_time_database, no_of_read_time_db


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
