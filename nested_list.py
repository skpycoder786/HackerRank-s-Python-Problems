if __name__ == '__main__':
    n=int(input())
    
lst=list()
list1=list()
list2=list()
for i in range(0,n):
    ele = [input(), float(input())] 
    lst.append(ele)
#print(lst)
for i in lst :
    list1.append(i[1])
#print(list1)
m1=min(list1)
for i in lst :
    if i[1] == m1 :
        list1.remove(i[1])    
    else :
        continue
m2=min(list1)
#print(m2)
for i in lst:
    if i[1] == m2 :
        list2.append(i[0])
    else :
        continue
list2.sort()
#print(list2) 
for i in range(len(list2)) :
    print(list2[i])