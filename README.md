# 🎭 PythonPan de Muertos: Ofrenda Virtual Interactiva

<div align="center">

![Día de Muertos](https://img.shields.io/badge/Festividad-D%C3%ADa%20de%20Muertos-orange?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Activo-success?style=for-the-badge)
![Framework](https://img.shields.io/badge/Framework-Tkinter-purple?style=for-the-badge)

---

🏆 *Una celebración digital de la tradición mexicana más colorida*

[Características](#-características) • 
[Instalación](#%EF%B8%8F-instalación) • 
[Uso](#-uso) • 
[Contribuir](#-contribuir) • 
[Créditos](#-créditos)

</div>

## 🌟 Descripción

**PythonPan de Muertos** es una experiencia interactiva que fusiona la programación moderna con la rica tradición del Día de Muertos mexicano. Esta aplicación única transforma tu pantalla en una vibrante ofrenda digital, donde cada elemento ha sido cuidadosamente diseñado para honrar esta celebración ancestral.

### 🎨 Diseño Visual
```
┌────────────────────────────────────┐
│     🎭 Papel Picado Animado 🎭     │
├────────────────────────────────────┤
│                                    │
│    📜 Calaverita Literaria 📜     │
│                                    │
│    🕯️     💀     🌺     💀     🕯️  │
│                                    │
│         [Controles GUI]           │
└────────────────────────────────────┘
```

## ✨ Características

### 🎭 Elementos Visuales Dinámicos
- **Velas Danzantes** 
  - Animación fluida de llamas
  - Efecto de parpadeo realista
  - Cambio dinámico de intensidad

- **Calaveras Animadas** 
  - GIFs personalizados con personalidad única
  - Movimientos coordinados
  - Interacción con el entorno

- **Efectos Ambientales**
  - Cambios de color atmosféricos
  - Transiciones suaves
  - Paleta inspirada en el Día de Muertos

### 🎵 Experiencia Auditiva
- Música de fondo temática
- Controles de reproducción discretos
- Ambiente inmersivo

### 💻 Interfaz Intuitiva
- **Navegación Fluida**
  - Cursor personalizado con diseño de calavera
  - Menús contextuales temáticos
  - Transiciones suaves entre secciones

- **Elementos Interactivos**
  - Botones con efectos hover
  - Animaciones responsivas
  - Retroalimentación visual

## 🛠️ Tecnologías Utilizadas

<div align="center">

| Tecnología | Uso |
|------------|-----|
| ![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python) | Lenguaje base |
| ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-purple?style=flat-square) | Interfaz gráfica |
| ![Pillow](https://img.shields.io/badge/Pillow-Imágenes-orange?style=flat-square) | Procesamiento de imágenes |
| ![Pygame](https://img.shields.io/badge/Pygame-Audio-red?style=flat-square) | Sistema de audio |

</div>

## 🏗️ Instalación

### Prerequisitos
```bash
# Verifica tu versión de Python
python --version  # Debe ser 3.x
```

### Pasos de Instalación

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu-usuario/pythonpan-de-muertos.git
   cd pythonpan-de-muertos
   ```

2. **Crear y Activar Entorno Virtual**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/MacOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar Recursos**
   ```
   proyecto/
   ├── assets/
   │   ├── gifs/
   │   │   ├── Calaverita.gif
   │   │   ├── CalaveraBaileSuelo.gif
   │   │   └── CalaveraTocandoSaxofon.gif
   │   ├── images/
   │   │   ├── papel1.png
   │   │   └── ...
   │   └── music/
   │       └── La Muerte y La Ecuacion.mp3
   ├── main.py
   └── README.md
   ```

## 🚀 Uso

### Iniciar la Aplicación
```bash
python main.py
```

### 🎮 Guía de Navegación

#### Panel Principal
- 🖱️ **Cursor Personalizado**: Navega con un cursor temático
- 🔄 **Botón "Siguiente Parte"**: Alterna entre partes de la calaverita
- 🎵 **Control de Música**: Reproduce/pausa la música de fondo

#### Menú de Opciones
1. **Créditos** 
   - Información del equipo
   - Logos institucionales
   - Animaciones especiales

2. **Ayuda**
   - Guía de usuario
   - Controles
   - Información adicional

3. **Salir**
   - Cierre seguro
   - Guardado de preferencias

## 💡 Características Avanzadas

### Sistema de Animación
```python
# Ejemplo de implementación de animaciones
def animar_calaverita(self):
    y_base = 275
    y = y_base + next(self.animacion)
    self.canvas.coords(self.texto_calaverita, 550, y)
    self.root.after(150, self.animar_calaverita)
```

### Gestión de Recursos
```python
# Ejemplo de carga de recursos
def cargar_recursos(self):
    self.frames_gifs = {}
    self.velita_frames = []
    # Implementación de carga...
```

## 👥 Créditos

### Equipo de Desarrollo
<div align="center">

| Rol | Desarrollador |
|-----|--------------|
| 👨‍💻 Frontend | Bravo Ibañez Luis Fernando |
| 🎨 Diseño | Contreras Matla Luis Fernando |
| 🔧 Backend | Garcia Velandia Samuel Obed |
| 📊 Testing | Policarpio Moran Michell Alexis |

</div>

### Institucional
- **Universidad Veracruzana (UV)**
  - Facultad de Ingeniería Eléctrica y Electrónica (FIEE)
  - Curso: Sistemas de Interacción Humano-Computadora
  - NRC: 13221

### Dirección Académica
- **Profesor**: Raul Juarez Aguirre

## 🤝 Contribuir

¡Nos encantaría recibir tu ayuda! Aquí te explicamos cómo:

1. 🍴 Fork el proyecto
2. 🔨 Crea tu rama de características
   ```bash
   git checkout -b feature/NuevaCaracteristica
   ```
3. 💻 Realiza tus cambios
4. 📝 Documenta en el README si es necesario
5. 🚀 Push a tu rama
   ```bash
   git push origin feature/NuevaCaracteristica
   ```
6. 🔄 Abre un Pull Request

## 📄 Licencia

Este proyecto está protegido bajo la Licencia MIT. Consulta el archivo [`LICENSE`](LICENSE) para más detalles.

## 🌟 Agradecimientos

Un agradecimiento especial a:
- 🏫 Universidad Veracruzana
- 👨‍🏫 Profesor Raul Juarez Aguirre
- 👥 Todos los contribuidores

---

<div align="center">

**¿Encontraste un bug? ¿Tienes una sugerencia?**  
Abre un [issue](https://github.com/tu-usuario/pythonpan-de-muertos/issues) 🐛

[![Síguenos](https://img.shields.io/github/followers/tu-usuario?style=social)](https://github.com/tu-usuario)

</div>
