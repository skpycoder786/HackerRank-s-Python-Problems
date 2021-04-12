def designerPdfViewer(hieghts_lst, word_lst):
    h=[]    # list for putting words's alphabets height
    for i in word_lst:
        temp=Alphabets_lst.index(i)
        h.append(hieghts_lst[temp])
    #check-2) print(h)
    Area=max(h)*len(word_lst)    
    return(Area)

# using naive method, for filling alphabets 
Alphabets_lst=[]
alpha = 'a'
for i in range(0, 26): 
    Alphabets_lst.append(alpha) 
    alpha = chr(ord(alpha) + 1)
#check-1) print(Alphabets_lst)
hieghts_lst=h = list(map(int, input().rstrip().split()))
word=input()
word_lst=list(word)
ans=designerPdfViewer(hieghts_lst, word_lst)
print(ans)
    