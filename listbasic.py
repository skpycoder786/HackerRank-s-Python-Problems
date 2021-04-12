if __name__ == '__main__':
    N = int(input())

list1=list()    
for i in range(N) :
    string=input()
    words=string.split()
    command = words[0]
    if command == 'insert' :
        index = int(words[1])
        data = int(words[2])
        list1.insert(index,data)
    elif command == 'print' :
        print(list1)
    elif command == 'remove' :
        list1.remove(int(words[1]))   
    elif command == 'append' :
        list1.append(int(words[1]))    
    elif command == 'sort' :
        list1.sort()
    elif command == 'pop' :
        list1.pop()
    elif command == 'reverse' :
        list1.reverse()        
        
m2=max(list1)    
for k,v in dic.items() :
    if k == m2 :
        print(dic(k))
    else :
        continue  