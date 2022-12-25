n = int(input())
sum = 0

for number in range(2, n + 1):
    i = 2
    for i in range(2, number):
        if (int(number % i) == 0):
            i = number
            break;

    if i is not number:
        sum = sum + number
print( sum)
