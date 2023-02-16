# def suma():
#     a=int(input("Ingrese el numero maximo de datos a sumar"))
#     S=0
#     i=0
#     while i < a :
#         b=float(input("Ingrese el valor del numero "))
#         S=S+b
#         i+=1
#     return(S)

def resta():
    a=int(input("Ingrese el numero maximo de datos a restar"))
    S=0
    i=0
    r=[]
    
    while i < a :
        b=float(input("Ingrese el valor del numero "))
        r.append(b)
        i+=1
        print(r)
                    #tienes que hacer que el primer digito sea positivo
    for item in r:
        if item ==0:
            S+item 
        else:
            S-=item
        
    return(S)

# def multi():
#     a=int(input("Ingrese el numero maximo de datos a multiplicar"))
#     S=0
#     i=0
#     while i < a :
#         b=float(input("Ingrese el valor del numero "))
#         S=S*b
#         i+=1
#     return(S)

# def div():
#     a=float(input("Ingrese el primer valor a dividir"))
#     b=float(input("Ingrese el segundo valor a dividir"))
    
#     if b==0:
#         return("Valor no valido")
#     else:
#         S=a/b

#     return(S)



op=resta()
print(op)