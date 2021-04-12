# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n-(i+1)):
            print(' ',end='')
        for k in range(i+1):
            print('#',end='')
        print('\r')       
            
# \r is "Carriage Return" (CR, ASCII character 13), \n is "Line Feed" (LF, ASCII character 10). 
#Back in the days, you had two ASCII characters at the end of each line to tell a printer what to do  ?
#CR would tell the printer to go back to the left edge of the paper,
# LF would advance to the next line.            
num=int(input())
staircase(num)    
