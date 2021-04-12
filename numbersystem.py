#numbersystem
def print_formatted(number):
    for i in range(1,number+1) :
        a=oct(i)
        a=a[2:]
        b=hex(i)
        b=b[2:].upper()
        c=bin(i)
        c=c[2:]
        w=len(c)
        print("{} {} {} {}".format(i,a,b,c))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
#exact method:
def print_formatted(number):
    n=number
    space=len(bin(n))-2
    for i in range(1,n+1):
        string=''
        for j in range(0,space-len(list(str(i)))):
            string+=' '
        string+=str(i)
        string+=' '
        for j in range(0,space-len(oct(i))+2):
            string+=' '
        string+=str(oct(i))[2:]
        string+=' '
        for j in range(0,space-len(hex(i))+2):
            string+=' '
        string+=str(hex(i))[2:].upper()
        string+=' '
        for j in range(0,space-len(bin(i))+2):
            string+=' '
        string+=str(bin(i))[2:]
        print(string)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)    
