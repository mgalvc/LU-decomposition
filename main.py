import LU
import numpy as np

M = [
    [10,2,1,7],
    [1,5,1,-8],
    [2,3,10,6]
]

LU.solve(np.array(M, dtype=np.float64))
