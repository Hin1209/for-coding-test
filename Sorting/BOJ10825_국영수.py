import sys
n = int(sys.stdin.readline())
student = []

for i in range(n):
    data = sys.stdin.readline().split()
    student.append([data[0], int(data[1]), int(data[2]), int(data[3])])


result = sorted(student, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(len(student)):
    print(result[i][0])