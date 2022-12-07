n=int(input())
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(1, n-1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
