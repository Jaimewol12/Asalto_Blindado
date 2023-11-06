import tkinter as tk
from PIL import ImageTk, Image

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

class Creditos():

	def __init__(self, DR, idioma, raiz = None):

		# Imágenes

		self.DR = DR
		self.Idioma = idioma

		self.Google_img = AbrirImagen("Imagenes/Google.png", self.DR)
		self.Youtube_img = AbrirImagen("Imagenes/Youtube.png", self.DR)
		self.Yo_img = AbrirImagen("Imagenes/Yo.png", self.DR)
		self.Vicente_img = AbrirImagen("Imagenes/Vicente.png", self.DR)
		self.Pildoras_img = AbrirImagen("Imagenes/PildorasInformaticas.png", self.DR)
		self.Discord_img = AbrirImagen("Imagenes/Discord.png", self.DR)
		self.Colegio_img = AbrirImagen("Imagenes/Colegio.png", self.DR)

		if self.Idioma == "español":
			Creditos_str = "Créditos"
			Programador_str = "Programador:"
			Artista_str = "Artista gráfico:"
			Musica_str = "Musica y audio:"
			Tester_str = "Beta Tester:"
			Programador_info_str = "Jaime Sepúlveda"
			Artista_info_str = "70% Yo y 30% Internet"
			Musica_info_str = "Youtube"
			Tester_info_str = "Vicente Sepúlveda"
			Apoyo_str = "Muchas gracias Martín, Ivan, Jean, Alejandro,\nNicolás, Alonso, y todos los demás del discord."
			Profesor_str = "Gracias profesor Sebastían por hacer este electivo."
			Pildoras_str = "Muchas gracias Pildoras Informáticas por\ncrear un curso de Python en español y gratis."
			Volver_str = "Volver"
			Anterior_str = "Anterior"
			Siguiente_str = "Siguiente"

		elif self.Idioma == "english":
			Creditos_str = "Credits"
			Programador_str = "Developer:"
			Artista_str = "Graphic artist:"
			Musica_str = "Music and audio:"
			Tester_str = "Beta Tester:"
			Programador_info_str = "Jaime Sepúlveda"
			Artista_info_str = "70% Me and 30% Internet"
			Musica_info_str = "Youtube"
			Tester_info_str = "Vicente Sepúlveda"
			Apoyo_str = "Thank you very much Martín, Ivan, Jean, Alejandro,\nNicolás, Alonso, and everyone else from discord."
			Profesor_str = "Thanks Teacher Sebastían for teaching this class."
			Pildoras_str = "Thanks a lot Pildoras Informáticas for\ncreating a free Python Course in spanish."
			Volver_str = "Return"
			Anterior_str = "Previous"
			Siguiente_str = "Next"

		self.Creditos_Frame = tk.Frame(raiz, width = 2050, height = 420)
		self.Creditos_Frame.pack()

		self.Botones_Frame = tk.Frame(raiz, width = 2050, height = 420)
		self.Botones_Frame.pack()

		self.Creditos_label = tk.Label(self.Creditos_Frame, text = Creditos_str, font = ("Arial", Redondear(60, self.DR)))

		self.Creditos_Titulo_Frame = tk.Frame(self.Creditos_Frame)
		self.Programador_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#9FE7FF")
		self.Artista_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#AFFF9F")
		self.Musica_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#FFB2B2")
		self.Tester_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#FFFFB7")
		self.Apoyo_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#FFFFB7")
		self.Profesor_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#FFDA9E")
		self.Pildoras_Frame = tk.Frame(self.Creditos_Frame, relief = "ridge", bd = Redondear(4, self.DR), bg = "#C6FFBB")

		self.Creditos_Titulo_Frame.grid(row = 0, column = 0)

		self.Programador_label = tk.Label(self.Programador_Frame, text = Programador_str, font = ("Arial", Redondear(30, self.DR)), bg = "#9FE7FF")
		self.Artista_label = tk.Label(self.Artista_Frame, text = Artista_str, font = ("Arial", Redondear(30, self.DR)), bg = "#AFFF9F")
		self.Musica_label = tk.Label(self.Musica_Frame, text = Musica_str, font = ("Arial", Redondear(30, self.DR)), bg = "#FFB2B2")
		self.Tester_label = tk.Label(self.Tester_Frame, text = Tester_str, font = ("Arial", Redondear(30, self.DR)), bg = "#FFFFB7")

		self.Programador_info_label = tk.Label(self.Programador_Frame, text = Programador_info_str, font = ("Arial", Redondear(30, self.DR)), bg = "#9FE7FF")
		self.Artista_info_label = tk.Label(self.Artista_Frame, text = Artista_info_str, font = ("Arial", Redondear(30, self.DR)), bg = "#AFFF9F")
		self.Musica_info_label = tk.Label(self.Musica_Frame, text = Musica_info_str, font = ("Arial", Redondear(30, self.DR)), bg = "#FFB2B2")
		self.Tester_info_label = tk.Label(self.Tester_Frame, text = Tester_info_str, font = ("Arial", Redondear(30, self.DR)), bg = "#FFFFB7")
		self.Apoyo_info_label = tk.Label(self.Apoyo_Frame, text = Apoyo_str,
			font = ("Arial", Redondear(28, self.DR)), bg = "#FFFFB7", anchor = "center")

		self.Profesor_info_label = tk.Label(self.Profesor_Frame, text = Profesor_str, font = ("Arial", Redondear(28, self.DR)), bg = "#FFDA9E", anchor = "center")
		self.Pildoras_info_label = tk.Label(self.Pildoras_Frame, text = Pildoras_str, font = ("Arial", Redondear(28, self.DR)), bg = "#C6FFBB", anchor = "center")

		self.Volver_button = tk.Button(self.Botones_Frame, text = Volver_str, font = ("Arial", Redondear(30, self.DR)), command = lambda:self.Destruir(), bd = Redondear(6, self.DR))

		self.Anterior_button = tk.Button(self.Botones_Frame, text = Anterior_str, font = ("Arial", Redondear(30, self.DR)), command = lambda:self.CambiarPagina(1), bd = Redondear(6, self.DR))

		self.Siguiente_button = tk.Button(self.Botones_Frame, text = Siguiente_str, font = ("Arial", Redondear(30, self.DR)), command = lambda:self.CambiarPagina(2), bd = Redondear(6, self.DR))

		self.Creditos_label.grid(row = 0, column = 0, pady = (Redondear(10, self.DR),0), columnspan = 2)

		self.Creditos_Frame.after(0, lambda:self.CambiarPagina(1))

	def CambiarPagina(self, pagina):

		if pagina == 1:

			try:
				self.Apoyo_Frame.grid_forget()
				self.Profesor_Frame.grid_forget()
				self.Pildoras_Frame.grid_forget()
				self.Discord_label.grid_forget()
				self.Colegio_label.grid_forget()
				self.Pildoras_img_label.grid_forget()
			except:
				pass

			self.Anterior_button["state"] = "disabled"
			self.Siguiente_button["state"] = "normal"

			self.Programador_Frame.grid(row = 1, column = 0, pady = Redondear(20, self.DR), sticky = "ew")
			self.Artista_Frame.grid(row = 2, column = 0, sticky = "ew")
			self.Musica_Frame.grid(row = 3, column = 0, pady = Redondear(20, self.DR), sticky = "ew")
			self.Tester_Frame.grid(row = 4, column = 0, sticky = "ew")

			self.Volver_button.grid(row = 5, column = 1, pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))
			self.Anterior_button.grid(row = 5, column = 0, pady = Redondear(20, self.DR))
			self.Siguiente_button.grid(row = 5, column = 2, pady = Redondear(20, self.DR))

			self.Programador_label.grid(row = 0, column = 0, pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))
			self.Artista_label.grid(row = 0, column = 0, pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))
			self.Musica_label.grid(row = 0, column = 0, pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))
			self.Tester_label.grid(row = 0, column = 0, pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))

			self.Programador_info_label.grid(row = 0, column = 1, padx = Redondear(20, self.DR))
			self.Artista_info_label.grid(row = 0, column = 1, pady = Redondear(10, self.DR), padx = Redondear(20, self.DR))
			self.Musica_info_label.grid(row = 0, column = 1, padx = Redondear(20, self.DR))
			self.Tester_info_label.grid(row = 0, column = 1, pady = Redondear(10, self.DR), padx = (Redondear(50, self.DR),0))

			self.Yo_label = tk.Label(self.Creditos_Frame, image = self.Yo_img)
			self.Yo_label.grid(row = 1, column = 1, padx = (Redondear(20, self.DR),0))

			self.Google_label = tk.Label(self.Creditos_Frame, image = self.Google_img)
			self.Google_label.grid(row = 2, column = 1, padx = (Redondear(20, self.DR),0))

			self.Youtube_label = tk.Label(self.Creditos_Frame, image = self.Youtube_img)
			self.Youtube_label.grid(row = 3, column = 1, padx = (Redondear(20, self.DR),0))

			self.Vicente_label = tk.Label(self.Creditos_Frame, image = self.Vicente_img)
			self.Vicente_label.grid(row = 4, column = 1, padx = (Redondear(20, self.DR),0))

		else:

			self.Programador_Frame.grid_forget()
			self.Artista_Frame.grid_forget()
			self.Musica_Frame.grid_forget()
			self.Tester_Frame.grid_forget()

			self.Yo_label.grid_forget()
			self.Google_label.grid_forget()
			self.Youtube_label.grid_forget()
			self.Vicente_label.grid_forget()

			self.Anterior_button["state"] = "normal"
			self.Siguiente_button["state"] = "disabled"

			self.Apoyo_Frame.grid(row = 1, column = 0, pady = Redondear(20, self.DR), sticky = "ew")
			self.Apoyo_info_label.pack(pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))

			self.Profesor_Frame.grid(row = 2, column = 0, pady = 0, sticky = "ew")
			self.Profesor_info_label.pack(pady = Redondear(20, self.DR), padx = Redondear(20, self.DR))

			self.Pildoras_Frame.grid(row = 3, column = 0, pady = Redondear(20, self.DR), sticky = "ew")
			self.Pildoras_info_label.pack(pady = (Redondear(20, self.DR),Redondear(17, self.DR)), padx = Redondear(20, self.DR))

			self.Discord_label = tk.Label(self.Creditos_Frame, image = self.Discord_img)
			self.Discord_label.grid(row = 1, column = 1, padx = (Redondear(20, self.DR),0))

			self.Colegio_label = tk.Label(self.Creditos_Frame, image = self.Colegio_img)
			self.Colegio_label.grid(row = 2, column = 1, padx = (Redondear(20, self.DR),0))

			self.Pildoras_img_label = tk.Label(self.Creditos_Frame, image = self.Pildoras_img)
			self.Pildoras_img_label.grid(row = 3, column = 1, padx = (0,0))

	def Destruir(self):
		self.Botones_Frame.destroy()
		self.Creditos_Frame.destroy()