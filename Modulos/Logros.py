import tkinter as tk
from PIL import ImageTk, Image
from io import open as io
import re

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

class Logros():

	def __init__(self, DR, idioma, raiz = None):

		self.Logro_No_img = AbrirImagen("Imagenes/Logro_No.png", DR)
		self.Logro_1_img = AbrirImagen("Imagenes/Logro_Victoria_Facil.png", DR)
		self.Logro_2_img = AbrirImagen("Imagenes/Logro_Derrota_Estrategica.png", DR)
		self.Logro_3_img = AbrirImagen("Imagenes/Logro_Mala_Suerte.png", DR)
		self.Logro_4_img = AbrirImagen("Imagenes/Logro_Victoria_Media.png", DR)
		self.Logro_5_img = AbrirImagen("Imagenes/Logro_Artillero_Experimentado.png", DR)
		self.Logro_6_img = AbrirImagen("Imagenes/Logro_AntiTanque_Eficaz.png", DR)
		self.Logro_7_img = AbrirImagen("Imagenes/Logro_Victoria_Dificil.png", DR)
		self.Logro_8_img = AbrirImagen("Imagenes/Logro_Apoyo_Aereo_Superior.png", DR)
		self.Logro_9_img = AbrirImagen("Imagenes/Logro_Maniobras_Evasivas.png", DR)
		self.Logro_10_img = AbrirImagen("Imagenes/Logro_Victoria_Extrema.png", DR)
		self.Logro_11_img = AbrirImagen("Imagenes/Logro_Tecnología_De_Punta.png", DR)
		self.Logro_12_img = AbrirImagen("Imagenes/Logro_Comandante_De_Tanques_Veterano.png", DR)

		self.Daño_Realizado_img = AbrirImagen("Imagenes/Estadistica_Daño_Realizado.png", DR)
		self.Daño_Recibido_img = AbrirImagenEX("Imagenes/Estadistica_Daño_Recibido.png", DR)
		self.Puntos_Conseguidos_img = AbrirImagenEX("Imagenes/Estadistica_Puntos_Conseguidos.png", DR)
		self.Victorias_img = AbrirImagen("Imagenes/Estadistica_Victorias_Totales.png", DR)
		self.Derrotas_img = AbrirImagenEX("Imagenes/Estadistica_Derrotas_Totales.png", DR)

		self.Ataque_1_img = AbrirImagen("Imagenes/Municion.png", DR)
		self.Ataque_2_img = AbrirImagen("Imagenes/PerforadorBlindaje.png", DR)
		self.Ataque_3_img = AbrirImagen("Imagenes/BalaExplosiva.png", DR)
		self.Ataque_4_img = AbrirImagen("Imagenes/BombardeoAereo.png", DR)
		self.Accion_1_img = AbrirImagen("Imagenes/AnalizandoDebilidades.png", DR)
		self.Accion_2_img = AbrirImagen("Imagenes/Reparacion.png", DR)

		self.DR = DR

		self.Idioma = idioma

		if self.Idioma == "español":
			Logros_str = "Logros"
			Logro_1_str = "¡Victoria!"
			Logro_1_desc_str = "Gana una partida en dificultad fácil."
			Logro_2_str = "¿Derrota estratégica?"
			Logro_2_desc_str = "Pierde una partida."
			Logro_3_str = "Mala suerte"
			Logro_3_desc_str = "Falla el disparo explosivo."
			Volver_str = "Volver"
			Anterior_str = "Anterior"
			Siguiente_str = "Siguiente"

		elif self.Idioma == "english":
			Logros_str = "Achievements"
			Logro_1_str = "Victory!"
			Logro_1_desc_str = "Win a game on easy difficulty."
			Logro_2_str = "Strategic defeat?"
			Logro_2_desc_str = "Lose a game."
			Logro_3_str = "Bad luck"
			Logro_3_desc_str = "Be damaged by the explosive shot."
			Volver_str = "Return"
			Anterior_str = "Previous"
			Siguiente_str = "Next"

		self.Titulo_Frame = tk.Frame(raiz, width = 2050, height = 420)
		self.Titulo_Frame.pack(pady = Redondear(20, self.DR))

		self.Logros_Frame = tk.Frame(raiz, width = 2050, height = 420, relief = "ridge", bd = Redondear(6, self.DR))
		self.Logros_Frame.pack(fill = "x", padx = Redondear(280, self.DR))

		self.Botones_Frame = tk.Frame(raiz, width = 2050, height = 420)
		self.Botones_Frame.pack(pady = Redondear(20, self.DR))

		self.Cuerpo_Frame = tk.Frame(self.Logros_Frame)

		self.Cuerpo_Frame.grid(row = 0, column = 0)

		self.Titulo_label = tk.Label(self.Titulo_Frame, text = Logros_str, font = ('Arial', Redondear(60, self.DR)))
		self.Titulo_label.pack(padx = Redondear(250, self.DR))

		self.Logro_1_img_label = tk.Label(self.Cuerpo_Frame, image = self.Logro_No_img)
		self.Logro_2_img_label = tk.Label(self.Cuerpo_Frame, image = self.Logro_No_img)
		self.Logro_3_img_label = tk.Label(self.Cuerpo_Frame, image = self.Logro_No_img)

		self.Logro_1_titulo_label = tk.Label(self.Cuerpo_Frame, text = Logro_1_str, font = ('Arial', Redondear(30, self.DR)))
		self.Logro_1_desc_label = tk.Label(self.Cuerpo_Frame, text = Logro_1_desc_str, font = ('Arial', Redondear(20, self.DR)))

		self.Logro_2_titulo_label = tk.Label(self.Cuerpo_Frame, text = Logro_2_str, font = ('Arial',Redondear(30, self.DR)))
		self.Logro_2_desc_label = tk.Label(self.Cuerpo_Frame, text = Logro_2_desc_str, font = ('Arial', Redondear(20, self.DR)))

		self.Logro_3_titulo_label = tk.Label(self.Cuerpo_Frame, text = Logro_3_str, font = ('Arial',Redondear(30, self.DR)))
		self.Logro_3_desc_label = tk.Label(self.Cuerpo_Frame, text = Logro_3_desc_str, font = ('Arial', Redondear(20, self.DR)))

		self.Volver_button = tk.Button(self.Botones_Frame, text = Volver_str, font = ("Arial", Redondear(30, self.DR)), command = lambda:self.Destruir(), bd = Redondear(6, self.DR))

		self.Anterior_button = tk.Button(self.Botones_Frame, text = Anterior_str, font = ("Arial", Redondear(30, self.DR)), command = lambda:self.CambiarPagina(self.Pagina_Actual - 1), bd = Redondear(6, self.DR))

		self.Siguiente_button = tk.Button(self.Botones_Frame, text = Siguiente_str, font = ("Arial", Redondear(30, self.DR)), command = lambda:self.CambiarPagina(self.Pagina_Actual + 1), bd = Redondear(6, self.DR))

		self.Pagina_Actual = 1

		self.Anterior_button.grid(row = 0, column = 0)
		self.Volver_button.grid(row = 0, column = 1, padx = Redondear(20, self.DR))
		self.Siguiente_button.grid(row = 0, column = 2)

		self.Archivo_Logros = open("Logros_Y_Estadisticas.txt","r")
		self.Logros = self.Archivo_Logros.readlines()

		self.Verificador_De_Logros = []
		self.Estadisticas = []

		count = 0

		for line in self.Logros[0:12]:

			for line in self.Logros[count:count + 1]:

				Resultado = (line.split(":")[-1].strip())

				if Resultado == "True":
					Resultado = True
				else:
					Resultado = False

				count += 1

				self.Verificador_De_Logros.append(Resultado)

		for line in self.Logros[12:23]:

			for line in self.Logros[count:count + 1]:

				Resultado = (line.split(":")[-1].strip())

				count += 1

				self.Estadisticas.append(Resultado)



		self.Daño_Total_Realizado_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[0], font = ('Arial',Redondear(35, self.DR)))
		self.Daño_Total_Recibido_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[1], font = ('Arial',Redondear(35, self.DR)))
		self.Puntos_Totales_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[2], font = ('Arial',Redondear(35, self.DR)))
		self.Victorias_Totales_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[3], font = ('Arial',Redondear(35, self.DR)))
		self.Derrotas_Totales_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[4], font = ('Arial',Redondear(35, self.DR)))

		if self.Idioma == "español":
			Veces_str = "veces"
			self.Daño_Total_Realizado_str = tk.Label(self.Cuerpo_Frame, text = "Daño total realizado:", font = ('Arial',Redondear(35, self.DR)), image = self.Daño_Realizado_img, compound = "left")
			self.Daño_Total_Recibido_str = tk.Label(self.Cuerpo_Frame, text = "Daño total recibido:", font = ('Arial',Redondear(35, self.DR)), image = self.Daño_Recibido_img, compound = "left")
			self.Puntos_Totales_str = tk.Label(self.Cuerpo_Frame, text = "Puntos totales:", font = ('Arial',Redondear(35, self.DR)), image = self.Puntos_Conseguidos_img, compound = "left")
			self.Victorias_Totales_str = tk.Label(self.Cuerpo_Frame, text = "Victorias totales:", font = ('Arial',Redondear(35, self.DR)), image = self.Victorias_img, compound = "left")
			self.Derrotas_Totales_str = tk.Label(self.Cuerpo_Frame, text = "Derrotas totales:", font = ('Arial',Redondear(35, self.DR)), image = self.Derrotas_img, compound = "left")

		elif self.Idioma == "english":
			Veces_str = "times"
			self.Daño_Total_Realizado_str = tk.Label(self.Cuerpo_Frame, text = "Total damage done:", font = ('Arial',Redondear(35, self.DR)), image = self.Daño_Realizado_img, compound = "left")
			self.Daño_Total_Recibido_str = tk.Label(self.Cuerpo_Frame, text = "Total damage received:", font = ('Arial',Redondear(35, self.DR)), image = self.Daño_Recibido_img, compound = "left")
			self.Puntos_Totales_str = tk.Label(self.Cuerpo_Frame, text = "Total points:", font = ('Arial',Redondear(35, self.DR)), image = self.Puntos_Conseguidos_img, compound = "left")
			self.Victorias_Totales_str = tk.Label(self.Cuerpo_Frame, text = "Total victories:", font = ('Arial',Redondear(35, self.DR)), image = self.Victorias_img, compound = "left")
			self.Derrotas_Totales_str = tk.Label(self.Cuerpo_Frame, text = "Total defeats:", font = ('Arial',Redondear(35, self.DR)), image = self.Derrotas_img, compound = "left")

		self.Cantidad_1_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[5], font = ('Arial',Redondear(60, self.DR)))
		self.Cantidad_1_str = tk.Label(self.Cuerpo_Frame, text = Veces_str, font = ('Arial',Redondear(40, self.DR)))

		self.Cantidad_2_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[8], font = ('Arial',Redondear(60, self.DR)))
		self.Cantidad_2_str = tk.Label(self.Cuerpo_Frame, text = Veces_str, font = ('Arial',Redondear(40, self.DR)))

		self.Cantidad_3_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[7], font = ('Arial',Redondear(60, self.DR)))
		self.Cantidad_3_str = tk.Label(self.Cuerpo_Frame, text = Veces_str, font = ('Arial',Redondear(40, self.DR)))

		self.Cantidad_4_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[6], font = ('Arial',Redondear(60, self.DR)))
		self.Cantidad_4_str = tk.Label(self.Cuerpo_Frame, text = Veces_str, font = ('Arial',Redondear(40, self.DR)))

		self.Cantidad_5_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[9], font = ('Arial',Redondear(60, self.DR)))
		self.Cantidad_5_str = tk.Label(self.Cuerpo_Frame, text = Veces_str, font = ('Arial',Redondear(40, self.DR)))

		self.Cantidad_6_int = tk.Label(self.Cuerpo_Frame, text = self.Estadisticas[10], font = ('Arial',Redondear(60, self.DR)))
		self.Cantidad_6_str = tk.Label(self.Cuerpo_Frame, text = Veces_str, font = ('Arial',Redondear(40, self.DR)))

		self.Imagen_1_Label = tk.Label(self.Cuerpo_Frame, image = self.Ataque_1_img)
		self.Imagen_2_Label = tk.Label(self.Cuerpo_Frame, image = self.Ataque_2_img)
		self.Imagen_3_Label = tk.Label(self.Cuerpo_Frame, image = self.Ataque_3_img)
		self.Imagen_4_Label = tk.Label(self.Cuerpo_Frame, image = self.Ataque_4_img)
		self.Imagen_5_Label = tk.Label(self.Cuerpo_Frame, image = self.Accion_1_img)
		self.Imagen_6_Label = tk.Label(self.Cuerpo_Frame, image = self.Accion_2_img)

		self.Archivo_Logros.close()

		self.CambiarPagina(0)

	def CambiarPagina(self, pagina):

		pagina_anterior = self.Pagina_Actual

		if pagina == 0:

			self.Anterior_button["state"] = "disabled"

			self.Logro_1_img_label.grid(row = 0, column = 0, rowspan = 2, pady = (Redondear(20, self.DR), Redondear(20, self.DR)), padx = Redondear(20, self.DR))
			self.Logro_2_img_label.grid(row = 2, column = 0, rowspan = 2, pady = (0, Redondear(20, self.DR)))
			self.Logro_3_img_label.grid(row = 4, column = 0, rowspan = 2, pady = (0, Redondear(20, self.DR)))

			if self.Verificador_De_Logros[0] == True:
				self.Logro_1_titulo_label.config(fg = "#3CD800")
				self.Logro_1_img_label.config(image = self.Logro_1_img)
			if self.Verificador_De_Logros[1] == True:
				self.Logro_2_titulo_label.config(fg = "#D80000")
				self.Logro_2_img_label.config(image = self.Logro_2_img)
			if self.Verificador_De_Logros[2] == True:
				self.Logro_3_titulo_label.config(fg = "#FF7000")
				self.Logro_3_img_label.config(image = self.Logro_3_img)

			self.Logro_1_titulo_label.grid(row = 0, column = 1, sticky = "w", pady = (Redondear(20, self.DR),0))
			self.Logro_1_desc_label.grid(row = 1, column = 1, sticky = "w", pady = (0, Redondear(20, self.DR)))
			self.Logro_2_titulo_label.grid(row = 2, column = 1, sticky = "w")
			self.Logro_2_desc_label.grid(row = 3, column = 1, sticky = "w", pady = (0, Redondear(20, self.DR)))
			self.Logro_3_titulo_label.grid(row = 4, column = 1, sticky = "w")
			self.Logro_3_desc_label.grid(row = 5, column = 1, sticky = "w", pady = (0, Redondear(20, self.DR)))	

		else:

			self.Pagina_Actual = pagina

			self.Logro_1_img_label.config(image = self.Logro_No_img)
			self.Logro_1_titulo_label.config(fg = "black")
			self.Logro_2_img_label.config(image = self.Logro_No_img)
			self.Logro_2_titulo_label.config(fg = "black")
			self.Logro_3_img_label.config(image = self.Logro_No_img)
			self.Logro_3_titulo_label.config(fg = "black")

			if pagina == 1:

				self.Anterior_button["state"] = "disabled"

				if self.Verificador_De_Logros[0] == True:
					self.Logro_1_titulo_label.config(fg = "#3CD800")
					self.Logro_1_img_label.config(image = self.Logro_1_img)
				if self.Verificador_De_Logros[1] == True:
					self.Logro_2_titulo_label.config(fg = "#D80000")
					self.Logro_2_img_label.config(image = self.Logro_2_img)
				if self.Verificador_De_Logros[2] == True:
					self.Logro_3_titulo_label.config(fg = "#FF7000")
					self.Logro_3_img_label.config(image = self.Logro_3_img)

				if self.Idioma == "español":
					self.Logro_1_titulo_label.config(text = "¡Victoria!")
					self.Logro_1_desc_label.config(text = "Gana una partida en dificultad fácil.")
					self.Logro_2_titulo_label.config(text = "¿Derrota estratégica?")
					self.Logro_2_desc_label.config(text = "Pierde una partida.")
					self.Logro_3_titulo_label.config(text = "Mala suerte")
					self.Logro_3_desc_label.config(text = "Falla el disparo explosivo.")

				elif self.Idioma == "english":
					self.Logro_1_titulo_label.config(text = "Victory!")
					self.Logro_1_desc_label.config(text = "Win a game on easy difficulty.")
					self.Logro_2_titulo_label.config(text = "Strategic defeat?")
					self.Logro_2_desc_label.config(text = "Lose a game.")
					self.Logro_3_titulo_label.config(text = "Bad luck")
					self.Logro_3_desc_label.config(text = "Be damaged by the explosive shot.")

			elif pagina == 2:

				self.Anterior_button["state"] = "normal"

				if self.Verificador_De_Logros[3] == True:
					self.Logro_1_titulo_label.config(fg = "#EFC300")
					self.Logro_1_img_label.config(image = self.Logro_4_img)
				if self.Verificador_De_Logros[4] == True:
					self.Logro_2_titulo_label.config(fg = "#16A1E0")
					self.Logro_2_img_label.config(image = self.Logro_5_img)
				if self.Verificador_De_Logros[5] == True:
					self.Logro_3_titulo_label.config(fg = "#0EA900")
					self.Logro_3_img_label.config(image = self.Logro_6_img)

				if self.Idioma == "español":
					self.Logro_1_titulo_label.config(text = "Estratega aficionado")
					self.Logro_1_desc_label.config(text = "Gana una partida en dificultad media.")
					self.Logro_2_titulo_label.config(text = "Artillero experimentado")
					self.Logro_2_desc_label.config(text = "Realiza un disparo perforador perfecto.")
					self.Logro_3_titulo_label.config(text = "Antitanque eficaz")
					self.Logro_3_desc_label.config(text = "Disminuye el blindaje del enemigo a 0.")

				elif self.Idioma == "english":
					self.Logro_1_titulo_label.config(text = "Amateur strategist")
					self.Logro_1_desc_label.config(text = "Win a game on medium difficulty.")
					self.Logro_2_titulo_label.config(text = "Experienced gunner")
					self.Logro_2_desc_label.config(text = "Perform a perfect piercing shot.")
					self.Logro_3_titulo_label.config(text = "Efective anti-tank")
					self.Logro_3_desc_label.config(text = "Reduce the enemy's armor to 0.")

			elif pagina == 3:

				if self.Verificador_De_Logros[6] == True:
					self.Logro_1_titulo_label.config(fg = "#EC5F0E")
					self.Logro_1_img_label.config(image = self.Logro_7_img)
				if self.Verificador_De_Logros[7] == True:
					self.Logro_2_titulo_label.config(fg = "#FF0000")
					self.Logro_2_img_label.config(image = self.Logro_8_img)
				if self.Verificador_De_Logros[8] == True:
					self.Logro_3_titulo_label.config(fg = "#838383")
					self.Logro_3_img_label.config(image = self.Logro_9_img)

				if self.Idioma == "español":
					self.Logro_1_titulo_label.config(text = "Experto en tácticas")
					self.Logro_1_desc_label.config(text = "Gana una partida en dificultad difícil.")
					self.Logro_2_titulo_label.config(text = "Apoyo aéreo superior")
					self.Logro_2_desc_label.config(text = "Presiona 20 veces o más durante el ataque bombardeo.")
					self.Logro_3_titulo_label.config(text = "Maniobras evasivas")
					self.Logro_3_desc_label.config(text = "Esquiva todas las flechas amarillas en dificultad difícil o extrema.")

				elif self.Idioma == "english":
					self.Logro_1_titulo_label.config(text = "Tactical expert")
					self.Logro_1_desc_label.config(text = "Win a game on hard difficulty.")
					self.Logro_2_titulo_label.config(text = "Superior air support")
					self.Logro_2_desc_label.config(text = "Press 20 times or more during the Tactical bombing attack.")
					self.Logro_3_titulo_label.config(text = "Evasive maneuvers")
					self.Logro_3_desc_label.config(text = "Dodge all the yellow arrows on hard or extreme difficulty.")

			elif pagina == 4:

				if pagina_anterior == 5:

					self.Titulo_label.config(text = "Logros")
				
				if self.Logro_1_img_label.winfo_viewable() == False:

					self.Daño_Total_Realizado_str.grid_forget()
					self.Daño_Total_Recibido_str.grid_forget()
					self.Puntos_Totales_str.grid_forget()
					self.Victorias_Totales_str.grid_forget()
					self.Derrotas_Totales_str.grid_forget()

					self.Daño_Total_Realizado_int.grid_forget()
					self.Daño_Total_Recibido_int.grid_forget()
					self.Puntos_Totales_int.grid_forget()
					self.Victorias_Totales_int.grid_forget()
					self.Derrotas_Totales_int.grid_forget()

					self.Logro_1_img_label.grid(row = 0, column = 0, rowspan = 2, pady = (Redondear(20, self.DR), Redondear(20, self.DR)), padx = Redondear(20, self.DR))
					self.Logro_2_img_label.grid(row = 2, column = 0, rowspan = 2, pady = (0, Redondear(20, self.DR)))
					self.Logro_3_img_label.grid(row = 4, column = 0, rowspan = 2, pady = (0, Redondear(20, self.DR)))

					self.Logro_1_titulo_label.grid(row = 0, column = 1, sticky = "w", pady = (Redondear(20, self.DR),0))
					self.Logro_1_desc_label.grid(row = 1, column = 1, sticky = "w", pady = (0, Redondear(20, self.DR)))
					self.Logro_2_titulo_label.grid(row = 2, column = 1, sticky = "w")
					self.Logro_2_desc_label.grid(row = 3, column = 1, sticky = "w", pady = (0, Redondear(20, self.DR)))
					self.Logro_3_titulo_label.grid(row = 4, column = 1, sticky = "w")
					self.Logro_3_desc_label.grid(row = 5, column = 1, sticky = "w", pady = (0, Redondear(20, self.DR)))	



				if self.Verificador_De_Logros[9] == True:
					self.Logro_1_titulo_label.config(fg = "#8A00E2")
					self.Logro_1_img_label.config(image = self.Logro_10_img)
				if self.Verificador_De_Logros[10] == True:
					self.Logro_2_titulo_label.config(fg = "#0025D4")
					self.Logro_2_img_label.config(image = self.Logro_11_img)
				if self.Verificador_De_Logros[11] == True:
					self.Logro_3_titulo_label.config(fg = "#33B100")
					self.Logro_3_img_label.config(image = self.Logro_12_img)

				if self.Idioma == "español":
					self.Logro_1_titulo_label.config(text = "Asalto final")
					self.Logro_1_desc_label.config(text = "Gana una partida en dificultad extrema.")
					self.Logro_2_titulo_label.config(text = "Tecnología de punta")
					self.Logro_2_desc_label.config(text = "Compra todo lo posible de la tienda.")
					self.Logro_3_titulo_label.config(text = "Comandante de tanques veterano")
					self.Logro_3_desc_label.config(text = "Gana una partida en dificultad extrema con el tanque básico.")

				elif self.Idioma == "english":
					self.Logro_1_titulo_label.config(text = "Final assault")
					self.Logro_1_desc_label.config(text = "Win a game on extreme difficulty.")
					self.Logro_2_titulo_label.config(text = "State-of-the-art technology")
					self.Logro_2_desc_label.config(text = "Buy all the upgrades in the shop.")
					self.Logro_3_titulo_label.config(text = "Veteran tank commander")
					self.Logro_3_desc_label.config(text = "Win a game on extreme difficulty using the basic tank.")

			elif pagina == 5:

				if pagina_anterior == 4:

					self.Logro_1_img_label.grid_forget()
					self.Logro_2_img_label.grid_forget()
					self.Logro_3_img_label.grid_forget()

					self.Logro_1_titulo_label.grid_forget()
					self.Logro_1_desc_label.grid_forget()
					self.Logro_2_titulo_label.grid_forget()
					self.Logro_2_desc_label.grid_forget()
					self.Logro_3_titulo_label.grid_forget()
					self.Logro_3_desc_label.grid_forget()

				elif pagina_anterior == 6:

					self.Imagen_1_Label.grid_forget()
					self.Imagen_2_Label.grid_forget()
					self.Imagen_3_Label.grid_forget()
					self.Imagen_4_Label.grid_forget()
					self.Imagen_5_Label.grid_forget()
					self.Imagen_6_Label.grid_forget()
					self.Cantidad_1_int.grid_forget()
					self.Cantidad_1_str.grid_forget()
					self.Cantidad_2_int.grid_forget()
					self.Cantidad_2_str.grid_forget()
					self.Cantidad_3_int.grid_forget()
					self.Cantidad_3_str.grid_forget()
					self.Cantidad_4_int.grid_forget()
					self.Cantidad_4_str.grid_forget()
					self.Cantidad_5_int.grid_forget()
					self.Cantidad_5_str.grid_forget()
					self.Cantidad_6_int.grid_forget()
					self.Cantidad_6_str.grid_forget()

				self.Siguiente_button["state"] = "normal"

				if self.Idioma == "español":
					self.Titulo_label.config(text = "Estadísticas")
				elif self.Idioma == "english":
					self.Titulo_label.config(text = "Statistics")

				self.Daño_Total_Realizado_str.grid(row = 0, column = 1, pady = (Redondear(27, self.DR),Redondear(26, self.DR)), sticky = "e", padx = (Redondear(120, self.DR),0))
				self.Daño_Total_Recibido_str.grid(row = 1, column = 1, sticky = "e")
				self.Puntos_Totales_str.grid(row = 2, column = 1, pady = (Redondear(26, self.DR),Redondear(26, self.DR)), sticky = "e")
				self.Victorias_Totales_str.grid(row = 3, column = 1, sticky = "e")
				self.Derrotas_Totales_str.grid(row = 4, column = 1, pady = (Redondear(26, self.DR),Redondear(26, self.DR)), sticky = "e")

				self.Daño_Total_Realizado_int.grid(row = 0, column = 2, pady = (Redondear(26, self.DR),Redondear(26, self.DR)), padx = (Redondear(50, self.DR),0))
				self.Daño_Total_Recibido_int.grid(row = 1, column = 2, padx = (Redondear(50, self.DR),0))
				self.Puntos_Totales_int.grid(row = 2, column = 2, pady = (Redondear(26, self.DR),Redondear(26, self.DR)), padx = (Redondear(50, self.DR),0))
				self.Victorias_Totales_int.grid(row = 3, column = 2, padx = (Redondear(50, self.DR),0))
				self.Derrotas_Totales_int.grid(row = 4, column = 2, pady = (Redondear(26, self.DR),Redondear(26, self.DR)), padx = (Redondear(50, self.DR),0))

			elif pagina == 6:

				self.Siguiente_button["state"] = "disabled"

				if self.Idioma == "español":
					self.Titulo_label.config(text = "Habilidades usadas")
				elif self.Idioma == "english":
					self.Titulo_label.config(text = "Skills used")

				self.Daño_Total_Realizado_str.grid_forget()
				self.Daño_Total_Recibido_str.grid_forget()
				self.Puntos_Totales_str.grid_forget()
				self.Victorias_Totales_str.grid_forget()
				self.Derrotas_Totales_str.grid_forget()

				self.Daño_Total_Realizado_int.grid_forget()
				self.Daño_Total_Recibido_int.grid_forget()
				self.Puntos_Totales_int.grid_forget()
				self.Victorias_Totales_int.grid_forget()
				self.Derrotas_Totales_int.grid_forget()

				self.Imagen_1_Label.grid(row = 0, column = 0, pady = (Redondear(20, self.DR),0), padx = (Redondear(80, self.DR), Redondear(20, self.DR)))
				self.Imagen_2_Label.grid(row = 1, column = 0, pady = (Redondear(20, self.DR),0), padx = (Redondear(80, self.DR), Redondear(20, self.DR)))
				self.Imagen_3_Label.grid(row = 2, column = 0, pady = (Redondear(20, self.DR),Redondear(20, self.DR)), padx = (Redondear(80, self.DR), Redondear(20, self.DR)))

				self.Cantidad_1_int.grid(row = 0, column = 1, pady = (Redondear(20, self.DR),0))
				self.Cantidad_1_str.grid(row = 0, column = 2, pady = (Redondear(36, self.DR),0))
				self.Cantidad_2_int.grid(row = 1, column = 1, pady = (Redondear(20, self.DR),0))
				self.Cantidad_2_str.grid(row = 1, column = 2, pady = (Redondear(36, self.DR),0))
				self.Cantidad_3_int.grid(row = 2, column = 1, pady = (Redondear(20, self.DR),Redondear(20, self.DR)))
				self.Cantidad_3_str.grid(row = 2, column = 2, pady = (Redondear(20, self.DR),0))

				self.Imagen_4_Label.grid(row = 0, column = 3, pady = (Redondear(20, self.DR),0), padx = (Redondear(80, self.DR), Redondear(20, self.DR)))
				self.Imagen_5_Label.grid(row = 1, column = 3, pady = (Redondear(20, self.DR),0), padx = (Redondear(80, self.DR), Redondear(20, self.DR)))
				self.Imagen_6_Label.grid(row = 2, column = 3, pady = (Redondear(20, self.DR),Redondear(20, self.DR)), padx = (Redondear(80, self.DR), Redondear(20, self.DR)))

				self.Cantidad_4_int.grid(row = 0, column = 4, pady = (Redondear(20, self.DR),0))
				self.Cantidad_4_str.grid(row = 0, column = 5, pady = (Redondear(36, self.DR),0))
				self.Cantidad_5_int.grid(row = 1, column = 4, pady = (Redondear(20, self.DR),0))
				self.Cantidad_5_str.grid(row = 1, column = 5, pady = (Redondear(36, self.DR),0))
				self.Cantidad_6_int.grid(row = 2, column = 4, pady = (Redondear(20, self.DR),Redondear(20, self.DR)))
				self.Cantidad_6_str.grid(row = 2, column = 5, pady = (Redondear(20, self.DR),0))

	def Destruir(self):
		self.Titulo_Frame.destroy()
		self.Botones_Frame.destroy()
		self.Logros_Frame.destroy()