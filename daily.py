"""A python file which creates the interface to check the daily spent"""
import tkinter as tk
from datetime import datetime
from csv import writer


def add_expense(date: str, where: str, which: str, amount: int):
    """Add a new row of information to a csv file"""
    with open('expense_record.csv', 'a') as c_file:
        w_object = writer(c_file)
        c_file.write('/n')
        w_object.writerow([date, where, which, amount])
        c_file.close()


def create_daily_interface() -> None:
    """Create the interface for adding the daily expense"""
    add_interface = tk.Tk()
    add_interface.title("Add expense")
    add_interface.geometry("500x600")

    # Where did you spend?
    tk.Label(add_interface, text='Where?').place(relx=0.2, rely=0.1)
    w_text = tk.StringVar(add_interface)
    w_text.set('')
    where = tk.Entry(add_interface, textvariable=w_text)
    where.place(relx=0.4, rely=0.1)

    # Which category does this expense fall into?
    tk.Label(add_interface, text='Which?').place(relx=0.2, rely=0.3)
    c_text = tk.StringVar(add_interface)
    c_text.set('Select one')
    lists = ["Food", "Academics", "Transportation", "Entertainment"]
    category = tk.OptionMenu(add_interface, c_text, *lists)
    category.pack()
    category.place(relx=0.4, rely=0.3)

    # How much did you spend?
    tk.Label(add_interface, text='How much?').place(relx=0.2, rely=0.5)
    a_text = tk.StringVar()
    a_text.set('0')
    amount = tk.Entry(add_interface, textvariable=a_text)
    amount.place(relx=0.4, rely=0.5)

    # Complete button
    complete = tk.Button(add_interface, text="Complete!",
                         command=lambda: add_expense(datetime.today().strftime('%Y-%m-%d'),
                                                     w_text.get(),
                                                     c_text.get(),
                                                     a_text.get()))
    complete.place(relx=0.5, rely=0.7, anchor='center')

    add_interface.mainloop()
