def unique(n):
 unique = set(n)
 unique = list(unique)
 return unique
a = int(input())
n=list(map(int,input().split()))
print(unique(n))
