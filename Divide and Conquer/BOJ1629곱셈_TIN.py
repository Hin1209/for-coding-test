import sys

input = sys.stdin.readline

num, exp, div = map(int, input().split())

def pow(num, exp, div):
    if exp == 0:
        return 1
    tmp = pow(num, exp//2, div)
    tmp = (tmp * tmp) % div
    if exp % 2 == 0:
        return tmp
    return (num * tmp) % div 
    

print(pow(num, exp, div))        
