M=int(input())
lis1=input().split()
newlis1 = list(map(int, lis1))  #Making list of integers by using map function.
N=int(input())
lis2=input().split()
newlis2 = list(map(int, lis2))
#print(newlis1,newlis2)

set1=set(newlis1)
set2=set(newlis2)

uni=set1.union(set2)
inter=set1.intersection(set2)
symm_diff=uni.difference(inter)
#print(symm_diff)
lst=list(symm_diff)
lst.sort()
#print(lst)
for i in lst:
    print(i)
