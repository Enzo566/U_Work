i=int(input("Ingrese el primer valor"))
j=int(input("Ingrese el primer valor"))
k=int(input("Ingrese el primer valor"))

for i in range (0,i):
    print("Tabla triple de ", i+1)
    for j in range(0,j):
        print("Tabla secundaria", j+1)
        for k in range(0,k+1):
            print (i, "x" ,j ,"x", k ,"=", i*j*k)
