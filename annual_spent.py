"""A python file which creates the interface to check the annual spent"""
import tkinter as tk
import csv
from tkinter import ttk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Calculate all the expenses
def yearly_expense_record_interface() -> None:
    """Create an interface of showing the list of all expenses spent on the specific year"""
    global yearly_interface
    yearly_interface = tk.Tk()
    yearly_interface.title("Check your annual spent!")
    yearly_interface.geometry('700x800')
    q1 = tk.Label(yearly_interface, text="Which year \n do you want to check?",
                  font=("Helvetica", 17, 'italic'))
    q1.place(relx=0.1, rely=0.1)
    years = ('2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030')

    selected_year = tk.StringVar(yearly_interface)
    global year_combobox
    year_combobox = ttk.Combobox(yearly_interface, textvariable=selected_year,
                                 values=years, state='readonly')
    year_combobox.place(relx=0.5, rely=0.1)
    year_combobox.bind('<<ComboboxSelected>>', create_graph)

    yearly_interface.mainloop()


# Display a graph
def create_graph(event) -> None:
    """This function will create a pie chart showing the distribution of expenses"""
    amount = 0
    total_record = 0
    data = {"Food": 0, "Academics": 0, "Transportation": 0, "Entertainment": 0}
    with open('expense_record.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            date = row[0].split('-')
            if date[0] == year_combobox.get():
                data[row[2]] += 1
                amount += int(row[3])
                total_record += 1

    data_modified = {'percentage': [(data['Food'] / total_record) * 100,
                                    (data['Academics'] / total_record) * 100,
                                    (data['Transportation'] / total_record) * 100,
                                    (data['Entertainment'] / total_record) * 100]}
    amount_label = tk.Label(yearly_interface, text="You spent ￦ " + str(amount),
                            font=("Helvetica", 17, 'bold'))
    amount_label.place(relx=0.1, rely=0.4)
    df = DataFrame(data_modified, columns=['percentage'],
                   index=['Food', 'Academics', 'Transportation', 'Entertainment'])
    figure = plt.Figure(figsize=(5, 3), dpi=100)
    ax = figure.add_subplot(111)
    df.plot(y='percentage', kind='pie', ax=ax, figsize=(5, 3), legend=False, autopct='%1.1f%%')
    pie_chart = FigureCanvasTkAgg(figure, yearly_interface)
    pie_chart.get_tk_widget().place(relx=0.1, rely=0.5)

    ax.set_title('Distribution of expenses')
