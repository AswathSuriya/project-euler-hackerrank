def checkprime(n,P):
    for x in P:
        if n%x==0:
            return False
        if x>pow(n,0.5):
            return True
        

T=int(input())
primes=[2,3,5,7,11,13,17,19]
while T:
    N=int(input())
    L=len(primes)
    if N<L:
        print(primes[N-1])
    else:
        i=primes[L-1]+2
        while L<N:
            if checkprime(i,primes):
                primes.append(i)
            L=len(primes)
            i+=2
        print(primes[L-1])
    T-=1
