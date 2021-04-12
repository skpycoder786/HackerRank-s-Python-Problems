from itertools import combinations
S,k=input().split()
k=int(k)
lst=list(S)
lst.sort()
S="".join(lst)
#print(S)
for i in range(k) :
    lst1=list(combinations(S,i+1))
    #print(lst1)    
    for j in range(len(lst1)) :
        temp="".join(lst1[j])
        print(temp)