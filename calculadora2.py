

print("-----Calculadora-----")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division ")
print("5. Salir")

r=int(input("Seleccione una opcion"))

a=float(input("Ingrese el primer numero: "))
b=float(input("Ingrese el segundo numero"))

if r==1:
    Suma=a+b
    print("El resultado de la suma es de ", Suma)
elif r==2:
    Resta=a-b
    print("El resultado de la resta es de ", Resta)
elif r==3:
    Multi=a*b
    print("El resultado de la multicplicacion es de ", Multi)
elif r==4:
    if b==0:
        print("La division para cero no existe")
    else:
        Divi=a/b
        print("El resultado de la division es de ", Divi)
elif r==5:
    print("Adios")
else:
    print("opcion no valida")
