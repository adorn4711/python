import re 
import sys
from collections import defaultdict

print ("Day9")

def solve(data,numChecks):
    for pos in range(numChecks+1,len(data)):
        found = False
        for i in range(numChecks):
            for j in range(numChecks):
                if (i==j): continue
                #print (data[pos],data[pos-i-1],data[pos-j-1],data[pos-i-1]+data[pos-j-1])    
                if data[pos] == data[pos-i-1] + data[pos-j-1]:
                    found = True
                    break;
            if found: break
        if not found:
            return data[pos]

def solve2(data,numChecks,invalidNum):
    for pos in range(len(data)):
        sum =0
        numList = []
        for i in range(pos,len(data)):
            numList.append(data[i])
            sum +=data[i]
            if sum == invalidNum:
                return min(numList)+max(numList)
            if sum > invalidNum : break
            
        


data = [int(line.strip()) for line in open("input_day9.txt", 'r')]
#print (data)
invalid = solve(data,25)
print(solve2(data,25,invalid))

data1 = [int(line.strip()) for line in open("input_day9_sample.txt", 'r')]
print (data1)
invalid = solve(data1,5)
print(solve2(data1,5,invalid))
