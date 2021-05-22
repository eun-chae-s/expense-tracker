"""A python file which creates the interface to check the daily spent"""
import tkinter as tk
from datetime import datetime
import csv
import tkinter.ttk as ttk
from tkinter import messagebox


def add_expense(date: str, where: str, which: str, amount: int):
    """Add a new row of information to a csv file"""
    with open('expense_record.csv', 'a') as c_file:
        w_object = csv.writer(c_file)
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
    a_text = tk.StringVar(add_interface)
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


def onClick(amount: str) -> None:
    """Create a message box"""
    messagebox.showinfo('Result!', 'You spent ￦' + str(amount))


def daily_expense_record_interface() -> None:
    """Create an interface of showing the list of all daily expenses"""
    # These things should be displayed on the message box
    daily_interface = tk.Tk()
    # total_amount = tk.IntVar(daily_interface)
    # tk.Label(daily_interface, text="Today, you spent..." + str(total_amount.get()),
    #          height=5, font=("Helvetica", 20, 'bold')).place(relx=0.1, rely=0.05)
    daily_interface.title("Today you spent...")
    daily_interface.geometry('600x400')
    tree = ttk.Treeview(daily_interface, columns=('#1', '#2', '#3'), show='headings')
    tree.heading('#1', text='Where')
    tree.heading('#2', text='Category')
    tree.heading('#3', text='Amount')
    amount = tk.StringVar(daily_interface)
    with open('expense_record.csv') as c_file:
        reader = csv.reader(c_file)
        next(reader)
        current_date = datetime.today().strftime('%Y-%m-%d')
        for row in reader:
            if row[0] == current_date:
                tree.insert('', tk.END, values=(row[1], row[2], row[3]))
        amount.set(str(sum([int(row[3]) for row in reader if row[0] == current_date])))

    tree.grid(row=0, column=0, sticky='nsew')
    # Add a scrollbar
    scrollbar = ttk.Scrollbar(daily_interface, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # Add a button which shows the messagebox
    message_btn = tk.Button(daily_interface, text="Total amount?",
                            command=onClick(amount.get()))
    message_btn.place(relx=0.4, rely=0.9)
    daily_interface.mainloop()
