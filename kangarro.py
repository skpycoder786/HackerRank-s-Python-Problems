# (x1 + v1*y) == (x2 + v2*y) has to be true, where y=no. of jumps by each one
# (x1-x2)/(v2-v1) == y     ,And y has to be integer
# (x1-x2)%(v2-v1) == 0     , remainder should be zero
def kangaroo(x1, v1, x2, v2):
    if v2 >= v1 :
        return("NO")
    else:
        if (x1-x2)%(v2-v1) == 0 :   
            return("YES")
        else:
            return("NO")
        
x1,v1,x2,v2=input().split()
x1,v1,x2,v2=int(x1),int(v1),int(x2),int(v2) 
ans=kangaroo(x1, v1, x2, v2)
print(ans)       