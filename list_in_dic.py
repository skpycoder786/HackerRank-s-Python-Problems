if __name__ == '__main__':
    n = int(input())
student_marks = {}
for i in range(n) :
    string=input()
    name, *scores =string.split()
    student_marks[name]=scores
#print(student_marks)
list1=list()
q_name=input()
q_scores=student_marks[q_name]
for i in q_scores :
    list1.append(float(i))
#print(list1)    
sum=0
for i in list1 :
    sum=sum+i
#print(sum)
print("{0:.2f}".format(sum/3))  