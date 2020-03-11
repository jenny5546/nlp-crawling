def printPicked(picked):
    result = []
    for i in picked:
        result.append(i)
    print(result)

def pick(n, picked, toPick):
    if toPick ==0:
        printPicked(picked)
        return
    smallest = 0 if len(picked)==0 else picked[-1]+1;
    
    for next in range(smallest,n):
        picked.append(next)
        pick(n, picked, toPick-1)
        picked.pop()
    
        
pick(7,[],4)