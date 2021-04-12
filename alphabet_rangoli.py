def print_rangoli(size):
    N=size
    w=(4*N)-3
    import string
    resulted_string=string.ascii_lowercase  #To take lowercase string="abcdefghijklmnopqrstuvwxyz"
    resultslice=resulted_string[:N]
    result=resultslice[::-1]  #To reverse a string
    
    #Top_part
    for t in range(N-1):
        lst1=list()
        for i in range(t+1):
            lst1.append(result[i])
        i=t-1
        while i>=0 :
            lst1.append(result[i])
            i=i-1
        R="-".join(lst1)
        print(R.center(w,"-"))  #ANS=how to align string at center
 
    #middle_line
    lst=list()
    for i in range(N):
        lst.append(result[i])
    i=N-2
    while i>=0 :
        lst.append(result[i])
        i=i-1
    RR="-".join(lst)
    print(RR.center(w,"-"))
    
    #Bottom_part
    for t in range(N-1)[::-1]:  #ANS=how to run reverse for loop
        lst1=list()
        for i in range(t+1):
            lst1.append(result[i])
        i=t-1
        while i>=0 :
            lst1.append(result[i])
            i=i-1
        R="-".join(lst1)
        print(R.center(w,"-"))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)    