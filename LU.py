import numpy as np

def factLU(A):
    """
        A é matriz aumentada
        b é a solução do sistema
        U é a matriz escalonada
        n é a ordem da matriz
        L é a matriz diagonal com os fatores na parte inferior
    """
    b = A[:,-1]
    U = np.copy(A[:,0:-1])
    n = np.shape(U)[0]
    L = np.eye(n)

    # fazer o escalonamento percorrendo as colunas
    j = 0
    # primeira linha não é alterada
    i = 1
    while j < n:
        pivo = U[i-1][j]

        # loop para escalonar cada linha utilizando o pivo
        k = i
        while k < n:
            fator = U[k][j]/pivo
            L[k][j] = fator
            U[k] = U[k] - U[j]*fator
            k += 1

        j += 1
        i += 1

    return [U,L,b]

def solve(L, U, b):


A = np.array([
        [1,1,1,0],
        [2,1,-1,5],
        [2,-1,1,3]
    ])

U, L, b = factLU(A)
print(U)
print(L)
print(b)

