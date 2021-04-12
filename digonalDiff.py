def intlist(lst):
    for i in range(len(lst)):
        lst[i]=int(lst[i])
    return lst    

def diagonalDifference(lst):    #  basically here lst is list of lists
    LtoR_D,RtoL_D=0,0
    for i in range(len(lst)):
        LtoR_D+=lst[i][i]
    lst.reverse()
    for i in range(len(lst)):
        RtoL_D+=lst[i][i]
    Diff=abs(LtoR_D-RtoL_D)
    return Diff

n=input()
n=int(n)
listoflist=[]
for i in range(n):
    r=input().split()
    int_r=intlist(r)
    listoflist.append(int_r)
#check-1)    
#print(listoflist)
#print(type(listoflist[0]))
#print(type(listoflist[0][1]))
ans=diagonalDifference(listoflist)
print(ans)
