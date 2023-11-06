from io import open as io
from random import choice

def CalcularMisDatos(Tanque, Nombre):
	Archivo_Datos = open("Datos.txt","r")
	Datos = Archivo_Datos.readlines()

	Lista_Principal = [250, 30, 15, 10, 25, 4, Nombre] # Vida / Ataque / Blindaje / Crítico / Fallar / Bombardeo
	Lista_Principal_Maxima = (30, 10, 10, 40, -15, 1) # Mejoras al máximo
	Lista_Principal_Nivel2 = (15, 5, 5, 40, -15, 1)
	Lista_Principal_Nivel1 = (5, 2, 2, 15, -5, 1)
	Lista = []

	count = 1

	for line in Datos[1:7]:

		for line in Datos[count:count + 1]:

			Valor = int(line.split(":")[-1].strip())

			count += 1

			Lista.append(Valor)


	count = 0

	for i in range(6):

		if Lista[count] == 3:
			Lista_Principal[count] = Lista_Principal[count] + Lista_Principal_Maxima[count]
		elif Lista[count] == 2:
			Lista_Principal[count] = Lista_Principal[count] + Lista_Principal_Nivel2[count]
		elif Lista[count] == 1:
			Lista_Principal[count] = Lista_Principal[count] + Lista_Principal_Nivel1[count]

		count += 1

	if Tanque == 2: # Tanque destructor ligero

		Lista_Principal[0] = round(0.95*(Lista_Principal[0]))
		Lista_Principal[1] = round(1.25*(Lista_Principal[1]))

	elif Tanque == 3: # Tanque Mediano

		Lista_Principal[0] = round(1.1*(Lista_Principal[0]))
		Lista_Principal[2] = round(1.1*(Lista_Principal[2]))

	elif Tanque == 4: # Tanque Misterioso

		Lista_Principal[3] = (Lista_Principal[3]) + 25

	Lista_Principal.append(Tanque)
	print(Lista_Principal)

	Archivo_Datos.close()

	return(Lista_Principal)

def CalcularDatosEnemigos(Dificultad):

	Nombre = choice(["Tiger", "KV-1", "M6A1", "Super"])

	if Dificultad == 1:
		Lista_Principal = [260, 32, 16, "Panzer", Dificultad, 1] # Vida/Ataque/Blindaje/Nombre/Dificultad/Reparaciones

	elif Dificultad == 2:
		Lista_Principal = [290, 36, 20, "Panzer", Dificultad, 1]

	elif Dificultad == 3:
		Lista_Principal = [320, 40, 25, "Panzer", Dificultad, 2]

	elif Dificultad == 4:
		Lista_Principal = [350, 44, 29, "Tiger", Dificultad ,2]

	return Lista_Principal