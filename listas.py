#---------------Solo toma un argumento cuando queremos agregar mas de uno debes agregar mas corchetes, agegamos un solo elemto y una lista------------

# a=input("ingresa")

# my_list=["Enzo",21,"Cortesz", "Ecuatoriano"]
# my_list.append([15,25,a])
# my_list.append(["Tomas","Ana"] )
# print(my_list)

#----------extend=permite agregar lso valores de una lista a otra------------

# a=input("ingresa")
# #Puedes crear una lista vacia
# my_list=["Enzo",21,"Cortesz", "Ecuatoriano"]
# my_list.extend(a)# con corchete los inpreme indiviualmente tenlo en cuenta
# print(my_list)

#-------------remove=va a remover el primer valor que se le asigne de izquierda a derecha----------

# a=input("ingresa")

# my_list=["Enzo",21,"Cortesz", "Ecuatoriano",21]
# print(my_list)
# my_list.remove(21)
# my_list.extend(["Tomas","Ana"] )
# print(my_list)

#----------ciclo-----------------#
# list=[1,2,2,3,4,5,6,8,7,7,8,9,9,4,3]
# print(len(list))#len es la longitud de la lista 
# print(list)
# i=0
# while i<=len(list):
#     if 7 in list:
#         list.remove(7)
#     i+=1
# print(list)

#---------index(posicion)------#
# print("\n***la posicion del elemento EC en la lista")
# lista=[1,2,"EC","Carlos","Increible"]
# print(lista.index("EC"))

#-------count(cantidad de elemtos eh una lista)--------#
# print("\n contamos cuantos elementos de la lista tienen el 5")
# list=[1,5,6,4,8,5,5,4,2,5,"EC"]
# print(list.count(5))

#--------revert(invierte los elementos de la lista)
# print("\n invertir los elemntos de la lista ")
# list=[1,1,3,6,8,9,"ROW","ROW","Cortez"]
# list.reverse()
# print(list)

#------metodo para invertir sin reverse---
# print("\n ejemplo de invertir la lista")
# original_list=[1,2,3,4,5]
# print("Lista orden original: ", original_list)
# reverse_list=[]
# for value in original_list:
#     reverse_list=[value]+original_list
# print("Lista invertida: ", reverse_list)

#------pop(Toma el ultimo lelemto de la lista la imprime)---
# print("\n ejemplo cilclo while")
# b=["O","Z","N","E"]
# reverselist=[]
# while b: 
#     reverselist.append(b.pop())
#     print(reverselist) #puedes invertir dependiendo de donde este la identación


#------Ejemplo-------#
# print("\n ejemplo ciclo for coon una lista ")
# my_list=["apple","banana","cherry"]
# for index, item in enumerate(my_list):
#     print(index ,item)

#-------Ejemplo--------#
# print("obtener la suma de los numers pares de una lista ")
# my_list=[1,2,3,4,5,6,7,8,9,10]
# sum_of_events=0
# for item in my_list:
#     if item % 2== 0:
#         sum_of_events +=item
# print(sum_of_events)

#----------ejemplo--------#
# print("Obtener una nueva lista con los elementos de otra lista elevados al cuadarado ")
# my_list=[1,2,2,3,1,7,5]
# squared_list=[item**2 for item in my_list]
# print(squared_list)

#-----------Ejemplo-------#
# my_list=[1, 2, 3, 4, 5]
# number_to_find=3
# found=False
# for item in my_list:
#     if item == number_to_find:
#         found=True
#         break
# if found:
#     print(f'{number_to_find} esta en la lista') #concatenas variables
# else:
#     print(f'{number_to_find} no esta en la lista')

#-----Ejempo-----#
"Encontrar el numero mayot y menor de una lista"
my_list=[1,2,3,4,5,6,7,8,9,10]
min_item=my_list[0]
max_item=my_list[0]
for item in my_list:
    if item<min_item:
        min_item=item
    if item > max_item:
        max_item=item
print(f"menor: {min_item}, mayor {max_item}")
