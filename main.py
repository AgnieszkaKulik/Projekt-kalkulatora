from tkinter import *
from tkinter import ttk

from basic_functions import *

# Dodaj funkcję obsługi przecinka dziesiętnego
def button_comma():
    global expression
    expression = comma()
    equation.set(expression)

def button_press(number):
    global flag

    value, flag = press(number, flag)
    equation.set(value)


def button_power2_fun():
    set_flag()

    value = power2_fun()
    equation.set(value)

    add_to_history(value)

def button_sqrt_fun():
    set_flag()
    
    value = sqrt_fun()
    equation.set(value)

    add_to_history(value)

def button_equal_fun():
    set_flag()

    value = equal_fun()
    equation.set(value)

    add_to_history(value)

def button_imaginary_part():
    global expression
    expression = imaginary_part()
    equation.set(expression)


def set_flag():
    global flag
    flag = 1

    
def add_to_history(operation):
    if operation != "ERROR":
        if len(history) >= 10:
            history.pop()
        history.insert(0, operation) # dodawanie do historii
        update_history_listbox()


def update_history_listbox():
    history_listbox.delete(0, END)
    if show_history:
        for i, item in enumerate(history, start=1):
            history_listbox.insert(END, f"{i}: {item}")


def toggle_history():
    global show_history
    show_history = not show_history
    update_history_listbox() # wyświetlanie historii


def clear_history():
    history.clear()
    history_listbox.delete(0, END) # czyszczenie historii


def use_history(index):
    if index >= 1 and index <= len(history):
        button_press(history[index-1])


def clear_calculator():
    equation.set("")  # Czyszczenie okna kalkulatora


if __name__ == "__main__":

    root = Tk()
    root.title("Kalkulator")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=10)
    frame.grid()

    equation = StringVar()
    flag = 0
    history = []
    show_history = True

    buttons = {}
    for i in range(1, 10):
        button = Button(frame, text=f"{i}", command=lambda i=i: button_press(f"{i}")).grid(row=3 - (2 - ((i - 1) // 3)),
                                                                                           column=((i - 1) % 3))
        buttons[i] = button

    button_0 = Button(frame, text="0", command=lambda: button_press("0")).grid(row=4, column=1)
    button_i = Button(frame, text = "i", command = button_imaginary_part).grid(row=5, column=1)

    add = Button(frame, text="+", command=lambda: button_press('+')).grid(row=3, column=3)
    subtraction = Button(frame, text="-", command=lambda: button_press('-')).grid(row=2, column=3)
    multiply = Button(frame, text="*", command=lambda: button_press('*')).grid(row=1, column=3)
    divide = Button(frame, text="/", command=lambda: button_press('/')).grid(row=0, column=3)

    power2 = Button(frame, text="x^2", command=button_power2_fun).grid(row=0, column=1)
    sqrt = Button(frame, text="sqrt", command=button_sqrt_fun).grid(row=0, column=2)

    dot = Button(frame, text=".", command=button_comma).grid(row=4, column=0)
    plus_minus = Button(frame, text="+/-", command=lambda: button_press('-')).grid(row=4, column=2)
    equal = Button(frame, text="=", command=button_equal_fun).grid(row=4, column=3)

    text = Label(root, height=2, textvariable=equation, width=30).grid(column=10, row=0)

    history_label = Label(root, text="Historia operacji:").grid(column=10, row=1)
    history_listbox = Listbox(root, height=10, width=30)
    history_listbox.grid(column=10, row=2, rowspan=5)

    history_frame = ttk.Frame(root, padding=10)
    history_frame.grid(column=10, row=8, rowspan=5)

    history_buttons = {}
    for i in range(1, 11):
        row_index = (i - 1) // 2
        col_index = (i - 1) % 2
        history_button = Button(history_frame, text=f"{i}", command=lambda index=i: use_history(index))
        history_button.grid(row=row_index, column=col_index, padx=5, pady=5)
        history_buttons[i] = history_button

    history_text = Label(root, text="Odwołaj się:").grid(column=9, row=9, pady=5, sticky=E)

    toggle_button = Button(root, text="Pokaż/Ukryj historię", command=toggle_history)
    toggle_button.grid(column=10, row=7)
    clear_button = Button(root, text="Wyczyść historię", command=clear_history)
    clear_button.grid(column=10, row=6)

    root.mainloop()
