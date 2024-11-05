import tkinter as tk

def mover():
    global dx, dy
    x1, y1, x2, y2 = lienzo.coords(circulo)
    
    if x1 <= 0 or x2 >= 300:
        dx = -dx  # Cambia de dirección en X
    if y1 <= 0 or y2 >= 200:
        dy = -dy  # Cambia de dirección en Y
    
    lienzo.move(circulo, dx, dy)
    ventana.after(30, mover)

ventana = tk.Tk()
lienzo = tk.Canvas(ventana, width=300, height=200)
lienzo.pack()

circulo = lienzo.create_oval(10, 10, 50, 50, fill='green')

dx, dy = 5, 3  # Velocidad inicial en X e Y
mover()

ventana.mainloop()
