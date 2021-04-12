from itertools import combinations_with_replacement
S,k=input().split()
k=int(k)
lst=list(S)
lst.sort()
S="".join(lst)
#print(S)
lst1=list(combinations_with_replacement(S,k))
#print(lst1)
for i in range(len(lst1)) :
    temp="".join(lst1[i])
    print(temp)