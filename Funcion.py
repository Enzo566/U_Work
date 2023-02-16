
def Suma():
    a=float(input("INGRESA NUN NUMERO: "))
    b=float(input("INGRESA UH NUMERO: "))
    S=a+b
    print(S)
#Suma()

def Resta():
    a=float(input("ingrese un numero"))
    b=float(input("ingrese un numero"))
    R=a-b
    print(R)
#Resta()

def multi():
    a=float(input("ingrese un numero"))
    b=float(input("ingrese un numero"))
    M=a*b
    print(M)
#multi()

def div():
    a=float(input("ingrese un numero"))
    b=float(input("ingrese un numero"))
    if b!=0:
        D=a/b
        print(D)
    else:
        D=print("Valor no valido")     
#div()

while True:
    print("----Menu-----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Division")
    print("5. Salir")
    t=int(input("Seleccione la operacion que desea realizar"))

    if t==1:
        Suma()
    elif t==2:
        Resta()
    elif t==3:
        multi()
    elif t==4:
        div()

    e=input("Desea continuar: Si/No: ")
    if e =="No":
        print("Ciao")
        break 
