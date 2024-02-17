def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
    
print(fac(5))

def feibo(n):
    if n==1 or n==2:
        return 1
    else:
        return feibo(n-1)+feibo(n-2)
print(feibo(9))