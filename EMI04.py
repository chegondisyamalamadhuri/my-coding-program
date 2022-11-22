p=int(input("principal amount:"))
t=int(input("time period:"))
r=float(input("rate of inerest:"))
si=(p*t*r)/100
print("simple interest:",si)
EMI=(si+p)/t*12
print(EMI)
