from tkinter import *
from tkinter import ttk

from basic_functions import press, power2_fun, sqrt_fun, equal_fun

"""
    Funkcjie obsługiwane przez kalkulator
"""

def button_press(number):
    global flag

    value, flag = press(number,flag)
    equation.set(value)

def button_power2_fun():

    value = power2_fun()
    equation.set(value)

def button_sqrt_fun():

    value = sqrt_fun()
    equation.set(value)


def button_equal_fun():
    global flag
    flag = 1

    value = equal_fun()
    equation.set(value)

def button_comma():

    value = comma()
    equation.set(value)
"""
    Ustawienia początkowe okna
"""

if __name__ == "__main__":

    root = Tk()
    root.title("Kalkulator")
    root.resizable(False,False)
    
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    equation = StringVar()
    flag = 0

    """
        Ustawienie przycisków z cyframi od 0 do 9
    """
    buttons = {}
    for i in range(1,10):
        button = Button(frame, text = f"{i}", command=lambda i = i: button_press(f"{i}")).grid(row=(5- (i-1)//3), column= ((i-1)%3))
        buttons = button

    button = Button(frame, text = f"{0}", command=lambda: button_press("0")).grid(row=(5- (-1)//3), column= 1)


    """
        Dodanie podstawowych operacji jakich jak: dodawanie, odejmowanie, mnożenie, dzielenie, podnoszenie do kwadratu, pierwiastek kwadratowy
    """

    add = Button(frame, text = "+", command=lambda: button_press('+')).grid(row=5, column= 3)
    subtraction = Button(frame, text = "-", command=lambda: button_press('-')).grid(row=4, column= 3)
    multiply = Button(frame, text = "*", command=lambda: button_press('*')).grid(row=3, column= 3)
    divide = Button(frame, text = "/", command=lambda: button_press('/')).grid(row=2, column= 3)

    power2 = Button(frame, text = f"x^2", command=lambda: button_power2_fun()).grid(row=2, column=1)
    sqrt = Button(frame, text = f"sqrt", command=lambda: button_sqrt_fun()).grid(row=2, column=2)

    """
        Dodanie dodatkowych operatów: równa się, przecinka oraz wartości ujemnej
    """
    dot = Button(frame, text = ".", command=lambda: button_comma()).grid(row=(5- (-1)//3), column= 2)
    plus_minus = Button(frame, text = "+/-", command=lambda: button_press('-')).grid(row=(5- (-1)//3), column=0)


    equal = Button(frame, text = "=", command=lambda: button_equal_fun()).grid(row=(5- (-1)//3), column=3)


    """
        Tekst wyświetlany na ekranie kalkulatora
    """
    text = Label(root, height=2,textvariable=equation, width=30).grid(column=10,row=0)


    root.mainloop()


