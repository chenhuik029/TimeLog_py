import sys
import os.path
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication


def check_path_existence(path_defined):
    # To check if current path exist
    if not os.path.exists(path_defined):
        try:
            os.mkdir(path_defined)
        except OSError:
            print("Creation of the directory %s failed" % path_defined)
        else:
            print("Successfully created the directory %s " % path_defined)
    else:
        # print(f'Folder {path_defined} has existed.')
        pass


class EmployeeDataBase:
    def __init__(self, id=None, employee_name=None, employee_id=None, card_id=None, employee_salary=None,
                 employee_stat="Active", employee_join_date=None):
        self.id = id
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.card_id = card_id
        self.employee_salary = employee_salary
        self.employee_stat = employee_stat
        self.employee_joined_date = employee_join_date
        self.read_id = []
        self.read_emp_name = []
        self.read_emp_id = []
        self.read_card_id = []
        self.read_emp_sal = []
        self.read_emp_stat = []
        self.read_emp_j_date = []

    def add_employee_to_database(self):
        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = "./Database"
        check_path_existence(path_defined)
        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        connection = sqlite3.connect('./Database/employee_database.db')

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.cursor()
        try:
            # Create a table
            cursor.execute(('''CREATE TABLE employee_database
                            (id, employee_name, employee_id, card_id, employee_salary, employee_stat, employee_join_date)'''))

        except sqlite3.OperationalError:
            connection.rollback()
            print('Table not created as it has been created')

        # -------------------------------------------------------------
        # Insert a row of data
        # --------------------------------------------------------------
        data = [(self.id, self.employee_name, self.employee_id, self.card_id, self.employee_salary, self.employee_stat, self.employee_joined_date)]
        cursor.executemany("INSERT INTO employee_database VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        connection.commit()
        connection.close()

    def delete_employee_from_database(self):
        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = "./Database"
        check_path_existence(path_defined)
        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        connection = sqlite3.connect('./Database/employee_database.db')

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.cursor()

        # -------------------------------------------------------------
        # Delete a row of data
        # --------------------------------------------------------------
        try:
            cursor.execute("DELETE FROM employee_database WHERE id=?", (self.id,))
            connection.commit()
        except:
            connection.rollback()

        connection.close()

    def read_employee_from_database(self):
        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = "./Database"
        check_path_existence(path_defined)

        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        connection = sqlite3.connect('./Database/employee_database.db')

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.execute("SELECT count(name) FROM sqlite_master WHERE type='table' "
                                    "AND name='employee_database'")

        # ------------------------------------------------------------
        # Check if table exist in database
        # ------------------------------------------------------------
        if cursor.fetchone()[0] == 1:
            pass
        else:
            try:
                # Create a table
                # print('Table is not available, a new table is created.')
                cursor.execute(('''CREATE TABLE employee_database
                                (id, employee_name, employee_id, card_id, employee_salary, employee_stat, 
                                employee_join_date)'''))

            except sqlite3.OperationalError:
                connection.rollback()
                # print('Table not created as it has been created')
        connection.commit()
        # ------------------------------------------------------------
        # Check data is already exist before insert new data
        # ------------------------------------------------------------

        # cursor.execute()
        cursor.execute('SELECT * FROM employee_database')
        data_received = cursor.fetchall()
        # print('Reading database and check for existent name')
        # print(f'Total existent employee : {len(data_received)}')
        # print(data_received)
        return data_received, len(data_received)

    def edit_employee_database(self, data_row_id, column_item_to_update, new_data):
        column_name = {
            0: "id",
            1: "employee_name",
            2: "employee_id",
            3: "card_id",
            4: "employee_salary",
            5: "employee_stat",
            6: "employee_join_date"
        }

        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = "./Database"
        check_path_existence(path_defined)
        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        connection = sqlite3.connect('./Database/employee_database.db')

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.cursor()

        # -------------------------------------------------------------
        # Delete a row of data
        # --------------------------------------------------------------
        try:
            cursor.execute(f"UPDATE employee_database SET {column_name[column_item_to_update]} = ? WHERE id = ?",
                           (str(new_data), str(data_row_id)))
            connection.commit()
        except:
            connection.rollback()
        connection.close()


class EmployeeLogInOut:
    def __init__(self, dir_name, file_name, id="", emp_name="", date="", time_in="",
                 time_out="", time_per_session="", time_per_day="", time_per_month=""):
        self.id = id
        self.dir_name = dir_name
        self.file_name = file_name
        self.emp_name = emp_name
        self.date = date
        self.time_in = time_in
        self.time_out = time_out
        self.time_per_session = time_per_session
        self.time_per_day = time_per_day
        self.time_per_month = time_per_month

    def add_session(self):
        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = f"./TimeLogData"
        check_path_existence(path_defined)
        path_defined = f"./TimeLogData/{self.dir_name}"
        check_path_existence(path_defined)
        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        db_file_directory = f'{path_defined}/{self.file_name}.db'
        connection = sqlite3.connect(db_file_directory)

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.cursor()
        try:
            # Create a table
            cursor.execute(('''CREATE TABLE employee_log_in_out
                            (id, session_date, time_in, time_out, 
                            time_per_session, time_work_per_day, total_work_hour_per_month)'''))

        except sqlite3.OperationalError:
            connection.rollback()
            print('Table not created as it has been created')

        # -------------------------------------------------------------
        # Insert a row of data
        # --------------------------------------------------------------
        data = [(self.id, self.date, self.time_in, self.time_out, self.time_per_session, self.time_per_day,
                 self.time_per_month)]
        cursor.executemany("INSERT INTO employee_log_in_out VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        connection.commit()
        connection.close()

    def del_session(self):
        pass

    def edit_session(self, data_row_id, column_item_to_update, new_data):
        column_name = {
            0: "id",
            1: "session_date",
            2: "time_in",
            3: "time_out",
            4: "time_per_session",
            5: "time_work_per_day",
            6: "total_work_hour_per_month"
        }

        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = f"./TimeLogData"
        check_path_existence(path_defined)
        path_defined = f"./TimeLogData/{self.dir_name}"
        check_path_existence(path_defined)
        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        db_file_directory = f'{path_defined}/{self.file_name}.db'
        connection = sqlite3.connect(db_file_directory)

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.cursor()

        # -------------------------------------------------------------
        # Delete a row of data
        # --------------------------------------------------------------
        try:
            cursor.execute(f"UPDATE employee_log_in_out SET {column_name[column_item_to_update]} = ? WHERE id = ?",
                           (str(new_data), str(data_row_id)))
            connection.commit()
        except:
            connection.rollback()
            print(f'Fatal error: Item to EDIT at row {self.id} is not available in the database table')
        connection.close()

    def read_session(self):
        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = f"./TimeLogData"
        check_path_existence(path_defined)
        path_defined = f"./TimeLogData/{self.dir_name}"
        check_path_existence(path_defined)
        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        db_file_directory = f'{path_defined}/{self.file_name}.db'
        connection = sqlite3.connect(db_file_directory)

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.execute("SELECT count(name) FROM sqlite_master WHERE type='table' "
                                    "AND name='employee_log_in_out'")

        # ------------------------------------------------------------
        # Check if table exist in database
        # ------------------------------------------------------------
        if cursor.fetchone()[0] == 1:
            pass
        else:
            try:
                cursor.execute(('''CREATE TABLE employee_log_in_out
                            (id, session_date, time_in, time_out, 
                            time_per_session, time_work_per_day, total_work_hour_per_month)'''))

            except sqlite3.OperationalError:
                connection.rollback()
                print(f'Fatal error: Item to READ at row {self.id} is not available in the database table')
        connection.commit()

        # ------------------------------------------------------------
        # Check data is already exist before insert new data
        # ------------------------------------------------------------
        cursor.execute('SELECT * FROM employee_log_in_out')
        data_received = cursor.fetchall()
        # print('Reading database and check for existent name')
        # print(f'Total existent employee : {len(data_received)}')
        # print(data_received)
        return data_received, len(data_received)

    def edit_by_column(self, id, session_date, time_in, time_out, time_per_session, time_work_per_day,
                       total_work_hour_per_month):

        column_name = {
            0: "id",
            1: "session_date",
            2: "time_in",
            3: "time_out",
            4: "time_per_session",
            5: "time_work_per_day",
            6: "total_work_hour_per_month"
        }

        # ------------------------------------------------------
        # Check Directory existence
        # ------------------------------------------------------
        path_defined = f"./TimeLogData"
        check_path_existence(path_defined)
        path_defined = f"./TimeLogData/{self.dir_name}"
        check_path_existence(path_defined)

        # ------------------------------------------------------------
        # open database connection
        # ------------------------------------------------------------
        db_file_directory = f'{path_defined}/{self.file_name}.db'
        connection = sqlite3.connect(db_file_directory)

        # ------------------------------------------------------------
        # Prepare a cursor object using cursor() method
        # ------------------------------------------------------------
        cursor = connection.cursor()

        # -------------------------------------------------------------
        # Delete a row of data
        # --------------------------------------------------------------
        try:
            sqlite_update_query = f"UPDATE employee_log_in_out SET session_date = ?, time_in = ?, time_out = ?, time_per_session = ?, time_work_per_day = ?, total_work_hour_per_month = ? where id = ?"
            columnValues = (session_date, time_in, time_out, time_per_session, time_work_per_day, total_work_hour_per_month, id)
            cursor.execute(sqlite_update_query, columnValues)
            connection.commit()

        except sqlite3.Error as error:
            connection.rollback()
            print(f'Fatal error: Unable to update multiple column of data', error)

        connection.close()