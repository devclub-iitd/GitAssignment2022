#My solution for a codeforces contest problem.

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def algo(n,h):
    if h%2==0:
        h-=1
    while h>2:
        if h<=n:
            return -1
        fac=list(factors(h))
        fac.remove(1)
        fac.remove(h)
        if len(fac)==0:
            return h
        m=min(fac)
        if m>=n:
            return h
        else:
            h-=2
    return -1


(n,h)=map(int,input().split())
print(algo(n,h))