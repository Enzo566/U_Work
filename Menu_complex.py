
print("1. Triangulo con orientación derecha")
print("2. Triangulo con orientación izquierda")
print("3. paralelo")
print("4. Diamante")
print("5. Cuadrado con simbolo interno")
print("6. Salir")

m=int(input("Selecione una opción"))

if m==1:
    a=int(input("Ingrese la altura de la forma"))
    s=str(input("Ingrese el simpbolo que desea imprimir"))
    
    for i in range(0,a):
        for j in range(0,a,-1):
            print(" ",end=" ") 
        for k in range(0,i):
            print(s,end=" ")
        print(" ")
elif m==2:
    a=int(input("2.Ingrese la altura de la forma"))
    s=str(input("2.Ingrese el simpbolo que desea imprimir"))

    for i in range(0,a):
        for j in range(i,0):
            print(s ,end=" ") 
        for k in range(0,i):
            print(" s",end=" ")
            
        print(" ")
elif m==3:
    a=int(input("Ingrese la altura de la forma"))
    s=str(input("Ingrese el simpbolo que desea imprimir"))
    
    if a!=0:
        for i in range(0,a):
            for j in range(0,a,-1):
                print(" ",end=" ") 
            for k in range(0,i):
                print(s,end=" ")
            print(" ")
            
        for i in range(a,0,-1) :
            for j in range(0,a,-1):
                print(" ",end=" ") 
            for k in range(0,i):
                print(s,end=" ")
            print(" ")
    else:
        print("Valor no valido")
        print("Intente denuevo")
elif m==4:
    a=int(input("Ingrese la altura de la forma"))
elif m==5:
    a=int(input("Ingrese la altura de la forma"))
elif m==6:
    print("Ciao")
