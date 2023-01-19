def valid(s):
    for i in range(0,n):
        s=input()
        l=[]
        k=0
        kl=0;
        while(k<len(s)):
            if(s[k]=='{' or s[k]=="[" or s[k]=="("):
                l.append(s[k])
            else:
                if(s[k]=="}" and len(l)>0):
                    if(l[-1]!="{"):
                        print("NO")
                        kl=1;
                        break
                    else:
                        l.pop()
                elif(s[k]=="]" and len(l)>0):
                    if(l[-1]!="["):
                        print("NO")
                        kl=1;
                        break
                    else:
                        l.pop()
                elif(s[k]==")" and len(l)>0):
                    if(l[-1]!="("):
                        print("NO")
                        kl=1;
                        break
                    else:
                        l.pop()
            k+=1
        if(len(l)==0 and kl==0):
            print("YES")
        elif(kl==0):
            print("NO")
n=int(input())
valid(n)
