"""
This Python file is for creating the Desktop GUI of the expense tracker
"""
import tkinter as tk
from datetime import datetime


# Need to know how to save the selected value from the OptionMenu
def add_spent(amount: int) -> None:
    """This function will show the list of the daily spent."""
    element = tk.Label(app, text=": " + str(amount))
    element.place(relx=0.2, rely=0.7)


app = tk.Tk()
app.title("Expense Tracker")
app.geometry("600x500")

# First page
notification1 = tk.Label(app, text="Today, you spent..." + datetime.today().strftime('%Y-%m-%d'),
                         height=5,
                         font=("Helvetica", 18, 'bold')).place(relx=0.05, rely=0.05)

# Where did you spend?
c_text = tk.StringVar(app)
c_text.set('Where did you spend?')
lists = ["Food", "Academics", "Transportation", "Entertainment"]
category = tk.OptionMenu(app, c_text, *lists)
category.place(relx=0.15, rely=0.2)

# How much did you spend?
a_text = tk.IntVar()
amount = tk.Entry(app, textvariable=a_text).place(relx=0.55, rely=0.2)

# Keep track of money you spent
# Something that I need to consider
# as soon as you type the money, the data will be automatically saved in the excel file
confirm = tk.Button(app, text="Check!", width=10,
                    command=lambda: add_spent(a_text.get())).place(relx=0.5, rely=0.4, anchor='center')
# monthly = tk.Button(app, text="Check my monthly consumption!").place(relx=0.35, y=400)
# annually = tk.Button(app, text="Check my annual consumption!").place(relx=0.35, y=450)

# Run the app
app.mainloop()
