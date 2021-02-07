def isPrime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    return all(n%x>0 for x in range(3, int(n**0.5)+1, 2))

def genP(n):
    p = [2]
    p.extend([x for x in range(3, n+1, 2) if isPrime(x)])
    return p

def primepartition(n):
    p = genP(n)
    for i in range(0,len(p)):
        for j in range(0,len(p)):
            if p[i]+p[j]==n:
                return True
    return False

def matched(n):
    n=list(n)
    c=0
    for i in range(len(n)):
        if c==-1:
            return False
        if n[i]=="(":
            c=c+1
        if n[i]==")":
            c=c-1
    if c==0:
        return True
    else:
        return False

def rotatelist(l,k):
    output_list = []
    k = k%len(l)

    # Will add values from n to the new list
    for item in range(k, len(l)):
        output_list.append(l[item])
    # Will add the values before
    # n to the end of new list
    for item in range(0, k):
        output_list.append(l[item])
    return output_list