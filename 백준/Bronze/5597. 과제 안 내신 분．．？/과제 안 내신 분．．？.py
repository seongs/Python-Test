import sys

student = [i for i in range(1,31)]

for _ in range(28):
    n = int(sys.stdin.readline())
    student.remove(n)

for i in student:
    print(i)
