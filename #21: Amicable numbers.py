def d(x):
    dsum=1    
    for i in range(2,x):
        if(x%i==0):            
            dsum=dsum+i    
    return dsum

def fn(i,N):
    sum1=d(i)
    if((sum1<=N)and(sum1>i)):
        if(d(sum1)==i):
            return(i+sum1)
    return (0)    
T=int(input())
while(T):
    AR=[220,284,1184,1210,2620,2924,5020,5564,6232,6368,10744, 10856,12285,14595,17296,18416,63020,66928,66992,67095, 69615,71145,76084,79750,87633,88730 ]
    N=int(input())
    sum=0
    for i in AR:
        if(i<N):
            sum=sum+i
        else:
            break
    print (sum)
    T=T-1
