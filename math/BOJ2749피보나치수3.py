import sys

input = sys.stdin.readline

n = int(input())

MOD = 1000000

def fibonacci_matrix(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_matrix = [[1, 1], [1, 0]]
        
        result_matrix = matrix_power(fib_matrix, n-1)
        
        return result_matrix[0][0] % MOD
    
def matrix_power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return matrix
    else:
        matrix_half = matrix_power(matrix, n//2)
        matrix_n = matrix_multiply(matrix_half, matrix_half)
        
        if n % 2 == 1:
            matrix_n = matrix_multiply(matrix_n, matrix)
            
        return matrix_n
    
def matrix_multiply(matrix1, matrix2):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                result[i][j] %= MOD
    return result

print(fibonacci_matrix(n))
