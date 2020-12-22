import re 
import sys
from collections import defaultdict

print ("Day18")

def solution(data):
    mysum =0
    for line in data:
        operationList = re.findall('\d+|\+|\*|\(|\)', line )
        result,_ = calc(operationList,0)
        print (result)
        mysum +=result
    return mysum    

def calc(operationList,index):
    #print("calc",operationList,index)
    result =0
    addition = False
    multiply = False
    first =True
    while True:
        if index >= len(operationList):
            break
        term = operationList[index]
        #print("term",index,term)
        index +=1
        
        if term =='+':
            addition = True
            continue
        if term =='*':
            multiply = True
            continue
        if term ==')':
            break;
        if term =='(':
            #print("(call")
            termResult,index =calc(operationList,index)
            #print("(close")
        else:    
            termResult =int(term)
        if first:
            result = termResult
            first = False
        else:
            if multiply:
                result *=termResult
                multiply = False    
            if addition:
                result +=termResult
                addition = False    
    #print("result",result,index)            
    return result,index     

        
data = [line.strip() for line in open("input_day18_sample.txt", 'r')]
data = [line.strip() for line in open("input_day18.txt", 'r')]
print("solution",solution(data))
#print (solution(data,1))    
#print (solution(data,2))    
