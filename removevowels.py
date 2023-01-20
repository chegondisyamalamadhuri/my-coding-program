string = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
res = ""

for i in string:
    if i not in vowels:
        res= res + i
print(res)
