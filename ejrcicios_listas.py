#Llenar una lista con datos ingressados por teclado y luego eliminar los datos que se requiera 
list=[]
while True:
    print("Generador y modificar de listas ")
    print("1. Generar")
    print("2. Elinimar elementos de la lista ")
    print("3. Salir")

    t=int(input("Selecione una opcion "))
    
    if t==1:  
        longitud=int(input("ingrese la longitud de la lista "))  
        for j in range(0,longitud):
            k=input("ingrese un valor")
            list.extend([k])
        print(list)

    elif t==2:
        if list == list:
            print(" Lista vacia")
        else:
            a=input("Seleccione el valor que desea eliminar ")
            for j in range(0,longitud):
                if a in list:
                    list.remove(a)
            print(list)
    elif t==3:
        break
  
