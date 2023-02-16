# def Cortez():
#     print("Hola Enzo como estas ")
# Cortez()

#--------------------------------#
# def funcion(nombre):
#     print("Estamos estudioando python ", nombre)
# funcion("Enzo")

#---------------------------------#
# Los argumentos se pueden pasar de dos formas.
# Argumentos posicionales: Se asoscian a los parama}etros de la misma funcion que aparecen en la definicion de la funcion.
# Argumentos Nominales: Se indica explicitamente el nombre del parametro al que se asocia el argumento de la forma: parametro=argumento.

# print("Paso de argukmento a una funcion")
# def datos(nombre,apellido):
#     print("Estamos estudiando pyton", nombre,apellido)

# datos("Enzo","Cortez") #Argumentos posicionales
# datos(nombre="Enzo",apellido="Cortez") #Argumentos nominales 

#---------------------------------#
# print("Retorno de una función")
# def are_triangulo(base,altura):
#     calc=base*altura/2
#     print(calc)
# #UNA MISMA FUNCION PUEDE TRABAJAR CON DIFERENTE VALORES 
# are_triangulo(2,4) 
# are_triangulo(5,6)

#---------------------------------#
# print("Argumentos por defecto")
# def welcome(nombre,lenguaje="pyton"):
#     print("!Bienvenido a", lenguaje, nombre + "¡") #El + hace que se imprimasin espacio a diferencia de la ,
# welcome("Enzo") #DATOS ORIGINALES
# welcome("Enzo", "JAVA") #cAMBIO DE DATOS SE REEMPLAZA EL LENGUAJE

#---------------------------------#
# print(" Pasar un argumento indetermnado")
# def  menu(*platos): #El * se usa para definir un parametro como indetermindo.
#     print("Hoy tenemos: ", end=" ")
#     for plato in platos:
#         print(plato, end=", ")
# menu("Arroz","Pizza","Pasta","Ensalada")
# print("\n")

#---------------------------------#
# **parametro: Se anteponen dos asteriscos an nombre del parametro y en la invovación de la función se pasa el 
# numero de variable de argumentos por pares nombre = valor, separados por comas.
# def contacto(**info):
#     print(" \n Datos del contacto")
#     for clave, valor in info.items():
#         print(clave, ":" ,valor)
# contacto(Nombre="Enzo", Email="enzocortez125@fmail.com")
# print("\n")

# contacto(Nombre="Enzo", Email="enzocortez125@fmail.com", Dirección="Quito/Ecuador")
# print("\n")

# #---------------------------------#
# print("Paso de argumentos por asignación")
# primer_curso=["POO II","APP"]#lISTA
# def añade_asignatura(curso,asignatura):
#     curso.append(asignatura)
# añade_asignatura(primer_curso, "REDES")
# print(primer_curso)
# print("\n")