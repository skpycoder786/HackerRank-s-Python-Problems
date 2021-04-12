def clock(s):
    lst=[]
    for i in range(len(s)):
        lst.append(s[i])
    #check1) print(lst)
    tag=s[8:10]
    if tag=='AM' :
        if s[0:2]=='12' :
            lst[0],lst[1]='0','0'
        else:
            pass
    elif tag=='PM':
        if s[0:2]=='12' :
           pass
        else:
            hr=int(s[0:2])
            hr+=12
            strhr=str(hr)
            lst[0],lst[1]=strhr[0],strhr[1]
    #check2) print(lst)        
    newstr="".join(lst)
    return newstr[0:8]
    
timestr=input()
ans=clock(timestr)
print(ans)    