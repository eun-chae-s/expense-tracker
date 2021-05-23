"""A python file which creates the interface to check the monthly spent"""
import tkinter as tk
import csv
from tkinter import ttk


# Calculate all the expenses
def monthly_expense_record_interface() -> None:
    """Create an interface of showing the list of all expenses spent on the specific month"""
    monthly_interface = tk.Tk()
    monthly_interface.title("Check your monthly spent!")
    monthly_interface.geometry('700x800')

    q1 = tk.Label(monthly_interface, text="Which month \n do you want to check?",
                  font=("Helvetica", 17, 'italic'))
    q1.place(relx=0.1, rely=0.1)
    months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    selected_month = tk.StringVar(monthly_interface)
    global month_combobox
    month_combobox = ttk.Combobox(monthly_interface, textvariable=selected_month,
                                  values=months, state='readonly')
    month_combobox.place(relx=0.5, rely=0.1)
    month_combobox.bind('<<ComboboxSelected>>', month_changed)
    monthly_interface.mainloop()


def month_changed(event) -> None:
    """This function will show a pie chart and the result"""
    with open('expense_record.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        months_numeric = {'Jan': '01', 'Feb': '02', 'Mar': '03',
                          'Apr': '04', 'May': '05', 'Jun': '06',
                          'Jul': '07', 'Aug': '08', 'Sep': '09',
                          'Oct': '10', 'Nov': '11', 'Dec': '12'}
        for row in reader:
            date = row[0].split('-')
            if date[1] == months_numeric[month_combobox.get]:
                ...
# Display a graph
