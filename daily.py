"""A python file which creates the interface to check the daily spent"""
import tkinter as tk

add_interface = tk.Tk()
add_interface.title("Add expense")
add_interface.geometry("500x600")


def add_spent(col: str, amount: int) -> None:
    """This function will show the list of the daily spent."""
    element = tk.Label(add_interface, text=col + ": " + str(amount))
    # How to put the list of statements in different positions
    element.place(relx=0.2, rely=0.7)


# Where did you spend?
w_text = tk.StringVar(add_interface)
w_text.set('')
where = tk.Entry(add_interface, textvariable=w_text).place(relx=0.2, rely=0.1)

# Which category does this expense fall into?
c_text = tk.StringVar(add_interface)
c_text.set('Where did you spend?')
lists = ["Food", "Academics", "Transportation", "Entertainment"]
category = tk.OptionMenu(add_interface, c_text, *lists)
category.place(relx=0.2, rely=0.3)

# How much did you spend?
a_text = tk.IntVar()
a_text.set(0)
amount = tk.Entry(add_interface, textvariable=a_text).place(relx=0.2, rely=0.2)

# Complete button
complete = tk.Button(add_interface, textvariable="Complete!"
                     ).place(relx=0.5, rely=0.7, anchor='CENTER')


add_interface.mainloop()
