print("INgrese los 9 digitos enetros de la matrix 3x3")


def input_matrix():
    m = []
    print("Ingresa los elementos de la matriz de 3x3:")
    for i in range(3):
        row = []
        for j in range(3):
            while True:
                try:
                    element = int(input(f"Ingrese el elemento [{i}][{j}]: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número entero.")
            row.append(element)
        m.append(row)
    return m

def print_matrix(m):
    for row in m:
        print(row)

m = input_matrix()
print("\nMatriz ingresada:")
print_matrix(m)



print("que fila deseas ordenar?")
i=int(input())
if(m[i][0]>m[i][1]):
    if(m[i][0]>m[i][2]):
        if(m[i][2]>m[i][1]):
            k=m[i][2]
            m[i][2]=m[i][0]
            m[i][0]=m[i][1]
            m[i][1]=k
        else:
            k = m[i][2]
            m[i][2] = m[i][0]
            m[i][0] = k
    else:
        k = m[i][1]
        m[i][1] = m[i][0]
        m[i][0] = k
else:
    if (m[i][0] > m[i][2]):
        k = m[i][2]
        m[i][2] = m[i][1]
        m[i][1] = m[i][0]
        m[i][0]=k

print(m)



