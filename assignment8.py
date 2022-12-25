startyear=int(input())
endyear=int(input())
for year in range(startyear,endyear):
   if (year%4==0) and(year%100!=0) or (year%400==0):
    print(year)
