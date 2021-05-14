"""
This Python file is for creating the Desktop GUI of the expense tracker
"""
import tkinter as tk

app = tk.Tk()
app.title("Expense Tracker")
app.geometry("600x500")

# First page
notification1 = tk.Label(app, text="Today, you spent...",
                         width=20, height=5,
                         font=("Helvetica", 18, 'bold')).place(x=0, y=10)

# Where did you spend? (Dropdown menu)
c_text = tk.StringVar()
category = tk.Entry(app, width=20, textvariable=c_text).place(x=30, y=100)

# How much did you spend?
a_text = tk.IntVar()
amount = tk.Entry(app, width=25, textvariable=a_text).place(x=300, y=100)

# Keep track of money you spent
# Something that I need to consider
# as soon as you type the money, the data will be automatically saved in the excel file
confirm = tk.Button(app, text="Check!").place(x=250, y=170)  # need to connect with function
monthly = tk.Button(app, text="Check my monthly consumption!").place(x=180, y=200)
annually = tk.Button(app, text="Check my annual consumption!").place(x=180, y=230)

# The amount you spent will be shown as a list in the bottom of the GUI


# Second page (monthly tracker)
# This interface will be opened when you click the button "check my monthly consumption"


# Run the app
app.mainloop()
