import itertools


def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

def getprimes(L,n):    
    for i in L:        
        j=2
        N=max(L)
        while j*i <= N:            
            if j*i in L:
                L.remove(j*i)
            j+=1
    return L

def isprime(n):
    n*=1.0
    if n%2==0 and n!=2 or n%3==0 and n!=3:
        return False
    for b in range(1,int((n**0.5+1)/6.0+1)):
        if n%(6*b-1)==0:
            return False
        if n %(6*b+1)==0:
           return False
    return True

def getcirc(n,P,N):
    num = str(n)
    nums = []
    l = len(num)
    for i in range(1,l):
        dig = int(num[i:l]+num[0:i])
        #print(dig)
        if dig<N and dig not in P:
            return False
        elif isprime(dig) != True:
            return False        
    return True

def checkcirc(L,P,N):
    flag=0
    for i in L:
        if i<N and i not in P:
            flag = 1
            return False
        else:
            if isprime(i) != True:
                flag = 1
                return False
    return True
        
 
    
    
N=int(input())
P=[]
#P.extend(range(2,N))
P=primes_sieve(N)
#print(len(P))

sum = 2
for i in P:
    num = str(i)
    if '0' in num or '2' in num or '4' in num or '6' in num or '8' in num:
        continue
    elif getcirc(i,P,N):        
        sum+=i
print (sum)
           
