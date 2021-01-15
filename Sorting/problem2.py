n = int(input())
student = []
for i in range(n):
    student.append(input().split())
a = sorted(student, key = lambda x : int(x[1]))
for i in range(n):
    print(a[i][0], end = ' ')

