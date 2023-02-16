


a=float(input("Ingrese el primer numero"))
b=float(input("Ingrese el segundo numero"))

print("--------Calculadora------")
print("1. Suma")
print("2. resta")
print("3. Multiplicación")
print("4. Division")

n1=int(input("Seleccione una opcion"))

if n1==1:
    Suma=a+b
    print("El resultado de la suma de los dos numeros es:", Suma)
else:
    if n1==2:
        Resta=a-b
        print("El resultado de la suma de los dos numeros es:", Resta)
    else:
        if n1==3:
            Multi=a*b
            print("El resultado de los valores es: ", Multi)
        else:
            if n1==4:
                if b==0:
                    print("La division para cero no existe")
                else:
                    Divison=a/b
                    print("El resutado de la division es de ", Divison)