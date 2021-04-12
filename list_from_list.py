# question:
#There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
#1) The elements of the first array are all factors of the integer being considered
#2) The integer being considered is a factor of all elements of the second array
#These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

def getTotalX(a,b):
    check_lst1=[]
    for i in range(a[n-1],b[0]+1):
        if i%a[n-1] == 0 :
            check_lst1.append(i)
    #print(check_lst1)  
    check_lst2=[]
    for i in check_lst1:
        check_lst2.append(i)
    for j in check_lst1:
        for k in a:
            if j%k==0 :
                pass
            else:
                check_lst2.remove(j)
                break
    #print(check_lst2)
    check_lst3=[]
    for i in check_lst2:
        check_lst3.append(i)
    for j in check_lst2:
        for k in b:
            if k%j==0 :
                pass
            else:
                check_lst3.remove(j)
                break
    #print(check_lst3)              
    return (len(check_lst3))            

n,m=input().split()
n,m=int(n),int(m)
a=input().split()
for i in range(n):
    a[i]=int(a[i])
b=input().split()
for i in range(m):
    b[i]=int(b[i]) 
ans=getTotalX(a,b)
print(ans)
        
    