# coupon code offer 5000+ discount10% 3000+ discount 6% 1000+ discount 4%, coupon code='DIWALI'
 #  coupon code offer 3000+ discount 20% 2000+ discount 10% 1000+ discount 5%, coupon code='CHRISMAS'
rice=200
oil=120
sugar=50
pulses=30
flour=20
cphno=input('enter customer phone number:')
cname=input('enter customer name:')
caddr=input('enter customer address:')
riceq=int(input('how many rice packets you want!'))
oilq=int(input('how many oil packets you want!'))
sugarq=int(input('how many sugar packets you want!'))
pulsesq=int(input('how many pulses packets you want!'))
flourq=int(input('how many flour packets you want!'))
bill=(rice*riceq)+(oil*oilq)+(sugar*sugarq)+(pulses*pulsesq)+(flour*flourq)
coupon=input('enter the coupon code in capital letters:')
if bill>3000:
 tax=bill*5/100
elif bill>2000:
 tax=bill*7/100
elif bill>1000:
 tax=bill*10/100 
elif bill>500:
 tax=bill*15/100
else:
     tax=100
if coupon=='DIWALI' and bill>=5000:
         dis=bill*10/100
if coupon=='DIWALI' and bill>=3000:
         dis=bill*6/100
if coupon=='DIWALI' and bill>=1000:
         dis=bill*4/100
if coupon=='CHRISMAS' and bill>=3000:
         dis=bill*20/100
if coupon=='CHRISMAS' and bill>=2000:
         dis=bill*10/100
if coupon=='CHRISMAS' and bill>=1000:
         dis=bill*5/100
else:
     dis=0
     bill=bill+tax-dis
     print(cphno)
     print(cname)
     print(caddr)
     print(bill)
     print(tax)
     print(dis)
