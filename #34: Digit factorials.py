import math
N=int(input())
f=[]
sum=0
for i in range (0,10):
    f.append(math.factorial(i))
for num in range(19,N):
    n=num
    nsum=0
    while(n):
        #print(n)
        nsum=nsum+f[int(n%10)]
        n=int(n/10)
        #print(nsum)     
    if (nsum%num==0):
        sum=sum+num
print (sum)
        
        
