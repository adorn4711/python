import re 
import sys
print ("Day6")
def questionCheck(data):
    sum = 0
    passport = {}
    currentGroup = set()
    newList=True
    for i in range(len(data)):
        line = data[i]
        if (len(line)==0):
  #          print(currentGroup)
            sum += len(currentGroup)
            currentGroup = set()
            newList=True
#            print ("new Group")
        else:
 #           print(list(line))
            currentLineSet = set(list(line))
            if newList:
                currentGroup = set(list(line))
                newList = False
            else:
                currentGroup = currentGroup.intersection(currentLineSet)
    sum += len(currentGroup)
    return sum
    
    
        
        
data = [line.strip() for line in open("input_day6.txt", 'r')]
print(questionCheck(data))