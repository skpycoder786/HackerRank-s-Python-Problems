import textwrap

i=0
def wrap(string, max_width):
    i=0
    while i<len(string) :
        slice=string[i:(i+max_width)]
        i=i+max_width
        if i<len(string):
            print(slice)
        else :
            break
    return slice             
  
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
#method 2 
i=0
def wrap(string, max_width):
    i=0
    while i<len(string) :
        try:
            slice=string[i:(i+max_width)]
        except:
            slice=string[i:]
        print(slice)
        i=i+max_width

if __name__ == '__main__':
    string, max_width = input(), int(input())
    wrap(string, max_width)
     