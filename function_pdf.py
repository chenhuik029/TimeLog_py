from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title

    def header(self):
        # Arial Bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(self.title) + 6
        self.set_x((210-w)/2)
        # Title
        self.cell(w, 9, self.title, 0, 1, 'C', 0)
        # Line break
        self.ln(5)

    def footer(self):
        # Position at  1.5cm from the bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 6, 'Page' + str(self.page_no()), 0, 0, 'C')

    def month_year_title(self, month, year):
        # Arial Bold 15
        self.set_font('Arial', 'U', 15)
        # Text to display
        Month_Year = f'Month: {month} / Year: {year}'
        # Calculate width of title and position
        w = self.get_string_width(Month_Year) + 6
        self.set_x((210-w)/2)
        # Print Text
        self.cell(w, 9, Month_Year, 0, 1, 'C', 0)
        # Line break
        self.ln(5)

    def employee_info(self, Name, Emp_ID, Card_ID, Status):
        # Employee Name
        self.set_font('Arial', '', 12)
        self.cell(35, 11, 'Employee Name')
        self.set_font('Arial', 'B', 12)
        self.cell(100, 11, f': {Name}')
        self.ln(7)

        # Employee ID
        self.set_font('Arial', '', 12)
        self.cell(35, 11, 'Employee ID')
        self.set_font('Arial', 'B', 12)
        self.cell(100, 11, f': {Emp_ID}')
        self.ln(7)

        # Card ID
        self.set_font('Arial', '', 12)
        self.cell(35, 11, 'Card ID')
        self.set_font('Arial', 'B', 12)
        self.cell(100, 11, f': {Card_ID}')
        self.ln(7)

        # Employee Status
        self.set_font('Arial', '', 12)
        self.cell(35, 11, 'Employee Status')
        self.set_font('Arial', 'B', 12)
        self.cell(100, 11, f': {Status}')
        self.ln(10)

    def time_log_table(self, time_log_db):

        # Print time table - Header
        # ---------------------------------------------------------------------------
        # Arial normal 10
        self.set_font('Arial', '', 10)
        # Set Thickness of frame
        self.set_line_width(0.4)
        # Print Header
        self.cell(10,  10, "No.", 1, 0, 'C')
        self.cell(35, 10, "Session Date", 1, 0, 'C')
        self.cell(25, 10, "Time In", 1, 0, 'C')
        self.cell(25, 10, "Time Out", 1, 0, 'C')
        self.cell(30, 10, "TIme Per Session", 1, 0, 'C')
        self.cell(30, 10, "Time Per Day", 1, 0, 'C')
        self.cell(30, 10, "Time Per Month", 1, 0, 'C')
        self.ln()

        # Print time table - Time Data
        # ---------------------------------------------------------------------------
        self.set_line_width(0.2)
        for row in range(len(time_log_db)):
            self.cell(10, 8, time_log_db[row][0], 1, 0, 'C')
            self.cell(35, 8, time_log_db[row][1], 1, 0, 'C')
            self.cell(25, 8, time_log_db[row][2], 1, 0, 'C')
            self.cell(25, 8, time_log_db[row][3], 1, 0, 'C')
            self.cell(30, 8, time_log_db[row][4], 1, 0, 'C')
            self.cell(30, 8, time_log_db[row][5], 1, 0, 'C')
            self.cell(30, 8, time_log_db[row][6], 1, 0, 'C')
            self.ln()

    def print_document(self, month, year, Name, Emp_ID, Card_ID, Status, Time_log_db=None):
        self.add_page()
        self.month_year_title(month=month, year=year)
        self.employee_info(Name, Emp_ID, Card_ID, Status)
        self.time_log_table(Time_log_db)


if __name__ == "__main__":
    title = "Time Log Report"
    pdf = PDF(title=title)
    pdf.set_title(title)
    pdf.set_author("XXX")
    pdf.print_document(12, 2020, "Leong Chen Hui", "1000", "2000", "Active")
    pdf.output("timelog_1.pdf", 'F')
