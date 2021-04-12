lis=input().split() #   n,m values
n=lis[0]
m=lis[1]

lis_n=input().split()   #   array(list) of n elements
newlist = list(map(int, lis_n))

lis1=input().split()    #   set A
newlis1 = list(map(int, lis1))  
A=set(newlis1)

lis2=input().split()    #   set B
newlis2 = list(map(int, lis2))
B=set(newlis2)

happ=0
for i in newlist :
    if i in A :
        happ += 1
    elif i in B :
        happ -= 1
    else :
        continue
print(happ)        
    
# Programme for Add elements in SET.    
#num=int(input())
#SET=set()
#for i in range(num):
#    SET.add(input())
#print(len(SET))    
