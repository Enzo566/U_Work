Edad=int(input("Ingrese su edad"))
#P=int(input("Ingrese dependiendo su pais el minimo de edad para ser considera adulto "))

# if Edad >= 18:
#     print("Es mayor de edad ")
# else:
#     print("No es mayor de edad")

# if Edad < 12:
#     print("Es un niño")

# if Edad >= 13 and Edad <=17:
#     print(" Es un adolecente")

# if Edad >= 18 and Edad <=64:
#     print(" Es un adulto")

# if Edad >= 65:
#     print(" Es un adulto mayor")


# if Edad < 12:
#     print("Es un niño")
# else:
#     if Edad >= 13 and Edad <=17:
#         print("Es un adolecente")
#     else:
#         if Edad >= 18 and Edad <=64:
#             print("Es un adulto")
#         else:
#             if Edad >= 65:
#                 print("Es un adulto mayor")


if Edad < 12:
    print("La edad de ", Edad, "años le pertenece a un niño")

elif Edad >= 13 and Edad <=19:
    print("La edad de ", Edad, "años le pertenece a un adolecente")

elif Edad>= 18 and Edad <=64:
    print("La edad de ", Edad, "años le pertenece a un adulto")

elif Edad >= 65:
    print("La edad de ", Edad, "años le pertenece a un adulto mayor")