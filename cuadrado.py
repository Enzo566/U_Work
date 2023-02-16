v=input("Ingrese el simbolo que desea ")
c=input("ingrese el el segundo simbolo")
a=int(input("ingrese el alto del cuadrado"))
b=int(input("ingrese el ancho"))

# for i in range (0,a):
#    print((" "+str(v)+" ")*b)
   
print((" "+str(c)+" ")*b)   

for i in range (0,a-2):
    print("",c,(" "+str(v)+" ")*(b-2),c)

print((" "+str(c)+" ")*b) 