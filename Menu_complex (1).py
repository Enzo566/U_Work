while True:
    print("1. Triangulo con orientación derecha")
    print("2. Triangulo con orientación izquierda")
    print("3. Medio diamante")
    print("4. Diamante")
    print("5. Cuadrado con simbolo interno")
    print("6. Salir")

    m=int(input("Selecione una opción: "))
    if m <1 or m>=6:
        print("Opcion no valida intenta de nuevo")
    else:
        if m==1:
            #Triangulo con orientación derecha
            a=int(input("1. Ingrese la altura de la forma"))
            s=str(input("1. Ingrese el simpbolo que desea imprimir"))
            
            for i in range(0,a+1):

                for j in range(0,a,-1):
                    print(" ",end=" ") 
                for k in range(0,i):
                    print(s,end=" ")
                print(" ")
        elif m==2:
            #Triangulo con orientación izquierda
            a=int(input("2.Ingrese la altura de la forma: "))
            s=str(input("2.Ingrese el simpbolo que desea imprimir: "))

            for i in range(a,-1,-1):
                for j in range (i):
                    print(" ", end="")
                for k in range( i, a):
                    print(s,end="")
                print("")
        elif m==3:
            #Medio diamante
            a=int(input("3. Ingrese la altura de la forma: "))
            s=str(input("3. Ingrese el simpbolo que desea imprimir: "))
            t=int((a-1)/2)
            b=int((a+1)/2)

            if a!=0:
                for i in range(0,t+1):
                    for j in range(0,a,-1):
                        print(" ",end=" ") 
                    for k in range(0,i):
                        print(s,end=" ")
                    print(" ")
                    
                for i in range(b,0,-1) :
                    for j in range(0,a,-1):
                        print(" ",end=" ") 
                    for k in range(0,i):
                        print(s,end=" ")
                    print(" ")
            else:
                print("Valor no valido")
                print("Intente denuevo")
        elif m==4:
            #Diamante
            a=int(input("4. Ingrese la altura de la forma: "))
            s=str(input("4. Ingrese el simpbolo que desea imprimir: "))
            t=int((a-1)/2)
            b=int((a+1)/2)
            if a%2!=0:

                #parte superior
                for i in range(0,t+1):
                    print(" "*(a-i),end=" ")
                    print(s*(i+i-1))
                    
                #parte inferior
                for i in range(b,-1,-1):
                    print(" "*(a-i),end=" ")
                    print(s*(i+i-1))
            else:
                print("Valor no valido, porfavor intenta denuevo")
        elif m==5:
            #Cuadrado con simbolo interno

            a=int(input("5. Ingrese la altura de la forma "))
            b=int(input("5. ingrese el ancho de la forma "))
            s=str(input("5. Ingrese el primer simpbolo "))
            r=str(input("5. ingrese el segundo simbolo "))

            print((" "+str(r)+" ")*b)   

            for i in range (0,a-2):
                print("",r,(" "+str(s)+" ")*(b-2),r)

            print((" "+str(r)+" ")*b) 
    if m==6:
        #Salir
        print("Ciao") 
        break