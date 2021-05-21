"""
This Python file is for creating the Desktop GUI of the expense tracker
"""
import tkinter as tk
from datetime import datetime
from daily import create_daily_interface
import csv


def open_daily() -> None:
    """This function opens a new window for recording the daily expense data."""
    create_daily_interface()


def daily_expense() -> int:
    """This function calculates the sum of all the expenses spent on that day."""
    current_date = datetime.today().strftime('%Y-%m-%d')
    with open('expense_record.csv') as c_file:
        read_c_file = csv.reader(c_file)
        next(read_c_file)

        return sum([int(row[3]) for row in read_c_file if row[0] == current_date])


app = tk.Tk()
app.title("Expense Tracker")
app.geometry("1000x500")

# The entire interface design
# Today's date
date = tk.Label(app, text=datetime.today().strftime('%Y-%m-%d'),
                height=4,
                font=("Helvetica", 13, 'italic')).place(relx=0.8, rely=0.01)

# Overall record
notification1 = tk.Label(app, text="Today, you spent ",
                         height=5,
                         font=("Helvetica", 20, 'bold')).place(relx=0.1, rely=0.05)
amount_label = tk.Label(app, text='￦' + str(daily_expense()),
                        height=4,
                        fg='pink',
                        font=("MS Sans Serif", 26, 'bold')).place(relx=0.4, rely=0.04)

# Buttons
add_btn = tk.Button(app, text="Add expense",
                    command=open_daily, width=15).place(relx=0.1, rely=0.4)
daily_btn = tk.Button(app, text="Daily expenses", width=15).place(relx=0.3, rely=0.4)
monthly_btn = tk.Button(app, text="Monthly expenses", width=15).place(relx=0.5, rely=0.4)
annual_btn = tk.Button(app, text="Annual expenses", width=15).place(relx=0.7, rely=0.4)

# Run the app
app.mainloop()
