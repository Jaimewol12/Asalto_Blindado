import tkinter as tk
from tkinter import ttk
from pygame import mixer
from PIL import ImageTk, Image
from io import open as io
from random import choice, randint, random

def AbrirImagen(archivo, DiferenciaResolucion):

		ImagenReajustada = Image.open(archivo)		# Abrir Imagen

		Ancho, Altura = ImagenReajustada.size		
		Ancho = round(Ancho*DiferenciaResolucion)
		Altura = round(Altura*DiferenciaResolucion)
		Medidas = Ancho, Altura

		ImagenReajustada = ImagenReajustada.resize(Medidas, Image.ANTIALIAS) # Ajustar el tamaño de la imagen

		ImagenReajustada = ImageTk.PhotoImage(ImagenReajustada)

		return ImagenReajustada

def AbrirImagenEX(archivo, DiferenciaResolucion):

		ImagenReajustada = Image.open(archivo)

		Ancho, Altura = ImagenReajustada.size
		Ancho = round(Ancho*DiferenciaResolucion)
		Altura = round(Altura*DiferenciaResolucion)
		Medidas = Ancho, Altura

		ImagenReajustada = ImagenReajustada.resize(Medidas, Image.ANTIALIAS)

		ImagenReajustada = ImagenReajustada.convert("RGBA") # Eliminar el fondo negro que aparece en algunas imagenes
		Datas = ImagenReajustada.getdata()

		newData = []

		for item in Datas:
			if item[0] == 255 and item[1] == 255 and item[2] == 255:
				newData.append((255, 255, 255, 0))
			else:
				newData.append(item)
				
		ImagenReajustada.putdata(newData)

		ImagenReajustada = ImageTk.PhotoImage(ImagenReajustada)

		return ImagenReajustada

def Redondear(Valor, DiferenciaResolucion):
	return round(Valor*DiferenciaResolucion)

class Batalla():

	def __init__(self, Yo, Enemigo, DR, idioma, raiz = None, BarraMenu = None):

		self.DR = DR
		self.Idioma = idioma
		mixer.init()

		# --------------------------- Imagenes

		self.Ataque_1 = AbrirImagen("Imagenes/Municion.png", self.DR)
		self.Ataque_2 = AbrirImagen("Imagenes/GolpeDoble.png", self.DR)
		self.Ataque_3 = AbrirImagen("Imagenes/PerforadorBlindaje.png", self.DR)
		self.Ataque_4 = AbrirImagen("Imagenes/BalaExplosiva.png", self.DR)
		self.Ataque_5 = AbrirImagen("Imagenes/BombardeoAereo.png", self.DR)
		self.Ataque_5_Mira = AbrirImagenEX("Imagenes/Mira.png", self.DR)

		self.Ataque_6_Izquierda = AbrirImagenEX("Imagenes/Izquierda.png", self.DR)
		self.Ataque_6_Derecha = AbrirImagenEX("Imagenes/Derecha.png", self.DR)

		self.Ataque_7 = AbrirImagen("Imagenes/FuegoAbrumador.png", self.DR)

		self.Ataque_8 = AbrirImagen("Imagenes/Embestida.png", self.DR)
		self.Ataque_8_Yo = AbrirImagenEX("Imagenes/Derecha2.png", self.DR)
		self.Ataque_8_Yo_Derrotado = AbrirImagen("Imagenes/Derecha2Derrotado.png", self.DR)
		self.Ataque_8_Enemigo = AbrirImagenEX("Imagenes/Izquierda2.png", self.DR)
		self.Ataque_8_Enemigo_Potente = AbrirImagen("Imagenes/Izquierda2Potente.png", self.DR)
		self.Ataque_8_Enemigo_Potente_3 = AbrirImagen("Imagenes/Izquierda2Potente_3.png", self.DR)
		self.Ataque_8_Enemigo_Derrotado = AbrirImagen("Imagenes/Izquierda2Derrotado.png", self.DR)

		self.Ataque_9 = AbrirImagenEX("Imagenes/Izquierda3.png", self.DR)
		self.Ataque_9_Enemigo = AbrirImagen("Imagenes/FuegoAbrumadorV2.png", self.DR)

		self.Accion_1 = AbrirImagen("Imagenes/AnalizandoDebilidades.png", self.DR)
		self.Accion_1_Conteo = AbrirImagen("Imagenes/AnalizandoDebilidadesCortado.png", self.DR) 
		self.Accion_2 = AbrirImagen("Imagenes/Reparacion.png", self.DR)

		self.Numero_0 = AbrirImagen("Imagenes/0.png", self.DR)
		self.Numero_1 = AbrirImagen("Imagenes/1.png", self.DR)
		self.Numero_2 = AbrirImagen("Imagenes/2.png", self.DR)
		self.Numero_3 = AbrirImagen("Imagenes/3.png", self.DR)
		self.Numero_4 = AbrirImagen("Imagenes/4.png", self.DR)
		self.Numero_5 = AbrirImagen("Imagenes/5.png", self.DR)
		self.Numero_6 = AbrirImagen("Imagenes/6.png", self.DR)
		self.Numero_7 = AbrirImagen("Imagenes/7.png", self.DR)
		self.Numero_8 = AbrirImagen("Imagenes/8.png", self.DR)
		self.Numero_9 = AbrirImagen("Imagenes/9.png", self.DR)

		self.Tanque_Ligero_img = AbrirImagen("Imagenes/Tanque_Ligero.png", self.DR)
		self.Tanque_DL_img = AbrirImagen("Imagenes/Tanque_Destructor_Ligero.png", self.DR)
		self.Tanque_M_img = AbrirImagen("Imagenes/Tanque_Mediano.png", self.DR)
		self.Tanque_X_img = AbrirImagen("Imagenes/Tanque_Misterioso.png", self.DR)

		self.Nuevo_Logro_img = AbrirImagen("Imagenes/Nuevo_Logro.png", self.DR)

		# ----------------------------------- Audio

		self.Sonido_Disparo_Basico = mixer.Sound("Musicas_Random/Sonido Disparo Basico.mp3")
		self.Sonido_Disparo_Basico.set_volume(0.26)

		self.Sonido_Disparo_Critico = mixer.Sound("Musicas_Random/Sonido Disparo Critico.mp3")
		self.Sonido_Disparo_Critico.set_volume(0.12)

		self.Sonido_Avion_Bombardero = mixer.Sound("Musicas_Random/Sonido de Avion Bombardero.mp3")
		self.Sonido_Avion_Bombardero.set_volume(0.11)

		self.Sonido_Bombardeo = mixer.Sound("Musicas_Random/Sonido de Bombardeo.mp3")
		self.Sonido_Bombardeo.set_volume(0.1)

		self.Sonido_Bombardeo_2 = mixer.Sound("Musicas_Random/Sonido de Bombardeo 2.mp3")
		self.Sonido_Bombardeo_2.set_volume(0.6)

		self.Sonido_Perforador = mixer.Sound("Musicas_Random/Sonido Disparo Perforador.mp3")
		self.Sonido_Perforador.set_volume(0.12)

		self.Sonido_RompeBlindaje = mixer.Sound("Musicas_Random/Sonido RompeBlindaje.mp3")
		self.Sonido_RompeBlindaje.set_volume(0.75)

		self.Sonido_Explosivo = mixer.Sound("Musicas_Random/Sonido de Explosion.mp3")
		self.Sonido_Explosivo.set_volume(0.14)

		self.Sonido_Barra_Perforador = mixer.Sound("Musicas_Random/Sonido Barra Perforador.mp3")
		self.Sonido_Barra_Perforador.set_volume(0.32)

		self.Sonido_Esquivar_Flechas = mixer.Sound("Musicas_Random/Sonido Esquivar Flechas.mp3")
		self.Sonido_Esquivar_Flechas.set_volume(0.7)

		self.Sonido_Flechas_V2 = mixer.Sound("Musicas_Random/Sonido Ataque Flechas V2.mp3")
		self.Sonido_Flechas_V2.set_volume(0.12)

		self.Sonido_Engranajes = mixer.Sound("Musicas_Random/Sonido Engranajes.mp3")
		self.Sonido_Engranajes.set_volume(0.18)

		self.Sonido_Reparacion = mixer.Sound("Musicas_Random/Sonido Reparacion.mp3")
		self.Sonido_Reparacion.set_volume(0.6)

		self.Sonido_Quemadura = mixer.Sound("Musicas_Random/Sonido Quemadura.mp3")
		self.Sonido_Quemadura.set_volume(0.45)

		self.Sonido_Embestida = mixer.Sound("Musicas_Random/Sonido Embestida.mp3")
		self.Sonido_Embestida.set_volume(0.1)

		self.Sonido_Analisis = mixer.Sound("Musicas_Random/Sonido Analisis.mp3")
		self.Sonido_Analisis.set_volume(0.4)

		self.Sonido_Estadisticas = mixer.Sound("Musicas_Random/Sonido Estadisticas.mp3")
		self.Sonido_Estadisticas.set_volume(0.8)

		self.Sonido_Logros = mixer.Sound("Musicas_Random/Efecto acierto.mp3")
		self.Sonido_Logros.set_volume(0.8)

		self.BarraMenu = BarraMenu
		self.ArchivoColor = tk.Menu(self.BarraMenu, tearoff = 0) # Crear uno de los cuadritos del menu
		self.BarraMenu.add_cascade(label = "Color", menu = self.ArchivoColor)
		self.ArchivoOtros = tk.Menu(self.BarraMenu, tearoff = 0) # Crear uno de los cuadritos del menu

		if self.Idioma == "español":
			self.ArchivoColor.add_command(label = "Rojo", command = lambda:self.CambioColor("Rojo"))
			self.ArchivoColor.add_command(label = "Azul", command = lambda:self.CambioColor("Azul"))
			self.ArchivoColor.add_command(label = "Verde", command = lambda:self.CambioColor("Verde"))
			self.ArchivoColor.add_command(label = "Amarillo", command = lambda:self.CambioColor("Amarillo"))
			self.BarraMenu.add_cascade(label = "Otros", menu = self.ArchivoOtros)
			self.ArchivoOtros.add_command(label = "Autodestrucción", command = lambda:self.Autodestruccion())
		elif self.Idioma == "english":
			self.ArchivoColor.add_command(label = "Red", command = lambda:self.CambioColor("Rojo"))
			self.ArchivoColor.add_command(label = "Blue", command = lambda:self.CambioColor("Azul"))
			self.ArchivoColor.add_command(label = "Green", command = lambda:self.CambioColor("Verde"))
			self.ArchivoColor.add_command(label = "Yellow", command = lambda:self.CambioColor("Amarillo"))
			self.BarraMenu.add_cascade(label = "Other", menu = self.ArchivoOtros)
			self.ArchivoOtros.add_command(label = "Self-destruction", command = lambda:self.Autodestruccion())

		self.Yo_Nombre = Yo[6]
		self.Yo_Vida = Yo[0]
		self.Yo_VidaActual = Yo[0]
		self.Yo_Ataque = Yo[1]
		self.Yo_Blindaje = Yo[2]
		self.Yo_Basico_Critico = Yo[3]
		self.Yo_Explosivo_Falla = Yo[4]
		self.Yo_Daño_Bombardeo = Yo[5]
		self.TanqueElegido = Yo[7]

		self.Enemigo_Nombre = Enemigo[3]
		self.Enemigo_Vida = Enemigo[0]
		self.Enemigo_VidaActual = Enemigo[0]
		self.Enemigo_Ataque = Enemigo[1]
		self.Enemigo_Blindaje = Enemigo[2]
		self.Enemigo_Reparaciones = Enemigo[5]
		self.Enemigo_Lanzo_Embestida = False
		self.Dificultad = Enemigo[4]

		self.Largo = 0
		self.DistanciaIpadx = -1
		self.TurnoActual = 1
		self.Presionado = 0
		self.No_Presionado = 0
		self.Esquivado = 0
		self.Palabra = ""
		self.Cantidad = 0
		self.DañoTotal = 0
		self.Tiempo = 0
		self.Embestida_Fase = 0
		self.Embestida_Fase_4 = False
		self.Probabilidad_Flechas_1 = 50
		self.Probabilidad_Perforador = 75 + 5*self.Dificultad

		self.Daño_Realizado = 0
		self.Daño_Recibido = 0
		self.N_Ataque_Basico = 0
		self.N_Ataque_Bombardeo = 0
		self.N_Ataque_Explosivo = 0
		self.N_Ataque_Perforador = 0
		self.N_Accion_Reparacion = 0
		self.N_Accion_Analisis = 0

		self.Enfoque = 0
		self.Recarga_Perforador = 0
		self.Recarga_Explosivo = 0
		self.Recarga_Analisis = 0
		self.CantidadReparacion = 2
		self.CantidadBombardeo = 1

		self.Color_Ataque = "#FFFB56"
		self.Color_Acciones = "#FFFC6B"
		self.Color_Estadisticas = "#FFFC85"
		self.Color_Volver = "#FFFC99"
		self.Color_Enemigo = "#FCFF19"
		self.Color_Yo = "#FCFF19"
		self.Color_Pantalla_Texto = "#FDFECB"

		self.FramePrincipal = tk.Frame(raiz)
		self.SegundoFrame = tk.Frame(raiz, width = Redondear(1150, self.DR), height = Redondear(265, self.DR))
		self.FramePrincipal.pack()
		self.SegundoFrame.pack(pady = Redondear(10, self.DR))

		self.Texto = tk.StringVar()
		self.Texto.set("\n")

		self.CambioVidaJefe = tk.StringVar()
		self.MiVida = tk.StringVar()
		self.Descripcion = tk.StringVar()
		self.Descripcion2 = tk.StringVar()
		self.ProgresoYo = tk.StringVar()
		self.ProgresoEnemigo = tk.StringVar()

		self.Turnos = tk.StringVar()
		self.Segundos = tk.StringVar()
		self.SegundaFaseFlechas = False

		self.CambioVidaJefe.set(self.Enemigo_Nombre + " " + str(self.Enemigo_VidaActual) + "/" + str(self.Enemigo_Vida))
		self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))

		if self.Idioma == "español":
			self.Turnos.set("Turno " + str(self.TurnoActual) + ":")    # Cambiar turnos
		elif self.Idioma == "english":
			self.Turnos.set("Turn " + str(self.TurnoActual) + ":")

		# ------------------- Estructura


		self.PantallaTurnos = tk.Label(self.FramePrincipal, textvariable = self.Turnos, font = ('Arial',Redondear(30, self.DR)))
		self.PantallaTurnos.grid(row = 0, column = 0, sticky = "w")

		# ------------------- Pantalla de texto

		self.PantallaTexto = tk.Message(self.FramePrincipal, textvariable = self.Texto, width = Redondear(1000, self.DR), bg = self.Color_Pantalla_Texto, font = ('Arial', Redondear(35, self.DR)),
		 bd = Redondear(5, self.DR), relief = "ridge", justify = "center")
		self.PantallaTexto.grid(row = 1, column = 0, columnspan = 4, sticky = "ew", pady = Redondear(10, self.DR))

		# ------------------- Pantalla de vida

		self.PantallaVidaEnemigo = tk.Label(self.FramePrincipal, textvariable = self.CambioVidaJefe
			, font = ('Arial', Redondear(30, self.DR)), anchor = "e", bg = self.Color_Enemigo)
		self.PantallaVida = tk.Label(self.FramePrincipal, textvariable = self.MiVida, anchor = "w", font = ('Arial', Redondear(25, self.DR)), bg = self.Color_Yo)

		self.PantallaVidaEnemigo.grid(row = 0, column = 1, sticky = "e", columnspan = 3)
		self.PantallaVida.grid(row = 2, column = 0, columnspan = 2, sticky = "w") 	# sticky es para que se pegue a la derecha

		# ------------------- Botones principales ---------------------

		# ------------------- Atacar

		if self.Idioma == "español":
			Atacar_str = "Atacar"
			AtaqueBasico_str = "Ataque Básico"
			AtaquesEspeciales_str = "Ataques especiales"
			BombardeoAereo_str = "Bombardeo\naéreo"
			DisparoPerforador_str = "Disparo\nperforador"
			Izquierda_str = "Izquierda"
			Derecha_str = "Derecha"
			Empujar_str = "Empujar"
			DisparoExplosivo_str = "Disparo\nexplosivo"
			Volver_str = "Volver"
			Acciones_str = "Acciones"
			AnalizarEnfocar_str = "Analizar y enfocar"
			Reforzar_str = "Reforzar"
			Estadisticas_str = "Estadísticas"
			Enemigo_str = "Enemigo"

		elif self.Idioma == "english":
			Atacar_str = " Attack "
			AtaqueBasico_str = " Basic Attack "
			AtaquesEspeciales_str = "  Special attacks  "
			BombardeoAereo_str = "  Tactical  \n  bombing  "
			DisparoPerforador_str = " Piercing \n shot "
			Izquierda_str = "   Left   "
			Derecha_str = " Right "
			Empujar_str = "Advance"
			DisparoExplosivo_str = "Explosive\nshot"
			Volver_str = "Return"
			Acciones_str = " Actions "
			AnalizarEnfocar_str = "Analyze and focus"
			Reforzar_str = "Reinforce"
			Estadisticas_str = "   Statistics   "
			Enemigo_str = "Enemy"

		self.BotonAtacar = tk.Button(self.FramePrincipal, text = Atacar_str, command = lambda:self.CambiarBotonesAAS(1), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Ataque, cursor = "hand2")
		self.BotonAtacar.grid(row = 3, column = 0, ipadx = Redondear(76, self.DR))

		self.AtaqueBasico = tk.Button(self.FramePrincipal, text = AtaqueBasico_str, command = lambda:self.AtacarBasico(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Ataque, cursor = "hand2")

		if self.AtaqueBasico["state"] == "normal":
			self.AtaqueBasico.bind("<Enter>", self.Descripcion_Ataque_Basico_Mouse)
			self.AtaqueBasico.bind("<Leave>", self.Descripcion_Sin_Mouse)
		else:
			pass

		self.AtaquesEspeciales = tk.Button(self.FramePrincipal, text = AtaquesEspeciales_str, command = lambda:self.AtacarEspecial(), font = ("Arial", Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Ataque, cursor = "hand2")

		self.Boton_Ataque_Bombardeo = tk.Button(self.FramePrincipal, text = BombardeoAereo_str, command = lambda:self.Atacar_Bombardeo(), font = ('Arial',Redondear(25, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Ataque, cursor = "hand2")

		if self.Boton_Ataque_Bombardeo["state"] == "normal":
			self.Boton_Ataque_Bombardeo.bind("<Enter>", self.Descripcion_Ataque_Bombardeo_Mouse)
			self.Boton_Ataque_Bombardeo.bind("<Leave>", self.Descripcion_Sin_Mouse)
		else:
			pass



		# ----------------------------------- Ataque Perforador

		self.Ataque_Perforador = tk.Button(self.FramePrincipal, text = DisparoPerforador_str, command = lambda:self.Atacar_Perforador(), font = ("Arial", Redondear(25, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Ataque, cursor = "hand2")

		self.BotonRojo = tk.Button(self.SegundoFrame, image = self.Ataque_5_Mira, border = Redondear(4, self.DR), relief = "flat", cursor = "hand2", command = lambda:self.Presionar())
		self.BotonIzquierda = tk.Button(self.SegundoFrame, text = Izquierda_str, bg = "#71FF54", font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), command = lambda:self.Presionar_Esquivar_Izquierda(self.Cantidad), cursor = "hand2")
		self.BotonDerecha = tk.Button(self.SegundoFrame, text = Derecha_str, bg = "#71FF54", font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), command = lambda:self.Presionar_Esquivar_Derecha(self.Cantidad), cursor = "hand2")
		self.BotonEmpujar = tk.Button(self.SegundoFrame, text = Empujar_str, bg = "#BDFFB1", font = ("Arial", Redondear(40, self.DR)), border = Redondear(6, self.DR), command = lambda:self.Presionar_Empujar(), cursor = "hand2")

		self.EstiloBarra = ttk.Style()
		self.EstiloSegundaBarra = ttk.Style()
		self.EstiloTerceraBarra = ttk.Style()
		self.EstiloBarra.theme_use("clam")

		self.EstiloBarra.configure("custom.Horizontal.TProgressbar", troughcolor='#5A504E',background='#FFE300',
			darkcolor="#EEE900", lightcolor="#FFFC6F", bordercolor="black")

		self.EstiloSegundaBarra.configure("BarraDeAtaqueEstilo.Horizontal.TProgressbar", troughcolor='#5A504E',background='#FFE300',
			darkcolor="#EEE900", lightcolor="#FFFC6F", bordercolor="black")

		self.EstiloTerceraBarra.configure("BarraDeTiempoEstilo.Horizontal.TProgressbar", troughcolor='#5A504E',background='#FFE300',
			darkcolor="#EEE900", lightcolor="#FFFC6F", bordercolor="black")

		self.Progreso = ttk.Progressbar(self.PantallaTexto, style = "custom.Horizontal.TProgressbar", orient = "horizontal", length = Redondear(300, self.DR), mode = "determinate")

		self.ProgresoTemporizador = ttk.Progressbar(self.SegundoFrame, style = "BarraDeTiempoEstilo.Horizontal.TProgressbar", orient = "horizontal", length = Redondear(500, self.DR), mode = "determinate")

		self.LabelSegundos = tk.Label(self.SegundoFrame, textvariable = self.Segundos, font = ('Arial', Redondear(30, self.DR)), anchor = "center")

		self.LabelProgresoYo = tk.Label(self.PantallaTexto, textvariable = self.ProgresoYo, font = ('Arial', Redondear(30, self.DR)), anchor = "center", bg = "#FDFECB")
		self.LabelProgresoEnemigo = tk.Label(self.PantallaTexto, textvariable = self.ProgresoEnemigo, font = ('Arial', Redondear(30, self.DR)), anchor = "center", bg = "#FDFECB")


		if self.Ataque_Perforador["state"] == "normal":
			self.Ataque_Perforador.bind("<Enter>", self.Descripcion_Ataque_Perforador_Mouse)
			self.Ataque_Perforador.bind("<Leave>", self.Descripcion_Sin_Mouse)

		else:
			pass

		# ------------------- Ataque Explosivo

		self.Ataque_Explosivo = tk.Button(self.FramePrincipal, text = DisparoExplosivo_str, command = lambda:self.Atacar_Explosivo(), font = ("Arial", Redondear(25, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Ataque, cursor = "hand2")

		if self.Ataque_Explosivo["state"] == "normal":
			self.Ataque_Explosivo.bind("<Enter>", self.Descripcion_Ataque_Explosivo_Mouse)
			self.Ataque_Explosivo.bind("<Leave>", self.Descripcion_Sin_Mouse)

		else:
			pass

		self.Boton_Volver = tk.Button(self.FramePrincipal, text = Volver_str, command = lambda:self.Volver(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Volver, cursor = "hand2")

		# ------------------- Acciones

		self.BotonAcciones = tk.Button(self.FramePrincipal, text = Acciones_str, command = lambda:self.CambiarBotonesAAS(2), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Acciones, cursor = "hand2")
		self.BotonAcciones.grid(row = 3, column = 1, ipadx = Redondear(76,self.DR))

		self.AnalizandoTanque = tk.Button(self.FramePrincipal, text = AnalizarEnfocar_str, command = lambda:self.AnalizarTanque(),
			font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Acciones, cursor = "hand2")

		if self.AnalizandoTanque["state"] == "normal":
			self.AnalizandoTanque.bind("<Enter>", self.Descripcion_Accion_Analizar)
			self.AnalizandoTanque.bind("<Leave>", self.Descripcion_Sin_Mouse)

		else:
			pass

		self.BotonReparacion = tk.Button(self.FramePrincipal, text = Reforzar_str, command = lambda:self.Reparar(), font = ('Arial',Redondear(40, self.DR))
			, border = Redondear(6, self.DR), bg = self.Color_Acciones, cursor = "hand2")

		if self.BotonReparacion["state"] == "normal":
			self.BotonReparacion.bind("<Enter>", self.Descripcion_Accion_Reparar)
			self.BotonReparacion.bind("<Leave>", self.Descripcion_Sin_Mouse)

		else:
			pass

		# ------------------- Estadisticas

		self.BotonStats = tk.Button(self.FramePrincipal, text = Estadisticas_str, font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), command = lambda:self.CambiarBotonesAAS(3), bg = self.Color_Estadisticas, cursor = "hand2")
		self.BotonStats.grid(row = 3, column = 2, ipadx = Redondear(9,self.DR))

		self.StatsEnemigo = tk.Button(self.FramePrincipal, text = Enemigo_str, command = lambda:self.EstadisticasTanque(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Volver, cursor = "hand2")

		self.Tu = tk.Button(self.FramePrincipal, text = self.Yo_Nombre, command = lambda:self.EstadisticasYo(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR), bg = self.Color_Volver, cursor = "hand2")

		# ------------------- Descripción

		self.PantallaDescripcion = tk.Label(self.FramePrincipal, textvariable = self.Descripcion, font = ('Arial',Redondear(27, self.DR)))

		self.PantallaDescripcion2 = tk.Label(self.FramePrincipal, textvariable = self.Descripcion2, font = ('Arial',Redondear(27, self.DR)))

		# ------------------- Label Imagenes

		self.Imagen_Mi_Lado = tk.Label(self.PantallaTexto, image = self.Ataque_1, border = 0)
		self.Imagen_Su_Lado = tk.Label(self.PantallaTexto, image = self.Ataque_1, border = 0)

		self.Imagen_Flechas = tk.Label(self.PantallaTexto, image = self.Ataque_6_Izquierda, bg = "#FDFECB") # La Imagen base será izquierda
		self.Imagen_Flechas.config(border = 0)

		self.Imagen_Embestida_Yo = tk.Label(self.PantallaTexto, image = self.Ataque_8_Yo, bg = "#FDFECB")
		self.Imagen_Embestida_Yo.config(border = 0)

		self.Imagen_Embestida_Enemigo = tk.Label(self.PantallaTexto, image = self.Ataque_8_Enemigo, bg = "#FDFECB")
		self.Imagen_Embestida_Enemigo.config(border = 0)




	# -------------------- Tanque Enemigo

	def EstadisticasTanque(self):
		mixer.Channel(2).play(self.Sonido_Estadisticas)

		if self.Idioma == "español":
			self.Texto.set ("Nombre: " + self.Enemigo_Nombre + "\nVida: " + str(self.Enemigo_Vida) + "\nAtaque: " +
			str(self.Enemigo_Ataque) + "\nBlindaje: " + str(self.Enemigo_Blindaje))
		elif self.Idioma == "english":
			self.Texto.set ("Name: " + self.Enemigo_Nombre + "\nHealth: " + str(self.Enemigo_Vida) + "\nAttack: " +
			str(self.Enemigo_Ataque) + "\nArmor: " + str(self.Enemigo_Blindaje))

	def EnemigoBlindajePerdido(self):

		if self.Enfoque > 0:
			Perdida = 4
		else:
			Perdida = choice([3,4])

		self.Enemigo_Blindaje -= Perdida

		if self.Enemigo_Blindaje < 0:
			self.Enemigo_Blindaje = 0

		if self.Enemigo_Blindaje == 0:
			self.ConfirmarLogros(6)

		if self.Idioma == "español":
			self.Texto.set("Hemos perforado su blindaje." + "\nSu blindaje actual es " + str(self.Enemigo_Blindaje) + ".")
		elif self.Idioma == "english":
			self.Texto.set("We have pierced their armor." + "\nTheir current armor is " + str(self.Enemigo_Blindaje) + ".")

	def EnemigoQuemadura(self):

		daño = choice([1, 2, 3, 4, 5, 6])

		if self.Idioma == "español":
			self.Texto.set(self.Enemigo_Nombre + " se está quemando." + "\nHa recibido " + str(daño) + " de daño.")
		elif self.Idioma == "english":
			self.Texto.set(self.Enemigo_Nombre + " is burning." + "\nThey have received " + str(daño) + " damage.")
		self.Daño_Realizado += daño
		self.Enemigo_VidaActual -= daño

		self.CambioVidaJefe.set(self.Enemigo_Nombre + " " + str(self.Enemigo_VidaActual) + "/" + str(self.Enemigo_Vida))

	def DañoAlJefe(self, daño, numero, probabilidad):

		if numero == 3 and probabilidad == True:

			self.PantallaTexto.after(500, lambda:self.PonerSonido(2, self.Sonido_RompeBlindaje))
			self.PantallaTexto.after(750, lambda:self.PonerSonido(4, self.Sonido_Disparo_Critico))
			self.PantallaTexto.after(2000, self.EnemigoBlindajePerdido)

		elif numero == 4 and probabilidad >= 3:

			self.PantallaTexto.after(1000, lambda:self.PonerSonido(2, self.Sonido_Quemadura))
			self.PantallaTexto.after(2000, self.EnemigoQuemadura)

		elif numero == 5:

			daño = self.Yo_Daño_Bombardeo*self.Presionado

			if self.Presionado >= 20:
				self.ConfirmarLogros(8)

			self.Presionado = 0


		if self.Enfoque > 0 and numero != 5:
			daño = daño - round(self.Enemigo_Blindaje/2)
		else:
			daño = daño - self.Enemigo_Blindaje

		if daño <= 0:
			daño = 0

			if self.Idioma == "español":
				self.Texto.set(self.Texto.get() + "Su blindaje ha bloqueado todo el daño.")
			elif self.Idioma == "english":
				self.Texto.set(self.Texto.get() + "Their armor has blocked all the damage.")

		else:
			if self.Idioma == "español":
				self.Texto.set(self.Texto.get() + self.Enemigo_Nombre + " ha recibido " + str(daño) + " de daño.")
			elif self.Idioma == "english":
				self.Texto.set(self.Texto.get() + self.Enemigo_Nombre + " has received " + str(daño) + " damage.")

		self.Daño_Realizado += daño
		self.Enemigo_VidaActual -= daño
		self.CambioVidaJefe.set(self.Enemigo_Nombre + " " + str(self.Enemigo_VidaActual) + "/" + str(self.Enemigo_Vida))

	def Enemigo_Habilidades(self, numero):

		self.Imagen_Mi_Lado.place_forget()          # Desaparece mi ataque

		if numero == 1:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " ha realizado un disparo.\n")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " has fired one shot.\n")
			self.Imagen_Su_Lado.config(image = self.Ataque_1)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))
			mixer.Channel(3).play(self.Sonido_Disparo_Basico)
		elif numero == 2:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " ha realizado dos disparos.\n")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " has fired two shots.\n")
			self.Imagen_Su_Lado.config(image = self.Ataque_2)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))
			self.PantallaTexto.after(0, lambda:self.PonerSonido(3, self.Sonido_Disparo_Basico))
			self.PantallaTexto.after(375, lambda:self.PonerSonido(4, self.Sonido_Disparo_Basico))
		elif numero == 3:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " ha disparado una bala perforante.\n")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " has fired an armor-piercing bullet.\n")
			self.Imagen_Su_Lado.config(image = self.Ataque_3)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))
			mixer.Channel(3).play(self.Sonido_Perforador)
		elif numero == 4:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " está siendo reparado.\n")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " is being repaired.\n")
			self.Imagen_Su_Lado.config(image = self.Accion_2)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))
			masblindaje = choice([2,3])
			mixer.Channel(3).play(self.Sonido_Reparacion)
			self.PantallaTexto.after(1500, self.Enemigo_Curacion, 50, masblindaje)
		elif numero == 5:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " se prepara para ejecutar\nmultiples disparos.")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " prepares to fire multiple\nbullets quickly")
			self.Imagen_Su_Lado.config(image = self.Ataque_7)
			self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))

			Distancia = self.FramePrincipal.winfo_width() - Redondear(270, self.DR) - Redondear(253, self.DR) # Tamaños actuales de los cuadros Izquierda/Derecha

			self.BotonIzquierda.grid(row = 0, column = 0, padx = (0,Distancia))
			self.BotonDerecha.grid(row = 0, column = 1)
			self.BotonIzquierda["state"] = "disabled"
			self.BotonDerecha["state"] = "disabled"
		elif numero == 6:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " lanza una embestida con\ntodas sus fuerzas restantes.")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " charges at you with\nall their remaining strength.")
			self.Imagen_Su_Lado.config(image = self.Ataque_8)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))
		elif numero == 7:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " se prepara para ejecutar\nmultiples disparos.")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " prepares to fire multiple\nbullets quickly")
			self.Imagen_Su_Lado.config(image = self.Ataque_9_Enemigo)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))
		elif numero == 8:
			if self.Idioma == "español":
				self.Texto.set(self.Enemigo_Nombre + " reune todas sus fuerzas para\ndisparar la ráfaga final.")
			elif self.Idioma == "english":
				self.Texto.set(self.Enemigo_Nombre + " gather all their strength to\nfire the last burst.")
			self.Imagen_Su_Lado.config(image = self.Ataque_9_Enemigo)
			self.Imagen_Su_Lado.place(relx = 0.9, y = Redondear(3, self.DR))

	def Enemigo_GolpeBasico(self):
		Daño = choice([self.Enemigo_Ataque - 1, self.Enemigo_Ataque, self.Enemigo_Ataque + 1])
		return Daño

	def Enemigo_RompeCorazas(self):
		Daño = choice([self.Enemigo_Ataque - 3, self.Enemigo_Ataque -2, self.Enemigo_Ataque -1])
		return Daño

	def Enemigo_Curacion(self, masvida, masblindaje):
		self.Enemigo_Reparaciones -= 1
		if self.Idioma == "español":
			self.Texto.set(self.Enemigo_Nombre + " recuperó " + str(masvida) + " de vida." + "\nY obtuvo " + str(masblindaje) + " extra de blindaje.")
		elif self.Idioma == "english":
			self.Texto.set(self.Enemigo_Nombre + " restored " + str(masvida) + " health." + "\nAnd they got " + str(masblindaje) + " extra armor.")
		self.Enemigo_VidaActual += masvida
		self.Enemigo_Blindaje += masblindaje

		self.CambioVidaJefe.set(self.Enemigo_Nombre + " " + str(self.Enemigo_VidaActual) + "/" + str(self.Enemigo_Vida))

	def Enemigo_FuegoAbrumador(self):

		self.Palabra = choice(["Izquierda", "Derecha"])
		self.Texto.set("\n")

		if self.Palabra == "Izquierda":
			self.Imagen_Flechas.config(image = self.Ataque_6_Izquierda)
			self.Imagen_Flechas.place(x = Redondear(520, self.DR), y = Redondear(15, self.DR))

		elif self.Palabra == "Derecha":
			self.Imagen_Flechas.config(image = self.Ataque_6_Derecha)
			self.Imagen_Flechas.place(x = Redondear(520, self.DR), y = Redondear(15, self.DR))

		self.ProgresoTemporizador.place(relx = 0.29)
		self.ProgresoTemporizador["value"] = 100
		self.LabelSegundos.place(relx = 0.4, rely = 0.4)

		self.BotonIzquierda["state"] = "normal"
		self.BotonDerecha["state"] = "normal"

		self.PantallaTexto.after(0, self.Enemigo_Temporizador)

	def Enemigo_TiempoFuegoAbrumador(self):

		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))

		if self.SegundaFaseFlechas:

			if self.Dificultad == 1: # Fácil
				self.Cantidad = 5
				self.Tiempo = 3000
				self.Imagen_Mi_Lado.config(image = self.Numero_5)

			elif self.Dificultad == 2: # Media
				self.Cantidad = 7
				self.Tiempo = 4000
				self.Imagen_Mi_Lado.config(image = self.Numero_7)
			elif self.Dificultad == 3: # Díficil
				self.Cantidad = 9
				self.Tiempo = 5000
				self.Imagen_Mi_Lado.config(image = self.Numero_9)
			elif self.Dificultad == 4: # Extremo
				self.Cantidad = 9
				self.Tiempo = 4500
				self.Imagen_Mi_Lado.config(image = self.Numero_9)

			self.SegundaFaseFlechas = False

		elif self.SegundaFaseFlechas == False:

			if self.Dificultad == 1: # Fácil
				self.Cantidad = 4
				self.Tiempo = 3500
				self.Imagen_Mi_Lado.config(image = self.Numero_4)

			elif self.Dificultad == 2: # Media
				self.Cantidad = 6
				self.Tiempo = 4000
				self.Imagen_Mi_Lado.config(image = self.Numero_6)
			elif self.Dificultad == 3: # Díficil
				self.Cantidad = 8
				self.Tiempo = 5000
				self.Imagen_Mi_Lado.config(image = self.Numero_8)
			elif self.Dificultad == 4: # Extremo
				self.Cantidad = 7
				self.Tiempo = 4000
				self.Imagen_Mi_Lado.config(image = self.Numero_7)

			self.SegundaFaseFlechas = True

	def Enemigo_Temporizador(self):
		self.FramePrincipal.update_idletasks()

		if self.ProgresoTemporizador["value"] > 0:

			self.ProgresoTemporizador["value"] -= 1

			Tiempito = self.Tiempo/100
			Tiempito = round(Tiempito)

			self.PantallaTexto.after(Tiempito, self.Enemigo_Temporizador)

			Tiempito = Tiempito/10

			Segunditos = (Tiempito * self.ProgresoTemporizador["value"])/100

			Segunditos = f"{Segunditos:.2f}" 

			if self.Idioma == "español":
				self.Segundos.set(str(Segunditos) + " segundos")
			elif self.Idioma == "english":
				self.Segundos.set(str(Segunditos) + " seconds")

		else:

			self.QuitarBoton("Flechas")

	def Enemigo_FA_V2(self, final = False):

		def CambiarGif1(self):
			if self.BarraVertical.winfo_exists() == 1:
				self.Fondo.configure(image = self.FondoGif1)
				self.PantallaTexto.after(100, lambda:CambiarGif2(self))

		def CambiarGif2(self):
			if self.BarraVertical.winfo_exists() == 1:
				self.Fondo.configure(image = self.FondoGif2)
				self.PantallaTexto.after(100, lambda:CambiarGif1(self))

		self.FondoGif1 = AbrirImagen("Imagenes/BarraVerticalFondo.png", self.DR)
		self.FondoGif2 = AbrirImagen("Imagenes/BarraVerticalFondo2.png", self.DR)
		self.Fondo = tk.Label(self.SegundoFrame, image = self.FondoGif1)

		self.BarraVertical = tk.Scale(self.SegundoFrame, from_= 0, to = 160, length = Redondear(250, self.DR), sliderlength = Redondear(49, self.DR), showvalue = 0, width = Redondear(40, self.DR),
			relief = "flat", troughcolor = self.Color_Pantalla_Texto, bd = 0, cursor = "hand2") # Color plata: #F9FFF5
		self.BarraVertical.place(relx = 0.057, y = Redondear(5, self.DR))

		self.BarraVertical.set(39)

		self.Fondo.place(relx = 0.01)

		mixer.Channel(2).play(self.Sonido_Engranajes, loops = -1)
		self.PantallaTexto.after(100, lambda:CambiarGif2(self))

		Patron = [0, 0 ,0, 0, 0, 0]
		Patron[0] = choice([1, 2])
		Patron[1] = choice([1, 2])
		Patron[2] = choice([1, 2])
		Patron[3] = choice([1, 2])
		Patron[4] = choice([1, 2])
		Patron[5] = choice([1, 2])

		Tiempo = 600

		if final == False:

			self.PantallaTexto.after(300, self.Enemigo_FA_V2_Crear)
			self.PantallaTexto.after(300, self.Enemigo_FA_V2_Crear)

			if Patron[0] == 1:
				self.PantallaTexto.after(Tiempo + 150, self.Enemigo_FA_V2_Crear, 0.028)
				self.PantallaTexto.after(Tiempo + 300, self.Enemigo_FA_V2_Crear, 0.5935)
				self.PantallaTexto.after(Tiempo, self.Enemigo_FA_V2_Crear, 0.782)

			elif Patron[0] == 2:
				self.PantallaTexto.after(Tiempo, self.Enemigo_FA_V2_Crear, 0.2165)
				self.PantallaTexto.after(Tiempo + 150, self.Enemigo_FA_V2_Crear, 0.405)
				self.PantallaTexto.after(Tiempo + 300, self.Enemigo_FA_V2_Crear, 0.5935)

			if Patron[1] == 1:
				self.PantallaTexto.after(Tiempo*2 + 100, self.Enemigo_FA_V2_Crear, 0.2165)
				self.PantallaTexto.after(Tiempo*2 + 100, self.Enemigo_FA_V2_Crear, 0.405)
				self.PantallaTexto.after(Tiempo*2 + 100, self.Enemigo_FA_V2_Crear, 0.782)

			elif Patron[1] == 2:
				self.PantallaTexto.after(Tiempo*2 + 100, self.Enemigo_FA_V2_Crear, 0.028)
				self.PantallaTexto.after(Tiempo*2 + 100, self.Enemigo_FA_V2_Crear, 0.5935)
				self.PantallaTexto.after(Tiempo*2 + 100, self.Enemigo_FA_V2_Crear, 0.782)

			self.PantallaTexto.after(Tiempo*3, self.Enemigo_FA_V2_Crear)
			self.PantallaTexto.after(Tiempo*3, self.Enemigo_FA_V2_Crear)
			self.PantallaTexto.after(Tiempo*3, self.Enemigo_FA_V2_Crear)

			if Patron[2] == 1:
				self.PantallaTexto.after(Tiempo*3 + 500, self.Enemigo_FA_V2_Crear, 0.028)
				self.PantallaTexto.after(Tiempo*4 + 200, self.Enemigo_FA_V2_Crear, 0.782)
				self.PantallaTexto.after(Tiempo*4 + 500, self.Enemigo_FA_V2_Crear, 0.5935)
				self.PantallaTexto.after(Tiempo*4 + 200, self.Enemigo_FA_V2_Crear, 0.2165)

			elif Patron[2] == 2:
				self.PantallaTexto.after(Tiempo*3 + 500, self.Enemigo_FA_V2_Crear, 0.2165)
				self.PantallaTexto.after(Tiempo*4 + 200, self.Enemigo_FA_V2_Crear, 0.405)
				self.PantallaTexto.after(Tiempo*4 + 500, self.Enemigo_FA_V2_Crear, 0.5935)
				self.PantallaTexto.after(Tiempo*4 + 200, self.Enemigo_FA_V2_Crear, 0.782)

			if self.Dificultad == 1:
				self.PantallaTexto.after(Tiempo*4 + 1100, self.Enemigo_FA_V2_Crear, 0.028)
				self.PantallaTexto.after(Tiempo*4 + 1100, self.Enemigo_FA_V2_Crear, 0.5935)
				self.PantallaTexto.after(5400, lambda:self.QuitarBoton("FlechasV2"))

			if self.Dificultad > 1:

				if Patron[3] == 1:
					self.PantallaTexto.after(Tiempo*5 + 100, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*5 + 100, self.Enemigo_FA_V2_Crear, 0.2165)
					self.PantallaTexto.after(Tiempo*5 + 100, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*5 + 500, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*5 + 500, self.Enemigo_FA_V2_Crear, 0.5935)
					self.PantallaTexto.after(Tiempo*5 + 500, self.Enemigo_FA_V2_Crear, 0.782)

				elif Patron[3] == 2:
					self.PantallaTexto.after(Tiempo*5 + 150, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*5 + 350, self.Enemigo_FA_V2_Crear, 0.2165)
					self.PantallaTexto.after(Tiempo*5 + 350, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*5 + 550, self.Enemigo_FA_V2_Crear, 0.782)
					self.PantallaTexto.after(Tiempo*5 + 550, self.Enemigo_FA_V2_Crear, 0.028)

				self.PantallaTexto.after(Tiempo*6 + 150, self.Enemigo_FA_V2_Crear)
				self.PantallaTexto.after(Tiempo*6 + 350, self.Enemigo_FA_V2_Crear)
				self.PantallaTexto.after(Tiempo*6 + 550, self.Enemigo_FA_V2_Crear)

				if self.Dificultad == 2:
					self.PantallaTexto.after(6050, lambda:self.QuitarBoton("FlechasV2"))

			if self.Dificultad > 2:

				if Patron[4] == 1:
					self.PantallaTexto.after(Tiempo*7 + 200, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*7 + 200, self.Enemigo_FA_V2_Crear, 0.5935)
					self.PantallaTexto.after(Tiempo*7 + 200, self.Enemigo_FA_V2_Crear, 0.782)
					self.PantallaTexto.after(Tiempo*7 + 500, self.Enemigo_FA_V2_Crear, 0.2165)
					self.PantallaTexto.after(Tiempo*7 + 500, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*7 + 500, self.Enemigo_FA_V2_Crear, 0.5935)
					self.PantallaTexto.after(Tiempo*8 + 300, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*8 + 400, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*8 + 500, self.Enemigo_FA_V2_Crear, 0.782)

				elif Patron[4] == 2:
					self.PantallaTexto.after(Tiempo*7 + 200, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*7 + 200, self.Enemigo_FA_V2_Crear, 0.2165)
					self.PantallaTexto.after(Tiempo*7 + 500, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*7 + 500, self.Enemigo_FA_V2_Crear, 0.5935)
					self.PantallaTexto.after(Tiempo*7 + 700, self.Enemigo_FA_V2_Crear, 0.782)
					self.PantallaTexto.after(Tiempo*7 + 500, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*8 + 300, self.Enemigo_FA_V2_Crear, 0.2165)
					self.PantallaTexto.after(Tiempo*8 + 300, self.Enemigo_FA_V2_Crear, 0.028)
					self.PantallaTexto.after(Tiempo*8 + 600, self.Enemigo_FA_V2_Crear, 0.405)
					self.PantallaTexto.after(Tiempo*8 + 600, self.Enemigo_FA_V2_Crear, 0.782)

				self.PantallaTexto.after(Tiempo*9 + 200, self.Enemigo_FA_V2_Crear)
				self.PantallaTexto.after(Tiempo*9 + 200, self.Enemigo_FA_V2_Crear)
				self.PantallaTexto.after(Tiempo*9 + 450, self.Enemigo_FA_V2_Crear)
				self.PantallaTexto.after(Tiempo*9 + 450, self.Enemigo_FA_V2_Crear)

				if self.Dificultad == 3:
					self.PantallaTexto.after(7750, lambda:self.QuitarBoton("FlechasV2"))

			if self.Dificultad > 3:

				if Patron[5] == 1:

					self.PantallaTexto.after(Tiempo*11, self.Enemigo_FA_V2_Crear, 0.028, 0.016)
					self.PantallaTexto.after(Tiempo*11 + 200, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)
					self.PantallaTexto.after(Tiempo*11 + 400, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
					self.PantallaTexto.after(Tiempo*11 + 450, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 100, self.Enemigo_FA_V2_Crear, 0.028, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 300, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 300, self.Enemigo_FA_V2_Crear, 0.782, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 450, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
					self.PantallaTexto.after(Tiempo*13, self.Enemigo_FA_V2_Crear, 0.028, 0.016)

				elif Patron[5] == 2:

					self.PantallaTexto.after(Tiempo*11, self.Enemigo_FA_V2_Crear, 0.782, 0.016)
					self.PantallaTexto.after(Tiempo*11 + 200, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)
					self.PantallaTexto.after(Tiempo*11 + 400, self.Enemigo_FA_V2_Crear, 0.028, 0.016)
					self.PantallaTexto.after(Tiempo*11 + 450, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 100, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 300, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)
					self.PantallaTexto.after(Tiempo*12 + 300, self.Enemigo_FA_V2_Crear, 0.782, 0.016)	
					self.PantallaTexto.after(Tiempo*12 + 450, self.Enemigo_FA_V2_Crear, 0.028, 0.016)
					self.PantallaTexto.after(Tiempo*13, self.Enemigo_FA_V2_Crear, 0.405, 0.016)

				self.PantallaTexto.after(9300, lambda:self.QuitarBoton("FlechasV2"))

		else:

			self.PantallaTexto.after(Tiempo + 100, self.Enemigo_FA_V2_Crear, 0.12225)
			self.PantallaTexto.after(Tiempo + 100, self.Enemigo_FA_V2_Crear, 0.68775)
			self.PantallaTexto.after(Tiempo + 450, self.Enemigo_FA_V2_Crear, 0.405)

			self.PantallaTexto.after(Tiempo*2 + 500, self.Enemigo_FA_V2_Crear, 0.12225, 0.013)
			self.PantallaTexto.after(Tiempo*2 + 500, self.Enemigo_FA_V2_Crear, 0.68775, 0.013)
			self.PantallaTexto.after(Tiempo*3 + 350, self.Enemigo_FA_V2_Crear, 0.405, 0.013)

			self.PantallaTexto.after(Tiempo*4 + 600, self.Enemigo_FA_V2_Crear, 0.028, 0.016)
			self.PantallaTexto.after(Tiempo*5 + 100, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)
			self.PantallaTexto.after(Tiempo*5 + 200, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
			self.PantallaTexto.after(Tiempo*5 + 300, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)

			self.PantallaTexto.after(Tiempo*6 + 100, self.Enemigo_FA_V2_Crear, 0.782, 0.016)
			self.PantallaTexto.after(Tiempo*6 + 200, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)
			self.PantallaTexto.after(Tiempo*6 + 300, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
			self.PantallaTexto.after(Tiempo*6 + 400, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)

			self.PantallaTexto.after(Tiempo*7 + 400, self.Enemigo_FA_V2_Crear, 0.028, 0.010)
			self.PantallaTexto.after(Tiempo*7 + 400, self.Enemigo_FA_V2_Crear, 0.2165, 0.010)
			self.PantallaTexto.after(Tiempo*7 + 400, self.Enemigo_FA_V2_Crear, 0.68775, 0.010)

			self.PantallaTexto.after(Tiempo*8 + 50, self.Enemigo_FA_V2_Crear, 0.49925, 0.010)
			self.PantallaTexto.after(Tiempo*8 + 50, self.Enemigo_FA_V2_Crear, 0.782, 0.010)

			self.PantallaTexto.after(Tiempo*8 + 300, self.Enemigo_FA_V2_Crear, 0.028, 0.010)
			self.PantallaTexto.after(Tiempo*8 + 300, self.Enemigo_FA_V2_Crear, 0.2165, 0.010)
			self.PantallaTexto.after(Tiempo*8 + 300, self.Enemigo_FA_V2_Crear, 0.68775, 0.010)

			self.PantallaTexto.after(Tiempo*9 + 200, self.Enemigo_FA_V2_Crear, 0.028, 0.010)
			self.PantallaTexto.after(Tiempo*9 + 200, self.Enemigo_FA_V2_Crear, 0.2165, 0.010)
			self.PantallaTexto.after(Tiempo*9 + 200, self.Enemigo_FA_V2_Crear, 0.68775, 0.010)

			self.PantallaTexto.after(Tiempo*9 + 450, self.Enemigo_FA_V2_Crear, 0.028, 0.010)
			self.PantallaTexto.after(Tiempo*9 + 450, self.Enemigo_FA_V2_Crear, 0.49925, 0.010)
			self.PantallaTexto.after(Tiempo*9 + 450, self.Enemigo_FA_V2_Crear, 0.782, 0.010)

			self.PantallaTexto.after(Tiempo*11 + 100, self.Enemigo_FA_V2_Crear, 0.028, 0.013)
			self.PantallaTexto.after(Tiempo*11 + 100, self.Enemigo_FA_V2_Crear, 0.2165, 0.013)
			self.PantallaTexto.after(Tiempo*11 + 100, self.Enemigo_FA_V2_Crear, 0.405, 0.013)
			self.PantallaTexto.after(Tiempo*11 + 100, self.Enemigo_FA_V2_Crear, 0.5935, 0.013)

			self.PantallaTexto.after(Tiempo*12 + 100, self.Enemigo_FA_V2_Crear, 0.405)
			self.PantallaTexto.after(Tiempo*12 + 250, self.Enemigo_FA_V2_Crear, 0.31075)
			self.PantallaTexto.after(Tiempo*12 + 250, self.Enemigo_FA_V2_Crear, 0.49925)

			self.PantallaTexto.after(Tiempo*12 + 500, self.Enemigo_FA_V2_Crear, 0.028)
			self.PantallaTexto.after(Tiempo*12 + 500, self.Enemigo_FA_V2_Crear, 0.782)

			self.PantallaTexto.after(Tiempo*13 + 150, self.Enemigo_FA_V2_Crear, 0.405)
			self.PantallaTexto.after(Tiempo*13 + 300, self.Enemigo_FA_V2_Crear, 0.31075)
			self.PantallaTexto.after(Tiempo*13 + 300, self.Enemigo_FA_V2_Crear, 0.49925)

			self.PantallaTexto.after(Tiempo*13 + 550, self.Enemigo_FA_V2_Crear, 0.028)
			self.PantallaTexto.after(Tiempo*13 + 550, self.Enemigo_FA_V2_Crear, 0.782)

			self.PantallaTexto.after(Tiempo*14 + 200, self.Enemigo_FA_V2_Crear, 0.405)
			self.PantallaTexto.after(Tiempo*14 + 350, self.Enemigo_FA_V2_Crear, 0.31075)
			self.PantallaTexto.after(Tiempo*14 + 350, self.Enemigo_FA_V2_Crear, 0.49925)

			self.PantallaTexto.after(Tiempo*14 + 600, self.Enemigo_FA_V2_Crear, 0.028)
			self.PantallaTexto.after(Tiempo*14 + 600, self.Enemigo_FA_V2_Crear, 0.782)

			self.PantallaTexto.after(Tiempo*15 + 500, self.Enemigo_FA_V2_Crear)
			self.PantallaTexto.after(Tiempo*16 + 500, self.Enemigo_FA_V2_Crear)
			self.PantallaTexto.after(Tiempo*17 + 400, self.Enemigo_FA_V2_Crear)

			self.PantallaTexto.after(Tiempo*19 + 100, self.Enemigo_FA_V2_Crear, 0.12225, 0.016)
			self.PantallaTexto.after(Tiempo*19 + 100, self.Enemigo_FA_V2_Crear, 0.68775, 0.016)

			self.PantallaTexto.after(Tiempo*20 + 600, self.Enemigo_FA_V2_Crear, 0.028, 0.016)
			self.PantallaTexto.after(Tiempo*20 + 100, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)
			self.PantallaTexto.after(Tiempo*20 + 200, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
			self.PantallaTexto.after(Tiempo*20 + 300, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)

			self.PantallaTexto.after(Tiempo*21 + 100, self.Enemigo_FA_V2_Crear, 0.782, 0.016)
			self.PantallaTexto.after(Tiempo*21 + 200, self.Enemigo_FA_V2_Crear, 0.5935, 0.016)
			self.PantallaTexto.after(Tiempo*21 + 300, self.Enemigo_FA_V2_Crear, 0.405, 0.016)
			self.PantallaTexto.after(Tiempo*21 + 400, self.Enemigo_FA_V2_Crear, 0.2165, 0.016)

			self.PantallaTexto.after(15100, lambda:self.QuitarBoton("FlechasV2"))

	def Enemigo_FA_V2_Crear(self, PosicionY = False, Velocidad = 0.01):

		Flecha = tk.Label(self.SegundoFrame, image = self.Ataque_9, bd = 0)

		if PosicionY == False:
			PosicionY = choice([0.028, 0.2165, 0.405, 0.5935, 0.782])

		PosicionX = 0.8

		Flecha.place(relx = PosicionX, rely = PosicionY)

		self.PantallaTexto.after(300, lambda:Enemigo_FA_V2_Mover(self, PosicionX, PosicionY, Velocidad))

		def Enemigo_FA_V2_Mover(self, PosicionX, PosicionY, Velocidad):

			if PosicionX > 0.10:
				PosicionX = PosicionX - Velocidad
				Flecha.place(relx = PosicionX)
				self.PantallaTexto.after(20, lambda:Enemigo_FA_V2_Mover(self, PosicionX, PosicionY, Velocidad))

			else:
				if round((self.BarraVertical.get()/40)/(100/18.85), 4) <= round(PosicionY - 0.21, 4) or round((self.BarraVertical.get()/40)/(100/18.85), 4) >= round(PosicionY + 0.1540, 4):	# El primero creo que esquiva abajo, y el segundo esquiva los de arriba
					Flecha.destroy()
					

				else:
					Ataque = choice([self.Enemigo_Ataque - 4, self.Enemigo_Ataque - 3, self.Enemigo_Ataque - 2, self.Enemigo_Ataque - 1])

					daño = Ataque - self.Yo_Blindaje
					if daño <= 0:
						daño = 0
					self.Yo_VidaActual = self.Yo_VidaActual - daño
					mixer.Channel(3).play(self.Sonido_Flechas_V2)
					self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))
					Flecha.destroy()


	def Enemigo_Embestida(self):
		self.Texto.set("\n")
		self.Progreso.place(relx = 0.5, rely = 0.25, anchor = "center")
		self.Imagen_Embestida_Yo.place(relx = 0.37, rely = 0.4)
		self.Imagen_Embestida_Enemigo.place(relx = 0.51, rely = 0.4)
		self.LabelProgresoYo.place(relx = 0.325, rely = 0.48)
		self.LabelProgresoEnemigo.place(relx = 0.63, rely = 0.48)
		self.Progreso["value"] = 50

		mixer.Channel(3).play(self.Sonido_Embestida)
		self.ProgresoYo.set(self.Progreso["value"])
		self.ProgresoEnemigo.set(100 - self.Progreso["value"])

		self.ruedas_img = AbrirImagenEX("Imagenes/Ruedas.png", self.DR)
		self.ruedas_2_img = AbrirImagenEX("Imagenes/Ruedas_2.png", self.DR)
		self.BotonEmpujar_ruedas = tk.Label(self.SegundoFrame, image = self.ruedas_img, border = 0)
		self.BotonEmpujar_ruedas.place(relx = 0.395, y = Redondear(113, self.DR))
		self.BotonEmpujar.place(relx = 0.4)
		self.BotonEmpujar["state"] = "disabled"

		def CambiarGifRuedas1(self):
			if self.BotonEmpujar_ruedas.winfo_exists() == 1:
				self.BotonEmpujar_ruedas.configure(image = self.ruedas_img)
				self.PantallaTexto.after(100, lambda:CambiarGifRuedas2(self))

		def CambiarGifRuedas2(self):
			if self.BotonEmpujar_ruedas.winfo_exists() == 1:
				self.BotonEmpujar_ruedas.configure(image = self.ruedas_2_img)
				self.PantallaTexto.after(100, lambda:CambiarGifRuedas1(self))

		self.PantallaTexto.after(1000, self.Enemigo_EmbestirRepetida)
		self.PantallaTexto.after(1100, lambda:CambiarGifRuedas2(self))

	def Enemigo_EmbestirRepetida(self):

		self.FramePrincipal.update_idletasks()

		def CambiarFase(self, Haciafase):

			if Haciafase == 2:
				self.Embestida_Fase = 2
			elif Haciafase == 3:
				self.Embestida_Fase = 3
			elif Haciafase == 4:
				self.Embestida_Fase = 4

		if self.BotonEmpujar["state"] != "normal":
			self.BotonEmpujar["state"] = "normal"

		if self.Embestida_Fase == 4:
			self.Progreso["value"] -= 3
			self.Imagen_Embestida_Enemigo.config(image = self.Ataque_8_Enemigo_Potente_3)
			self.Sonido_Embestida.set_volume(0.16)

			self.PantallaTexto.after(1000, lambda:CambiarFase(self, 3))

		elif self.Embestida_Fase == 2:
			self.Progreso["value"] -= 1
			self.Imagen_Embestida_Enemigo.config(image = self.Ataque_8_Enemigo)
			self.Sonido_Embestida.set_volume(0.1)

			if self.Dificultad == 3:
				self.PantallaTexto.after(2000, lambda:CambiarFase(self, 4))
			elif self.Dificultad == 2:
				self.PantallaTexto.after(2500, lambda:CambiarFase(self, 3))
			else:
				self.PantallaTexto.after(3000, lambda:CambiarFase(self, 3))

		elif self.Embestida_Fase == 3:
			self.Progreso["value"] -= 2
			self.Imagen_Embestida_Enemigo.config(image = self.Ataque_8_Enemigo_Potente)
			self.Sonido_Embestida.set_volume(0.13)

			if self.Dificultad == 3:	# Tiempo en que tarda en cambiar de fase
				self.PantallaTexto.after(3000, lambda:CambiarFase(self, 2))
			elif self.Dificultad == 2:
				self.PantallaTexto.after(3000, lambda:CambiarFase(self, 2))
			else:
				self.PantallaTexto.after(2000, lambda:CambiarFase(self, 2))

		else:
			self.Progreso["value"] -= 1
			self.Imagen_Embestida_Enemigo.config(image = self.Ataque_8_Enemigo)

			if self.Progreso["value"] >= 60:

				if self.Dificultad == 3:
					self.Embestida_Fase = 4

				else:
					self.Embestida_Fase = 3

		self.Enemigo_Embestida_Posicion()

	def Enemigo_Embestida_Posicion(self):

		if self.Progreso["value"] < 100 and self.Progreso["value"] > 0:

			Progresin = self.Progreso["value"]
			ProgresinEnemigo = 100 - Progresin

			self.ProgresoYo.set(f"{Progresin:02d}")
			self.ProgresoEnemigo.set(f"{ProgresinEnemigo:02d}")

			Posicion = (0.82 * self.Progreso["value"]/100) - 0.02
			PosicionLabelYo = (0.3 * self.Progreso["value"]/100) + 0.19
			PosicionFlechaYo = (0.3 * self.Progreso["value"]/100) + 0.24
			PosicionFlechaEnemigo = (0.3 * self.Progreso["value"]/100) + 0.37
			PosicionLabelEnemigo = (0.3 * self.Progreso["value"]/100) + 0.49

			if Posicion < 0:
				Posicion = 0
			self.BotonEmpujar.place(relx = Posicion)
			self.BotonEmpujar_ruedas.place(relx = Posicion - 0.005)
			self.Imagen_Embestida_Yo.place(relx = PosicionFlechaYo)
			self.Imagen_Embestida_Enemigo.place(relx = PosicionFlechaEnemigo)

			self.LabelProgresoYo.place(relx = PosicionLabelYo)
			self.LabelProgresoEnemigo.place(relx = PosicionLabelEnemigo)

			self.Texto.set("\n")

			self.PantallaTexto.after(50, self.Enemigo_EmbestirRepetida)

		else:

			if self.Progreso["value"] <= 0:
				self.ProgresoYo.set(0)
				self.ProgresoEnemigo.set(100)
				Posicion = 0
				self.BotonEmpujar.place(relx = Posicion)
				self.Imagen_Embestida_Yo.config(image = self.Ataque_8_Yo_Derrotado)
				self.PantallaTexto.after(1500, self.EjecutadorDelTurnoEnemigo, "Derrota")


			elif self.Progreso["value"] >= 100:
				self.ProgresoYo.set(100)
				self.ProgresoEnemigo.set(0)
				Posicion = 0.782
				self.BotonEmpujar.place(relx = Posicion)
				self.LabelProgresoYo.place(relx = 0.45)
				self.Imagen_Embestida_Enemigo.config(image = self.Ataque_8_Enemigo_Derrotado)
				self.PantallaTexto.after(1500, self.EjecutadorDelTurnoEnemigo, "Victoria")

			self.Progreso.place_forget()
			self.BotonEmpujar.place_forget()
			self.BotonEmpujar_ruedas.destroy()
			mixer.Channel(3).fadeout(500)
			self.PantallaTexto.after(1500, self.QuitarBoton, "Embestida")

	# ------------------- Yo

	def EstadisticasYo(self):
		mixer.Channel(2).play(self.Sonido_Estadisticas)

		if self.Idioma == "español":
			self.Texto.set ("Nombre: " + self.Yo_Nombre + "\nVida: " + str(self.Yo_Vida) + "\nAtaque: " +
			str(self.Yo_Ataque) + "\nBlindaje: " + str(self.Yo_Blindaje))
		elif self.Idioma == "english":
			self.Texto.set ("Name: " + self.Yo_Nombre + "\nHealth: " + str(self.Yo_Vida) + "\nAttack: " +
			str(self.Yo_Ataque) + "\nArmor: " + str(self.Yo_Blindaje))

	def Yo_BlindajePerdido(self):

		Perdida = choice([3,4])

		self.Yo_Blindaje -= Perdida

		if self.Yo_Blindaje < 0:
			self.Yo_Blindaje = 0
		if self.Idioma == "español":
			self.Texto.set("Nuestro blindaje ha sido perforado. " + "\nEl blindaje actual es " + str(self.Yo_Blindaje) + ".")
		elif self.Idioma == "english":
			self.Texto.set("Our armor has been pierced. " + "\nCurrent armor is " + str(self.Yo_Blindaje) + ".")

	def Yo_Enfocar(self):
		if self.Idioma == "español":
			self.Texto.set("Nuestros próximos 2 ataques tienen " + "\nmás precisión y atravesaran su blindaje.")
		elif self.Idioma == "english":
			self.Texto.set("Our next 2 attacks have more accuracy " + "\nand they will pass through their armor.")
		self.Enfoque = self.Enfoque + 3
		
		if self.Enfoque <= 3:
			self.Enfoque_Cantidad_Label = tk.Label(self.FramePrincipal, image = self.Accion_1_Conteo, border = 0)
			self.Enfoque_Cantidad_Label.grid(row = 2, column = 1, columnspan = 1, sticky = "w", ipadx = Redondear(6, self.DR))

	def Presionar(self):

		self.Presionado += 1

		Probabilidad = choice([1,2])

		if Probabilidad == 1:
			mixer.Channel(4).play(self.Sonido_Bombardeo)
		else:
			mixer.Channel(4).play(self.Sonido_Bombardeo_2)

		Posicion = choice([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85])
		self.BotonRojo.place(relx = Posicion)

	def Presionar_Empujar(self):

		if self.Dificultad == 3:
			self.Progreso["value"] += 7
		elif self.Dificultad == 2:
			self.Progreso["value"] += 8
		else:
			self.Progreso["value"] += 10

	def Presionar_Esquivar_Izquierda(self, Cantidad_):

		if self.Presionado < Cantidad_:

			if self.Palabra == "Izquierda":
				self.Esquivado += 1
				mixer.Channel(3).play(self.Sonido_Esquivar_Flechas)
			else:
				self.BotonIzquierda.config(bg = "#FF7A7A")
				mixer.Channel(3).play(self.Sonido_Flechas_V2)
				self.PantallaTexto.after(150, self.ResetearColorBoton)

				self.Fallado += 1

				Daño = choice([self.Enemigo_Ataque - 1, self.Enemigo_Ataque, self.Enemigo_Ataque + 1])

				Daño = Daño - self.Yo_Blindaje

				if Daño < 0:
					Daño = 0

				self.DañoTotal += Daño

				self.Yo_VidaActual = self.Yo_VidaActual - Daño
				self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))

			self.Presionado += 1

			self.CambiarNumero()

			if self.Presionado >= Cantidad_:
				self.Imagen_Flechas.place_forget()
				self.BotonIzquierda.grid_forget()
				self.BotonDerecha.grid_forget()

			else:

				Porcentaje = random()

				if Porcentaje <= 0.25:
					self.Palabra = "Izquierda"
				else:
					self.Palabra = "Derecha"

				if self.Palabra == "Izquierda":
					self.Imagen_Flechas.config(image = self.Ataque_6_Izquierda)

				elif self.Palabra == "Derecha":
					self.Imagen_Flechas.config(image = self.Ataque_6_Derecha)

	def Presionar_Esquivar_Derecha(self, Cantidad_):

		if self.Presionado < Cantidad_:

			if self.Palabra == "Derecha":
				self.Esquivado += 1
				mixer.Channel(3).play(self.Sonido_Esquivar_Flechas)
			else:
				self.BotonDerecha.config(bg = "#FF7A7A")
				mixer.Channel(3).play(self.Sonido_Flechas_V2)
				self.PantallaTexto.after(150, self.ResetearColorBoton)

				self.Fallado += 1

				Daño = choice([self.Enemigo_Ataque - 1, self.Enemigo_Ataque, self.Enemigo_Ataque + 1])

				Daño = Daño - self.Yo_Blindaje

				if Daño < 0:
					Daño = 0

				self.DañoTotal += Daño

				self.Yo_VidaActual = self.Yo_VidaActual - Daño
				self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))


			self.Presionado += 1

			self.CambiarNumero()

			if self.Presionado >= Cantidad_:
				self.Imagen_Flechas.place_forget()
				self.BotonIzquierda.grid_forget()
				self.BotonDerecha.grid_forget()

			else:

				Porcentaje = random()

				if Porcentaje <= 0.33:
					self.Palabra = "Derecha"
				else:
					self.Palabra = "Izquierda"

				if self.Palabra == "Izquierda":
					self.Imagen_Flechas.config(image = self.Ataque_6_Izquierda)

				if self.Palabra == "Derecha":
					self.Imagen_Flechas.config(image = self.Ataque_6_Derecha)

	def CambiarNumero(self):

		Numero = self.Cantidad - self.Presionado

		if Numero == 9:

			self.Imagen_Mi_Lado.config(image = self.Numero_9)

		elif Numero == 8:

			self.Imagen_Mi_Lado.config(image = self.Numero_8)

		elif Numero == 7:

			self.Imagen_Mi_Lado.config(image = self.Numero_7)

		elif Numero == 6:

			self.Imagen_Mi_Lado.config(image = self.Numero_6)

		elif Numero == 5:

			self.Imagen_Mi_Lado.config(image = self.Numero_5)

		elif Numero == 4:

			self.Imagen_Mi_Lado.config(image = self.Numero_4)

		elif Numero == 3:

			self.Imagen_Mi_Lado.config(image = self.Numero_3)

		elif Numero == 2:

			self.Imagen_Mi_Lado.config(image = self.Numero_2)

		elif Numero == 1:

			self.Imagen_Mi_Lado.config(image = self.Numero_1)

		elif Numero == 0:

			self.Imagen_Mi_Lado.config(image = self.Numero_0)

	def ResetearColorBoton(self):
		self.BotonDerecha.config(bg = "#71FF54")
		self.BotonIzquierda.config(bg = "#71FF54")

	def Yo_Repararme(self, masvida, masblindaje):

		if (masvida + self.Yo_VidaActual) > self.Yo_Vida:
			masvida = self.Yo_Vida - self.Yo_VidaActual

		if self.Idioma == "español":
			self.Texto.set("Recuperas " + str(masvida) + " de vida." + "\nY consigues " + str(masblindaje) + " extra de blindaje.")
		elif self.Idioma == "english":
			self.Texto.set("You recover " + str(masvida) + " health." + "\nAnd you obtain " + str(masblindaje) + " extra armor.")
		self.Yo_VidaActual += masvida
		self.Yo_Blindaje += masblindaje

		self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))

	def Presionar_Detener(self):

		mixer.Channel(2).fadeout(100)
		mixer.Channel(2).play(self.Sonido_Perforador)
		Progreso = self.ProgresoAtaque["value"]
		self.BotonDetenerBarra["state"] = "disabled"
		self.ProgresoAtaque.stop()
		self.Presionado = 1
		self.ProgresoAtaque["value"] = Progreso

	def DañoAMi(self, numero, daño, No_Presionado = 0, Probabilidad = 0):

		if numero == 0:

			daño = round(daño * 1.25)
			daño = daño - self.Yo_Blindaje

			if self.Idioma == "español":
				self.Texto.set("La bala ha explotado en nuestro cañon.\n" + "Hemos recibido " + str(daño) + " de daño.")
			elif self.Idioma == "english":
				self.Texto.set("The bullet has exploded inside our gun.\n" + "We have received " + str(daño) + " damage.")
			self.Yo_VidaActual = self.Yo_VidaActual - (daño)
			self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))
			Probabilidad = 5

		elif numero in (1, 2, 3):

			daño = daño - self.Yo_Blindaje

			if numero == 2:
				daño = daño*2

			elif numero == 3:
				if Probabilidad >= 4:
					self.PantallaTexto.after(500, lambda:self.PonerSonido(3, self.Sonido_RompeBlindaje))
					self.PantallaTexto.after(750, lambda:self.PonerSonido(4, self.Sonido_Disparo_Critico))
					self.PantallaTexto.after(2000, self.Yo_BlindajePerdido)
					self.PantallaTexto.after(3990, self.Volver)

			if daño <= 0:
				daño = 0
				if self.Idioma == "español":
					self.Texto.set(self.Texto.get() + "Tu blindaje ha bloqueado todo el daño.")
				elif self.Idioma == "english":
					self.Texto.set(self.Texto.get() + "Your armor has blocked all the damage.")
			else:
				if self.Idioma == "español":
					self.Texto.set(self.Texto.get() + self.Yo_Nombre + " ha recibido " + str(daño) + " de daño.")
				elif self.Idioma == "english":
					self.Texto.set(self.Texto.get() + self.Yo_Nombre + " has received " + str(daño) + " damage.")
			self.Yo_VidaActual = self.Yo_VidaActual - (daño)
			self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))

		elif numero == 5:

			DañoTotal = 0

			for i in range(No_Presionado):

				DañoFallado = choice([self.Enemigo_Ataque - 1, self.Enemigo_Ataque, self.Enemigo_Ataque + 1])
				DañoFallado = DañoFallado - self.Yo_Blindaje

				if DañoFallado < 0:
					DañoFallado = 0

				DañoTotal += DañoFallado

			self.Yo_VidaActual = self.Yo_VidaActual - DañoTotal
			self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))

			daño += DañoTotal

			VecesFallado = self.Fallado + No_Presionado

			if daño == 0:
				if self.Idioma == "español":
					self.Texto.set("Has esquivado todos los disparos." + "\n")
				elif self.Idioma == "english":
					self.Texto.set("You have dodged all the shots." + "\n")

			elif daño <= 0:
				if self.Idioma == "español":
					self.Texto.set("Tu blindaje ha bloqueado todo el daño." + "\n")
				elif self.Idioma == "english":
					self.Texto.set("Your armor has blocked all the damage." + "\n")
				daño = 0

			else:
				if VecesFallado == 1:
					if self.Idioma == "español":
						self.Texto.set("Has fallado solo " + str(VecesFallado) + " vez.\n" + self.Yo_Nombre +
						" ha recibido " + str(daño) + " de daño.")
					elif self.Idioma == "english":
						self.Texto.set("You have failed only " + str(VecesFallado) + " time.\n" + self.Yo_Nombre +
						" has received " + str(daño) + " damage.")
				else:
					if self.Idioma == "español":
						self.Texto.set("Has fallado " + str(VecesFallado) + " veces.\n" + self.Yo_Nombre +
						" ha recibido " + str(daño) + " de daño.")
					elif self.Idioma == "english":
						self.Texto.set("You have failed " + str(VecesFallado) + " times.\n" + self.Yo_Nombre +
						" has received " + str(daño) + " damage.")

		elif numero == 6:

			if daño == 0:
				if self.Idioma == "español":
					self.Texto.set("Has logrado parar al enemigo." + "\n")
				elif self.Idioma == "español":
					self.Texto.set("You have managed to stop the enemy." + "\n")
			else:
				if self.Idioma == "español":
					self.Texto.set(self.Yo_Nombre + " ha recibido " + str(daño) + " de daño." + "\n")
				elif self.Idioma == "english":
					self.Texto.set(self.Yo_Nombre + " has received " + str(daño) + " damage." + "\n")
			self.Yo_VidaActual = self.Yo_VidaActual - (daño)
			self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))
				
		elif numero == 7:

			if daño == 0:
				if self.Idioma == "español":
					self.Texto.set("Has esquivado todos los disparos." + "\n")
				elif self.Idioma == "english":
					self.Texto.set("You have dodged all the shots." + "\n")

				if self.Dificultad >= 3:
					self.ConfirmarLogros(9)

			else:
				if self.Idioma == "español":
					self.Texto.set("Has recibido " + str(daño) + " de daño." + "\n")
				elif self.Idioma == "english":
					self.Texto.set("You have received " + str(daño) + " damage." + "\n")

		self.Daño_Recibido += daño
		self.MiVida.set(self.Yo_Nombre + " " + str(self.Yo_VidaActual) + "/" + str(self.Yo_Vida))

		if self.Yo_VidaActual <= 0:
			self.PantallaTexto.after(2000, lambda:self.Derrota())
		
		elif Probabilidad >= 4:
			pass

		else:	
			self.PantallaTexto.after(990, self.Volver)

	# ------------------- Funciones de la estrucutra

	def SelectorAtaque(self,Turnos):

		if self.Dificultad < 4:

			if self.Dificultad in (1,2):
				if self.Enemigo_Reparaciones == 0:
					Turnos = Turnos - 1

			elif self.Dificultad == 3:

				if self.Enemigo_Reparaciones == 1:
					Turnos = Turnos - 1

				elif self.Enemigo_Reparaciones == 0:
					Turnos = Turnos - 2

			Minimo_Para_Curacion = choice([110, 130, 150]) # Mientras menor la cantidad, más rápido se curará.

			if (self.Enemigo_Vida - self.Enemigo_VidaActual) >= Minimo_Para_Curacion and self.Enemigo_Reparaciones >= 1:
				Eleccion = 4
				Daño = 50

			elif Turnos in (5, 10, 15, 20, 25, 30, 35) and self.Enemigo_Lanzo_Embestida == False:
				Eleccion = 2
				Daño = self.Enemigo_GolpeBasico()

			elif self.Enemigo_VidaActual - self.Yo_Ataque*1.25 <= 0 and self.Enemigo_Lanzo_Embestida == False:
				self.Enemigo_Lanzo_Embestida = True
				Eleccion = 6             # Ataque Embestida
				Daño = 0

			elif Turnos in (1, 4, 9, 13, 17, 21, 24, 28, 31) or self.Enemigo_Lanzo_Embestida == True:
				Eleccion = 1
				Daño = self.Enemigo_GolpeBasico()

			elif Turnos in (2, 6, 8, 12, 14, 18, 22, 27, 33):

				Probabilidad = randint(1, 100)

				if Probabilidad <= self.Probabilidad_Perforador:
					self.Probabilidad_Perforador -= 5
					Eleccion = 3
					Daño = self.Enemigo_RompeCorazas()

				else:
					self.Probabilidad_Perforador += 10
					Eleccion = 1
					Daño = self.Enemigo_GolpeBasico()


			elif Turnos in (3, 7, 11, 16, 19, 23, 26, 29, 32, 34):

				Probabilidad = randint(0, 100)

				if Probabilidad <= self.Probabilidad_Flechas_1:
					self.Probabilidad_Flechas_1 -= 10
					Eleccion = 5              # Ataque Flechas
					self.Enemigo_TiempoFuegoAbrumador()
					Daño = 0
				else:
					self.Probabilidad_Flechas_1 += 10
					Eleccion = 7             # Ataque Flechas V2
					self.PantallaTexto.after(2000, self.Enemigo_FA_V2)
					Daño = 0

			return(Eleccion, Daño)

		else:

			if self.Enemigo_Reparaciones == 1:
				Turnos = Turnos - 1

			elif self.Enemigo_Reparaciones == 0:
				Turnos = Turnos - 2


			if (self.Enemigo_Vida - self.Enemigo_VidaActual) >= 80 and self.Enemigo_Reparaciones >= 1:
				Eleccion = 4
				Daño = 0

			elif Turnos in (3, 8, 13, 18, 23, 28, 33) and self.Enemigo_Lanzo_Embestida == False:
				Eleccion = 2
				Daño = self.Enemigo_GolpeBasico()

			elif self.Enemigo_VidaActual - self.Yo_Ataque*1.25 <= 0 and self.Enemigo_Lanzo_Embestida == False:
				self.Enemigo_Lanzo_Embestida = True
				Eleccion = 8
				self.PantallaTexto.after(3000, self.Enemigo_FA_V2, True)
				Daño = 0

			elif Turnos in (4, 6, 9, 12, 16, 20, 24, 25, 27, 34):
				Eleccion = 1
				Daño = self.Enemigo_GolpeBasico()

			elif Turnos in (1, 5, 10, 14, 17, 22, 26, 32):

				Probabilidad = randint(1, 100)

				if Probabilidad <= self.Probabilidad_Perforador:
					self.Probabilidad_Perforador -= 5
					Eleccion = 3
					Daño = self.Enemigo_RompeCorazas()

				else:
					self.Probabilidad_Perforador += 15
					Eleccion = 1
					Daño = self.Enemigo_GolpeBasico()

			elif Turnos in (2, 7, 11, 15, 19, 21, 25, 29, 31, 35):

				Probabilidad = randint(1, 100)

				if Probabilidad <= self.Probabilidad_Flechas_1 + 20:
					self.Probabilidad_Flechas_1 -= 10
					Eleccion = 5              # Ataque Flechas
					self.Enemigo_TiempoFuegoAbrumador()
					Daño = 0
				else:
					self.Probabilidad_Flechas_1 += 10
					Eleccion = 7             # Ataque Flechas V2
					self.PantallaTexto.after(2000, self.Enemigo_FA_V2)
					Daño = 0

			else: # Si todo falla
				Eleccion = 1
				Daño = self.Enemigo_GolpeBasico()

			return(Eleccion, Daño)

	def EjecutadorDelTurnoEnemigo(self, VariableExtra = ""):

		if self.Enemigo_VidaActual <= 0:
			self.Victoria()

		elif self.Yo_VidaActual <= 0:
			self.Derrota()

		elif VariableExtra == "":

			Selector = self.SelectorAtaque(self.TurnoActual)

			self.PantallaTexto.after(0, self.Enemigo_Habilidades, Selector[0])

		else:
			Selector = [6, 0]

		if self.Enemigo_VidaActual <= 0 or self.Yo_VidaActual <= 0:
			pass

		elif Selector[0] == 3:

			if self.Dificultad >= 3:
				Probabilidad = choice([3,4])
			else:
				Probabilidad = choice([2,3,4])

			self.PantallaTexto.after(2000, lambda:self.DañoAMi(Selector[0], Selector[1], None , Probabilidad))

			if Probabilidad >= 4:

				self.PantallaTexto.after(6000, self.PasarTurnos)

			else:
				self.PantallaTexto.after(3000, self.PasarTurnos)

		elif Selector[0] == 5:

			self.PantallaTexto.after(3000, self.Enemigo_FuegoAbrumador)

			self.PantallaTexto.after(self.Tiempo + 3000 + 1500, lambda:self.DañoAMi(Selector[0], self.DañoTotal, self.Cantidad - self.Presionado)) # Amado Diosito Lambda

			self.PantallaTexto.after(self.Tiempo + 3000 + 2500, self.PasarTurnos)

		elif Selector[0] == 6:

			if VariableExtra == "Victoria":

				self.PantallaTexto.after(0, self.DañoAMi, Selector[0], Selector[1])

				self.PantallaTexto.after(1000, self.PasarTurnos)

			elif VariableExtra == "Derrota":

				self.PantallaTexto.after(0, self.DañoAMi, Selector[0], 80 + self.Enemigo_Ataque - self.Yo_Blindaje)

				self.PantallaTexto.after(1000, self.PasarTurnos)

			else:

				self.PantallaTexto.after(3000, self.Enemigo_Embestida)

		elif Selector[0] == 7:
			VidaActual = self.Yo_VidaActual

			if self.Dificultad == 1:
				self.PantallaTexto.after(7400, lambda:self.DañoAMi(Selector[0], VidaActual - self.Yo_VidaActual))
				self.PantallaTexto.after(8400, self.PasarTurnos)

			elif self.Dificultad == 2:
				self.PantallaTexto.after(8100, lambda:self.DañoAMi(Selector[0], VidaActual - self.Yo_VidaActual))
				self.PantallaTexto.after(9100, self.PasarTurnos)

			elif self.Dificultad == 3:
				self.PantallaTexto.after(9800, lambda:self.DañoAMi(Selector[0], VidaActual - self.Yo_VidaActual))
				self.PantallaTexto.after(10800, self.PasarTurnos)

			elif self.Dificultad == 4:
				self.PantallaTexto.after(11800, lambda:self.DañoAMi(Selector[0], VidaActual - self.Yo_VidaActual))
				self.PantallaTexto.after(12800, self.PasarTurnos)

		elif Selector[0] == 8:
			VidaActual = self.Yo_VidaActual

			self.PantallaTexto.after(17700, lambda:self.DañoAMi(Selector[0], VidaActual - self.Yo_VidaActual))
			self.PantallaTexto.after(18700, self.PasarTurnos)

		else:

			self.PantallaTexto.after(2000, self.DañoAMi, Selector[0], Selector[1])

			self.PantallaTexto.after(3000, self.PasarTurnos)

	def Autodestruccion(self):

		self.Bloquear_Botones("Principal")
		self.Bloquear_Botones("Basico")
		self.Bloquear_Botones("Acciones")
		self.Bloquear_Botones("Especiales")
		self.Bloquear_Botones("Estadisticas")

		Puntaje = round((self.TurnoActual * 20 + (self.Enemigo_Vida - self.Enemigo_VidaActual)*3)/2)

		if self.Dificultad == 2:
			Puntaje = round(Puntaje * 1.25)
		elif self.Dificultad == 3:
			Puntaje = round(Puntaje * 1.5)
		elif self.Dificultad == 4:
			Puntaje = round(Puntaje * 1.75)

		if self.Idioma == "español":
			self.Texto.set("Has perdido.\nObtienes " + str(Puntaje) + " puntos." )
			self.Regresar_Inicio = tk.Button(self.SegundoFrame, text = "Regresar al inicio", command = lambda:self.Destruir(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR))
		elif self.Idioma == "english":
			self.Texto.set("You lose.\nYou get " + str(Puntaje) + " points." )
			self.Regresar_Inicio = tk.Button(self.SegundoFrame, text = "Return to the start", command = lambda:self.Destruir(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR))
		self.Regresar_Inicio.grid(row = 0, column = 0)
		Archivo_Datos = open("Datos.txt","r+")
		Datos = Archivo_Datos.readlines()

		Archivo_Datos.seek(0)

		for i in Datos[0:1]:
			if 'Puntos' in i:
				Puntos = int(i.split(":")[-1].strip())

		Puntos = Puntos + Puntaje

		Datos[0] = ("Puntos: " + str(Puntos) + "\n")

		Datos = Datos[:12]

		Archivo_Datos.writelines(Datos)

		Archivo_Datos.close()

		self.Guardar_Estadisticas(Puntaje, False)
		self.ConfirmarLogros(2)

	def Derrota(self):

		Archivo_Logros = open("Logros_Y_Estadisticas.txt","r+")
		Logros = Archivo_Logros.readlines()
		Archivo_Logros.seek(0)

		for i in Logros[1:2]:

			Resultado = (i.split(":")[-1].strip())

			if Resultado == "False":
				Logros[1] = ("L_Derrota_Estrategica: True" + "\n")

		Logros = Logros[:24]

		Archivo_Logros.truncate()
		Archivo_Logros.writelines(Logros)
		Archivo_Logros.close()

		Puntaje = self.TurnoActual * 20 + (self.Enemigo_Vida - self.Enemigo_VidaActual)*3

		if self.Dificultad == 2:
			Puntaje = round(Puntaje * 1.25)
		elif self.Dificultad == 3:
			Puntaje = round(Puntaje * 1.5)
		elif self.Dificultad == 4:
			Puntaje = round(Puntaje * 1.75)

		if self.Idioma == "español":
			self.Texto.set("Has perdido.\nObtienes " + str(Puntaje) + " puntos." )
			self.Regresar_Inicio = tk.Button(self.SegundoFrame, text = "Regresar al inicio", command = lambda:self.Destruir(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR))
		elif self.Idioma == "english":
			self.Texto.set("You lose.\nYou get " + str(Puntaje) + " points." )
			self.Regresar_Inicio = tk.Button(self.SegundoFrame, text = "Return to the start", command = lambda:self.Destruir(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR))
		self.Regresar_Inicio.grid(row = 0, column = 0)

		Archivo_Datos = open("Datos.txt","r+")
		Datos = Archivo_Datos.readlines()

		Archivo_Datos.seek(0)

		for i in Datos[0:1]:
			if 'Puntos' in i:
				Puntos = int(i.split(":")[-1].strip())

		Puntos = Puntos + Puntaje

		Datos[0] = ("Puntos: " + str(Puntos) + "\n")

		Datos = Datos[:12]

		Archivo_Datos.writelines(Datos)

		Archivo_Datos.close()

		self.Guardar_Estadisticas(Puntaje, False)
		self.ConfirmarLogros(2)

	def Victoria(self):

		Puntaje = self.TurnoActual * 20 + self.Enemigo_Vida*3 + self.Yo_VidaActual*3 + 200

		if self.Dificultad == 1:
			self.ConfirmarLogros(1)

		elif self.Dificultad == 2:
			self.ConfirmarLogros(4)

			Puntaje = round(Puntaje * 1.25)

		elif self.Dificultad == 3:
			self.ConfirmarLogros(7)

			Puntaje = round(Puntaje * 1.5)

		elif self.Dificultad == 4:
			self.ConfirmarLogros(10)

			if self.TanqueElegido == 1:
				self.ConfirmarLogros(12)

			Puntaje = round(Puntaje * 1.75)

		if self.Idioma == "español":
			self.Texto.set("Has ganado.\nObtienes " + str(Puntaje) + " puntos." )
			self.Regresar_Inicio = tk.Button(self.SegundoFrame, text = "Regresar al inicio", command = lambda:self.Destruir(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR))
		elif self.Idioma == "english":
			self.Texto.set("You win.\nYou get " + str(Puntaje) + " points." )
			self.Regresar_Inicio = tk.Button(self.SegundoFrame, text = "Return to the start", command = lambda:self.Destruir(), font = ('Arial',Redondear(40, self.DR)), border = Redondear(6, self.DR))
		self.Regresar_Inicio.grid(row = 0, column = 0)

		Archivo_Datos = open("Datos.txt","r+")
		Datos = Archivo_Datos.readlines()

		Archivo_Datos.seek(0)

		for i in Datos[0:1]:
			if 'Puntos' in i:
				Puntos = int(i.split(":")[-1].strip())

		for i in Datos[10:11]:
			if 'Puntos_de_Victoria' in i:
				Puntos_de_Victoria = int(i.split(":")[-1].strip())

		Puntos = Puntos + Puntaje
		Puntos_de_Victoria = Puntos_de_Victoria + 1

		self.Guardar_Estadisticas(Puntaje, True)

		Datos[0] = ("Puntos: " + str(Puntos) + "\n")
		Datos[10] = ("Puntos_de_Victoria: " + str(Puntos_de_Victoria) + "\n")

		Datos = Datos[:12]

		Archivo_Datos.writelines(Datos)

		Archivo_Datos.close()

	def Destruir(self):

		if self.Idioma == "español":
			self.BarraMenu.delete("Otros")
		elif self.Idioma == "english":
			self.BarraMenu.delete("Other")

		self.BarraMenu.delete("Color")
		self.FramePrincipal.destroy()
		self.SegundoFrame.destroy()

	def Volver(self):


		self.AtaqueBasico.grid_forget()
		self.Boton_Ataque_Bombardeo.grid_forget()
		self.Ataque_Perforador.grid_forget()
		self.AtaquesEspeciales.grid_forget()
		self.Boton_Volver.grid_forget()

		self.AnalizandoTanque.grid_forget()
		self.BotonReparacion.grid_forget()

		self.Imagen_Mi_Lado.place_forget()
		self.Imagen_Su_Lado.place_forget()

		self.Tu.grid_forget()
		self.StatsEnemigo.grid_forget()

		self.AtaqueBasico["state"] = "normal"
		self.AtaquesEspeciales["state"] = "normal"
		self.AtaqueBasico.config(cursor = "hand2")
		self.AtaquesEspeciales.config(cursor = "hand2")

		self.RecargarTodo()

		self.Tu["state"] = "normal"   					# Desactivar botones
		self.StatsEnemigo["state"] = "normal"
		self.Boton_Volver["state"] = "normal"
		self.Boton_Volver.config(cursor = "hand2")

		self.BotonAtacar.grid(row = 3, column = 0, ipadx = Redondear(76, self.DR))
		self.BotonAcciones.grid(row = 3, column = 1, ipadx = Redondear(76,self.DR))
		self.BotonStats.grid(row = 3, column = 2, ipadx = Redondear(9,self.DR))

	def PasarTurnos(self):

		if self.Yo_VidaActual > 0:

			self.TurnoActual += 1

			if self.Idioma == "español":
				self.Turnos.set("Turno " + str(self.TurnoActual) + ":")    # Cambiar turnos
			elif self.Idioma == "english":
				self.Turnos.set("Turn  " + str(self.TurnoActual) + ":")

			if self.Enfoque > 0: 
				self.Enfoque -= 1
				if self.Enfoque == 0:
					self.Enfoque_Cantidad_Label.destroy()
			if self.Recarga_Explosivo > 0:
				self.Recarga_Explosivo -= 1
			if self.Recarga_Perforador > 0:
				self.Recarga_Perforador -= 1
			if self.Recarga_Analisis > 0:
				self.Recarga_Analisis -= 1
			self.Presionado = 0
			self.Fallado = 0
			self.DañoTotal = 0
			self.Cantidad = 0
			self.Esquivado = 0

			self.RecargarTodo()

	def RecargarTodo(self):

		if self.Idioma == "español":
			self.BarraMenu.entryconfig("Otros", state="normal")
		elif self.Idioma == "english":
			self.BarraMenu.entryconfig("Other", state="normal")

		if self.Recarga_Perforador == 0:
			self.Ataque_Perforador["state"] = "normal"
			self.Ataque_Perforador.config(cursor = "hand2")

		if self.Recarga_Explosivo == 0:
			self.Ataque_Explosivo["state"] = "normal"
			self.Ataque_Explosivo.config(cursor = "hand2")

		if self.Recarga_Analisis == 0:
			self.AnalizandoTanque["state"] = "normal"
			self.AnalizandoTanque.config(cursor = "hand2")

		if self.CantidadReparacion > 0:
			self.BotonReparacion["state"] = "normal"
			self.BotonReparacion.config(cursor = "hand2")

		if self.CantidadBombardeo > 0:
			self.Boton_Ataque_Bombardeo["state"] = "normal"
			self.Boton_Ataque_Bombardeo.config(cursor = "hand2")

	def CambiarBotonesAAS(self, opcion):

		if self.Largo == 0:

			self.Largo = self.PantallaTexto.winfo_width()

		else:
			pass

		self.BotonAtacar.grid_forget()
		self.BotonAcciones.grid_forget()
		self.BotonStats.grid_forget()

		if opcion == 1:

			self.AtaqueBasico.grid(row = 3, column = 0)
			self.AtaquesEspeciales.grid(row = 3, column = 1)
			self.Boton_Volver.grid(row = 3, column = 2, sticky = "ew", columnspan = 2, ipadx = Redondear(47, self.DR))

		elif opcion == 2:

			self.AnalizandoTanque.grid(row = 3, column = 0, sticky = "ew")
			self.BotonReparacion.grid(row = 3, column =1, sticky = "ew", ipadx = Redondear(66,self.DR))
			self.Boton_Volver.grid(row = 3, column = 2, sticky = "ew", columnspan = 2, ipadx = Redondear(47, self.DR))

		elif opcion == 3:

			self.Tu.grid(row = 3, column = 0, sticky = "ew")
			self.StatsEnemigo.grid(row = 3, column = 1, sticky = "ew", ipadx = Redondear(79,self.DR))
			self.Boton_Volver.grid(row = 3, column = 2, sticky = "ew", columnspan = 2, ipadx = Redondear(47, self.DR))

			def Algo(self):

				self.DistanciaIpadx = self.Largo - self.Tu.winfo_width() - self.StatsEnemigo.winfo_width() - self.Boton_Volver.winfo_width()

				self.DistanciaIpadx = round(self.DistanciaIpadx/2)

				if self.DistanciaIpadx < 0:
					self.DistanciaIpadx = 0
				elif self.DistanciaIpadx > Redondear(135, self.DR):
					self.DistanciaIpadx = Redondear(135, self.DR)

				self.Tu.grid(ipadx = self.DistanciaIpadx)

			if self.DistanciaIpadx == -1:
				self.PantallaTexto.after(1, lambda:Algo(self))
			else:
				self.Tu.grid(ipadx = self.DistanciaIpadx)

	def CambioColor(self, Color):


		if Color == "Rojo":
			self.Color_Ataque = "#FF887A"
			self.Color_Acciones = "#FF9584"
			self.Color_Estadisticas = "#FFA99B"
			self.Color_Enemigo = "#FEC7B2"
			self.Color_Yo = "#FEC7B2"
			self.Color_Volver = "#FFA9A9"
			self.Color_Pantalla_Texto = "#FED3CB"
			self.BotonAtacar.config(bg = self.Color_Ataque)
			self.BotonAcciones.config(bg = self.Color_Acciones)
			self.BotonStats.config(bg = self.Color_Estadisticas)
			self.Boton_Volver.config(bg = self.Color_Volver)
			self.Tu.config(bg = self.Color_Volver)
			self.StatsEnemigo.config(bg = self.Color_Volver)
			self.PantallaVidaEnemigo.config(bg = self.Color_Enemigo)
			self.PantallaVida.config(bg = self.Color_Yo)
			self.PantallaTexto.config(bg = self.Color_Pantalla_Texto)

			self.AtaqueBasico.config(bg = self.Color_Ataque)
			self.AtaquesEspeciales.config(bg = self.Color_Ataque)
			self.Ataque_Perforador.config(bg = self.Color_Ataque)
			self.Ataque_Explosivo.config(bg = self.Color_Ataque)
			self.Boton_Ataque_Bombardeo.config(bg = self.Color_Ataque)
			self.Imagen_Flechas.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Yo.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Enemigo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoYo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoEnemigo.config(bg = self.Color_Pantalla_Texto)

			self.AnalizandoTanque.config(bg = self.Color_Acciones)
			self.BotonReparacion.config(bg = self.Color_Acciones)

		elif Color == "Azul":
			self.Color_Ataque = "#70D8FF"
			self.Color_Acciones = "#86DEFF"
			self.Color_Estadisticas = "#A5E6FF"
			self.Color_Enemigo = "#B2E4FE"
			self.Color_Yo = "#B2E4FE"
			self.Color_Volver = "#99F0FF"
			self.Color_Pantalla_Texto = "#CBECFE"
			self.BotonAtacar.config(bg = self.Color_Ataque)
			self.BotonAcciones.config(bg = self.Color_Acciones)
			self.BotonStats.config(bg = self.Color_Estadisticas)
			self.Boton_Volver.config(bg = self.Color_Volver)
			self.Tu.config(bg = self.Color_Volver)
			self.StatsEnemigo.config(bg = self.Color_Volver)
			self.PantallaVidaEnemigo.config(bg = self.Color_Enemigo)
			self.PantallaVida.config(bg = self.Color_Yo)
			self.PantallaTexto.config(bg = self.Color_Pantalla_Texto)

			self.AtaqueBasico.config(bg = self.Color_Ataque)
			self.AtaquesEspeciales.config(bg = self.Color_Ataque)
			self.Ataque_Perforador.config(bg = self.Color_Ataque)
			self.Ataque_Explosivo.config(bg = self.Color_Ataque)
			self.Boton_Ataque_Bombardeo.config(bg = self.Color_Ataque)
			self.Imagen_Flechas.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Yo.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Enemigo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoYo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoEnemigo.config(bg = self.Color_Pantalla_Texto)

			self.AnalizandoTanque.config(bg = self.Color_Acciones)
			self.BotonReparacion.config(bg = self.Color_Acciones)

		elif Color == "Verde":
			self.Color_Ataque = "#90FF5E"
			self.Color_Acciones = "#A1FF78"
			self.Color_Estadisticas = "#B6FF95"
			self.Color_Enemigo = "#A1FF99"
			self.Color_Yo = "#A1FF99"
			self.Color_Volver = "#A4FF99"
			self.Color_Pantalla_Texto = "#CBFECB"
			self.BotonAtacar.config(bg = self.Color_Ataque)
			self.BotonAcciones.config(bg = self.Color_Acciones)
			self.BotonStats.config(bg = self.Color_Estadisticas)
			self.Boton_Volver.config(bg = self.Color_Volver)
			self.Tu.config(bg = self.Color_Volver)
			self.StatsEnemigo.config(bg = self.Color_Volver)
			self.PantallaVidaEnemigo.config(bg = self.Color_Enemigo)
			self.PantallaVida.config(bg = self.Color_Yo)
			self.PantallaTexto.config(bg = self.Color_Pantalla_Texto)
			self.Boton_Ataque_Bombardeo.config(bg = self.Color_Ataque)

			self.AtaqueBasico.config(bg = self.Color_Ataque)
			self.AtaquesEspeciales.config(bg = self.Color_Ataque)
			self.Ataque_Perforador.config(bg = self.Color_Ataque)
			self.Ataque_Explosivo.config(bg = self.Color_Ataque)
			self.Imagen_Flechas.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Yo.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Enemigo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoYo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoEnemigo.config(bg = self.Color_Pantalla_Texto)

			self.AnalizandoTanque.config(bg = self.Color_Acciones)
			self.BotonReparacion.config(bg = self.Color_Acciones)

		elif Color == "Amarillo":
			self.Color_Ataque = "#FFFB56"
			self.Color_Acciones = "#FFFC6B"
			self.Color_Estadisticas = "#FFFC85"
			self.Color_Enemigo = "#FCFF19"
			self.Color_Yo = "#FCFF19"
			self.Color_Volver = "#FFFC99"
			self.Color_Pantalla_Texto = "#FDFECB"
			self.BotonAtacar.config(bg = self.Color_Ataque)
			self.BotonAcciones.config(bg = self.Color_Acciones)
			self.BotonStats.config(bg = self.Color_Estadisticas)
			self.Boton_Volver.config(bg = self.Color_Volver)
			self.Tu.config(bg = self.Color_Volver)
			self.StatsEnemigo.config(bg = self.Color_Volver)
			self.PantallaVidaEnemigo.config(bg = self.Color_Enemigo)
			self.PantallaVida.config(bg = self.Color_Yo)
			self.PantallaTexto.config(bg = self.Color_Pantalla_Texto)
			self.Boton_Ataque_Bombardeo.config(bg = self.Color_Ataque)

			self.AtaqueBasico.config(bg = self.Color_Ataque)
			self.AtaquesEspeciales.config(bg = self.Color_Ataque)
			self.Ataque_Perforador.config(bg = self.Color_Ataque)
			self.Ataque_Explosivo.config(bg = self.Color_Ataque)
			self.Imagen_Flechas.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Yo.config(bg = self.Color_Pantalla_Texto)
			self.Imagen_Embestida_Enemigo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoYo.config(bg = self.Color_Pantalla_Texto)
			self.LabelProgresoEnemigo.config(bg = self.Color_Pantalla_Texto)

			self.AnalizandoTanque.config(bg = self.Color_Acciones)
			self.BotonReparacion.config(bg = self.Color_Acciones)

	def PonerSonido(self, NumCanal, sonido):
		mixer.Channel(NumCanal).play(sonido)

	def QuitarSonido(self, NumCanal, tiempo):
		mixer.Channel(NumCanal).fadeout(tiempo)

	def AtacarBasico(self):

		self.N_Ataque_Basico += 1

		if self.TanqueElegido == 4:

			Daño = choice([self.Yo_Ataque + 5, self.Yo_Ataque + 6, self.Yo_Ataque + 7])

		else:

			Daño = choice([self.Yo_Ataque - 1, self.Yo_Ataque, self.Yo_Ataque + 1, self.Yo_Ataque + 2])

		Probabilidad = randint(1, 100)

		mixer.Channel(2).play(self.Sonido_Disparo_Basico)

		if Probabilidad <= self.Yo_Basico_Critico:
			Daño = round(Daño*1.25)
			if self.Idioma == "español":
				self.Texto.set("Has realizado un ataque crítico.\n")
			elif self.Idioma == "english":
				self.Texto.set("You have made a critical attack.\n")
			self.PantallaTexto.after(400, lambda:self.PonerSonido(4, self.Sonido_Disparo_Critico))
			self.PantallaTexto.after(700, lambda:self.PonerSonido(4, self.Sonido_Disparo_Critico))

		else:
			if self.Idioma == "español":
				self.Texto.set("Has realizado un ataque básico.\n")
			elif self.Idioma == "english":
				self.Texto.set("You have used a basic attack.\n")

		self.Bloquear_Botones("Basico")

		self.Imagen_Mi_Lado.config(image = self.Ataque_1)
		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))

		self.PantallaTexto.after(1000, self.DañoAlJefe, Daño, 1, 0) # Tiempo + Función + valor Daño

		self.PantallaTexto.after(3000, self.EjecutadorDelTurnoEnemigo)

	def AtacarEspecial(self):
		self.AtaqueBasico.grid_forget()  # Desaparecer el widget
		self.AtaquesEspeciales.grid_forget()
		self.Boton_Volver.grid_forget()

		self.Boton_Ataque_Bombardeo.grid(row = 3, column = 0, sticky = "nsew", ipadx = Redondear(117, self.DR))
		self.Ataque_Perforador.grid(row = 3, column = 1, ipadx = Redondear(41, self.DR), sticky = "ns")
		self.Ataque_Explosivo.grid(row = 3, column = 2, ipadx = Redondear(40, self.DR), sticky = "ns")
		self.Boton_Volver.grid(row = 3, column = 3, sticky = "ew")

	def Atacar_Bombardeo(self):
		
		self.N_Ataque_Bombardeo += 1
		self.CantidadBombardeo -= 1

		if self.Idioma == "español":
			self.Texto.set("Has pedido apoyo aéreo.\n")
		elif self.Idioma == "english":
			self.Texto.set("You have requested air support.\n")
		mixer.Channel(2).play(self.Sonido_Avion_Bombardero)

		self.Bloquear_Botones("Especiales")

		self.Imagen_Mi_Lado.config(image = self.Ataque_5)
		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))

		Posicion = choice([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85])

		self.PantallaDescripcion.grid_forget()
		self.PantallaDescripcion2.grid_forget()

		def PonerBoton(Posicion):
			self.BotonRojo.place(relx = Posicion)

		self.PantallaTexto.after(1000, PonerBoton, Posicion)

		self.PantallaTexto.after(12000, lambda:self.QuitarBoton("BotonRojo"))

		self.PantallaTexto.after(12500, lambda:self.QuitarSonido(2, 300))

		self.PantallaTexto.after(13500, self.DañoAlJefe, self.Presionado, 5, 0)

		self.PantallaTexto.after(15500, self.EjecutadorDelTurnoEnemigo)

	def Atacar_Explosivo(self):
		self.N_Ataque_Explosivo += 1
		self.Recarga_Explosivo = 3

		Daño = choice([round(self.Yo_Ataque*1.5) - 1, round(self.Yo_Ataque*1.5) , round(self.Yo_Ataque*1.5) + 1])

		if self.Idioma == "español":
			self.Texto.set("Has disparado una bala explosiva.\n")
		elif self.Idioma == "english":
			self.Texto.set("You have fired an explosive bullet.\n")

		self.Bloquear_Botones("Especiales")

		self.Imagen_Mi_Lado.config(image = self.Ataque_4)
		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))
		
		mixer.Channel(2).play(self.Sonido_Explosivo)

		Probabilidad = randint(1, 100)
		Probabilidad2 = 0

		if Probabilidad < self.Yo_Explosivo_Falla:

			self.Yo_Explosivo_Falla -= 4
			self.PantallaTexto.after(1000, self.DañoAMi, 0, self.Yo_Ataque)
			self.PantallaTexto.after(1000, self.ConfirmarLogros, 3)

		else:

			self.Yo_Explosivo_Falla += 1
			Probabilidad2 = choice([1,2,3,4])
			self.PantallaTexto.after(1000, self.DañoAlJefe, Daño, 4, Probabilidad2) # Tiempo + Función + valor Daño + Ataque_3 + probabilidad

		if Probabilidad2 >= 3:

			self.PantallaTexto.after(5000, self.EjecutadorDelTurnoEnemigo)

		else:

			self.PantallaTexto.after(3000, self.EjecutadorDelTurnoEnemigo)

	def Atacar_Perforador(self):
		self.N_Ataque_Perforador += 1
		self.Recarga_Perforador = 2

		if self.Idioma == "español":
			self.Texto.set("Has disparado una bala perforante.\n")
			Malo_str = "Malo"
			Decente_str = "Decente"
			Perfecto_str = "Perfecto"
			Disparar_str = "Disparar"

		elif self.Idioma == "english":
			self.Texto.set("You have fired an armor-piercing bullet.\n")
			Malo_str = "Bad"
			Decente_str = "Decent"
			Perfecto_str = "Perfect"
			Disparar_str = "Shoot!"

		self.Bloquear_Botones("Especiales")

		self.Imagen_Mi_Lado.config(image = self.Ataque_3)
		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))

		Largo = self.FramePrincipal.winfo_width() - Redondear(258, self.DR) - Redondear(50, self.DR)
		self.ProgresoAtaque = ttk.Progressbar(self.SegundoFrame, style = "BarraDeAtaqueEstilo.Horizontal.TProgressbar", orient = "horizontal", length = Largo, mode = "determinate")
		self.BotonDetenerBarra = tk.Button(self.SegundoFrame, text = Disparar_str, font = ("Arial", Redondear(40, self.DR)), border = Redondear(6, self.DR), command = lambda:self.Presionar_Detener(), cursor = "hand2")
		self.LabelMalo = tk.Label(self.SegundoFrame, text = Malo_str, font = ("Arial", Redondear(30, self.DR)), anchor = "center", bg = "#FFA3A3")
		self.LabelDecente = tk.Label(self.SegundoFrame, text = Decente_str, font = ("Arial", Redondear(30, self.DR)), anchor = "center", bg = "#FFF9A3")
		self.LabelPerfecto = tk.Label(self.SegundoFrame, text = Perfecto_str, font = ("Arial", Redondear(30, self.DR)), anchor = "center", bg = "#B0FFA3")
		self.LabelMalo_2 = tk.Label(self.SegundoFrame, text = Malo_str, font = ("Arial", Redondear(30, self.DR)), anchor = "center", bg = "#FFA3A3")
		self.LabelDecente_2 = tk.Label(self.SegundoFrame, text = Decente_str, font = ("Arial", Redondear(30, self.DR)), anchor = "center", bg = "#FFF9A3")

		self.ProgresoAtaque.grid(row = 0, column = 0, columnspan = 5, pady = Redondear(4, self.DR))
		self.BotonDetenerBarra.grid(row = 0, column = 5, padx = (Redondear(50, self.DR), 0), rowspan = 2)
		self.LabelMalo.grid(row = 1, column = 0, sticky = "ew", ipadx = Redondear(33, self.DR))
		self.LabelDecente.grid(row = 1, column = 1, sticky = "ew", ipadx = Redondear(1, self.DR))
		self.LabelPerfecto.grid(row = 1, column = 2, sticky = "ew", ipadx = Redondear(4, self.DR))
		self.LabelDecente_2.grid(row = 1, column = 3, sticky = "ew", ipadx = Redondear(1, self.DR))
		self.LabelMalo_2.grid(row = 1, column = 4, sticky = "ew", ipadx = Redondear(36, self.DR))

		if self.Enfoque > 0:
			self.ProgresoAtaque.start(6)
		else:
			self.ProgresoAtaque.start(5) # Mientras más bajo el valor, más rápido se mueve la barra.

		mixer.Channel(2).play(self.Sonido_Barra_Perforador)

		def CambiarColorBarra(valor):

			if valor > 100:
				self.ProgresoAtaque["value"] = 0

			elif valor >= 40 and valor <= 60: # Color Barra Verde
				self.EstiloSegundaBarra.configure("BarraDeAtaqueEstilo.Horizontal.TProgressbar", background = "#1FFC03", lightcolor = "#72FF60", darkcolor = "#21E105")

			elif valor > 20 and valor < 80: # Color Barra Amarillo
				self.EstiloSegundaBarra.configure("BarraDeAtaqueEstilo.Horizontal.TProgressbar", background = "yellow", lightcolor = "#FFEE66", darkcolor = "#F0EF13")

			elif valor >= 0  and valor <= 100: # Color Barra Rojo
				self.EstiloSegundaBarra.configure("BarraDeAtaqueEstilo.Horizontal.TProgressbar", background = "red", lightcolor = "#FF908E", darkcolor = "#DD0000")

			if self.Presionado == 1:
				self.Presionado = 0
				CalculoDaño(valor)

			else:
				self.PantallaTexto.after(5, lambda:CambiarColorBarra(self.ProgresoAtaque["value"]))

		def CalculoDaño(valor):

			Probabilidad = randint(1, 100)
			SuerteExtra = 0
			Perfora = False

			if self.TanqueElegido == 4:
				SuerteExtra = 15

			if valor >= 40 and valor <= 60: # Color Verde Perfecto
				Daño = choice([self.Yo_Ataque - 3, self.Yo_Ataque - 2, self.Yo_Ataque - 1])

				self.ConfirmarLogros(5)

				if self.Enfoque > 0 and Probabilidad <= (75 + SuerteExtra):			# 75%
					Perfora = True

				elif Probabilidad <= (50 + SuerteExtra):		# 50%
					Perfora = True

			elif valor > 20 and valor < 80: # Color Amarillo Decente
				Daño = choice([self.Yo_Ataque - 5, self.Yo_Ataque - 4, self.Yo_Ataque - 3])

				if self.Enfoque > 0 and Probabilidad <= (50 + SuerteExtra):			# 50%
					Perfora = True

				elif Probabilidad <= (25 + SuerteExtra):		# 25%
					Perfora = True

			elif valor >= 0 and valor <= 100: # Color Rojo Malo
				Daño = choice([self.Yo_Ataque - 7, self.Yo_Ataque - 6, self.Yo_Ataque - 5])

				if self.Enfoque > 0 and Probabilidad <= (25 + SuerteExtra):			# 25%
					Perfora = True

				elif Probabilidad <= (10 + SuerteExtra):		# 10%	
					Perfora = True

			if self.TanqueElegido == 2:
				Daño += 2

			self.PantallaTexto.after(1500, self.DañoAlJefe, Daño, 3, Perfora)

			if Perfora == True:

				self.PantallaTexto.after(5490, self.QuitarBoton, "DetenerBarra")
				self.PantallaTexto.after(5500, lambda:self.EjecutadorDelTurnoEnemigo())

			else:

				self.PantallaTexto.after(3490, self.QuitarBoton, "DetenerBarra")
				self.PantallaTexto.after(3500, lambda:self.EjecutadorDelTurnoEnemigo())

		self.PantallaTexto.after(5, lambda:CambiarColorBarra(self.ProgresoAtaque["value"]))

	def AnalizarTanque(self):

		self.N_Accion_Analisis += 1
		self.Recarga_Analisis = 3

		if self.Idioma == "español":
			self.Texto.set("Analizas los puntos débiles del enemigo.\n")
		elif self.Idioma == "english":
			self.Texto.set("You analyze the weak points of the enemy.\n")

		self.Bloquear_Botones("Acciones")

		mixer.Channel(2).play(self.Sonido_Analisis)
		self.Imagen_Mi_Lado.config(image = self.Accion_1)
		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))

		self.PantallaTexto.after(2000, self.Yo_Enfocar) # Tiempo + Función

		self.PantallaTexto.after(5000, self.EjecutadorDelTurnoEnemigo)

	def Reparar(self):

		self.N_Accion_Reparacion += 1
		self.CantidadReparacion -= 1
		self.Yo_Explosivo_Falla -= 1

		self.Bloquear_Botones("Acciones")

		self.Imagen_Mi_Lado.config(image = self.Accion_2)
		self.Imagen_Mi_Lado.place(x = Redondear(40, self.DR), y = Redondear(3, self.DR))
		mixer.Channel(2).play(self.Sonido_Reparacion)

		if self.TanqueElegido == 3:
			Vida = 60
			Blindaje = choice([2, 3])

		else:
			Vida = 50
			Blindaje = choice([2, 3])

		self.PantallaTexto.after(0, self.Yo_Repararme, Vida, Blindaje) # Tiempo + Función + vida recuperada + blindaje extra

		self.PantallaTexto.after(3000, self.EjecutadorDelTurnoEnemigo)

	def QuitarBoton(self, Variable):

		if Variable == "BotonRojo":
			self.BotonRojo.place_forget()

		elif Variable == "Flechas":
			self.Imagen_Flechas.place_forget()
			self.BotonIzquierda.grid_forget()
			self.BotonDerecha.grid_forget()
			self.ProgresoTemporizador.place_forget()
			self.LabelSegundos.place_forget()


		elif Variable == "DetenerBarra":
			self.LabelMalo.grid_forget()
			self.LabelDecente.grid_forget()
			self.LabelPerfecto.grid_forget()
			self.LabelDecente_2.grid_forget()
			self.LabelMalo_2.grid_forget()
			self.ProgresoAtaque.grid_forget()
			self.BotonDetenerBarra.grid_forget()
		elif Variable == "Embestida":
			self.Progreso.place_forget()
			self.LabelProgresoYo.place_forget()
			self.LabelProgresoEnemigo.place_forget()
			self.Imagen_Embestida_Yo.place_forget()
			self.Imagen_Embestida_Enemigo.place_forget()

		elif Variable == "FlechasV2":
			mixer.Channel(2).fadeout(300)
			self.BarraVertical.destroy()
			self.Fondo.destroy()

		elif Variable == "Logros":
			try:
				self.Nuevo_Logro_Label.grid_forget()
			except:
				pass

		self.SegundoFrame.config(width = Redondear(1150, self.DR), height = Redondear(265, self.DR))


	def Bloquear_Botones(self, Seleccion):
		if self.Idioma == "español":
			self.BarraMenu.entryconfig("Otros", state="disabled")
		elif self.Idioma == "english":
			self.BarraMenu.entryconfig("Other", state="disabled")

		if Seleccion == "Principal":
			self.BotonAtacar["state"] = "disabled"
			self.BotonAtacar.config(cursor = "")
			self.BotonAcciones["state"] = "disabled"
			self.BotonAcciones.config(cursor = "")
			self.BotonStats["state"] = "disabled"
			self.BotonStats.config(cursor = "")

		elif Seleccion == "Basico":
			self.AtaqueBasico["state"] = "disabled"
			self.AtaqueBasico.config(cursor = "")
			self.AtaquesEspeciales["state"] = "disabled"
			self.AtaquesEspeciales.config(cursor = "")
			self.Boton_Volver["state"] = "disabled"
			self.Boton_Volver.config(cursor = "")

		elif Seleccion == "Especiales":
			self.Boton_Ataque_Bombardeo["state"] = "disabled"
			self.Boton_Ataque_Bombardeo.config(cursor = "")
			self.Ataque_Perforador["state"] = "disabled"
			self.Ataque_Perforador.config(cursor = "")
			self.Ataque_Explosivo["state"] = "disabled"
			self.Ataque_Explosivo.config(cursor = "")
			self.Boton_Volver["state"] = "disabled"
			self.Boton_Volver.config(cursor = "")

		elif Seleccion == "Acciones":
			self.AnalizandoTanque["state"] = "disabled"
			self.AnalizandoTanque.config(cursor = "")
			self.BotonReparacion["state"] = "disabled"
			self.BotonReparacion.config(cursor = "")
			self.Boton_Volver["state"] = "disabled"
			self.Boton_Volver.config(cursor = "")

		elif Seleccion == "Estadisticas":
			self.Tu["state"] = "disabled"
			self.Tu.config(cursor = "")
			self.StatsEnemigo["state"] = "disabled"
			self.StatsEnemigo.config(cursor = "")

		self.Descripcion_Sin_Mouse(0)

	def ConfirmarLogros(self, numero):

		Archivo_Logros = open("Logros_Y_Estadisticas.txt","r+")
		Logros = Archivo_Logros.readlines()
		Archivo_Logros.seek(0)

		if numero == 1:

			for i in Logros[0:1]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[0] = ("L_Victoria_Facil: True" + "\n")

		elif numero == 2:

			for i in Logros[1:2]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[1] = ("L_Derrota_Estrategica: True" + "\n")

		elif numero == 3:

			for i in Logros[2:3]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[2] = ("L_Mala_Suerte: True" + "\n")

		elif numero == 4:

			for i in Logros[3:4]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[3] = ("L_Victoria_Media: True" + "\n")

		elif numero == 5:

			for i in Logros[4:5]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[4] = ("L_Artillero_Experimentado: True" + "\n")

		elif numero == 6:

			for i in Logros[5:6]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[5] = ("L_AntiTanque_Eficaz: True" + "\n")

		elif numero == 7:

			for i in Logros[6:7]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[6] = ("L_Victoria_Dificil: True" + "\n")

		elif numero == 8:

			for i in Logros[7:8]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[7] = ("L_Apoyo_Aereo_Superior: True" + "\n")

		elif numero == 9:

			for i in Logros[8:9]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[8] = ("L_Maniobras_Evasivas: True" + "\n")

		elif numero == 10:

			for i in Logros[10:11]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[9] = ("L_Victoria_Extrema: True" + "\n")

		elif numero == 11:

			for i in Logros[10:11]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[10] = ("L_Tecnologia_De_Punta: True" + "\n")

		elif numero == 12:

			for i in Logros[11:12]:

				Resultado = (i.split(":")[-1].strip())

				if Resultado == "False":
					Logros[11] = ("L_Comandante_De_Tanques_Veterano: True" + "\n")


		if Resultado == "False":
			self.Nuevo_Logro_Label = tk.Label(self.FramePrincipal, image = self.Nuevo_Logro_img)
			self.Nuevo_Logro_Label.grid(row = 2, column = 2, columnspan = 2)
			mixer.Channel(5).play(self.Sonido_Logros)
			self.PantallaTexto.after(4000, self.QuitarBoton, "Logros")

		Logros = Logros[:24]

		Archivo_Logros.truncate()
		Archivo_Logros.writelines(Logros)
		Archivo_Logros.close()

	def Guardar_Estadisticas(self, puntaje, Victoria = False):

		Archivo_Logros = open("Logros_Y_Estadisticas.txt","r+")
		Logros = Archivo_Logros.readlines()
		Archivo_Logros.seek(0)

		for i in Logros[12:13]:

			Resultado = int((i.split(":")[-1].strip()))

			self.Daño_Realizado += Resultado

			Logros[12] = ("Daño_Realizado: " + str(self.Daño_Realizado) + "\n")

		for i in Logros[13:14]:

			Resultado = int((i.split(":")[-1].strip()))

			self.Daño_Recibido += Resultado

			Logros[13] = ("Daño_Recibido: " + str(self.Daño_Recibido) + "\n")

		for i in Logros[14:15]:

			Resultado = int((i.split(":")[-1].strip()))

			self.Puntos = Resultado + puntaje

			Logros[14] = ("Puntos_Conseguidos: " + str(self.Puntos) + "\n")

		if Victoria == True:

			for i in Logros[15:16]:

				Resultado = int((i.split(":")[-1].strip()))

				self.Victorias = Resultado + 1

				Logros[15] = ("Victorias_Totales: " + str(self.Victorias) + "\n")

		else:

			for i in Logros[16:17]:

				Resultado = int((i.split(":")[-1].strip()))

				self.Derrotas = Resultado + 1

				Logros[16] = ("Derrotas_Totales: " + str(self.Derrotas) + "\n")

		for i in Logros[17:18]:

			Resultado = int((i.split(":")[-1].strip()))

			self.N_Ataque_Basico += Resultado

			Logros[17] = ("Ataques_Basicos_Totales: " + str(self.N_Ataque_Basico) + "\n")

		for i in Logros[18:19]:

			Resultado = int((i.split(":")[-1].strip()))

			self.N_Ataque_Bombardeo += Resultado

			Logros[18] = ("Ataques_Bombardeos_Totales: " + str(self.N_Ataque_Bombardeo) + "\n")

		for i in Logros[19:20]:

			Resultado = int((i.split(":")[-1].strip()))

			self.N_Ataque_Explosivo += Resultado

			Logros[19] = ("Ataques_Explosivos_Totales: " + str(self.N_Ataque_Explosivo) + "\n")

		for i in Logros[20:21]:

			Resultado = int((i.split(":")[-1].strip()))

			self.N_Ataque_Perforador += Resultado

			Logros[20] = ("Ataques_Perforadores_Totales: " + str(self.N_Ataque_Perforador) + "\n")

		for i in Logros[21:22]:

			Resultado = int((i.split(":")[-1].strip()))

			self.N_Accion_Analisis += Resultado

			Logros[21] = ("Acciones_Analisis_Totales: " + str(self.N_Accion_Analisis) + "\n")

		for i in Logros[22:23]:

			Resultado = int((i.split(":")[-1].strip()))

			self.N_Accion_Reparacion += Resultado

			Logros[22] = ("Acciones_Reparaciones_Totales: " + str(self.N_Accion_Reparacion) + "\n")

		Logros = Logros[:24]

		Archivo_Logros.truncate()
		Archivo_Logros.writelines(Logros)
		Archivo_Logros.close()

	# -------------------- Funciones de Descripcion

	def Descripcion_Ataque_Basico_Mouse(self, e):

		if self.AtaqueBasico["state"] == "normal":

			self.PantallaDescripcion.grid(row = 4, column = 0, columnspan = 4, pady = (Redondear(20, self.DR),0))
			self.PantallaDescripcion2.grid(row = 5, column = 0, columnspan = 4, pady = (Redondear(5, self.DR),0))

			if self.TanqueElegido == 4: # Tipo de Tanque

				if self.Enfoque > 0: # Enfoque activado

					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 5) + " a " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 8) + " de daño.")
						self.Descripcion2.set("Tienes un " + str(self.Yo_Basico_Critico) + "% de hacer un golpe crítico (" + str(round((self.Yo_Ataque + 5)*1.25) - int(self.Enemigo_Blindaje/2)) + " a " + str(round((self.Yo_Ataque + 8)*1.25) - int(self.Enemigo_Blindaje/2)) + " de daño).")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 5) + " to " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 8) + " damage.")
						self.Descripcion2.set("You have a " + str(self.Yo_Basico_Critico) + "% of making a critical hit (" + str(round((self.Yo_Ataque + 5)*1.25) - int(self.Enemigo_Blindaje/2)) + " to " + str(round((self.Yo_Ataque + 8)*1.25) - int(self.Enemigo_Blindaje/2)) + " damage).")

				else:
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 5) + " a " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 8) + " de daño.")
						self.Descripcion2.set("Tienes un " + str(self.Yo_Basico_Critico) + "% de hacer un golpe crítico (" + str(round((self.Yo_Ataque + 5)*1.25) - self.Enemigo_Blindaje) + " a " + str(round((self.Yo_Ataque + 8)*1.25) - self.Enemigo_Blindaje) + " de daño).")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 5) + " to " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 8) + " damage.")
						self.Descripcion2.set("You have a " + str(self.Yo_Basico_Critico) + "% of making a critical hit (" + str(round((self.Yo_Ataque + 5)*1.25) - self.Enemigo_Blindaje) + " to " + str(round((self.Yo_Ataque + 8)*1.25) - self.Enemigo_Blindaje) + " damage).")
			else:

				if self.Enfoque > 0:

					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 1) + " a " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 2) + " de daño.")
						self.Descripcion2.set("Tienes un " + str(self.Yo_Basico_Critico) + "% de hacer un golpe crítico (" + str(round((self.Yo_Ataque - 1)*1.25) - int(self.Enemigo_Blindaje/2)) + " a " + str(round((self.Yo_Ataque + 2)*1.25) - int(self.Enemigo_Blindaje/2)) + " de daño).")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 1) + " to " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 2) + " damage.")
						self.Descripcion2.set("You have a " + str(self.Yo_Basico_Critico) + "% of making a critical hit (" + str(round((self.Yo_Ataque - 1)*1.25) - int(self.Enemigo_Blindaje/2)) + " to " + str(round((self.Yo_Ataque + 2)*1.25) - int(self.Enemigo_Blindaje/2)) + " damage).")

				else:
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 1) + " a " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 2) + " de daño.")
						self.Descripcion2.set("Tienes un " + str(self.Yo_Basico_Critico) + "% de hacer un golpe crítico (" + str(round((self.Yo_Ataque - 1)*1.25) - self.Enemigo_Blindaje) + " a " + str(round((self.Yo_Ataque + 2)*1.25) - self.Enemigo_Blindaje) + " de daño).")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 1) + " to " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 2) + " damage.")
						self.Descripcion2.set("You have a " + str(self.Yo_Basico_Critico) + "% of making a critical hit (" + str(round((self.Yo_Ataque - 1)*1.25) - self.Enemigo_Blindaje) + " a " + str(round((self.Yo_Ataque + 2)*1.25) - self.Enemigo_Blindaje) + " damage).")

	def Descripcion_Ataque_Perforador_Mouse(self, e):  # Le pasamos un parametro porque... sí

		if self.Ataque_Perforador["state"] == "normal":

			self.PantallaDescripcion.grid(row = 4, column = 0, columnspan = 4, pady = (Redondear(20, self.DR),0))
			self.PantallaDescripcion2.grid(row = 5, column = 0, columnspan = 4, pady = (Redondear(5, self.DR),0))

			if self.TanqueElegido == 4:

				if self.Enfoque > 0:	# Enfoque activado

					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 7) + " a " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 1) + " de daño.")
						self.Descripcion2.set("40% - 65% - 90% de perforar el blindaje del enemigo.")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 7) + " to " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 1) + " damage.")
						self.Descripcion2.set("40% - 65% - 90% of piercing enemy's armor.")

				else:
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 7) + " a " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 1) + " de daño.")
						self.Descripcion2.set("25% - 40% - 65% de perforar el blindaje del enemigo.")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 7) + " to " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 1) + " damage.")
						self.Descripcion2.set("25% - 40% - 65% of piercing enemy's armor.")

			elif self.TanqueElegido == 2:

				if self.Enfoque > 0:	# Enfoque activado
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 5) + " a " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 1) + " de daño.")
						self.Descripcion2.set("25% - 50% - 75% de perforar el blindaje enemigo.")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 5) + " to " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) + 1) + " damage.")
						self.Descripcion2.set("25% - 50% - 75% of piercing enemy's armor.")

				else:
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 5) + " a " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 1) + " de daño.")
						self.Descripcion2.set("10% - 25% - 50% de perforar el blindaje enemigo.")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 5) + " to " + str(self.Yo_Ataque - self.Enemigo_Blindaje + 1) + " damage.")
						self.Descripcion2.set("10% - 25% - 50% of piercing enemy's armor.")

			else:

				if self.Enfoque > 0:	# Enfoque activado
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 7) + " a " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 1) + " de daño.")
						self.Descripcion2.set("25% - 50% - 75% de perforar el blindaje enemigo.")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 7) + " to " + str(self.Yo_Ataque - int(self.Enemigo_Blindaje/2) - 1) + " damage.")
						self.Descripcion2.set("25% - 50% - 75% of piercing enemy's armor.")

				else:
					if self.Idioma == "español":
						self.Descripcion.set("Este disparo causara entre " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 7) + " a " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 1) + " de daño.")
						self.Descripcion2.set("10% - 25% - 50% de perforar el blindaje enemigo.")
					elif self.Idioma == "english":
						self.Descripcion.set("This shot will cause between " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 7) + " to " + str(self.Yo_Ataque - self.Enemigo_Blindaje - 1) + " damage.")
						self.Descripcion2.set("10% - 25% - 50% of piercing enemy's armor.")

	def Descripcion_Ataque_Explosivo_Mouse(self, e):

		if self.Ataque_Explosivo["state"] == "normal":

			self.PantallaDescripcion.grid(row = 4, column = 0, columnspan = 4, pady = (Redondear(20, self.DR),0))
			self.PantallaDescripcion2.grid(row = 5, column = 0, columnspan = 4, pady = (Redondear(5, self.DR),0))

			if self.Enfoque > 0:	# Enfoque activado
				if self.Idioma == "español":
					self.Descripcion.set("Este disparo causara entre " + str(int(round(self.Yo_Ataque) * 1.5) - int(self.Enemigo_Blindaje/2) - 1) + " a " + str(int(round(self.Yo_Ataque) * 1.5) - int(self.Enemigo_Blindaje/2) + 1) + " de daño.")
					self.Descripcion2.set(str(self.Yo_Explosivo_Falla) + "% de fallar y explotarte a ti mismo.")
				elif self.Idioma == "english":
					self.Descripcion.set("This shot will cause between " + str(int(round(self.Yo_Ataque) * 1.5) - int(self.Enemigo_Blindaje/2) - 1) + " to " + str(int(round(self.Yo_Ataque) * 1.5) - int(self.Enemigo_Blindaje/2) + 1) + " damage.")
					self.Descripcion2.set(str(self.Yo_Explosivo_Falla) + "% of failing and exploding yourself.")

			else:
				if self.Idioma == "español":
					self.Descripcion.set("Este disparo causara entre " + str(int(round(self.Yo_Ataque) * 1.5) - self.Enemigo_Blindaje - 1) + " a " + str(int(round(self.Yo_Ataque) * 1.5) - self.Enemigo_Blindaje + 1) + " de daño.")
					self.Descripcion2.set(str(self.Yo_Explosivo_Falla) + "% de fallar y explotarte a ti mismo.")
				elif self.Idioma == "english":
					self.Descripcion.set("This shot will cause between " + str(int(round(self.Yo_Ataque) * 1.5) - self.Enemigo_Blindaje - 1) + " to " + str(int(round(self.Yo_Ataque) * 1.5) - self.Enemigo_Blindaje + 1) + " damage.")
					self.Descripcion2.set(str(self.Yo_Explosivo_Falla) + "% of failing and exploding yourself.")

	def Descripcion_Accion_Analizar(self, e):

		if self.AnalizandoTanque["state"] == "normal":
			self.PantallaDescripcion.grid(row = 4, column = 0, columnspan = 4, pady = (Redondear(20, self.DR),0))
			self.PantallaDescripcion2.grid(row = 5, column = 0, columnspan = 4, pady = (Redondear(5, self.DR),0))
			
			if self.Idioma == "español":
				self.Descripcion.set("Aumenta la precisión e ignora la mitad del blindaje del enemigo por 2 turnos.")
			elif self.Idioma == "english":
				self.Descripcion.set("Increase the accuracy and ignore half of the enemy's armor for 2 turns.")

	def Descripcion_Accion_Reparar(self, e):

		if self.BotonReparacion["state"] == "normal":

			self.PantallaDescripcion.grid(row = 4, column = 0, columnspan = 4, pady = (Redondear(20, self.DR),0))
			self.PantallaDescripcion2.grid(row = 5, column = 0, columnspan = 4, pady = (Redondear(5, self.DR),0))

			if self.CantidadReparacion == 1:
				if self.Idioma == "español":
					refuerzos_str = "1 refuerzo"
				elif self.Idioma == "english":
					refuerzos_str = "1 reinforcement"
			else:
				if self.Idioma == "español":
					refuerzos_str = str(self.CantidadReparacion) + " refuerzos"
				elif self.Idioma == "english":
					refuerzos_str = str(self.CantidadReparacion) + " reinforcements"

			if self.TanqueElegido == 3:

				if (self.Yo_VidaActual + 60) > self.Yo_Vida:
					if self.Idioma == "español":
						self.Descripcion.set("Te curas " + str(self.Yo_Vida - self.Yo_VidaActual) + " de vida" + " (" + refuerzos_str + ").")
					elif self.Idioma == "english":
						self.Descripcion.set("You recover " + str(self.Yo_Vida - self.Yo_VidaActual) + " health" + " (" + refuerzos_str + ").")
				else:
					if self.Idioma == "español":
						self.Descripcion.set("Te curas 60 de vida" + " (" + refuerzos_str + ").")
					elif self.Idioma == "english":
						self.Descripcion.set("You recover 60 health" + " (" + refuerzos_str + ").")
			else:

				if (self.Yo_VidaActual + 50) > self.Yo_Vida:
					if self.Idioma == "español":
						self.Descripcion.set("Te curas " + str(self.Yo_Vida - self.Yo_VidaActual) + " de vida" + " (" + refuerzos_str + ").")
					elif self.Idioma == "english":
						self.Descripcion.set("You recover " + str(self.Yo_Vida - self.Yo_VidaActual) + " health" + " (" + refuerzos_str + ").")
				else:
					if self.Idioma == "español":
						self.Descripcion.set("Te curas 50 de vida" + " (" + refuerzos_str + ").")
					elif self.Idioma == "english":
						self.Descripcion.set("You recover 50 health" + " (" + refuerzos_str + ").")
			
			if self.Idioma == "español":
				self.Descripcion2.set("Consigues 2 a 3 de blindaje extra.")
			elif self.Idioma == "english":
				self.Descripcion2.set("You obtain 2 to 3 extra armor.")

		else:
			pass

	def Descripcion_Ataque_Bombardeo_Mouse(self, e):

		if self.Boton_Ataque_Bombardeo["state"] == "normal":

			self.PantallaDescripcion.grid(row = 4, column = 0, columnspan = 4, pady = (Redondear(20, self.DR),0))
			self.PantallaDescripcion2.grid(row = 5, column = 0, columnspan = 4, pady = (Redondear(5, self.DR),0))

			if self.Idioma == "español":
				self.Descripcion.set(str(self.Yo_Daño_Bombardeo) + " de daño por cada click" + " (" + str(self.CantidadBombardeo) + " disponible).")
				self.Descripcion2.set("Este ataque no se ve afectado por Enfoque.")
			elif self.Idioma == "english":
				self.Descripcion.set(str(self.Yo_Daño_Bombardeo) + " damage per click" + " (" + str(self.CantidadBombardeo) + " available).")
				self.Descripcion2.set("This attack is not affected by Focus.")

		else:
			pass

	def Descripcion_Sin_Mouse(self, e):  # Le pasamos un parametro porque... sí

		self.Descripcion.set("")
		self.Descripcion2.set("")
		self.PantallaDescripcion.grid_forget()
		self.PantallaDescripcion2.grid_forget()
