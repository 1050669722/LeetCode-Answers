import numpy as np

def encrypt(num):
    return np.mod(7**num, 11)

A, B = 3, 6
alpha, beta = encrypt(A), encrypt(B) # 2, 4

Alice, Bob = np.mod(beta**A, 11), np.mod(alpha**B, 11)
print(Alice, Bob)