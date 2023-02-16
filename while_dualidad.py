i=int(input("ingrese el rango de valores que desea"))
j=int(input("ingrese el rango de valores que desea"))

ini=i
end=j
# while i<j:
#     if i>0:
#         print(i) 
#     i+=1                            
# else:
#     print(i)
#     while ini<=end:
#         if i<0:
#             print(i)
#         i+=1
   
while i <=j:
    par=i%2
    if par==0:
        print(i, end=" ")
        if i>0:
            print( "positivo")     
        else:
            print( "negativo")
    i+=1
else:
    print("\n")
    while ini <= end:
        par=ini%2
        if par!=0:
            print(ini, end=" ")       
           
        ini+=1