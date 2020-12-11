#import re 
#import sys
from collections import defaultdict

print ("Day11")

ways = set()
tree = defaultdict(list)
reverseTree =defaultdict(list)

def solve1(data):
    data.sort()
    difference1 =0
    difference3 =0
    highest = max(data)+3
    data.append(highest)
    adapter =0
    for currVal in data:
        #print(adapter,currVal,difference1,difference3)
        if (currVal-adapter)==1:
            difference1 +=1
            adapter = currVal
        elif (currVal-adapter)==3:
            difference3 +=1
            adapter = currVal
        else:
            break
    print(difference1,difference3)        
    return difference1*difference3
        
def solve2(data):
    highest = max(data)+3
    data.append(highest)
    data.append(0)
    data.sort()
    #print(data)
    for e in data:
        for i in range(3):
            if e+i+1 in data:
                tree[e].append([e+i+1,-1])
    print(tree)
    getWay(0,"",highest)            
    print(ways)
    return len(ways)

def getWay(number,way,highest):
    way +=":"+str(number)
    if number==highest:
        ways.add(way)
    for e,sum in tree[number]:
        getWay(e,way,highest)

def solve3(data):
    highest = max(data)+3
    data.append(highest)
    data.append(0)
    data.sort()
    diffs = ''.join([str(b-a) for a,b in zip(data, data[1:])])
    part1= diffs.count('1')*diffs.count('3')
    diffs = diffs.replace('1111','a').replace('111','b').replace('11','c')
    part2 = 7**diffs.count('a') * 4**diffs.count('b') * 2**diffs.count('c')
    return part1, part2



data = [int(line.strip()) for line in open("input_day10.txt", 'r')]
#print (data)
#print(solve1(data))
print(solve3(data))