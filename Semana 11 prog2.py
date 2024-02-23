Matrix = [
    [5, 2, 6],
    [3, 4, 11],
    [1, 7, 8]
]
print(Matrix)
print("Ingrese el valor a buscar " )
v=int(input())
print(Matrix)
i=0
e=0
for f in Matrix:
    j=0
    for c in f:
        if (c==v):
            print(f'El numero ingresado se encuentra en la posicion [{i},{j}]')
        else:
            e+=1
        j+=1
    i+=1
if(e==9):
    print("El numero ingresado no existe")