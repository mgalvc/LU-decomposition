import numpy as np


np.set_printoptions(precision=16, suppress=True, linewidth=500, floatmode='fixed')


def factLU(A):
    """
        A é matriz aumentada
        b é a solução do sistema
        U é a matriz escalonada
        n é a ordem da matriz
        L é a matriz diagonal com os fatores na parte inferior
    """
    b = A[:, -1]
    U = np.copy(A[:, 0:-1])
    n = np.shape(U)[0]
    L = np.eye(n)

    # fazer o escalonamento percorrendo as colunas
    j = 0
    # primeira linha não é alterada
    i = 1
    while j < n-1:
        pivo = U[i - 1][j]

        # loop para escalonar cada linha utilizando o pivo
        k = i
        while k < n:
            fator = U[k][j] / pivo
            L[k][j] = fator
            U[k] = U[k] - U[j] * fator
            k += 1

        j += 1
        i += 1

    return [L, U, b, n]


def solve_system(L, U, b, n):
    # primeiro resolve Ly = b
    y = np.zeros(n)
    # pode-se fazer isso pq a matriz é triangular inferior
    y[0] = b[0]

    # resolvendo Ly = b
    i = 1
    while i < n:
        j = 0
        while j < i:
            y[i] += y[j] * L[i][j]
            j += 1
        y[i] = b[i] - y[i]
        i += 1

    print("Matriz y", y)

    # x é a matriz solução do sistema
    x = np.zeros(n)
    x[n-1] = y[n-1]/U[n-1][n-1]

    # agora resolvendo Ux = y
    i = n-2
    while i >= 0:
        j = n-1
        while j > i:
            x[i] += x[j]*U[i][j]
            j -= 1
        x[i] = (y[i] - x[i])/U[i][j]
        i -= 1

    print("Matriz x", x)


def solve(A):
    L, U, b, n = factLU(A)

    print("Matriz L:\n", L)
    print("\n")
    print("Matriz U:\n", U)
    print("\n")

    solve_system(L, U, b, n)

