"""
This Python file is for creating the Desktop GUI of the expense tracker
"""
import tkinter as tk
from datetime import datetime
from daily import create_daily_interface, daily_expense_record_interface
from monthly import monthly_expense_record_interface
from annual_spent import yearly_expense_record_interface


def open_daily() -> None:
    """This function opens a new window for recording the daily expense data."""
    create_daily_interface()


def daily_expense_check() -> None:
    """This function opens a new window for showing the expense for today"""
    daily_expense_record_interface()


def monthly_expense_check() -> None:
    """This function opens a new window for showing the expense for the selected month"""
    monthly_expense_record_interface()


def annual_expense_check() -> None:
    """This function opens a new window for showing the expense for the selected year"""
    yearly_expense_record_interface()


app = tk.Tk()
app.title("Expense Tracker")
app.geometry("1000x500")

# The entire interface design
# Today's date
date = tk.Label(app, text=datetime.today().strftime('%Y-%m-%d'),
                height=4,
                font=("Helvetica", 13, 'italic')).place(relx=0.8, rely=0.01)

# Overall record
# Need to make that the users can type their name...!
notification1 = tk.Label(app, text="User's Expense Tracker",
                         height=5,
                         font=("Helvetica", 20, 'bold')).place(relx=0.1, rely=0.05)

# Buttons
add_btn = tk.Button(app, text="Add expense",
                    command=open_daily, width=15).place(relx=0.1, rely=0.4)
daily_btn = tk.Button(app, text="Daily expenses",
                      command=daily_expense_check, width=15).place(relx=0.3, rely=0.4)
monthly_btn = tk.Button(app, text="Monthly expenses",
                        command=monthly_expense_check, width=15).place(relx=0.5, rely=0.4)
annual_btn = tk.Button(app, text="Annual expenses",
                       command=annual_expense_check,width=15).place(relx=0.7, rely=0.4)

# Run the app
app.mainloop()
