import re 
import sys
from collections import defaultdict

print ("Day13")
          
data = [line.strip() for line in open("input_day13_sample2.txt", 'r')]
#data = [line.strip() for line in open("input_day13_sample3.txt", 'r')]
#data = [line.strip() for line in open("input_day13_sample.txt", 'r')]
#data = [line.strip() for line in open("input_day13.txt", 'r')]
print(data[1])
earliestTime = int(data[0])
schedule = [int(time) for time in data[1].split(",") if time !="x"]
         
print(earliestTime)
rest = [earliestTime%x for x in schedule]
rest1 = [x-earliestTime%x for x in schedule]
index = rest1.index(min(rest1))
print(schedule)
print(rest)
print(rest1)

print("Solution 1",index,schedule[index]*rest1[index])
print("Valid 3417 {0: 17, 2: 13, 3: 19}")
print("Valid 187 {0: 17, 3: 19}")
print("Valid 17 {0: 17, 2: 19}")
print("Valid 754018 {0: 67, 1: 7, 2: 59, 3: 61} ")
schedule3 ={}
i =0
for char in data[1].split(","):
    if (char != 'x'):
        schedule3[i]=int(char)
    i +=1
schedule2 = [int(time if time !="x" else -1) for time in data[1].split(",") ]
#data = [line.strip() for line in open("input_day8_sample.txt", 'r')]
#print (data)
print (schedule3)
#print (schedule2)
first = schedule[0]
keys=list(schedule3.keys())

#print("W",first,782%17,782%13,782%19)
#print("W1",first,1068781%7,1068781%13,1068781%19)
#print("W2",first,1068781%7,1068782%13,1068788%19)
#print("W3417",3417%17,3417%13,3417%19)
#print("W4199",4199%17,(4199+2)%13,(4199+3)%19)
print(keys)
i=1
while True:
    t = i*first
    m = [(t+j)%x for j,x in schedule3.items()]
    m2 = [i*x for j,x in schedule3.items()]
    #print(i,t,m,m2)
    #if(keys==m):
    if sum(m)==0:
        print("found",i,t,m)
        break
    i +=1
    if i==1168781:
        print("not found",i,t,m)
   
        break
    