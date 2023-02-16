while True:
    print("---CALCULADORA EN TABLA---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplcación")
    print("4. Division")
    print("5. Salir")

    k=int(input("Seleccione la operacion que desea realizar"))
    if k>=1 and k<5:
        i=int(input("ingrese el numero de tablas que desea "))
        j=int(input("ingrese el tamaño de tablas que desea "))
        if  k==1:
            for i in range(1,i+1):
                print("Tabla de sumatoria de ", i)
                for j in range (1,j+1):
                    l=i+j
                    if l%2==0:
                        print(i,"+",j,"=",i+j, " par")
                    else:
                        print(i,"+",j,"=",i+j, "inpar")
        elif k==2:
            for i in range(1,i+1):
                print("Tabla de resta del ", i)
                for j in range (1,j+1):
                    l=i-j
                    if l%2==0:
                        print(i,"-",j,"=",i-j, " par")
                    else:
                        print(i,"-",j,"=",i-j, "inpar")
        elif k==3:
            for i in range(1,i+1):
                print("Tabla de multiplicación del ", i)
                for j in range (1,j+1):
                    l=i*j
                    if l%2==0:
                        print(i,"*",j,"=",i*j, " par")
                    else:
                        print(i,"*",j,"=",i*j, "inpar")
        elif k==4:
            for i in range(1,i+1):
                print("Tabla de diviosion del ", i)
                for j in range (0,j+1):
                    if j==0:
                        print(0,"/",0,"=","La division para cero no existe")
                    else:
                        l=i/j
                        if l%2==0:
                            print(i,"/",j,"=",i/j, " par")
                        else:
                            print(i,"/",j,"=",i/j, "inpar") 
    else:
        if k==5:
            print("adios")
            break #Esto te permite cerrer el o salir del bucle
        else:
            print("Valor no valido")       
             