def climbingStaircase(n, k):
    tpattern=[(0,[])] #list of tuples (currentStep, path)
    atStep=0
    while atStep<n:
        ntpattern=[]
        for s,p in tpattern:
            if s==atStep:
                lim=min(k+1, n-atStep+1)
                for size in range(1,lim):
                    ntpattern.append((s+size,p+[size]))
            else:
                ntpattern.append((s,p))
        tpattern=ntpattern
        atStep+=1
    _,r=zip(*tpattern)
    return r
