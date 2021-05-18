"""A python file which creates the interface to check the daily spent"""
import tkinter as tk

app = tk.Tk()
app.title("Add expense")
app.geometry("500x600")


def add_spent(col: str, amount: int) -> None:
    """This function will show the list of the daily spent."""
    element = tk.Label(app, text=col + ": " + str(amount))
    # How to put the list of statements in different positions
    element.place(relx=0.2, rely=0.7)


# Where did you spend?
c_text = tk.StringVar(app)
c_text.set('Where did you spend?')
lists = ["Food", "Academics", "Transportation", "Entertainment"]
category = tk.OptionMenu(app, c_text, *lists)
category.place(relx=0.15, rely=0.2)

# How much did you spend?
a_text = tk.IntVar()
amount = tk.Entry(app, textvariable=a_text).place(relx=0.55, rely=0.2)
