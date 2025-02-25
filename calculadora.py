import tkinter as tk

# Función para evaluar la expresión matemática ingresada
def evaluate_expression():
    try:
        # Evaluar la expresión ingresada en la caja de texto
        result = eval(entry.get())
        entry.delete(0, tk.END)  # Borrar la entrada anterior
        entry.insert(tk.END, str(result))  # Mostrar el resultado
    except Exception as e:
        entry.delete(0, tk.END)  # Borrar la entrada en caso de error
        entry.insert(tk.END, "Error")  # Mostrar un mensaje de error

# Función para manejar el botón "Clear" que borra la pantalla
def clear_entry():
    entry.delete(0, tk.END)

# Función para manejar los botones de números y operadores
def append_to_entry(value):
    entry.insert(tk.END, value)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear una caja de texto para ingresar la expresión matemática
entry = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones para números y operadores
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Crear y colocar los botones en la ventana
for (text, row, col) in buttons:
    if text == '=':
        # Botón "=" para calcular el resultado
        btn = tk.Button(root, text=text, font=("Arial", 18), command=evaluate_expression)
    else:
        # Otros botones para números y operadores
        btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: append_to_entry(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Botón para borrar la entrada
btn_clear = tk.Button(root, text="C", font=("Arial", 18), command=clear_entry)
btn_clear.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Ajustar tamaño de las filas y columnas
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Ejecutar la aplicación
root.mainloop()
