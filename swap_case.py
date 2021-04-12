def swap_case(s):
    s=s.split()
    #print(s)
    for i in range(len(s)):
        s[i]=s[i].swapcase()
    s=" ".join(s)
    return s    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)