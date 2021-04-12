n=int(input())
lst=input().split()
newlst=list(map(int,lst))
SET=set(newlst)
noc=int(input())

for i in range(noc) :
    words=input().split()
    command = words[0]
    if command == 'pop' :
        try: 
            SET.pop()
        except:
            continue    
    elif command == 'remove' :
        element = int(words[1])
        try:
            SET.remove(element)
        except:
            continue    
    elif command == 'discard' :
        element = int(words[1])
        SET.discard(element) 
    else :
        continue

final_lst=list(SET)
SUM=sum(final_lst)
print(SUM)        