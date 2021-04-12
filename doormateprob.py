# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = input().split()
N=int(N)
M=int(M)
c='.|.'
i=0
j=1
k=N
#Top
for i in range(N//2):
    i=i+j
    print((c*i).center(M,'-'))
    j=j+1
#Middle
print('WELCOME'.center(M,'-'))    

#Bottom
for i in range(N//2):
    k=k-2
    print((c*k).center(M,'-'))

    
   