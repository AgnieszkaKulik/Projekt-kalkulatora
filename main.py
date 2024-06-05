from tkinter import *
from tkinter import ttk

from basic_functions import *
from plotter import plot_graph

# Dodaj funkcję obsługi przecinka dziesiętnego
def button_comma():
    equation.set(comma())

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
    global flag

    value, flag = imaginary_part(flag)
    equation.set(value)

def button_reset():
    equation.set(reset_fun()) 


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

def show_plot():
    expression = plot_expression.get()
    plot_graph(expression)

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

    text = Label(frame, height=2, textvariable=equation, width=30, background='white')
    text.grid(column=0, row=0, columnspan=4, pady=10)

    button_frame = ttk.Frame(frame, padding=10)
    button_frame.grid(column=0, row=1, columnspan=4)

    buttons = {}
    for i in range(1, 10):
        button = Button(button_frame, text=f"{i}", command=lambda i=i: button_press(f"{i}"))
        button.grid(row=3 - (2 - ((i - 1) // 3)), column=((i - 1) % 3), padx=5, pady=5)
        buttons[i] = button

    button_0 = Button(button_frame, text="0", command=lambda: button_press("0"))
    button_0.grid(row=4, column=1, padx=5, pady=5)
    button_j = Button(button_frame, text = "j", command = button_imaginary_part)
    button_j.grid(row=5, column=1, padx=5, pady=5)
    button_lbrac = Button(button_frame, text="(", command=lambda: button_press("("))
    button_lbrac.grid(row=5, column=2, padx=5, pady=5)
    button_rbrac = Button(button_frame, text=")", command=lambda: button_press(")"))
    button_rbrac.grid(row=5, column=3, padx=5, pady=5)

    add = Button(button_frame, text="+", command=lambda: button_press('+'))
    add.grid(row=3, column=3, padx=5, pady=5)
    subtraction = Button(button_frame, text="-", command=lambda: button_press('-'))
    subtraction.grid(row=2, column=3, padx=5, pady=5)
    multiply = Button(button_frame, text="*", command=lambda: button_press('*'))
    multiply.grid(row=1, column=3, padx=5, pady=5)
    divide = Button(button_frame, text="/", command=lambda: button_press('/'))
    divide.grid(row=0, column=3, padx=5, pady=5)

    power2 = Button(button_frame, text="x^2", command=button_power2_fun)
    power2.grid(row=0, column=1, padx=5, pady=5)
    sqrt = Button(button_frame, text="sqrt", command=button_sqrt_fun)
    sqrt.grid(row=0, column=2, padx=5, pady=5)

    dot = Button(button_frame, text=".", command=button_comma)
    dot.grid(row=4, column=0, padx=5, pady=5)
    plus_minus = Button(button_frame, text="+/-", command=lambda: button_press('-'))
    plus_minus.grid(row=4, column=2, padx=5, pady=5)
    reset = Button(button_frame, text='C', command=button_reset)
    reset.grid(row=0,column=0, padx=5, pady=5)
    equal = Button(button_frame, text="=", command=button_equal_fun)
    equal.grid(row=4, column=3, padx=5, pady=5)

    history_frame = ttk.Frame(root, padding=10)
    history_frame.grid(column=1, row=0, rowspan=10, padx=20)

    history_label = Label(history_frame, text="Historia operacji:")
    history_label.grid(row=0, column=0, pady=5)
    history_listbox = Listbox(history_frame, height=10, width=30)
    history_listbox.grid(row=1, column=0, rowspan=5, pady=5)

    history_buttons_frame = ttk.Frame(history_frame, padding=10)
    history_buttons_frame.grid(row=6, column=0, pady=10)

    history_buttons = {}
    for i in range(1, 11):
        row_index = (i - 1) // 2
        col_index = (i - 1) % 2
        history_button = Button(history_buttons_frame, text=f"{i}", command=lambda index=i: use_history(index))
        history_button.grid(row=row_index, column=col_index, padx=5, pady=5)
        history_buttons[i] = history_button

    history_text = Label(history_frame, text="Odwołaj się:")
    history_text.grid(row=7, column=0, pady=5, sticky=W)

    toggle_button = Button(history_frame, text="Pokaż/Ukryj historię", command=toggle_history)
    toggle_button.grid(row=8, column=0, pady=5, sticky=W)
    clear_button = Button(history_frame, text="Wyczyść historię", command=clear_history)
    clear_button.grid(row=9, column=0, pady=5, sticky=W)

    # Dodanie pola tekstowego i przycisku do wyświetlania wykresów na dole
    plot_expression = StringVar()
    plot_entry = Entry(frame, textvariable=plot_expression, width=30)
    plot_entry.grid(column=0, row=2, columnspan=3, pady=5)
    plot_button = Button(frame, text="Pokaż wykres", command=show_plot)
    plot_button.grid(column=3, row=2, pady=5)

    note_label = Label(frame, text="""
Instrukcje wprowadzania danych:
1. Funkcje kwadratowe:
   - Przykład: x**2 - 3*x + 1
2. Funkcje logarytmiczne:
   - Przykład: log(x, 10) (dla x > 0)
3. Funkcje trygonometryczne:
   - Przykład: sin(x)
4. Funkcje z nawiasami:
   - Przykład: sin(x**2 - 3*x + 1)

Upewnij się, że wszystkie nawiasy są zrównoważone i używaj poprawnych symboli matematycznych.
""", justify=LEFT)
    note_label.grid(column=0, row=3, columnspan=4, pady=10)

    root.mainloop()
