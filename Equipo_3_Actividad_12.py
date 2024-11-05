import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import itertools
from tkinter import ttk, Label
from itertools import cycle
import pygame
from tkinter import messagebox

class VentanaCreditos:
    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title("Créditos")
        self.ventana.geometry("730x650")
        self.ventana.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        # Colores
        self.dia_de_muertos_colors = ["#000000", "#4B0082", "#138b75", "#8b1362", "#c5c174"]
        self.color_naranja_muertos = "#FF6B1A"  # Naranja Día de Muertos
        self.color_cycle = itertools.cycle(self.dia_de_muertos_colors)
        self.current_color = self.dia_de_muertos_colors[0]
        
        # Cargar logos
        try:
            self.logo_uv = ImageTk.PhotoImage(Image.open("LogoUV.png").resize((80, 100)))
            self.logo_fiee = ImageTk.PhotoImage(Image.open("LogoFIEE.png").resize((100, 100)))
            
            # Mostrar logos
            logo_uv_label = Label(self.ventana, image=self.logo_uv, bg=self.current_color)
            logo_uv_label.grid(row=0, column=0, padx=(10, 20), pady=10, sticky="e")
            logo_fiee_label = Label(self.ventana, image=self.logo_fiee, bg=self.current_color)
            logo_fiee_label.grid(row=0, column=2, padx=(380, 10), pady=10, sticky="w")
            
            self.logo_labels = [logo_uv_label, logo_fiee_label]
        except Exception as e:
            print(f"Error al cargar los logos: {e}")
            self.logo_labels = []
        
        # Encabezado
        self.header = tk.Label(self.ventana, 
                         text="PythonPan de Muertos\nReto de Visualización del Día de Muertos",
                         font=("Arial", 18, "bold"), 
                         fg="white",
                         bg=self.current_color)
        self.header.grid(row=0, column=1, columnspan=2, padx=10, pady=20, sticky="w")
        
        # Información del curso
        self.info = tk.Label(self.ventana, 
                       text="Materia: Sistemas Interaccion Humano Computadora (NRC: 13221)\n"
                            "Profesor: Raul Juarez Aguirre\n"
                            "Facultad de Ingeniería Eléctrica y Electrónica (FIEE) - Universidad Veracruzana (UV)",
                       font=("Arial", 12),
                       fg="white",
                       bg=self.current_color)
        self.info.grid(row=1, column=0, columnspan=4, padx=40, pady=20, sticky="n")
        
        # Información de integrantes con GIFs
        self.integrantes = [
            ("Bravo Ibañez Luis Fernando - zS21002428   ", "CalaveraFiestera.gif"),
            ("Contreras Matla Luis Fernando - zS21020225", "CalaveraGay.gif"),
            ("Garcia Velandia Samuel Obed - zS21002413  ", "CalaveraEnamorada.gif"),
            ("Policarpio Moran Michell Alexis - zS21002379", "CalaveraDinero.gif")
        ]
        
        self.gif_labels = []
        self.name_labels = []
        self.frames_by_label = {}
        
        # Crear y colocar GIFs y nombres
        for i, (nombre, gif) in enumerate(self.integrantes, start=2):
            try:
                # Cargar y preparar el GIF
                gif_image = Image.open(gif)
                frames = []
                for frame in ImageSequence.Iterator(gif_image):
                    frame_copy = frame.copy()
                    frame_copy = frame_copy.resize((90, 90))
                    frame_tk = ImageTk.PhotoImage(frame_copy)
                    frames.append(frame_tk)
                
                # Label para el GIF
                gif_label = Label(self.ventana, bg=self.current_color)
                gif_label.grid(row=i, column=1, padx=10, pady=5, sticky="e")
                self.gif_labels.append(gif_label)
                self.frames_by_label[gif_label] = frames
                
                # Frame naranja para el nombre
                name_frame = tk.Frame(self.ventana, bg=self.color_naranja_muertos)
                name_frame.grid(row=i, column=2, columnspan=2, padx=40, pady=30, sticky="w")
                
                # Label del nombre
                name_label = tk.Label(name_frame, 
                                    text=nombre, 
                                    font=("Arial", 12, "bold"),
                                    fg="white",
                                    bg=self.color_naranja_muertos,
                                    padx=15,
                                    pady=8)
                name_label.pack()
                self.name_labels.append(name_frame)
                
                # Iniciar animación
                self.animate_gif(gif_label, frames)
                
            except Exception as e:
                print(f"Error al cargar el GIF {gif}: {e}")
        
        # Iniciar cambio de fondo
        self.change_background()
    
    def change_background(self):
        """Cambia el color de fondo periódicamente"""
        self.current_color = next(self.color_cycle)
        
        # Actualizar color de la ventana
        self.ventana.configure(bg=self.current_color)
        
        # Actualizar color de los elementos
        for label in self.gif_labels + self.logo_labels:
            label.configure(bg=self.current_color)
        
        self.header.configure(bg=self.current_color)
        self.info.configure(bg=self.current_color)
        
        self.ventana.after(500, self.change_background)
    
    def animate_gif(self, label, frames, idx=0):
        """Anima un GIF específico"""
        if label.winfo_exists():
            frame = frames[idx]
            label.configure(image=frame)
            label.image = frame
            next_idx = (idx + 1) % len(frames)
            self.ventana.after(40, lambda: self.animate_gif(label, frames, next_idx))

class VentanaAnimada:
    def __init__(self, root):
        self.root = root
        self.root.title("Ofrenda Virtual")
        self.root.geometry("1150x755")
        ##self.root.iconbitmap("calavera.ico")
        
        # Crear menú
        self.crear_menu()
        
        # Inicializar pygame para el audio
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("La Muerte y La Ecuacion.mp3")
            pygame.mixer.music.play(-1)  # Reproducir música automáticamente en loop
        except Exception as e:
            print(f"Error al cargar la música: {e}")
        
        # Marco decorativo
        self.marco = tk.Frame(self.root, bg="#FF8C00", bd=10)
        self.marco.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Canvas
        self.canvas = tk.Canvas(self.marco, bg="#B2EBF2")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Variables de estado
        self.frames_gifs = {'izquierda': None, 'centro': None, 'derecha': None}
        self.frame_actual = {'izquierda': 0, 'centro': 0, 'derecha': 0}
        self.gif_en_canvas = {'izquierda': None, 'centro': None, 'derecha': None}
        
        # Cargar y colocar las imágenes de tumbitas
        try:
            # Cargar imagen de Diana
            diana_img = Image.open("tumbitawoo.png")
            diana_img = diana_img.resize((150, 140), Image.LANCZOS)
            self.diana_photo = ImageTk.PhotoImage(diana_img)
            self.canvas.create_image(100, 547, anchor="nw", image=self.diana_photo)
            
            # Cargar imagen de Woo
            woo_img = Image.open("tumbitadiana.png")
            woo_img = woo_img.resize((150, 140), Image.LANCZOS)
            self.woo_photo = ImageTk.PhotoImage(woo_img)
            self.canvas.create_image(850, 547, anchor="nw", image=self.woo_photo)
        except Exception as e:
            print(f"Error al cargar las imágenes: {e}")
        
        # Variables para velitas
        self.velita_frames = []
        self.velita_items = []
        self.velita_index = 0
        
        # Línea decorativa
        self.canvas.create_line(15, 20, 1100, 15, fill="black", width=2)
        
        # Cargar imágenes del papel picado
        self.imagenes_papel = []
        for i in range(1, 5):
            imagen = Image.open(f"papel{i}.png").resize((50, 42), Image.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(imagen)
            self.imagenes_papel.append(imagen_tk)
        
        # Colocar papeles picados
        self.colocar_papeles_picados()
        
        # Cursor personalizado
        cursor_image = Image.open("calaveramouse.png").resize((40, 40), Image.LANCZOS)
        self.imagen_cursor_tk = ImageTk.PhotoImage(cursor_image)
        self.imagen_cursor = self.canvas.create_image(0, 0, anchor="center", image=self.imagen_cursor_tk)
        
        # Dividir la calaverita en dos partes
        self.parte1 = """Estaba la muerte resolviendo una ecuacion diferencial,
Que ni la maestra Diana había podido controlar
Pues la integración por partes tampoco era el método para avanzar.

Acudieron al cementerio,
se encontraron a la profesora Woo
Con sus conocimientos de electrónica,
parecía una gurú, 
pero no la pudo resolver ella, ni Diana, ni tú."""

        self.parte2 = """Programarla en python quizá era el remedio
Pero en el curso de IA no estaba la ecuación en el libreto
La resolución de esa ecuacion diferencial
parecía el más profundo secreto.

A todos los seres que nos visitan del más allá
Su ayuda para resolver esta ecuacion diferencial
les venimos a implorar
Ya que ni Luis, Poli, Samuel y Matla lograron concretar
Así que una calaverita se pusieron a redactar."""

        # Variable para controlar qué parte se muestra
        self.mostrar_parte1 = True
        
        # Crear un rectángulo semitransparente para el fondo del texto
        self.texto_bg = self.canvas.create_rectangle(
            150, 150, 950, 400,
            fill='#B2EBF2',
            outline='#FF8C00',
            width=8
        )
        
        # Texto inicial (parte 1)
        self.texto_calaverita = self.canvas.create_text(
            550, 275,
            text=self.parte1,
            fill="black", 
            font=("impact", 14),
            anchor="center",
            justify="center"
        )
        
        # Botón para cambiar entre partes
        self.boton_cambiar = tk.Button(
            self.canvas,
            text="Siguiente Parte",
            font=("arial", 12),
            command=self.cambiar_texto,
            bg="#FF8C00",
            fg="black",
            relief="raised",
            bd=3
        )
        self.boton_cambiar_window = self.canvas.create_window(
            550, 440,
            window=self.boton_cambiar,
            anchor="center"
        )
        
        # Cargar GIFs y velitas
        self.cargar_gifs()
        self.cargar_velitas()
        
        # Configuración de animación del texto
        self.animacion = itertools.cycle([0, 2, 4, 2, 0, -2, -4, -2])
        self.animar_calaverita()
        
        # Colores para el fondo
        self.colores = cycle([
            '#800020',  # Naranja cempasúchil
            '#4B0082',  # Índigo (morado tradicional)
            '#8B4513',  # Marrón (color tierra/barro)
            '#8b1362',
            '#c5c174',
            '#138b75'   # Dorado (para las veladoras)
        ])
        
        # Configuración del cursor
        self.root.config(cursor="none")
        self.canvas.bind("<Motion>", self.actualizar_posicion)
        
        # Iniciar animaciones
        self.actualizar_velitas()
        self.animar_gifs()

    def crear_menu(self):
        # Crear la barra de menú
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menú de opciones
        opciones_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opciones", menu=opciones_menu)
        
        # Añadir elementos al menú
        opciones_menu.add_command(label="Créditos", command=self.mostrar_creditos)
        opciones_menu.add_command(label="Ayuda", command=self.mostrar_ayuda)
        opciones_menu.add_separator()
        opciones_menu.add_command(label="Salir", command=self.cerrar_aplicacion)

    def mostrar_creditos(self):
        VentanaCreditos()

    def mostrar_ayuda(self):
        messagebox.showinfo("Ayuda", 
            "Bienvenido a la Ofrenda Virtual!\n\n"
            "- Use el botón 'Siguiente Parte' para ver la calaverita completa\n"
            "- Disfrute de las animaciones y la música\n"
            "- El cursor es personalizado con tema de Día de Muertos\n"
            "- Puede acceder a los créditos desde el menú Opciones")

    def cerrar_aplicacion(self):
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            self.root.destroy()

    def cargar_gifs(self):
        y_position = 545
        
        gif_info = {
            'izquierda': ("Calaverita.gif", (350, y_position)),
            'centro': ("CalaveraBaileSuelo.gif", (550, y_position)),
            'derecha': ("CalaveraTocandoSaxofon.gif", (750, y_position))
        }
        
        for gif_id, (filename, position) in gif_info.items():
            try:
                gif = Image.open(filename)
                frames = []
                
                for frame in ImageSequence.Iterator(gif):
                    frame = frame.resize((200, 200), Image.LANCZOS)
                    frame_tk = ImageTk.PhotoImage(frame)
                    frames.append(frame_tk)
                
                self.frames_gifs[gif_id] = frames
                self.gif_en_canvas[gif_id] = self.canvas.create_image(
                    position[0], position[1],
                    image=frames[0]
                )
                
            except Exception as e:
                print(f"Error al cargar el GIF {filename}: {e}")
                self.frames_gifs[gif_id] = None

    def cambiar_texto(self):
        self.mostrar_parte1 = not self.mostrar_parte1
        texto_actual = self.parte1 if self.mostrar_parte1 else self.parte2
        self.boton_cambiar.config(text="Siguiente Parte" if self.mostrar_parte1 else "Parte Anterior")
        self.canvas.itemconfig(self.texto_calaverita, text=texto_actual)

    def colocar_papeles_picados(self):
        x = 35
        espacio = 74
        for i in range(15):
            imagen = self.imagenes_papel[i % len(self.imagenes_papel)]
            self.canvas.create_image(x, 20, anchor="n", image=imagen)
            x += espacio

    def cargar_velitas(self):
        velita_gif = Image.open("velita.gif")
        for i in range(velita_gif.n_frames):
            velita_gif.seek(i)
            frame = velita_gif.copy().resize((60, 60), Image.LANCZOS).convert("RGBA").convert("P")
            self.velita_frames.append(ImageTk.PhotoImage(frame))

        velita_positions = [(350, 670), (450, 670), (550, 670), 
                          (650, 670), (750, 670)]
        
        for pos in velita_positions:
            velita_item = self.canvas.create_image(pos[0], pos[1], image=self.velita_frames[0])
            self.velita_items.append(velita_item)

    def actualizar_velitas(self):
        self.velita_index = (self.velita_index + 1) % len(self.velita_frames)
        for item in self.velita_items:
            self.canvas.itemconfig(item, image=self.velita_frames[self.velita_index])
        self.root.after(100, self.actualizar_velitas)

    def animar_gifs(self):
        for gif_id in self.frames_gifs:
            if self.frames_gifs[gif_id]:
                self.frame_actual[gif_id] = (self.frame_actual[gif_id] + 1) % len(self.frames_gifs[gif_id])
                self.canvas.itemconfig(
                    self.gif_en_canvas[gif_id],
                    image=self.frames_gifs[gif_id][self.frame_actual[gif_id]]
                )
        
        if self.frame_actual['centro'] % 40 == 0:
            self.canvas.configure(bg=next(self.colores))
            self.canvas.itemconfig(self.texto_bg, fill='#B2EBF2')
        
        self.root.after(35, self.animar_gifs)

    def mover_cursor(self, event):
        if not self.root.winfo_exists():
            return
        self.canvas.coords(self.imagen_cursor, event.x, event.y)
        self.canvas.tag_raise(self.imagen_cursor)
    
    def actualizar_posicion(self, event):
        self.root.after(5, self.mover_cursor, event)
    
    def animar_calaverita(self):
        y_base = 275
        y = y_base + next(self.animacion)
        self.canvas.coords(self.texto_calaverita, 550, y)
        self.canvas.coords(self.texto_bg, 150, y-125, 950, y+125)
        self.root.after(150, self.animar_calaverita)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaAnimada(root)
    root.mainloop()