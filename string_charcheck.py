if __name__ == '__main__':
    s = input()

words=list(s)
#print (words)

def foralnum (words):
    for word in words :
        if word.isalnum() :
            return True
        else :
            continue
    return False
    
def foralpha(words):            
    for word in words :
        if word.isalpha() :
          return True
        else :
            continue
    return False      

def fordigit (words):        
    for word in words :
        if word.isdigit() :
            return True
        else :
            continue
    return False

def forlower (words):
    for word in words :
        if word.islower() :
             return True
        else :
            continue
    return False

def forupper (words):
    for word in words :
        if word.isupper() :
             return True
        else :
            continue
    return False

bool1=foralnum(words)    
bool2=foralpha(words)
bool3=fordigit(words)
bool4=forlower(words)
bool5=forupper(words)

print(bool1,"\n",bool2,"\n",bool3,"\n",bool4,"\n",bool5,sep="")











