import tkinter as tk
from tkinter import ttk
from pygame import mixer # Música
from io import open as io
from Modulos.Tienda import *
from Modulos.CalcularStatsIniciales import *
from Modulos.Batalla import *
from Modulos.Logros import *
from Modulos.Creditos import *

raiz = tk.Tk()
raiz.geometry("1920x1080")
raiz.state("zoomed")
raiz.title("Asalto Blindado")
raiz.iconbitmap("Icono.ico")

mixer.init() # Habilitar Música
mixer.set_reserved(2)	# Nosotros
mixer.Channel(2).set_volume(0.5) 
mixer.set_reserved(3)			 # Enemigo
mixer.Channel(3).set_volume(0.5)
mixer.set_reserved(4)
mixer.Channel(4).set_volume(0.5) # Extras
mixer.set_reserved(5)
mixer.Channel(5).set_volume(0.5) # Logros

BarraMenu = tk.Menu(raiz)  # Crear el menu
raiz.config(menu = BarraMenu)

ArchivoMusical = tk.Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Músicas", menu = ArchivoMusical)
ArchivoMusical.add_command(label = "The World Revolving Metal By RichaadEB", command = lambda:CambioMusica("Jevil"))
ArchivoMusical.add_command(label = "Spider Dance Metal By FalKKonE", command = lambda:CambioMusica("Spider"))
ArchivoMusical.add_command(label = "Vs. Susie Metal By FalKKonE", command = lambda:CambioMusica("Susie"))
ArchivoMusical.add_command(label = "Big Shot by Toby Fox", command = lambda:CambioMusica("Big Shot"))
ArchivoMusical.add_command(label = "Chaos King Metal By FalKKonE", command = lambda:CambioMusica("King"))
ArchivoMusical.add_command(label = "Night of Nights Metal by FalKKonE", command = lambda:CambioMusica("Night"))
ArchivoMusical.add_separator() # Crear una línea separadora
ArchivoMusical.add_command(label = "Pausar la música", command = lambda:CambioMusica("Pausar"))
ArchivoMusical.add_command(label = "Reanudar la música", command = lambda:CambioMusica("Reanudar"))
ArchivoMusical.add_command(label = "Detener la música", command = lambda:CambioMusica("Stop"))
ArchivoMusical.add_command(label = "Subir el volumen", command = lambda:CambioMusica("Mas"))
ArchivoMusical.add_command(label = "Bajar el volumen", command = lambda:CambioMusica("Menos"))

# --------------------------- Funciones que no quize poner abajo para no cambiar todo

def ExtraerStats():

	Archivo_Logros = open("Logros_Y_Estadisticas.txt","r")
	Logros = Archivo_Logros.readlines()

	Logros_Conseguidos = 0

	count = 0

	for line in Logros[0:12]:

		for line in Logros[count:count + 1]:

			Resultado = (line.split(":")[-1].strip())

			if Resultado == "True":
				Logros_Conseguidos += 1
			else:
				pass

			count += 1

	return Logros_Conseguidos

	Archivo_Logros.close()

Cantidad_Logros = ExtraerStats()

def ExtraerDatos():

	global Puntos, Tanque_DL, Tanque_M, Tanque_X, Puntos_de_Victoria, Idioma

	Archivo_Datos = open("Datos.txt","r")
	Datos = Archivo_Datos.readlines()

	for i in Datos[0:1]:
		if 'Puntos' in i:
			Puntos = i.split(":")[-1].strip()

	for i in Datos[7:8]:
		if 'Tanque_DL' in i:
			Tanque_DL = i.split(":")[-1].strip()

	for i in Datos[8:9]:
		if 'Tanque_M' in i:
			Tanque_M = i.split(":")[-1].strip()

	for i in Datos[9:10]:
		if 'Tanque_X' in i:
			Tanque_X = i.split(":")[-1].strip()

	for i in Datos[10:11]:
		if 'Puntos_de_Victoria' in i:
			Puntos_de_Victoria = i.split(":")[-1].strip()

	for i in Datos[11:12]:
		if 'Idioma:' in i:
			Idioma.set(i.split(":")[-1].strip())

	Archivo_Datos.close()

def ActualizarCambioDeIdioma(idioma):

	if Idioma.get() == "español":
		Facil_str.set("Fácil")
		Media_str.set("Media")
		Dificil_str.set("Difícil")
		Extrema_str.set("Extrema")
		Jugar_str.set("Jugar")
		Tienda_str.set("Tienda")
		Logros_str.set("Logros")
		Creditos_str.set("Créditos")
		Iniciar_str.set("Iniciar")
		Volver_str.set("Volver")
		BarraMenu.entryconfigure(1, label = "Músicas")
		ArchivoMusical.entryconfigure(7, label = "Pausar la música")
		ArchivoMusical.entryconfigure(8, label = "Reanudar la música")
		ArchivoMusical.entryconfigure(9, label = "Detener la música")
		ArchivoMusical.entryconfigure(10, label = "Subir el volumen")
		ArchivoMusical.entryconfigure(11, label = "Bajar el volumen")

	elif Idioma.get() == "english":
		Facil_str.set("Easy")
		Media_str.set("Medium")
		Dificil_str.set("Hard")
		Extrema_str.set("Extreme")
		Jugar_str.set("Play")
		Tienda_str.set("Shop")
		Logros_str.set("Achievements")
		Creditos_str.set("Credits")
		Iniciar_str.set("Start")
		Volver_str.set("Return")
		BarraMenu.entryconfigure(1, label = "Music")
		ArchivoMusical.entryconfigure(7, label = "Pause the music")
		ArchivoMusical.entryconfigure(8, label = "Resume the music")
		ArchivoMusical.entryconfigure(9, label = "Stop the music")
		ArchivoMusical.entryconfigure(10, label = "Turn up the volume")
		ArchivoMusical.entryconfigure(11, label = "Turn down the volume")

# --------------------------- Datos iniciales

Puntos = 0
Tanque_DL = False
Tanque_M = False
Tanque_X = False
Puntos_de_Victoria = 0
Idioma = tk.StringVar()
ExtraerDatos()

# -------------------------- Localización

Facil_str = tk.StringVar()
Media_str = tk.StringVar()
Dificil_str = tk.StringVar()
Extrema_str = tk.StringVar()
Jugar_str = tk.StringVar()
Tienda_str = tk.StringVar()
Logros_str = tk.StringVar()
Creditos_str = tk.StringVar()
Iniciar_str = tk.StringVar()
Volver_str = tk.StringVar()
ActualizarCambioDeIdioma(Idioma.get())

# -------------------------- Inicio

Inicio = tk.Frame(raiz)
Inicio.pack()

MonitorAncho = raiz.winfo_screenwidth()
MonitorAltura = raiz.winfo_screenheight()

DR = ((MonitorAltura)/864 + (MonitorAncho)/1536)/2

EspanolFrame = tk.Frame(raiz, bg = "#FFF", bd = Redondear(5, DR), relief = "solid", width = Redondear(200, DR))
EnglishFrame = tk.Frame(raiz, bg = "#FFF", bd = Redondear(5, DR), relief = "solid", width = Redondear(200, DR))

DificultadFrame = tk.Frame(raiz, bg = "#FFF", bd = Redondear(5, DR), relief = "solid")
ElegirTanqueFrame = tk.Frame(raiz, bg = "#FFF", bd = Redondear(5, DR), relief = "solid")
NombreFrame = tk.Frame(raiz, bg = "#FFF", bd = Redondear(5, DR), relief = "solid", width = Redondear(500, DR))

ImagenPortada = AbrirImagenEX("Imagenes/Portada.png", DR)
ImagenCompletado = AbrirImagenEX("Imagenes/Completado.png", DR)
ImagenIngles = AbrirImagenEX("Imagenes/Ingles.png", DR)
ImagenEspanol = AbrirImagenEX("Imagenes/Espanol.png", DR)

BotonEnglish = tk.Button(Inicio, image = ImagenIngles, command = lambda:SeleccionarIdioma("english"), border = Redondear(6, DR), cursor = "hand2")
BotonEnglish.grid(row = 0, column = 0, padx = Redondear(50, DR), pady = (Redondear(20, DR),0))

Portada = tk.Label(Inicio, image = ImagenPortada)
Portada.grid(row = 0, column = 1, columnspan = 2, pady = (Redondear(20, DR),0))

BotonJugar = tk.Button(Inicio, textvariable = Jugar_str, command = lambda:SeleccionarTanque(), font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), cursor = "hand2")
BotonJugar.grid(row = 1, column = 1, pady = Redondear(30, DR), sticky = "ew", padx = (0,Redondear(25, DR)))

BotonTienda = tk.Button(Inicio, textvariable = Tienda_str, command = lambda:SeleccionarTienda(DR, Idioma.get()), font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), cursor = "hand2")
BotonTienda.grid(row = 1, column = 2, sticky = "ew", padx = (Redondear(25, DR),0))

BotonLogros = tk.Button(Inicio, textvariable = Logros_str, command = lambda:SeleccionarLogros(DR, Idioma.get()), font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), cursor = "hand2")
BotonLogros.grid(row = 2, column = 1, sticky = "ew", padx = (0,Redondear(25, DR)))

BotonCreditos = tk.Button(Inicio, textvariable = Creditos_str, command = lambda:SeleccionarCreditos(DR, Idioma.get()), font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), cursor = "hand2")
BotonCreditos.grid(row = 2, column = 2, sticky = "ew", padx = (Redondear(25, DR),0))

BotonEspanol = tk.Button(Inicio, image = ImagenEspanol, command = lambda:SeleccionarIdioma("español"), border = Redondear(6, DR), cursor = "hand2")
BotonEspanol.grid(row = 0, column = 3, padx = Redondear(50, DR), pady = (Redondear(20, DR),0))

if Idioma.get() == "español":
	BotonEspanol.config(relief = "solid")
	BotonEnglish.config(relief = "raised")
elif Idioma.get() == "english":
	BotonEspanol.config(relief = "raised")
	BotonEnglish.config(relief = "solid")

Completado = tk.Label(Inicio, image = ImagenCompletado)

if Cantidad_Logros == 12:
	Completado.grid(row = 3, column = 0, columnspan = 4, pady = (Redondear(20, DR),0))

TanqueElegidoValor = tk.IntVar()

DificultadElegidaValor = tk.IntVar()

Escribir_Nombre = tk.StringVar()

Tanque_Ligero_img = AbrirImagenEX("Imagenes/Tanque_Ligero.png", DR)
Tanque_DL_img = AbrirImagenEX("Imagenes/Tanque_Destructor_Ligero.png", DR)
Tanque_M_img = AbrirImagenEX("Imagenes/Tanque_Mediano.png", DR)
Tanque_X_img = AbrirImagenEX("Imagenes/Tanque_Misterioso.png", DR)

BotonTanqueLigero = tk.Radiobutton(ElegirTanqueFrame, image = Tanque_Ligero_img, variable = TanqueElegidoValor, value = 1, font = ('Arial',35), border = Redondear(6, DR), relief = "ridge", cursor = "hand2")
BotonDestructorLigero = tk.Radiobutton(ElegirTanqueFrame, image = Tanque_DL_img, variable = TanqueElegidoValor, value = 2, font = ('Arial',35), border = Redondear(6, DR), relief = "ridge", state = "disabled")
BotonTanqueMediano = tk.Radiobutton(ElegirTanqueFrame, image = Tanque_M_img, variable = TanqueElegidoValor, value = 3, font = ('Arial',35), border = Redondear(6, DR), relief = "ridge", state = "disabled")
BotonTanqueMisterioso = tk.Radiobutton(ElegirTanqueFrame, image = Tanque_X_img, variable = TanqueElegidoValor, value = 4, font = ('Arial',35), border = Redondear(6, DR), relief = "ridge", state = "disabled")

BotonDificultadFacil = tk.Radiobutton(DificultadFrame, textvariable = Facil_str, variable = DificultadElegidaValor, command = lambda:CambioColorInicio(),
	value = 1, font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), relief = "ridge", bg = "#BCFFAB", cursor = "hand2")

BotonDificultadMedia = tk.Radiobutton(DificultadFrame, textvariable = Media_str, variable = DificultadElegidaValor, command = lambda:CambioColorInicio(), 
	value = 2, font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), relief = "ridge", bg = "#FFFCAB", cursor = "hand2")

BotonDificultadDificil = tk.Radiobutton(DificultadFrame, textvariable = Dificil_str, variable = DificultadElegidaValor, command = lambda:CambioColorInicio(), 
	value = 3, font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), relief = "ridge", bg = "#FFAB99", cursor = "hand2")

BotonDificultadExtrema = tk.Radiobutton(DificultadFrame, textvariable = Extrema_str, variable = DificultadElegidaValor, command = lambda:CambioColorInicio(), 
	value = 4, font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), relief = "ridge", bg = "#D4ABFF", cursor = "hand2")

PantallaNombre = tk.Entry(NombreFrame, font = ('Arial',Redondear(35, DR)), text = Escribir_Nombre)

BotonIniciar = tk.Button(Inicio, textvariable = Iniciar_str, command = lambda:Aceptar_Eleccion_Tanque(DR, Idioma.get()), font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), cursor = "hand2", width = 7)
BotonVolver = tk.Button(Inicio, textvariable = Volver_str, command = lambda:VolverAlMenu(), font = ('Arial',Redondear(40, DR)), border = Redondear(6, DR), cursor = "hand2", width = 7)

def character_limit(Escribir_Nombre):
    if len(Escribir_Nombre.get()) > 11:
        Escribir_Nombre.set(Escribir_Nombre.get()[:11])

Escribir_Nombre.trace("w", lambda *args: character_limit(Escribir_Nombre))

def SeleccionarIdioma(idioma):

	Archivo_Datos = open("Datos.txt","r+")
	Datos = Archivo_Datos.readlines()

	Datos[11] = f"Idioma: {idioma}"
	
	Archivo_Datos.seek(0)
	Datos = Datos[:12]

	Archivo_Datos.writelines(Datos) # Esto lo reescribe completamente
	Archivo_Datos.close()

	Idioma.set(idioma)
	ActualizarCambioDeIdioma(idioma)

	if idioma == "español":
		BotonEspanol.config(relief = "solid")
		BotonEnglish.config(relief = "raised")
	elif idioma == "english":
		BotonEspanol.config(relief = "raised")
		BotonEnglish.config(relief = "solid")

def SeleccionarTanque():

	global Tanque_M, Tanque_DL, Tanque_X

	Portada.grid_forget()
	BotonJugar.grid_forget()
	BotonTienda.grid_forget()
	BotonLogros.grid_forget()
	BotonCreditos.grid_forget()
	BotonEnglish.grid_forget()
	BotonEspanol.grid_forget()

	try:
		Completado.grid_forget()
	except:
		pass

	ElegirTanqueFrame.pack(pady = Redondear(30, DR))
	DificultadFrame.pack()
	NombreFrame.pack(pady = Redondear(30, DR))

	if Tanque_DL == "True":
		BotonDestructorLigero.config(state = "normal", cursor = "hand2")

	if Tanque_M == "True":
		BotonTanqueMediano.config(state = "normal", cursor = "hand2")

	if Tanque_X == "True":
		BotonTanqueMisterioso.config(state = "normal", cursor = "hand2")

	BotonTanqueLigero.grid(row = 0, column = 0, ipadx = Redondear(18, DR), padx = (Redondear(30, DR),Redondear(30, DR)), sticky = "nsew", pady = Redondear(25, DR))
	BotonDestructorLigero.grid(row = 0, column = 1, ipadx = Redondear(18, DR), padx = (0,Redondear(30, DR)), sticky = "nsew", pady = Redondear(25, DR))
	BotonTanqueMediano.grid(row = 0, column = 2, ipadx = Redondear(18, DR), sticky = "nsew", pady = Redondear(25, DR))
	BotonTanqueMisterioso.grid(row = 0, column = 3, ipadx = Redondear(18, DR), padx = Redondear(30, DR), sticky = "nsew", pady = Redondear(25, DR))

	BotonDificultadFacil.grid(row = 0, column = 0, ipadx = Redondear(21, DR), padx = (Redondear(30, DR),0))
	BotonDificultadMedia.grid(row = 0, column = 1, ipadx = Redondear(21, DR), pady = Redondear(30, DR), padx = Redondear(30, DR))
	BotonDificultadDificil.grid(row = 0, column = 2, ipadx = Redondear(21, DR), padx = (0, Redondear(30, DR)))
	BotonDificultadExtrema.grid(row = 0, column = 3, ipadx = Redondear(21, DR), padx = (0, Redondear(30, DR))) 

	PantallaNombre.pack()

	TanqueElegidoValor.set(0)
	DificultadElegidaValor.set(0)
	Escribir_Nombre.set("")

	BotonIniciar.grid(row = 0, column = 1, rowspan = 3, pady = (Redondear(30, DR),0), padx = (0,Redondear(40, DR)))
	BotonVolver.grid(row = 0, column = 2, rowspan = 3, pady = (Redondear(30, DR),0), padx = (Redondear(40, DR),0))

def Aceptar_Eleccion_Tanque(DR, idioma):  # Tipo de tanque

	if TanqueElegidoValor.get() != 0 and DificultadElegidaValor.get() != 0 and Escribir_Nombre.get() != "":
		EmpezarJuego(DR, idioma)

	else:
		pass

def VolverAlMenu():

	Cantidad_Logros = ExtraerStats()

	try:
		BotonIniciar.grid_forget()
		BotonVolver.grid_forget()
		DificultadFrame.pack_forget()
		ElegirTanqueFrame.pack_forget()
		NombreFrame.pack_forget()
	except:
		pass

	Inicio.pack()
	BotonEnglish.grid(row = 0, column = 0, padx = Redondear(50, DR), pady = (Redondear(20, DR),0))
	Portada.grid(row = 0, column = 1, columnspan = 2, pady = (Redondear(20, DR),0))
	BotonJugar.grid(row = 1, column = 1, pady = Redondear(30, DR), sticky = "ew", padx = (0,Redondear(25, DR)))
	BotonTienda.grid(row = 1, column = 2, sticky = "ew", padx = (Redondear(25, DR),0))
	BotonLogros.grid(row = 2, column = 1, sticky = "ew", padx = (0,Redondear(25, DR)))
	BotonCreditos.grid(row = 2, column = 2, sticky = "ew", padx = (Redondear(25, DR),0))
	BotonEspanol.grid(row = 0, column = 3, padx = Redondear(50, DR), pady = (Redondear(20, DR),0))

	if Cantidad_Logros == 12:
		Completado.grid(row = 3, column = 0, columnspan = 4, pady = (Redondear(20, DR),0))

def SeleccionarTienda(DR, idioma):

	Portada.grid_forget()
	BotonJugar.grid_forget()
	BotonTienda.grid_forget()
	BotonLogros.grid_forget()
	BotonCreditos.grid_forget()
	BotonEnglish.grid_forget()
	BotonEspanol.grid_forget()
	Inicio.pack_forget()

	try:
		Completado.grid_forget()
	except:
		pass

	Tiendita = Tienda(DR, idioma, raiz)

	def CheckVisibilidad():

		if Tiendita.Botones_Frame.winfo_exists() == 1:
			Inicio.after(250, CheckVisibilidad)

		else:
			VolverAlMenu()

	CheckVisibilidad()

def CambioColorInicio():

	if DificultadElegidaValor.get() == 1:
		BotonDificultadFacil.config(bg = "#87FF69") # Verde más fuerte
		BotonDificultadMedia.config(bg = "#FFFCAB")
		BotonDificultadDificil.config(bg = "#FFAB99")
		BotonDificultadExtrema.config(bg = "#D4ABFF")

	elif DificultadElegidaValor.get() == 2:

		BotonDificultadFacil.config(bg = "#BCFFAB")
		BotonDificultadMedia.config(bg = "#FFF83B") # Amarillo más fuerte
		BotonDificultadDificil.config(bg = "#FFAB99")
		BotonDificultadExtrema.config(bg = "#D4ABFF")

	elif DificultadElegidaValor.get() == 3:

		BotonDificultadFacil.config(bg = "#BCFFAB")
		BotonDificultadMedia.config(bg = "#FFFCAB")
		BotonDificultadDificil.config(bg = "#FF613F") # Rojo más fuerte
		BotonDificultadExtrema.config(bg = "#D4ABFF")

	elif DificultadElegidaValor.get() == 4:

		BotonDificultadFacil.config(bg = "#BCFFAB")
		BotonDificultadMedia.config(bg = "#FFFCAB")
		BotonDificultadDificil.config(bg = "#FFAB99")
		BotonDificultadExtrema.config(bg = "#B66EFF") # Morado más fuerte

def EmpezarJuego(DR, idioma):

	BotonDificultadFacil.config(bg = "#BCFFAB")
	BotonDificultadMedia.config(bg = "#FFFCAB")
	BotonDificultadDificil.config(bg = "#FFAB99")
	BotonDificultadExtrema.config(bg = "#D4ABFF")

	Inicio.pack_forget()
	BotonIniciar.grid_forget()
	BotonVolver.grid_forget()
	DificultadFrame.pack_forget()
	ElegirTanqueFrame.pack_forget()
	NombreFrame.pack_forget()
	Yo = CalcularMisDatos(TanqueElegidoValor.get(), Escribir_Nombre.get())
	Enemigo = CalcularDatosEnemigos(DificultadElegidaValor.get())

	Juego = Batalla(Yo, Enemigo, DR, idioma, raiz, BarraMenu)

	def CheckVisibilidad():

		if Juego.FramePrincipal.winfo_exists() == 1:
			Inicio.after(500, CheckVisibilidad)

		else:
			VolverAlMenu()

	CheckVisibilidad()

def CambioMusica(Musica):
	if Musica == "Jevil":
		mixer.music.load("Musicas_Random/001 - The World Revolving Metal.mp3")
		mixer.music.set_volume(0.085)
		mixer.music.play(loops = 0)

	elif Musica == "Spider":
		mixer.music.load("Musicas_Random/002 - Spider Dance Metal.mp3")
		mixer.music.set_volume(0.09)
		mixer.music.play(loops = 0)

	elif Musica == "Susie":
		mixer.music.load("Musicas_Random/003 - Vs. Susie Metal.mp3")
		mixer.music.set_volume(0.07)
		mixer.music.play(loops = 0)

	elif Musica == "Big Shot":
		mixer.music.load("Musicas_Random/004 - Big Shot.mp3")
		mixer.music.set_volume(0.13)
		mixer.music.play(loops = 0)

	elif Musica == "King":
		mixer.music.load("Musicas_Random/005 - Chaos King Metal.mp3")
		mixer.music.set_volume(0.09)
		mixer.music.play(loops = 0)

	elif Musica == "Night":
		mixer.music.load("Musicas_Random/006 - Night of Nights Metal.mp3")
		mixer.music.set_volume(0.085)
		mixer.music.play(loops = 0)

	elif Musica == "Pausar":
		Volumen = mixer.music.pause()

	elif Musica == "Reanudar":
		Volumen = mixer.music.unpause()

	elif Musica == "Mas":
		Volumen = mixer.music.get_volume()
		mixer.music.set_volume(Volumen + 0.01)

	elif Musica == "Menos":
		Volumen = mixer.music.get_volume()
		mixer.music.set_volume(Volumen - 0.01)

	elif Musica == "Stop":
		mixer.music.stop()

def SeleccionarCreditos(DR, idioma):

	Portada.grid_forget()
	BotonJugar.grid_forget()
	BotonTienda.grid_forget()
	BotonLogros.grid_forget()
	BotonCreditos.grid_forget()
	BotonEnglish.grid_forget()
	BotonEspanol.grid_forget()
	Inicio.pack_forget()

	try:
		Completado.grid_forget()
	except:
		pass

	PantallaCreditos = Creditos(DR, idioma, raiz)

	def CheckVisibilidad():

		if PantallaCreditos.Creditos_Frame.winfo_exists() == 1:
			Inicio.after(250, CheckVisibilidad)

		else:
			VolverAlMenu()

	CheckVisibilidad()

def SeleccionarLogros(DR, idioma):

	Portada.grid_forget()
	BotonJugar.grid_forget()
	BotonTienda.grid_forget()
	BotonLogros.grid_forget()
	BotonCreditos.grid_forget()
	BotonEnglish.grid_forget()
	BotonEspanol.grid_forget()
	Inicio.pack_forget()

	try:
		Completado.grid_forget()
	except:
		pass

	PantallaLogros = Logros(DR, idioma, raiz)

	def CheckVisibilidad():

		if PantallaLogros.Botones_Frame.winfo_exists() == 1:
			Inicio.after(250, CheckVisibilidad)

		else:
			VolverAlMenu()

	CheckVisibilidad()

Inicio.mainloop()