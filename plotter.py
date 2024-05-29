import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import re

# Function to plot the graph
def plot_graph(expression, x_min=-10, x_max=10):
    try:
        if not expression.strip():
            raise ValueError("Wprowadź wyrażenie.")
        
        # Remove 'y=' prefix if present
        expression = re.sub(r'^\s*y\s*=\s*', '', expression, flags=re.IGNORECASE)
        
        # Create a range of x values
        x = sp.symbols('x')
        expr = sp.sympify(expression)
        f = sp.lambdify(x, expr, 'numpy')
        
        if 'log' in str(expr):
            x_vals = np.linspace(0.1, x_max, 400)  # Avoid log(0) and negative values
        elif 'tan' in str(expr):
            x_vals = np.linspace(x_min, x_max, 400)
            x_vals = x_vals[np.abs(np.cos(x_vals)) > 0.1]  # Avoid points where cos(x) is close to 0
        else:
            x_vals = np.linspace(x_min, x_max, 400)
        
        y_vals = f(x_vals)
        
        # Enable interactive mode
        plt.ion()
        
        # Plot the graph
        plt.figure()
        plt.plot(x_vals, y_vals)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Wykres funkcji: {expression}')
        plt.grid(True)
        if 'tan' in str(expr):
            plt.ylim([-10, 10])  # Limit y-axis to make the graph look better
        plt.show()
    except ValueError as ve:
        messagebox.showerror("Błąd", str(ve))
    except Exception as e:
        messagebox.showerror("Błąd", f"Nieprawidłowe wyrażenie: {e}")

# Function to save the plot
def save_plot():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            plt.savefig(file_path)
            messagebox.showinfo("Zapisano", f"Wykres zapisano jako {file_path}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zapisać wykresu: {e}")

# Function to load the plot
def load_plot():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            img = plt.imread(file_path)
            plt.imshow(img)
            plt.axis('off')
            plt.show()
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się wczytać wykresu: {e}")

# Function to create the GUI
def create_plotter_gui():
    root = tk.Tk()
    root.title("Kalkulator z Wykresem")

    def on_button_click():
        expression = entry.get()
        plot_graph(expression)

    # Create entry widget
    entry = tk.Entry(root, width=40)
    entry.pack(pady=10)

    # Create a frame for the buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Create buttons
    plot_button = tk.Button(button_frame, text="Pokaż wykres", command=on_button_click)
    plot_button.grid(row=0, column=0, padx=5)

    save_button = tk.Button(button_frame, text="Zapisz wykres", command=save_plot)
    save_button.grid(row=0, column=1, padx=5)

    load_button = tk.Button(button_frame, text="Wczytaj wykres", command=load_plot)
    load_button.grid(row=0, column=2, padx=5)

    # Create instruction label
    instructions = tk.Label(root, text="""
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
""", justify=tk.LEFT)
    instructions.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_plotter_gui()