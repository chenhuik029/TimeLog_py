import function_DB
from datetime import date, datetime, timedelta
from function_msgbox import msg_box_auto_close
import calendar
import os.path


# -----------------------------------------------------------------------------------------------------
# Employee ID Verification
# -----------------------------------------------------------------------------------------------------
def employee_verification(employee_name=None, employee_id=None, card_id=None):
    match = False
    employee_database = function_DB.EmployeeDataBase()
    read_database, no_of_read = employee_database.read_employee_from_database()

    for x in range(no_of_read):

        if card_id is None:
            if employee_name.upper() == read_database[x][1].upper() and employee_id == read_database[x][2]:
                match = True
                break

        else:
            if card_id == read_database[x][3]:
                employee_name = read_database[x][1]
                employee_id = read_database[x][2]
                match = True
                break

    return match, employee_name, employee_id


def employee_time_per_session_calc(datetime_in=None, datetime_out=None):

    # Lunch session time per day
    lunch_session = 45
    dinner_session = 45

    if datetime_in is not None and datetime_out is not None:

        # Calculate time work per session if no go out for lunch/ dinner
        if datetime_in.time() <= datetime.strptime("11:15:00", '%H:%M:%S').time() and \
                datetime_out.time() >= datetime.strptime("13:15:00", '%H:%M:%S').time():
            calculated_time_diff = datetime_out - datetime_in
            if datetime_in.time() <= datetime.strptime("18:00:00", '%H:%M:%S').time() and \
                    datetime_out.time() >= datetime.strptime("20:00:00", '%H:%M:%S').time():
                calculated_time_diff = calculated_time_diff - \
                                       timedelta(minutes=lunch_session) - \
                                       timedelta(minutes=dinner_session)
            else:
                calculated_time_diff = calculated_time_diff - timedelta(minutes=lunch_session)

        # Calculate Time work per session if log out for lunch/dinner
        else:
            calculated_time_diff = datetime_out - datetime_in

        time_diff_in_sec = calculated_time_diff.total_seconds()
        minutes, sec = divmod(time_diff_in_sec, 60)
        hours, minutes = divmod(minutes, 60)
        calculated_time_session = "%02d:%02d:%02d" % (hours, minutes, sec)

    else:
        calculated_time_session = "%02d:%02d:%02d" % (22, 29, 59)

    return calculated_time_session


def employee_time_per_day_calc(time_log_db=None, no_item_time_log_db=0, log_out_date=None, new_session_time="00:00:00"):

    new_session_time_obj = datetime.strptime(new_session_time, '%H:%M:%S')
    new_session_hour = new_session_time_obj.time().hour
    new_session_minute = new_session_time_obj.time().minute
    new_session_second = new_session_time_obj.time().second

    time_session = new_session_time_obj

    if no_item_time_log_db > 1:
        date_time_log_db = datetime.strptime(time_log_db[no_item_time_log_db - 2][1], '%Y-%m-%d').date()

        if date_time_log_db == log_out_date:
            datetime_session_db_obj = datetime.strptime(time_log_db[no_item_time_log_db-2][5], '%H:%M:%S')
            time_session = datetime_session_db_obj + timedelta(hours=new_session_hour, minutes=new_session_minute, seconds=new_session_second)

    return time_session.time()


def employee_time_per_month_calc(time_log_db=None, no_item_time_log_db=0, latest_time_session="00:00:00"):

    time_b4_add_obj = datetime.strptime("00:00:00", '%H:%M:%S')
    time_af_add_obj = time_b4_add_obj
    latest_time_session_obj = datetime.strptime(latest_time_session, '%H:%M:%S')

    for item in range(no_item_time_log_db):

        if time_log_db[item][5] is not "":

            date_time_session = datetime.strptime(time_log_db[item][5], '%H:%M:%S')
            time_af_add_obj = time_af_add_obj + timedelta(hours=date_time_session.hour,
                                                          minutes=date_time_session.minute,
                                                          seconds=date_time_session.second)

    time_af_add_obj = time_af_add_obj + timedelta(hours=latest_time_session_obj.hour,
                                                  minutes=latest_time_session_obj.minute,
                                                  seconds=latest_time_session_obj.second)

    total_time_per_month_obj = time_af_add_obj - time_b4_add_obj
    time_total = total_time_per_month_obj.total_seconds()
    minutes, sec = divmod(time_total, 60)
    hours, minutes = divmod(minutes, 60)
    calculated_time_session = "%03d:%02d:%02d" % (hours, minutes, sec)

    return calculated_time_session


class EmployeeLogInOut:
    def __init__(self, employee_name=None, employee_id=None, card_id=None):
        self.employee_name = employee_name
        self.employee_id = str(employee_id)
        self.card_id = str(card_id)
        self.read_database = []
        self.no_of_read = 0
        self.get_date = 0
        self.time_log_id_data = []
        self.calculated_time_diff = timedelta(days=0)
        self.write_time_out = ""
        self.write_time_in = ""
        self.get_date_time = None
        self.time_per_session = ""
        self.get_date = date.today()
        self.get_datetime_now = datetime.now()
        self.login_out_file_name = ""

    # -----------------------------------------------------------------------------------------------------
    # Log in and out processes
    # -----------------------------------------------------------------------------------------------------
    def employee_log_in_out(self):

        # Get current date and time
        get_year = date.today().year
        get_month = date.today().month
        add_new_day_time_in = False
        add_new_day_time_out = False
        add_same_day_time_in = False
        add_same_day_time_out = False
        add_working_time_for_previous_month = False
        absent_day = False
        absent_day_previous_month = False

        write_id_in_previous_month = 0

        time_per_session_per_day = []
        time_per_session_day_pre_month = []
        time_per_day_same_day = ""              # For single calculation at 1 time
        time_per_day_multiple_day = []          # For multiple calculation at 1 time
        datetime_in_obj = ""

        read_time_log_db_previous_month = ""
        login_out_file_name_previous_month = ""
        last_date_of_month_obj = ""
        calculated_time_diff_previous_month = timedelta(days=0)
        datetime_in_obj_pre_month = ""
        time_per_day_multiple_day_previous_month = []
        timelog_data_previous_month = []
        no_of_read_previous_month = 0

        # -----------------------------------------------------------------------------------------------------
        # Create directory and file name for each employee time in/out if does not exist in database
        # -----------------------------------------------------------------------------------------------------
        login_out_file_dir = f'{self.employee_name.replace(" ","")}_{self.employee_id}'
        # self.login_out_file_name = f'{get_year}{get_month}_login_data'
        self.login_out_file_name = f'{get_year}{"%02d" % get_month}_login_data'

        # -----------------------------------------------------------------------------------------------------
        # Read login/out function database
        # -----------------------------------------------------------------------------------------------------
        self.read_time_log_db = function_DB.EmployeeLogInOut(login_out_file_dir, self.login_out_file_name)
        self.time_log_id_data, self.no_of_read = self.read_time_log_db.read_session()

        # -----------------------------------------------------------------------------------------------------
        # Calculate previous month with today's month
        # -----------------------------------------------------------------------------------------------------
        previous_month = self.get_datetime_now.month - 1
        if previous_month == 0:
            previous_month = 12
            year_previous_month = self.get_datetime_now.year - 1
        else:
            year_previous_month = self.get_datetime_now.year

        # -----------------------------------------------------------------------------------------------------
        # Decision making on get_time to be written onto which session in the database
        # -----------------------------------------------------------------------------------------------------
        # If existing data in the login/out database
        # -----------------------------------------------------------------------------------------------------
        if self.no_of_read:

            # Retrieve in date time
            datetime_in_str = self.time_log_id_data[self.no_of_read - 1][1] + " " + \
                              self.time_log_id_data[self.no_of_read - 1][2]
            datetime_in_obj = datetime.strptime(datetime_in_str, '%Y-%m-%d %H:%M:%S')

            self.calculated_time_diff = self.get_datetime_now.date() - datetime_in_obj.date()

            # If log in/out date is on the same day, edit same day data
            if str(self.get_date) == self.time_log_id_data[self.no_of_read-1][1]:

                # Write log out time on the same date
                if self.time_log_id_data[self.no_of_read-1][3] is "":
                    self.write_time_out = self.get_datetime_now.time().strftime("%H:%M:%S")
                    self.time_per_session = employee_time_per_session_calc(datetime_in_obj, self.get_datetime_now)
                    # Calculate previous day total working time
                    time_per_day_same_day = employee_time_per_day_calc(self.time_log_id_data,
                                                                       self.no_of_read,
                                                                       self.get_date,
                                                                       self.time_per_session)

                    write_id_in = self.no_of_read
                    add_same_day_time_out = True

                # Write log in time at new line for the same date if previous log out time already written
                # (example use case like lunch time log out then log in on the same day)
                else:
                    self.write_time_in = self.get_datetime_now.time().strftime("%H:%M:%S")
                    write_id_in = self.no_of_read + 1
                    add_same_day_time_in = True

            # If log in/out date is on different day
            else:
                # Log out on new day instead of same day
                if self.time_log_id_data[self.no_of_read-1][3] is "":

                    # To calculate session for each consecutive no log out day
                    for day in range(self.calculated_time_diff.days + 1):
                        date_time_out_str = f'{datetime_in_obj.date()} 23:59:59'
                        if day == 0:
                            date_time_out_obj = datetime.strptime(date_time_out_str, '%Y-%m-%d %H:%M:%S')
                            self.time_per_session = employee_time_per_session_calc(datetime_in_obj, date_time_out_obj)
                            time_per_session_per_day.append(self.time_per_session)

                        elif day < self.calculated_time_diff.days:
                            date_time_out_obj = datetime.strptime(date_time_out_str, '%Y-%m-%d %H:%M:%S')
                            self.time_per_session = employee_time_per_session_calc()
                            time_per_session_per_day.append(self.time_per_session)

                        else:
                            date_time_start_str = f'{date.today()} 00:00:00'
                            date_time_start_obj = datetime.strptime(date_time_start_str, '%Y-%m-%d %H:%M:%S')
                            date_time_out_obj = self.get_datetime_now
                            self.time_per_session = employee_time_per_session_calc(date_time_start_obj,
                                                                                   self.get_datetime_now)
                            time_per_session_per_day.append(self.time_per_session)

                        # Calculate previous day total working time
                        time_per_day_multiple_day.append(employee_time_per_day_calc(time_log_db=self.time_log_id_data,
                                                                                    no_item_time_log_db=self.no_of_read,
                                                                                    log_out_date=date_time_out_obj.date(),
                                                                                    new_session_time=self.time_per_session)
                                                         )

                    self.write_time_out = self.get_datetime_now.time().strftime("%H:%M:%S")
                    write_id_in = self.no_of_read
                    add_new_day_time_out = True

                # Write log in time on the new date
                else:
                    if self.time_log_id_data[self.no_of_read - 1][1] is not self.get_datetime_now.date()-timedelta(days=1):
                        absent_day = True

                    # Write log in time for new date
                    self.write_time_in = self.get_datetime_now.time().strftime("%H:%M:%S")
                    write_id_in = self.no_of_read + 1
                    add_new_day_time_in = True

        # -----------------------------------------------------------------------------------------------------
        # If no existing data in login/out database --> Check previous month log-out time
        # Or Directly Add new date and IN time
        # -----------------------------------------------------------------------------------------------------
        else:

            # Defined previous month time login_out file name
            login_out_file_name_previous_month = f'{year_previous_month}{"%02d" % previous_month}_login_data'

            # Check Path
            path_exist = f"./TimeLogData/{login_out_file_dir}/{login_out_file_name_previous_month}.db"

            # Check previous month time_log
            if os.path.exists(path_exist):

                # Read login/out in time log file
                read_time_log_db_previous_month = function_DB.EmployeeLogInOut(login_out_file_dir,
                                                                               login_out_file_name_previous_month)
                timelog_data_previous_month, no_of_read_previous_month = read_time_log_db_previous_month.read_session()

                # Retrieve last in date, time into datetime object
                # (Reuse code from log out different day in section above)
                datetime_in_str_pre_month = timelog_data_previous_month[no_of_read_previous_month - 1][1] + " " + \
                                            timelog_data_previous_month[no_of_read_previous_month - 1][2]
                datetime_in_obj_pre_month = datetime.strptime(datetime_in_str_pre_month, '%Y-%m-%d %H:%M:%S')

                # Get last datetime object of previous month
                last_date_of_month_obj = datetime(year=datetime_in_obj_pre_month.year,
                                                  month=datetime_in_obj_pre_month.month,
                                                  day=calendar.monthrange(datetime_in_obj_pre_month.year,
                                                                          datetime_in_obj_pre_month.month)[1],
                                                  hour=23,
                                                  minute=59,
                                                  second=59)

                calculated_time_diff_previous_month = last_date_of_month_obj.date() - datetime_in_obj_pre_month.date()

                # For time log in latest month after filling up previous month
                self.calculated_time_diff = self.get_datetime_now.date() - self.get_datetime_now.replace(day=1).date()

                # If there is no time-out in previous month time log database
                # -----------------------------------------------------------------------------------------------------
                datetime_in_obj = self.get_datetime_now.replace(day=1)
                if timelog_data_previous_month[no_of_read_previous_month - 1][3] is "":

                    # To calculate session for each consecutive no log out day for the previous month
                    for day in range(calculated_time_diff_previous_month.days + 1):

                        if day == 0:
                            date_time_out_str = f'{datetime_in_obj_pre_month.date()} 23:59:59'
                            date_time_out_obj = datetime.strptime(date_time_out_str, '%Y-%m-%d %H:%M:%S')
                            self.time_per_session = employee_time_per_session_calc(datetime_in_obj_pre_month, date_time_out_obj)
                            time_per_session_day_pre_month.append(self.time_per_session)

                        elif day < calculated_time_diff_previous_month.days + 1:
                            date_time_out_str = f'{datetime_in_obj_pre_month.date() + timedelta(days=1)} 23:59:59'
                            date_time_out_obj = datetime.strptime(date_time_out_str, '%Y-%m-%d %H:%M:%S')
                            self.time_per_session = employee_time_per_session_calc()
                            time_per_session_day_pre_month.append(self.time_per_session)

                        else:
                            date_time_start_str = f'{last_date_of_month_obj.date()} 00:00:00'
                            date_time_start_obj = datetime.strptime(date_time_start_str, '%Y-%m-%d %H:%M:%S')
                            date_time_out_obj = last_date_of_month_obj
                            self.time_per_session = employee_time_per_session_calc(date_time_start_obj,
                                                                                   last_date_of_month_obj)
                            time_per_session_day_pre_month.append(self.time_per_session)

                        # Calculate previous day total working time
                        time_per_day_multiple_day_previous_month.append(employee_time_per_day_calc(time_log_db=timelog_data_previous_month,
                                                                                                   no_item_time_log_db=no_of_read_previous_month,
                                                                                                   log_out_date=date_time_out_obj.date(),
                                                                                                   new_session_time=self.time_per_session
                                                                                                   )
                                                                        )

                    write_id_in_previous_month = no_of_read_previous_month
                    add_working_time_for_previous_month = True

                    # ------------------------------------------------------------------------------------------------

                    # To calculate session for each consecutive no log out day for latest month
                    # datetime_in_obj = self.get_datetime_now.replace(day=1)
                    for day in range(self.calculated_time_diff.days + 1):

                        date_time_out_str = f'{datetime_in_obj.date()} 23:59:59'

                        if day < self.calculated_time_diff.days:
                            date_time_out_obj = datetime.strptime(date_time_out_str, '%Y-%m-%d %H:%M:%S')
                            self.time_per_session = employee_time_per_session_calc()
                            time_per_session_per_day.append(self.time_per_session)

                        else:
                            date_time_out_obj = self.get_datetime_now
                            date_time_start_str = f'{date.today()} 00:00:00'
                            date_time_start_obj = datetime.strptime(date_time_start_str, '%Y-%m-%d %H:%M:%S')
                            self.time_per_session = employee_time_per_session_calc(date_time_start_obj,
                                                                                   self.get_datetime_now)
                            time_per_session_per_day.append(self.time_per_session)

                        # Calculate previous day total working time
                        time_per_day_multiple_day.append(employee_time_per_day_calc(time_log_db=self.time_log_id_data,
                                                                                    no_item_time_log_db=self.no_of_read,
                                                                                    log_out_date=date_time_out_obj.date(),
                                                                                    new_session_time=self.time_per_session)
                                                         )

                    self.write_time_out = self.get_datetime_now.time().strftime("%H:%M:%S")
                    write_id_in = self.no_of_read + 1
                    add_new_day_time_out = True

                # If time out in previous month last working day has filled up, log time-in for current month
                # -----------------------------------------------------------------------------------------------------
                else:

                    # Check if previous month time log last date is last day of month, if not, fill it up.
                    if datetime_in_obj_pre_month.date() != last_date_of_month_obj.date():
                        write_id_in_previous_month = no_of_read_previous_month
                        add_working_time_for_previous_month = True
                        absent_day_previous_month = True

                    if self.get_date != self.get_date.replace(day=1):
                        absent_day = True
                    else:
                        absent_day = False

                    self.write_time_in = self.get_datetime_now.time().strftime("%H:%M:%S")
                    write_id_in = self.no_of_read + 1
                    add_new_day_time_in = True

            # Write time in for a new day
            else:

                self.write_time_in = self.get_datetime_now.time().strftime("%H:%M:%S")
                write_id_in = self.no_of_read + 1
                add_new_day_time_in = True

        # -----------------------------------------------------------------------------------------------------
        # Write in log in/out time
        # -----------------------------------------------------------------------------------------------------
        self.add_time_log_db = function_DB.EmployeeLogInOut(dir_name=login_out_file_dir,
                                                            file_name=self.login_out_file_name,
                                                            id=str(write_id_in),
                                                            emp_name=self.employee_name,
                                                            date=str(self.get_date),
                                                            time_in=str(self.write_time_in),
                                                            time_out=str(self.write_time_out),
                                                            time_per_session=self.time_per_session
                                                            )

        if add_new_day_time_in:
            # Add in previous absent day data
            if absent_day:

                for day in range(self.calculated_time_diff.days):
                    # Fill in current log in time
                    if day == self.calculated_time_diff.days - 1:
                        self.add_time_log_db.id = str(write_id_in + day)
                        self.add_time_log_db.date = str(self.get_date)
                        self.add_time_log_db.time_in = str(self.write_time_in)
                        self.add_time_log_db.time_out = ""
                        self.add_time_log_db.time_per_session = ""
                        self.add_time_log_db.time_per_day = ""
                        self.add_time_log_db.add_session()

                    # Fill in absent days
                    else:
                        self.add_time_log_db.id = str(write_id_in + day)
                        print(datetime_in_obj.date())
                        self.add_time_log_db.date = f'{(datetime_in_obj.date() + timedelta(days=day+1))}'
                        print(self.add_time_log_db.date)
                        self.add_time_log_db.time_in = "00:00:00"
                        self.add_time_log_db.time_out = "00:00:00"
                        self.add_time_log_db.time_per_session = "00:00:00"
                        self.add_time_log_db.time_per_day = "00:00:00"
                        self.add_time_log_db.add_session()

            else:
                self.add_time_log_db.add_session()

            msg_box_auto_close(f'Welcome {self.employee_name} !\nLogin Time: {self.write_time_in}')

        elif add_same_day_time_out:
            self.add_time_log_db.edit_session(data_row_id=str(write_id_in),
                                         column_item_to_update=3,
                                         new_data=str(self.write_time_out)
                                         )
            self.add_time_log_db.edit_session(data_row_id=str(write_id_in),
                                         column_item_to_update=4,
                                         new_data=str(self.time_per_session)
                                         )
            self.add_time_log_db.edit_session(data_row_id=str(write_id_in),
                                         column_item_to_update=5,
                                         new_data=str(time_per_day_same_day)
                                         )
            if self.no_of_read:
                if self.time_log_id_data[write_id_in - 1][1] == self.time_log_id_data[write_id_in - 2][1]:
                    self.add_time_log_db.edit_session(data_row_id=str(write_id_in-1),
                                                 column_item_to_update=5,
                                                 new_data=str("")
                                                 )
            msg_box_auto_close(f'Goodbye {self.employee_name} !\nLogout Time: {self.write_time_out}')

        elif add_same_day_time_in:
            self.add_time_log_db.add_session()
            msg_box_auto_close(f'Welcome {self.employee_name} !\nLogin Time: {self.write_time_in}')

        elif add_new_day_time_out:

            for day in range(self.calculated_time_diff.days + 1):
                if day == 0:
                    # If there is data available in the time-log database:
                    if self.no_of_read:
                        if self.time_log_id_data[write_id_in - 1][1] == self.time_log_id_data[write_id_in - 2][1]:
                            self.add_time_log_db.edit_session(data_row_id=str(write_id_in-1),
                                                              column_item_to_update=5,
                                                              new_data=str("")
                                                              )
                        self.add_time_log_db.edit_session(data_row_id=str(write_id_in),
                                                          column_item_to_update=3,
                                                          new_data="23:59:59"
                                                          )
                        self.add_time_log_db.edit_session(data_row_id=str(write_id_in),
                                                          column_item_to_update=4,
                                                          new_data=str(time_per_session_per_day[day])
                                                          )
                        self.add_time_log_db.edit_session(data_row_id=str(write_id_in),
                                                          column_item_to_update=5,
                                                          new_data=str(time_per_day_multiple_day[day])
                                                          )

                    else: # First day of a new month
                        if self.calculated_time_diff.days > 0:
                            self.add_time_log_db.time_out = "23:59:59"
                        else:
                            self.add_time_log_db.time_out = str(self.write_time_out)
                        self.add_time_log_db.id = str(write_id_in + day)
                        self.add_time_log_db.date = f'{(datetime_in_obj.date().replace(day=1))}'
                        self.add_time_log_db.time_in = "00:00:00"
                        self.add_time_log_db.time_per_session = str(time_per_session_per_day[day])
                        self.add_time_log_db.time_per_day = str(time_per_day_multiple_day[day])
                        self.add_time_log_db.add_session()

                elif day < self.calculated_time_diff.days:
                    self.add_time_log_db.id = str(write_id_in + day)
                    self.add_time_log_db.date = f'{(datetime_in_obj.date() + timedelta(days=day))}'
                    self.add_time_log_db.time_in = "00:00:00"
                    self.add_time_log_db.time_out = "23:59:59"
                    self.add_time_log_db.time_per_session = str(time_per_session_per_day[day])
                    self.add_time_log_db.time_per_day = str(time_per_day_multiple_day[day])
                    self.add_time_log_db.add_session()

                else:
                    self.add_time_log_db.id = str(write_id_in + day)
                    self.add_time_log_db.date = f'{(datetime_in_obj.date() + timedelta(days=day))}'
                    self.add_time_log_db.time_in = "00:00:00"
                    self.add_time_log_db.time_out = str(self.write_time_out)
                    self.add_time_log_db.time_per_session = str(time_per_session_per_day[day])
                    self.add_time_log_db.time_per_day = str(time_per_day_multiple_day[day])
                    self.add_time_log_db.add_session()

            msg_box_auto_close(f'Goodbye {self.employee_name} !\nLogout Time: {self.write_time_out}')

        if add_working_time_for_previous_month:

            self.add_time_log_db.file_name = login_out_file_name_previous_month

            # Add in previous absent day data
            if absent_day_previous_month:
                for day in range(calculated_time_diff_previous_month.days):
                    self.add_time_log_db.id = str(write_id_in_previous_month + day + 1)
                    self.add_time_log_db.date = f'{(datetime_in_obj_pre_month.date() + timedelta(days=day + 1))}'
                    self.add_time_log_db.time_in = "00:00:00"
                    self.add_time_log_db.time_out = "00:00:00"
                    self.add_time_log_db.time_per_session = "00:00:00"
                    self.add_time_log_db.time_per_day = "00:00:00"
                    self.add_time_log_db.add_session()

            else:

                for day in range(calculated_time_diff_previous_month.days + 1):

                    if day == 0:
                        if timelog_data_previous_month[write_id_in_previous_month - 1][1] == timelog_data_previous_month[write_id_in_previous_month - 2][1]:
                            self.add_time_log_db.edit_session(data_row_id=str(write_id_in_previous_month - 1),
                                                              column_item_to_update=5,
                                                              new_data=str("")
                                                              )
                        self.add_time_log_db.edit_session(data_row_id=str(write_id_in_previous_month),
                                                          column_item_to_update=3,
                                                          new_data="23:59:59"
                                                          )
                        self.add_time_log_db.edit_session(data_row_id=str(write_id_in_previous_month),
                                                          column_item_to_update=4,
                                                          new_data=str(time_per_session_day_pre_month[day])
                                                          )
                        self.add_time_log_db.edit_session(data_row_id=str(write_id_in_previous_month),
                                                          column_item_to_update=5,
                                                          new_data=str(time_per_day_multiple_day_previous_month[day])
                                                          )
                    elif day < calculated_time_diff_previous_month.days + 1:
                        self.add_time_log_db.id = str(write_id_in_previous_month + day)
                        self.add_time_log_db.date = f'{(datetime_in_obj_pre_month.date() + timedelta(days=day))}'
                        self.add_time_log_db.time_in = "00:00:00"
                        self.add_time_log_db.time_out = "23:59:59"
                        self.add_time_log_db.time_per_session = str(time_per_session_day_pre_month[day])
                        self.add_time_log_db.time_per_day = str(time_per_day_multiple_day_previous_month[day])
                        self.add_time_log_db.add_session()

                    else:
                        self.add_time_log_db.id = str(write_id_in_previous_month + day)
                        self.add_time_log_db.date = f'{(datetime_in_obj_pre_month.date() + timedelta(days=day))}'
                        self.add_time_log_db.time_in = "00:00:00"
                        self.add_time_log_db.time_out = str(self.write_time_out)
                        self.add_time_log_db.time_per_session = str(time_per_session_day_pre_month[day])
                        self.add_time_log_db.time_per_day = str(time_per_day_multiple_day_previous_month[day])
                        self.add_time_log_db.add_session()

            # Calculate total working time for the previous month
            last_day_of_month = (calendar.monthrange(year_previous_month, previous_month))[1]
            pre_month_time_db, no_of_read_previous_month = read_time_log_db_previous_month.read_session()
            current_day = f'{pre_month_time_db[no_of_read_previous_month-1][1]} 23:59:59'
            current_day_obj = datetime.strptime(current_day, '%Y-%m-%d %H:%M:%S')
            self.compute_total_time_for_one_month(db_file_name=login_out_file_name_previous_month,
                                                  time_log_db_obj=read_time_log_db_previous_month,
                                                  current_day=current_day_obj.day,
                                                  last_day_of_month=last_day_of_month)

        # Calculate total working time for the latest month
        last_day_of_month = (calendar.monthrange(self.get_datetime_now.year, self.get_datetime_now.month))[1]
        self.compute_total_time_for_one_month(db_file_name=self.login_out_file_name,
                                              time_log_db_obj=self.read_time_log_db,
                                              current_day=self.get_datetime_now.day,
                                              last_day_of_month=last_day_of_month)

    # -----------------------------------------------------------------------------------------------------
    # Calculate total working time for the month and add to database table
    # -----------------------------------------------------------------------------------------------------
    def compute_total_time_for_one_month(self, db_file_name, time_log_db_obj, current_day, last_day_of_month):

        if current_day == last_day_of_month:
            # Re-read the database
            time_log_id_data, no_of_read = time_log_db_obj.read_session()

            if no_of_read:
                if time_log_id_data[no_of_read-1][2] is not "":
                    if time_log_id_data[no_of_read-1][3] is not "":
                        time_per_month = employee_time_per_month_calc(time_log_id_data,
                                                                      no_of_read)

                        time_log_db_obj.file_name = db_file_name

                        for item in range(no_of_read):
                            time_log_db_obj.edit_session(data_row_id=str(item),
                                                         column_item_to_update=6,
                                                         new_data=str("")
                                                         )
                        time_log_db_obj.edit_session(data_row_id=str(no_of_read),
                                                     column_item_to_update=6,
                                                     new_data=time_per_month
                                                     )











