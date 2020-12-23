import re 
import sys
from collections import defaultdict

print ("Day18")

def solution(data):
    mysum =0
    for line in data:
        operationList = re.findall('\d+|\+|\*|\(|\)', line )
        #print(operationList)
        result,_ = calc(operationList,0,False)
        print (line,result)
        mysum +=result
    return mysum    

def calc(operationList,index,multiPlyRekusion):
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
            termResult,index =calc(operationList,index,False)
            #print("(close")
        else:    
            termResult =int(term)
        if first:
            result = termResult
            first = False
        else:
            if multiply:
                index -=1
                termResult,index =calc(operationList,index,True)
                result *=termResult
                multiply = False    
                if multiPlyRekusion:
                    break
            if addition:
                result +=termResult
                addition = False    
    #print("result",result,index)            
    return result,index     


        
data = [line.strip() for line in open("input_day18_sample2.txt", 'r')]
#data = [line.strip() for line in open("input_day18.txt", 'r')]
print("solution",solution(data))
#print (solution(data,1))    
#print (solution(data,2))    


def calc_old(operationList,index):

    print("calc",operationList,index)
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
