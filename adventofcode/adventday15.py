import re 
import sys
from collections import defaultdict

print ("Day15")

def solution(data):
    myList = data.split(",")
    spoken ={}
    i =0
    lastSpeak =0
    #while i<30000000:
    while i<2020:
        if int(lastSpeak) in spoken.keys():
            lastValue,valueBefore = spoken[lastSpeak]
        else:
            lastValue,valueBefore = -1,-1    
        if i < len(myList):
            toSpeak = int(myList[i])
        else:    
            if valueBefore ==-1:
                toSpeak = 0;
            else:
                toSpeak = lastValue-valueBefore;
        #print(i," >>>ToSpeak",toSpeak)    
        if int(toSpeak) in spoken.keys():
            lastValue,valueBefore = spoken[toSpeak]
        else:
            lastValue,valueBefore = -1,-1    
        spoken[toSpeak]=(i,lastValue)
        lastSpeak=toSpeak
        i +=1
    return lastSpeak

                  
#data = [line.strip() for line in open("input_day15_sample.txt", 'r')]
#data = [line.strip() for line in open("input_day15.txt", 'r')]

data = "20,9,11,0,1,2"
#data = "0,3,6"
#data = "2,1,3"
print(solution(data))
#print (solution(data,1))    
#print (solution(data,2))    
