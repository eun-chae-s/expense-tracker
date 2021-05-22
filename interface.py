"""
This Python file is for creating the Desktop GUI of the expense tracker
"""
import tkinter as tk
from datetime import datetime
from daily import create_daily_interface


def open_daily() -> None:
    """This function opens a new window for recording the daily expense data."""
    create_daily_interface()


app = tk.Tk()
app.title("Expense Tracker")
app.geometry("1000x500")

# The entire interface design
# Today's date
date = tk.Label(app, text=datetime.today().strftime('%Y-%m-%d'),
                height=4,
                font=("Helvetica", 13, 'italic')).place(relx=0.8, rely=0.01)

# Overall record
total_amount = tk.StringVar(app)
total_amount.set('')
# Need to make that the users can type their name...!
notification1 = tk.Label(app, text="Rachel's Expense Tracker",
                         height=5,
                         font=("Helvetica", 20, 'bold')).place(relx=0.1, rely=0.05)
# amount_label = tk.Label(app, text='￦' + total_amount.get(),
#                         height=4,
#                         fg='pink',
#                         font=("MS Sans Serif", 26, 'bold')).place(relx=0.4, rely=0.04)

# Buttons
add_btn = tk.Button(app, text="Add expense",
                    command=open_daily, width=15).place(relx=0.1, rely=0.4)
daily_btn = tk.Button(app, text="Daily expenses", width=15).place(relx=0.3, rely=0.4)
monthly_btn = tk.Button(app, text="Monthly expenses", width=15).place(relx=0.5, rely=0.4)
annual_btn = tk.Button(app, text="Annual expenses", width=15).place(relx=0.7, rely=0.4)

# Run the app
app.mainloop()
