import tkinter as tk
from pygame import mixer
from PIL import ImageTk, Image
from io import open as io

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

class Tienda:
	def __init__(self, DR, idioma, raiz=None):

		self.raiz = raiz
		self.DR = DR
		self.Idioma = idioma
		mixer.init()

		if idioma == "español":
			STATS_str = "STATS"
			SPECIAL_str = "SPECIAL"
			MODELO_str = "MODELO"
			VOLVER_str = "VOLVER"

		elif idioma == "english":
			STATS_str = "STATS"
			SPECIAL_str = "SPECIAL"
			MODELO_str = "DESIGN"
			VOLVER_str = "RETURN"

		self.Botones_Frame = tk.Frame(self.raiz)
		self.Botones_Frame.pack()

		self.Stats_Button = tk.Button(self.Botones_Frame, text = STATS_str, font = ('Arial',Redondear(40, self.DR)), bd = Redondear(6, self.DR), command = lambda:self.Cambiar_De_Frame(1), cursor = "hand2")
		self.Stats_Button.grid(row = 0, column = 0, padx = Redondear(10, self.DR), pady = Redondear(10, self.DR))

		self.Special_Button = tk.Button(self.Botones_Frame, text = SPECIAL_str, font = ('Arial',Redondear(40, self.DR)), bd = Redondear(6, self.DR), command = lambda:self.Cambiar_De_Frame(2), cursor = "hand2")
		self.Special_Button.grid(row = 0, column = 1, padx = Redondear(10, self.DR), pady = Redondear(10, self.DR))

		self.Modelo_Button = tk.Button(self.Botones_Frame, text = MODELO_str, font = ('Arial',Redondear(40, self.DR)), bd = Redondear(6, self.DR), command = lambda:self.Cambiar_De_Frame(3), cursor = "hand2")
		self.Modelo_Button.grid(row = 0, column = 2, padx = Redondear(10, self.DR), pady = Redondear(10, self.DR))

		self.Volver_Button = tk.Button(self.Botones_Frame, text = VOLVER_str, font = ('Arial',Redondear(40, self.DR)), bd = Redondear(6, self.DR), command = lambda:self.Destruir(), cursor = "hand2")
		self.Volver_Button.grid(row = 0, column = 3, padx = Redondear(10, self.DR), pady = Redondear(10, self.DR))

		# Imágenes

		self.Vida = AbrirImagenEX("Imagenes/Vida.png", self.DR)
		self.Daño = AbrirImagen("Imagenes/Daño.png", self.DR)
		self.Blindaje = AbrirImagenEX("Imagenes/Blindaje.png", self.DR)
		self.Mejora_No_Vida = AbrirImagenEX("Imagenes/Mejora_Vida_No_Comprada.png", self.DR)
		self.Mejora_No_Ataque = AbrirImagenEX("Imagenes/Mejora_Ataque_No_Comprada.png", self.DR)
		self.Mejora_No_Blindaje = AbrirImagenEX("Imagenes/Mejora_Blindaje_No_Comprada.png", self.DR)
		self.Mejora_Vida = AbrirImagenEX("Imagenes/Mejora_Vida_1.png", self.DR)
		self.Mejora_Ataque = AbrirImagen("Imagenes/Mejora_Ataque_1.png", self.DR)
		self.Mejora_Blindaje = AbrirImagenEX("Imagenes/Mejora_Blindaje_1.png", self.DR)
		self.Vida_Grande_img = AbrirImagenEX("Imagenes/Vida_Grande.png", self.DR)
		self.Daño_Grande_img = AbrirImagen("Imagenes/Daño_Grande.png", self.DR)
		self.Blindaje_Grande_img = AbrirImagen("Imagenes/Blindaje_Grande.png", self.DR)

		self.Mejora_Golpe_Basico_1_img = AbrirImagen("Imagenes/Mejora_Golpe_Basico_1.png", self.DR)
		self.Mejora_Golpe_Basico_2_img = AbrirImagen("Imagenes/Mejora_Golpe_Basico_2.png", self.DR)
		self.Mejora_Ataque_Explosivo_1_img = AbrirImagen("Imagenes/Mejora_Ataque_Explosivo_1.png", self.DR)
		self.Mejora_Ataque_Explosivo_2_img = AbrirImagenEX("Imagenes/Mejora_Ataque_Explosivo_2.png", self.DR)
		self.Mejora_Ataque_Bombardeo_img = AbrirImagenEX("Imagenes/Mejora_Ataque_Bombardeo.png", self.DR)
		self.Basico_Grande_img = AbrirImagen("Imagenes/Basico_Grande.png", self.DR)
		self.Explosivo_Grande_img = AbrirImagen("Imagenes/Explosivo_Grande.png", self.DR)
		self.Bombardeo_Grande_img = AbrirImagen("Imagenes/Bombardeo_Grande.png", self.DR)
		self.Mejora_No_Basico_1_img = AbrirImagenEX("Imagenes/Mejora_Golpe_Basico_1_No_Comprada.png", self.DR)
		self.Mejora_No_Basico_2_img = AbrirImagenEX("Imagenes/Mejora_Golpe_Basico_2_No_Comprada.png", self.DR)
		self.Mejora_No_Explosivo_1_img = AbrirImagenEX("Imagenes/Mejora_Ataque_Explosivo_1_No_Comprada.png", self.DR)
		self.Mejora_No_Explosivo_2_img = AbrirImagenEX("Imagenes/Mejora_Ataque_Explosivo_2_No_Comprada.png", self.DR)
		self.Mejora_No_Bombardeo_img = AbrirImagenEX("Imagenes/Mejora_Ataque_Bombardeo_No_Comprada.png", self.DR)

		self.Tanque_Destructor_Ligero_img = AbrirImagenEX("Imagenes/Tanque_Destructor_Ligero.png", self.DR)
		self.Mejora_Tanque_Destructor_Ligero_img = AbrirImagen("Imagenes/Mejora_Tanque_Destructor_Ligero.png", self.DR)
		self.Mejora_No_DL_img = AbrirImagenEX("Imagenes/Mejora_Tanque_Destructor_Ligero_No_Comprada.png", self.DR)
		self.Tanque_Mediano_img = AbrirImagenEX("Imagenes/Tanque_Mediano.png", self.DR)
		self.Mejora_Tanque_Mediano_img = AbrirImagenEX("Imagenes/Mejora_Tanque_Mediano.png", self.DR)
		self.Mejora_No_TM_img = AbrirImagenEX("Imagenes/Mejora_Tanque_Mediano_No_Comprada.png", self.DR)
		self.Tanque_X_img = AbrirImagenEX("Imagenes/Tanque_Misterioso.png", self.DR)
		self.Mejora_Tanque_X_img = AbrirImagenEX("Imagenes/Mejora_Tanque_Misterioso.png", self.DR)
		self.Mejora_No_TMisterio_img = AbrirImagenEX("Imagenes/Mejora_Tanque_Misterioso_No_Comprada.png", self.DR)
		self.Tanque_DL_Grande_img = AbrirImagen("Imagenes/Tanque_DL_Grande.png", self.DR)
		self.Tanque_M_Grande_img = AbrirImagen("Imagenes/Tanque_M_Grande.png", self.DR)
		self.Tanque_X_Grande_img = AbrirImagen("Imagenes/Tanque_X_Grande.png", self.DR)

		self.Tienda_img = AbrirImagen("Imagenes/Tienda.png", self.DR)
		self.Tienda_2_img = AbrirImagen("Imagenes/Tienda_2.png", self.DR)
		self.Tienda_3_img = AbrirImagen("Imagenes/Tienda_3.png", self.DR)
		self.Comprar_img = AbrirImagen("Imagenes/Comprar.png", self.DR)
		self.Vendido_img = AbrirImagen("Imagenes/Vendido.png", self.DR)
		self.Bloqueado_img = AbrirImagenEX("Imagenes/Bloqueado.png", self.DR)

		self.Ataque_1_img = AbrirImagen("Imagenes/Municion.png", self.DR)
		self.Ataque_4_img = AbrirImagen("Imagenes/BalaExplosiva.png", self.DR)
		self.Ataque_5_img = AbrirImagen("Imagenes/BombardeoAereo.png", self.DR)

		self.Nuevo_Logro_img = AbrirImagen("Imagenes/Nuevo_Logro.png", self.DR)

		#####

		self.Tienda_Frame = tk.Frame(self.raiz, width = 2050, height = 420, bd = Redondear(20, self.DR), relief = "groove")
		self.Stats_Tienda_Frame = tk.Frame(self.Tienda_Frame, width = 1150, height = 420)
		self.Stats_Compra_Tienda_Frame = tk.Frame(self.Tienda_Frame, width = 550, height = 420)
		self.Special_Tienda_Frame = tk.Frame(self.Tienda_Frame, width = 1150, height = 420)
		self.Special_Compra_Tienda_Frame = tk.Frame(self.Tienda_Frame, width = 550, height = 420)

		self.Modelo_Tienda_Frame = tk.Frame(self.Tienda_Frame, width = 1150, height = 420)
		self.Modelo_Destructor_Ligero_Tienda_Frame = tk.Frame(self.Modelo_Tienda_Frame, width = 1150, height = 210)
		self.Modelo_Mediano_Tienda_Frame = tk.Frame(self.Modelo_Tienda_Frame, width = 1150, height = 210)
		self.Modelo_Misterioso_Tienda_Frame = tk.Frame(self.Modelo_Tienda_Frame, width = 1150, height = 210)
		self.Modelo_Compra_Tienda_Frame = tk.Frame(self.Tienda_Frame, width = 550, height = 420)

		self.Archivo_Datos = open("Datos.txt","r+")
		self.Datos = self.Archivo_Datos.readlines()
														# La primera forma que se me ocurrio como hacer esto (Con ayuda del internet)
		for i in self.Datos[0:1]:
			if 'Puntos' in i:
				Puntos = i.split(":")[-1].strip()

		for i in self.Datos[1:2]:
			if 'Mejora_Vida' in i:
				self.Cantidad_Mejora_Vida = int(i.split(":")[-1].strip())

		for i in self.Datos[2:3]:
			if 'Mejora_Ataque' in i:
				self.Cantidad_Mejora_Ataque = int(i.split(":")[-1].strip())

		for i in self.Datos[3:4]:
			if 'Mejora_Blindaje' in i:
				self.Cantidad_Mejora_Blindaje = int(i.split(":")[-1].strip())

		for i in self.Datos[4:5]:
			if 'Mejora_Basico' in i:
				self.Cantidad_Mejora_Basico = int(i.split(":")[-1].strip())

		for i in self.Datos[5:6]:
			if 'Mejora_Explosivo' in i:
				self.Cantidad_Mejora_Explosivo = int(i.split(":")[-1].strip())

		for i in self.Datos[6:7]:
			if 'Mejora_Bombardeo' in i:
				self.Cantidad_Mejora_Bombardeo = int(i.split(":")[-1].strip())

		for i in self.Datos[7:8]:
			if 'Tanque_DL' in i:
				self.Tanque_DL = i.split(":")[-1].strip()

				if self.Tanque_DL == "True":
					self.Tanque_DL = True

		for i in self.Datos[8:9]:
			if 'Tanque_M' in i:
				self.Tanque_M = i.split(":")[-1].strip()

				if self.Tanque_M == "True":
					self.Tanque_M = True

		for i in self.Datos[9:10]:
			if 'Tanque_X' in i:
				self.Tanque_X = i.split(":")[-1].strip()

				if self.Tanque_X == "True":
					self.Tanque_X = True

		for i in self.Datos[10:11]:
			if 'Puntos_de_Victoria' in i:
				Puntos_de_Victoria = i.split(":")[-1].strip()

		self.Puntos = tk.IntVar()
		self.Puntos.set(Puntos)

		self.Puntos_de_Victoria = tk.IntVar()
		self.Puntos_de_Victoria.set(Puntos_de_Victoria)

		self.Precio = tk.IntVar()
		self.Mejora = tk.StringVar()

		self.Se_Puede_Comprar = False
		self.Cambiar_De_Frame(0)

	def Destruir(self):
		self.Archivo_Datos.close()
		self.Botones_Frame.destroy()
		self.Tienda_Frame.destroy()
		try:
			self.Nuevo_Logro_Label.destroy()
		except:
			pass

	def Mostrar_Stats_Tienda_Frame(self):

		self.Tienda_Frame.pack()

		self.Stats_Tienda_Frame.grid(row = 0, column = 0, padx = Redondear(50, self.DR), pady = Redondear(30, self.DR))

		self.Vida_label = tk.Label(self.Stats_Tienda_Frame, image = self.Vida, border = 0)
		self.Vida_label.grid(row = 0, column = 0)

		self.Daño_label = tk.Label(self.Stats_Tienda_Frame, image = self.Daño, border = 0)
		self.Daño_label.grid(row = 1, column = 0, pady = Redondear(80, self.DR))

		self.Blindaje_label = tk.Label(self.Stats_Tienda_Frame, image = self.Blindaje, border = 0)
		self.Blindaje_label.grid(row = 2, column = 0)

		self.Mejora_Vida_1_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Vida, border = 0,
			command = lambda:self.Seleccionar_Mejora("Vida", 1), cursor = "hand2")
		self.Mejora_Vida_1_Button.grid(row = 0, column = 1, padx = Redondear(10, self.DR))

		self.Mejora_Vida_2_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Vida, border = 0,
			command = lambda:self.Seleccionar_Mejora("Vida", 2), cursor = "hand2")
		self.Mejora_Vida_2_Button.grid(row = 0, column = 2)

		self.Mejora_Vida_3_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Vida, border = 0,
			command = lambda:self.Seleccionar_Mejora("Vida", 3), cursor = "hand2")
		self.Mejora_Vida_3_Button.grid(row = 0, column = 3, padx = Redondear(10, self.DR))

		self.Mejora_Ataque_1_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Ataque, border = 0,
			command = lambda:self.Seleccionar_Mejora("Ataque", 1), cursor = "hand2")
		self.Mejora_Ataque_1_Button.grid(row = 1, column = 1, padx = Redondear(10, self.DR))

		self.Mejora_Ataque_2_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Ataque, border = 0,
			command = lambda:self.Seleccionar_Mejora("Ataque", 2), cursor = "hand2")
		self.Mejora_Ataque_2_Button.grid(row = 1, column = 2)

		self.Mejora_Ataque_3_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Ataque, border = 0,
			command = lambda:self.Seleccionar_Mejora("Ataque", 3), cursor = "hand2")
		self.Mejora_Ataque_3_Button.grid(row = 1, column = 3, padx = Redondear(10, self.DR))

		self.Mejora_Blindaje_1_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Blindaje, border = 0,
			command = lambda:self.Seleccionar_Mejora("Blindaje", 1), cursor = "hand2")
		self.Mejora_Blindaje_1_Button.grid(row = 2, column = 1, padx = Redondear(10, self.DR))

		self.Mejora_Blindaje_2_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Blindaje, border = 0,
			command = lambda:self.Seleccionar_Mejora("Blindaje", 2), cursor = "hand2")
		self.Mejora_Blindaje_2_Button.grid(row = 2, column = 2, padx = Redondear(10, self.DR))

		self.Mejora_Blindaje_3_Button = tk.Button(self.Stats_Tienda_Frame, image = self.Mejora_No_Blindaje, border = 0,
			command = lambda:self.Seleccionar_Mejora("Blindaje", 3), cursor = "hand2")
		self.Mejora_Blindaje_3_Button.grid(row = 2, column = 3, padx = Redondear(10, self.DR))

		self.Stats_Compra_Tienda_Frame.grid(row = 0, column = 1, padx = (Redondear(18, self.DR),Redondear(50, self.DR)))

		self.Poner_Comprar_Frame(self.Stats_Compra_Tienda_Frame, 1)

		if self.Idioma == "español":
			self.Mejora.set("Tienda de estadísticas")
		elif self.Idioma == "english":
			self.Mejora.set("Statistics Shop")

		self.Mejorar_Label(1)

	def Poner_Comprar_Frame(self, frame, tienda):

		self.Comprar_Button = tk.Button(frame, image = self.Comprar_img,
		bd = 0, cursor = "hand2", command = lambda:self.Comprar())

		self.Imagen_Venta_label = tk.Label(frame, image = self.Tienda_img, border = 0)

		if tienda == 2:
			self.Imagen_Venta_label.config(image = self.Tienda_2_img)
		elif tienda == 3:
			self.Imagen_Venta_label.config(image = self.Tienda_3_img)

		if self.Idioma == "español":
			Precio_str = "Precio: "
			Victorias_str = "P. Victorias: "
			Puntos_str = "Puntos: "

		elif self.Idioma == "english":
			Precio_str = "Price: "
			Victorias_str = "Victory Points: "
			Puntos_str = "Points: "

		self.Precio_frame = tk.Frame(frame)

		self.Aumento_label = tk.Label(frame, textvariable = self.Mejora, font = ('Arial',Redondear(25, self.DR)), border = 0)
		self.Precio_str_label = tk.Label(self.Precio_frame, text = Precio_str, font = ('Arial',Redondear(30, self.DR)), border = 0)
		self.Precio_int_label = tk.Label(self.Precio_frame, textvariable = self.Precio, font = ('Arial',Redondear(30, self.DR)), border = 0)

		if tienda == 3:
			self.Puntuacion_str_label = tk.Label(frame, text = Victorias_str, font = ('Arial',Redondear(30, self.DR)), border = 0)
			self.Puntuacion_int_label = tk.Label(frame, textvariable = self.Puntos_de_Victoria, font = ('Arial',Redondear(30, self.DR)), border = 0)
		else:
			self.Puntuacion_str_label = tk.Label(frame, text = Puntos_str, font = ('Arial',Redondear(30, self.DR)), border = 0)
			self.Puntuacion_int_label = tk.Label(frame, textvariable = self.Puntos, font = ('Arial',Redondear(30, self.DR)), border = 0)

		self.Imagen_Venta_label.grid(row = 0, column = 0, columnspan = 2)
		self.Aumento_label.grid(row = 1, column = 0, columnspan = 2, pady = (Redondear(20, self.DR),0))
		self.Precio_frame.grid(row = 2, column = 0, columnspan = 2)

		if tienda == 3:
			self.Precio_str_label.grid(row = 0, column = 0, sticky = "we")
			self.Precio_int_label.grid(row = 0, column = 1, sticky = "e")
			self.Puntuacion_str_label.grid(row = 4, column = 0, sticky = "we")
			self.Puntuacion_int_label.grid(row = 4, column = 0, sticky = "e")

		else:

			self.Precio_str_label.grid(row = 2, column = 0, sticky = "we")
			self.Precio_int_label.grid(row = 2, column = 1, sticky = "we")
			self.Puntuacion_str_label.grid(row = 4, column = 0, sticky = "we")
			self.Puntuacion_int_label.grid(row = 4, column = 1, sticky = "we")

		self.Comprar_Button.grid(row = 3, column = 0, columnspan = 2, pady = Redondear(20, self.DR))


	def Comprar(self):

		if self.Puntos.get() == 0:
			pass

		if self.Se_Puede_Comprar == True:

			self.Archivo_Datos.seek(0)

			mixer.Channel(2).play(mixer.Sound('Musicas_Random/Buying Sound.mp3'))

			if "Puntos" in self.Puntuacion_str_label.cget("text") or (self.Idioma == "english" and not "Victory Points" in self.Puntuacion_str_label.cget("text")):

				Puntos = self.Puntos.get() - self.Precio.get()

				self.Puntos.set(Puntos)
				self.Datos[0] = ("Puntos: " + str(Puntos) + "\n")

			elif "Victorias" in self.Puntuacion_str_label.cget("text") or "Victory Points" in self.Puntuacion_str_label.cget("text"):

				Puntos_de_Victoria = self.Puntos_de_Victoria.get() - self.Precio.get()

				self.Puntos_de_Victoria.set(Puntos_de_Victoria)
				self.Datos[10] = ("Puntos_de_Victoria: " + str(Puntos_de_Victoria) + "\n")

			if "Vida" in self.Mejora.get() or "Health" in self.Mejora.get():
				if self.Precio.get() == 500:
					self.Datos[1] = ("Mejora_Vida: 1" + "\n")
					self.Cantidad_Mejora_Vida = 1
				elif self.Precio.get() == 1000:
					self.Datos[1] = ("Mejora_Vida: 2" + "\n")
					self.Cantidad_Mejora_Vida = 2
				elif self.Precio.get() == 1500:
					self.Datos[1] = ("Mejora_Vida: 3" + "\n")
					self.Cantidad_Mejora_Vida = 3

			elif "Ataque" in self.Mejora.get() or "Attack" in self.Mejora.get():
				if self.Precio.get() == 500:
					self.Datos[2] = ("Mejora_Ataque: 1" + "\n")
					self.Cantidad_Mejora_Ataque = 1
				elif self.Precio.get() == 1000:
					self.Datos[2] = ("Mejora_Ataque: 2" + "\n")
					self.Cantidad_Mejora_Ataque = 2
				elif self.Precio.get() == 1500:
					self.Datos[2] = ("Mejora_Ataque: 3" + "\n")
					self.Cantidad_Mejora_Ataque = 3

			elif "Blindaje" in self.Mejora.get() or "Armor" in self.Mejora.get():
				if self.Precio.get() == 500:
					self.Datos[3] = ("Mejora_Blindaje: 1" + "\n")
					self.Cantidad_Mejora_Blindaje = 1
				elif self.Precio.get() == 1000:
					self.Datos[3] = ("Mejora_Blindaje: 2" + "\n")
					self.Cantidad_Mejora_Blindaje = 2
				elif self.Precio.get() == 1500:
					self.Datos[3] = ("Mejora_Blindaje: 3" + "\n")
					self.Cantidad_Mejora_Blindaje = 3

			elif "Básico" in self.Mejora.get() or "Basic" in self.Mejora.get():
				if self.Precio.get() == 1000:
					self.Datos[4] = ("Mejora_Basico: 1" + "\n")
					self.Cantidad_Mejora_Basico = 1
				elif self.Precio.get() == 2000:
					self.Datos[4] = ("Mejora_Basico: 2" + "\n")
					self.Cantidad_Mejora_Basico = 2

			elif "Explosivo" in self.Mejora.get() or "Explosive" in self.Mejora.get():
				if self.Precio.get() == 500:
					self.Datos[5] = ("Mejora_Explosivo: 1" + "\n")
					self.Cantidad_Mejora_Explosivo = 1
				elif self.Precio.get() == 2500:
					self.Datos[5] = ("Mejora_Explosivo: 2" + "\n")
					self.Cantidad_Mejora_Explosivo = 2

			elif "Bombardeo" in self.Mejora.get() or "bombing" in self.Mejora.get():
				if self.Precio.get() == 2000:
					self.Datos[6] = ("Mejora_Bombardeo: 1" + "\n")
					self.Cantidad_Mejora_Bombardeo = 1

			elif "Destructor" in self.Mejora.get() or "Destroyer" in self.Mejora.get():
				if self.Precio.get() == 2:
					self.Datos[7] = ("Tanque_DL: True" + "\n")
					self.Tanque_DL = True

			elif "Mediano" in self.Mejora.get() or "Medium" in self.Mejora.get():
				if self.Precio.get() == 2:
					self.Datos[8] = ("Tanque_M: True" + "\n")
					self.Tanque_M = True

			elif "Misterioso" in self.Mejora.get() or "Mysterious" in self.Mejora.get():
				if self.Precio.get() == 2:
					self.Datos[9] = ("Tanque_X: True" + "\n")
					self.Tanque_X = True

			self.Datos = self.Datos[:12]

			self.Archivo_Datos.truncate()

			self.Archivo_Datos.writelines(self.Datos)
			self.Comprar_Button.config(image = self.Vendido_img)
			self.Se_Puede_Comprar = False

			self.Archivo_Datos.close()

			self.Archivo_Datos = open("Datos.txt","r+")

			if self.Stats_Tienda_Frame.winfo_viewable() == 1:
				self.Mejorar_Label(1)
			elif self.Special_Tienda_Frame.winfo_viewable() == 1:
				self.Mejorar_Label(2)
			elif self.Modelo_Tienda_Frame.winfo_viewable() == 1:
				self.Mejorar_Label(3)

			if self.Cantidad_Mejora_Vida == 3 and self.Cantidad_Mejora_Ataque == 3 and self.Cantidad_Mejora_Blindaje == 3:

				if self.Cantidad_Mejora_Basico == 2 and self.Cantidad_Mejora_Explosivo == 2 and self.Cantidad_Mejora_Bombardeo == 1:

					if self.Tanque_M == True and self.Tanque_X == True and self.Tanque_DL == True:

						def Quitar_Imagen_Logro(self):
							self.Nuevo_Logro_Label.pack_forget()

						self.Nuevo_Logro_Label = tk.Label(self.raiz, image = self.Nuevo_Logro_img)
						self.Nuevo_Logro_Label.pack(pady = (Redondear(10, self.DR),0))

						Archivo_Logros = open("Logros_Y_Estadisticas.txt","r+")
						Logros = Archivo_Logros.readlines()
						Archivo_Logros.seek(0)

						for i in Logros[10:11]:

							Resultado = (i.split(":")[-1].strip())

							if Resultado == "False":
								Logros[10] = ("L_Tecnologia_De_Punta: True" + "\n")

						Logros = Logros[:24]

						Archivo_Logros.truncate()
						Archivo_Logros.writelines(Logros)
						Archivo_Logros.close()
						mixer.Channel(5).play(mixer.Sound('Musicas_Random/Efecto acierto.mp3'))
						self.Tienda_Frame.after(4000, lambda:Quitar_Imagen_Logro(self))

		else:
			pass

	def Mejorar_Label(self, tienda):

		if tienda == 1:

			if self.Cantidad_Mejora_Vida > 2:
				self.Mejora_Vida_3_Button.config(image = self.Mejora_Vida)

			if self.Cantidad_Mejora_Vida > 1:
				self.Mejora_Vida_2_Button.config(image = self.Mejora_Vida)

			if self.Cantidad_Mejora_Vida > 0:
				self.Mejora_Vida_1_Button.config(image = self.Mejora_Vida)

			if self.Cantidad_Mejora_Ataque > 2:
				self.Mejora_Ataque_3_Button.config(image = self.Mejora_Ataque)

			if self.Cantidad_Mejora_Ataque > 1:
				self.Mejora_Ataque_2_Button.config(image = self.Mejora_Ataque)

			if self.Cantidad_Mejora_Ataque > 0:
				self.Mejora_Ataque_1_Button.config(image = self.Mejora_Ataque)

			if self.Cantidad_Mejora_Blindaje > 2:
				self.Mejora_Blindaje_3_Button.config(image = self.Mejora_Blindaje)

			if self.Cantidad_Mejora_Blindaje > 1:
				self.Mejora_Blindaje_2_Button.config(image = self.Mejora_Blindaje)

			if self.Cantidad_Mejora_Blindaje > 0:
				self.Mejora_Blindaje_1_Button.config(image = self.Mejora_Blindaje)

		elif tienda == 2:

			if self.Cantidad_Mejora_Basico > 1:
				self.Mejora_Basico_2_button.config(image = self.Mejora_Golpe_Basico_2_img)

			if self.Cantidad_Mejora_Basico > 0:
				self.Mejora_Basico_1_button.config(image = self.Mejora_Golpe_Basico_1_img)

			if self.Cantidad_Mejora_Explosivo > 1:
				self.Mejora_Explosivo_2_button.config(image = self.Mejora_Ataque_Explosivo_2_img)

			if self.Cantidad_Mejora_Explosivo > 0:
				self.Mejora_Explosivo_1_button.config(image = self.Mejora_Ataque_Explosivo_1_img)

			if self.Cantidad_Mejora_Bombardeo > 0:
				self.Mejora_Bombardeo_button.config(image = self.Mejora_Ataque_Bombardeo_img)

		elif tienda == 3:

			if self.Tanque_DL == True:
				self.DL_button.config(image = self.Mejora_Tanque_Destructor_Ligero_img)
			if self.Tanque_M == True:
				self.TM_button.config(image = self.Mejora_Tanque_Mediano_img)
			if self.Tanque_X == True:
				self.TMisterio_button.config(image = self.Mejora_Tanque_X_img)

	def Seleccionar_Mejora(self, tipo, nivel):

		if self.Idioma == "español":
			Vida_str = ("+5 de Vida", "+10 de Vida", "+15 de Vida")
			Ataque_str = ("+2 de Ataque", "+3 de Ataque", "+5 de Ataque")
			Blindaje_str = ("+2 de Blindaje", "+3 de Blindaje", "+5 de Blindaje")
			Basico_str = ("Básico: +15% crítico", "Básico: +25% crítico")
			Explosivo_str = ("Explosivo: 20% de fallar", "Explosivo: 10% de fallar")
			Bombardeo_str = "Bombardeo: +1 de daño"
			Destructor_str = "Destructor Ligero"
			Mediano_str = "Tanque Mediano"
			Misterioso_str = "Tanque Misterioso"

		elif self.Idioma == "english":
			Vida_str = ("+5 Health Points", "+10 Health Points", "+15 Health Points")
			Ataque_str = ("+2 Attack Points", "+3 Attack Points", "+5 Attack Points")
			Blindaje_str = ("+2 Armor Points", "+3 Armor Points", "+5 Armor Points")
			Basico_str = ("Basic: +15% Critic", "Basic: +25% Critic")
			Explosivo_str = ("Explosive: 20% Failure", "Explosive: 10% Failure")
			Bombardeo_str = "T. bombing: +1 Damage"
			Destructor_str = "Light Destroyer"
			Mediano_str = "Medium Tank"
			Misterioso_str = "Mysterious Tank"

		if tipo == "Vida":

			self.Imagen_Venta_label.config(image = self.Vida_Grande_img)

			if nivel == 1:
				self.Precio.set(500)
				self.Mejora.set(Vida_str[0])
			elif nivel == 2:
				self.Precio.set(1000)
				self.Mejora.set(Vida_str[1])
			elif nivel == 3:
				self.Precio.set(1500)
				self.Mejora.set(Vida_str[2])


			if nivel > self.Cantidad_Mejora_Vida + 1:
				self.Comprar_Button.config(image = self.Bloqueado_img)
				self.Se_Puede_Comprar = False
			elif nivel <= self.Cantidad_Mejora_Vida:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Ataque":

			self.Imagen_Venta_label.config(image = self.Daño_Grande_img)

			if nivel == 1:
				self.Precio.set(500)
				self.Mejora.set(Ataque_str[0])
			elif nivel == 2:
				self.Precio.set(1000)
				self.Mejora.set(Ataque_str[1])
			elif nivel == 3:
				self.Precio.set(1500)
				self.Mejora.set(Ataque_str[2])

			if nivel > self.Cantidad_Mejora_Ataque + 1:
				self.Comprar_Button.config(image = self.Bloqueado_img)
				self.Se_Puede_Comprar = False
			elif nivel <= self.Cantidad_Mejora_Ataque:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Blindaje":

			self.Imagen_Venta_label.config(image = self.Blindaje_Grande_img)

			if nivel == 1:
				self.Precio.set(500)
				self.Mejora.set(Blindaje_str[0])
			elif nivel == 2:
				self.Precio.set(1000)
				self.Mejora.set(Blindaje_str[1])
			elif nivel == 3:
				self.Precio.set(1500)
				self.Mejora.set(Blindaje_str[2])

			if nivel > self.Cantidad_Mejora_Blindaje + 1:
				self.Comprar_Button.config(image = self.Bloqueado_img)
				self.Se_Puede_Comprar = False
			elif nivel <= self.Cantidad_Mejora_Blindaje:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Basico":

			self.Imagen_Venta_label.config(image = self.Basico_Grande_img)

			if nivel == 1:
				self.Precio.set(1000)
				self.Mejora.set(Basico_str[0])
			elif nivel == 2:
				self.Precio.set(2000)
				self.Mejora.set(Basico_str[1])

			if nivel > self.Cantidad_Mejora_Basico + 1:
				self.Comprar_Button.config(image = self.Bloqueado_img)
				self.Se_Puede_Comprar = False
			elif nivel <= self.Cantidad_Mejora_Basico:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Explosivo":

			self.Imagen_Venta_label.config(image = self.Explosivo_Grande_img)

			if nivel == 1:
				self.Precio.set(500)
				self.Mejora.set(Explosivo_str[0])
			elif nivel == 2:
				self.Precio.set(2500)
				self.Mejora.set(Explosivo_str[1])

			if nivel > self.Cantidad_Mejora_Explosivo + 1:
				self.Comprar_Button.config(image = self.Bloqueado_img)
				self.Se_Puede_Comprar = False
			elif nivel <= self.Cantidad_Mejora_Explosivo:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Bombardeo":

			self.Imagen_Venta_label.config(image = self.Bombardeo_Grande_img)

			if nivel == 1:
				self.Precio.set(2000)
				self.Mejora.set(Bombardeo_str)

			if nivel <= self.Cantidad_Mejora_Bombardeo:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Destructor":


			self.Imagen_Venta_label.config(image = self.Tanque_DL_Grande_img)

			if nivel == 1:
				self.Precio.set(2)
				self.Mejora.set(Destructor_str)

			if self.Tanque_DL == True:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos_de_Victoria.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Mediano":


			self.Imagen_Venta_label.config(image = self.Tanque_M_Grande_img)

			if nivel == 1:
				self.Precio.set(2)
				self.Mejora.set(Mediano_str)

			if self.Tanque_M == True:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos_de_Victoria.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False

		elif tipo == "Misterioso":


			self.Imagen_Venta_label.config(image = self.Tanque_X_Grande_img)

			if nivel == 1:
				self.Precio.set(2)
				self.Mejora.set(Misterioso_str)

			if self.Tanque_X == True:
				self.Comprar_Button.config(image = self.Vendido_img)
				self.Se_Puede_Comprar = False
			else:
				self.Comprar_Button.config(image = self.Comprar_img)

				if self.Puntos_de_Victoria.get() >= self.Precio.get():
					self.Se_Puede_Comprar = True
				else:
					self.Se_Puede_Comprar = False




	def Cambiar_De_Frame(self, seleccion):

		try:
			self.Imagen_Venta_label.grid_forget()
		except:
			pass

		try:
			self.Stats_Tienda_Frame.grid_forget()
			self.Stats_Compra_Tienda_Frame.grid_forget()

		except:
			pass

		try:
			self.Special_Tienda_Frame.grid_forget()
			self.Special_Compra_Tienda_Frame.grid_forget()
		except:
			pass

		try:
			self.Modelo_Tienda_Frame.grid_forget()
			self.Modelo_Compra_Tienda_Frame.grid_forget()
		except:
			pass

		# Retraso de milisegundos para que no sé vea feo

		if seleccion == 0:
			self.Tienda_Frame.after(0, lambda:self.Mostrar_Stats_Tienda_Frame())
			self.Precio.set(0)
		elif seleccion == 1:
			self.Tienda_Frame.after(90, lambda:self.Mostrar_Stats_Tienda_Frame())
			self.Precio.set(0)
		elif seleccion == 2:
			self.Tienda_Frame.after(90, lambda:self.Mostrar_Special_Tienda_Frame())
			self.Precio.set(0)
		elif seleccion == 3:
			self.Tienda_Frame.after(90, lambda:self.Mostrar_Modelo_Tienda_Frame())
			self.Precio.set(0)
		self.Se_Puede_Comprar = False


	def Mostrar_Special_Tienda_Frame(self):

		self.Tienda_Frame.pack()

		self.Special_Tienda_Frame.grid(row = 0, column = 0, padx = Redondear(50, self.DR), pady = Redondear(30, self.DR))
		self.Special_Compra_Tienda_Frame.grid(row = 0, column = 1, padx = (Redondear(87, self.DR),Redondear(50, self.DR)))

		self.Ataque_Basico_label = tk.Label(self.Special_Tienda_Frame, image = self.Ataque_1_img)
		self.Ataque_Explosivo_label = tk.Label(self.Special_Tienda_Frame, image = self.Ataque_4_img)
		self.Ataque_Bombardeo_label = tk.Label(self.Special_Tienda_Frame, image = self.Ataque_5_img)

		self.Mejora_Basico_1_button = tk.Button(self.Special_Tienda_Frame, image = self.Mejora_No_Basico_1_img, border = 0, relief = "flat", command = lambda:self.Seleccionar_Mejora("Basico",1), cursor = "hand2")
		self.Mejora_Basico_2_button = tk.Button(self.Special_Tienda_Frame, image = self.Mejora_No_Basico_2_img, border = 0, relief = "flat", command = lambda:self.Seleccionar_Mejora("Basico",2), cursor = "hand2")
		self.Mejora_Explosivo_1_button = tk.Button(self.Special_Tienda_Frame, image = self.Mejora_No_Explosivo_1_img, border = 0, relief = "flat", command = lambda:self.Seleccionar_Mejora("Explosivo",1), cursor = "hand2")
		self.Mejora_Explosivo_2_button = tk.Button(self.Special_Tienda_Frame, image = self.Mejora_No_Explosivo_2_img, border = 0, relief = "flat", command = lambda:self.Seleccionar_Mejora("Explosivo",2), cursor = "hand2")
		self.Mejora_Bombardeo_button = tk.Button(self.Special_Tienda_Frame, image = self.Mejora_No_Bombardeo_img, border = 0, relief = "flat", command = lambda:self.Seleccionar_Mejora("Bombardeo",1), cursor = "hand2")

		self.Ataque_Basico_label.grid(row = 0, column = 0)
		self.Ataque_Explosivo_label.grid(row = 1, column = 0, pady = Redondear(44, self.DR))
		self.Ataque_Bombardeo_label.grid(row = 2, column = 0)
		self.Mejora_Basico_1_button.grid(row = 0, column = 1, padx = (Redondear(20, self.DR),Redondear(16, self.DR)))
		self.Mejora_Basico_2_button.grid(row = 0, column = 2)
		self.Mejora_Explosivo_1_button.grid(row = 1, column = 1)
		self.Mejora_Explosivo_2_button.grid(row = 1, column = 2)
		self.Mejora_Bombardeo_button.grid(row = 2, column = 1, columnspan = 2, padx = (Redondear(18, self.DR),0))

		self.Poner_Comprar_Frame(self.Special_Compra_Tienda_Frame, 2)

		if self.Idioma == "español":
			self.Mejora.set("Tienda de habilidades")
		elif self.Idioma == "english":
			self.Mejora.set("Skills Shop")

		self.Mejorar_Label(2)

	def Mostrar_Modelo_Tienda_Frame(self):

		self.Tienda_Frame.pack()

		if self.Idioma == "español":
			DL_Mejora_1_str = "+25% de Ataque"
			DL_Mejora_2_str = "-5% de Vida"
			DL_Mejora_3_str = "Perforador: +2 de Daño"

			TM_Mejora_1_str = "+10% de Vida"
			TM_Mejora_2_str = "+10% de Blindaje"
			TM_Mejora_3_str = "Curación: +10 de Vida"

			TMisterio_Mejora_1_str = "Básico: +25% crítico"
			TMisterio_Mejora_2_str = "Básico: +6 de daño"
			TMisterio_Mejora_3_str = "Perforador: +15%"

		elif self.Idioma == "english":
			DL_Mejora_1_str = "+25% Attack Points"
			DL_Mejora_2_str = "-5% Health Points"
			DL_Mejora_3_str = "Piercing: +2 Damage " # Piercing Shot

			TM_Mejora_1_str = "+10% Health Points"
			TM_Mejora_2_str = "+10% Armor Points"
			TM_Mejora_3_str = "Healing: +10 Health " # Reinforce # Espacio necesario
			
			TMisterio_Mejora_1_str = "Basic: +25% Critic"
			TMisterio_Mejora_2_str = "Basic: +6 Damage"
			TMisterio_Mejora_3_str = "Piercing: +15%"


		self.Modelo_Tienda_Frame.grid(row = 0, column = 0, pady = Redondear(28, self.DR))
		self.Modelo_Destructor_Ligero_Tienda_Frame.grid(row = 0, column = 0, padx = (Redondear(44, self.DR),Redondear(9, self.DR)))
		self.Modelo_Destructor_Ligero_Tienda_Frame.config(bg = "#DBFCC5", relief = "ridge", bd = Redondear(10, self.DR))

		self.DL_label = tk.Label(self.Modelo_Destructor_Ligero_Tienda_Frame, image = self.Tanque_Destructor_Ligero_img, bg = "#DBFCC5")
		self.DL_Mejora_1_Label = tk.Label(self.Modelo_Destructor_Ligero_Tienda_Frame, text = DL_Mejora_1_str, font = ('Arial',Redondear(20, self.DR)), bg = "#DBFCC5")
		self.DL_Mejora_2_Label = tk.Label(self.Modelo_Destructor_Ligero_Tienda_Frame, text = DL_Mejora_2_str, font = ('Arial',Redondear(20, self.DR)), bg = "#DBFCC5")
		self.DL_Mejora_3_Label = tk.Label(self.Modelo_Destructor_Ligero_Tienda_Frame, text = DL_Mejora_3_str, font = ('Arial',Redondear(20, self.DR)), bg = "#DBFCC5")

		self.DL_label.grid(row = 0, column = 0, rowspan = 3, padx = (Redondear(10, self.DR),Redondear(20, self.DR)))
		self.DL_Mejora_1_Label.grid(row = 0, column = 1, sticky = "w")
		self.DL_Mejora_2_Label.grid(row = 1, column = 1, sticky = "w")
		self.DL_Mejora_3_Label.grid(row = 2, column = 1, sticky = "w")

		self.DL_button = tk.Button(self.Modelo_Tienda_Frame, image = self.Mejora_No_DL_img, command = lambda:self.Seleccionar_Mejora("Destructor", 1), border = 0, relief = "flat", cursor = "hand2")
		self.DL_button.grid(row = 0, column = 1)

		self.Modelo_Mediano_Tienda_Frame.grid(row = 1, column = 0, padx = (Redondear(44, self.DR),Redondear(9, self.DR)), pady = Redondear(29, self.DR))
		self.Modelo_Mediano_Tienda_Frame.config(bg = "#F6FFA6", relief = "ridge", bd = Redondear(10, self.DR))

		self.TM_label = tk.Label(self.Modelo_Mediano_Tienda_Frame, image = self.Tanque_Mediano_img, bg = "#F6FFA6")
		self.TM_Mejora_1_Label = tk.Label(self.Modelo_Mediano_Tienda_Frame, text = TM_Mejora_1_str, font = ('Arial',Redondear(20, self.DR)), bg = "#F6FFA6")
		self.TM_Mejora_2_Label = tk.Label(self.Modelo_Mediano_Tienda_Frame, text = TM_Mejora_2_str, font = ('Arial',Redondear(20, self.DR)), bg = "#F6FFA6")
		self.TM_Mejora_3_Label = tk.Label(self.Modelo_Mediano_Tienda_Frame, text = TM_Mejora_3_str, font = ('Arial',Redondear(20, self.DR)), bg = "#F6FFA6")

		self.TM_label.grid(row = 0, column = 0, rowspan = 3, padx = (Redondear(10, self.DR),Redondear(20, self.DR)))
		self.TM_Mejora_1_Label.grid(row = 0, column = 1, sticky = "w")
		self.TM_Mejora_2_Label.grid(row = 1, column = 1, sticky = "w")
		self.TM_Mejora_3_Label.grid(row = 2, column = 1, sticky = "w")

		self.TM_button = tk.Button(self.Modelo_Tienda_Frame, image = self.Mejora_No_TM_img, command = lambda:self.Seleccionar_Mejora("Mediano", 1), border = 0, relief = "flat", cursor = "hand2")
		self.TM_button.grid(row = 1, column = 1)

		self.Modelo_Misterioso_Tienda_Frame.grid(row = 2, column = 0, padx = (Redondear(44, self.DR),Redondear(9, self.DR)), sticky = "ew")
		self.Modelo_Misterioso_Tienda_Frame.config(bg = "#FFEFCC", relief = "ridge", bd = Redondear(10, self.DR))

		self.TMisterio_label = tk.Label(self.Modelo_Misterioso_Tienda_Frame, image = self.Tanque_X_img, bg = "#FFEFCC")
		self.TMisterio_Mejora_1_Label = tk.Label(self.Modelo_Misterioso_Tienda_Frame, text = TMisterio_Mejora_1_str, font = ('Arial',Redondear(20, self.DR)), bg = "#FFEFCC")
		self.TMisterio_Mejora_2_Label = tk.Label(self.Modelo_Misterioso_Tienda_Frame, text = TMisterio_Mejora_2_str, font = ('Arial',Redondear(20, self.DR)), bg = "#FFEFCC")
		self.TMisterio_Mejora_3_Label = tk.Label(self.Modelo_Misterioso_Tienda_Frame, text = TMisterio_Mejora_3_str, font = ('Arial',Redondear(20, self.DR)), bg = "#FFEFCC")

		self.TMisterio_label.grid(row = 0, column = 0, rowspan = 3, padx = (Redondear(10, self.DR),Redondear(20, self.DR)))
		self.TMisterio_Mejora_1_Label.grid(row = 0, column = 1, sticky = "w")
		self.TMisterio_Mejora_2_Label.grid(row = 1, column = 1, sticky = "w")
		self.TMisterio_Mejora_3_Label.grid(row = 2, column = 1, sticky = "w")

		self.TMisterio_button = tk.Button(self.Modelo_Tienda_Frame, image = self.Mejora_No_TMisterio_img, command = lambda:self.Seleccionar_Mejora("Misterioso", 1), border = 0, relief = "flat", cursor = "hand2")
		self.TMisterio_button.grid(row = 2, column = 1)

		self.Modelo_Compra_Tienda_Frame.grid(row = 0, column = 2, padx = (Redondear(55, self.DR),Redondear(31, self.DR)), rowspan = 3)

		self.Poner_Comprar_Frame(self.Modelo_Compra_Tienda_Frame, 3)

		if self.Idioma == "español":
			self.Mejora.set("Tienda de modelos")
		elif self.Idioma == "english":
			self.Mejora.set("Designs Shop")

		self.Mejorar_Label(3)