print("---CALCULADORA---")
print("1. Suma")
print("2. Resta")
print("3. Multiplcación")
print("4. Division")
print("5. Salir")

D=int(input("Seleccione la operacion que desea realizar"))
A=int(input("Ingrese la cantidad de tablas que desea"))
B=int(input("Inrese el tamaño de tabla que desea"))


for A in range(0,A+1):        
    print("----Tabla del ", A, "-----","\n")
    for B in range(0,B+1):
        print("  " ,A,"+", B, "=", A+B,"\n")

if D==5:
    print("Ciao")
else:
    if D==1:
        for A in range(0,A+1):
            print("----Tabla del ", A, "-----","\n")
            for B in range(0,B+1):
                print("  " ,A,"+", B, "=", A+B,"\n")
    elif D==2:
        for A in range(0,A+1):
            print("----Tabla del ", A, "-----","\n")
            for B in range(0,B+1):
                print("  " ,A,"-", B, "=", A-B,"\n")
    elif D==3:
        for A in range(0,A+1):
            print("----Tabla del ", A, "-----","\n")
            for B in range(0,B+1):
                print("  " ,A,"x", B, "=", A*B,"\n")
    if B==0:
        print("La division para cero no existe")
    else: 
        if D==4:
            for A in range(1,A+1):
                print("----Tabla del ", A, "-----","\n")
                for B in range(1,B+1):
                    print("  " ,A,"/", B, "=", A/B,"\n")