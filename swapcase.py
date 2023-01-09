def swap_case(s):
    res=''
    for i in s:
        if i.isupper():
            x=i.lower()
            res=res+x
        else:
            x=i.upper()
            res=res+x
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
