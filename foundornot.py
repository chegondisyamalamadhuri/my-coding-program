n=int(input())
l=list(map(int,input().split()))
x=int(input())
if x in l:
    print("Element is found at index",x)
else:
    print("Element is not found")
