if __name__ == '__main__':
    N,X = input().split()
N=int(N)
X=int(X)
lst=list()
for i in range(X):
    string=input()
    words=string.split()
    lst.append(words)
#print(lst) 
for i in lst :
    for j in range(len(i)) :
        i[j]=float(i[j])
print(lst)

