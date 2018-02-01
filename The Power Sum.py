import sys
import math

def powerSum(X, N):
    powerSum.number = 0

    A = [0] * 100

    def IsSum(X, N, k):
        for x in range(A[k-1]+1, int(X**(1/N) + 1)):
            if UCV(X, N, k, x):
                A[k] = x
                if sum(map(lambda x: x**N, A[:k+1])) == X:
                    powerSum.number += 1
                else:
                    IsSum(X,N,k+1)
    def UCV(X,N,k,x):
        if sum(map(lambda x: x**N, A[:k])) + x**N <= X:
            return 1
        return 0

    IsSum(X,N,1)
    return powerSum.number




if __name__ == "__main__":
    X = int(input().strip())
    N = int(input().strip())
    result = powerSum(X, N)
    print(result)