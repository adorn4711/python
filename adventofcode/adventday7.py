import re 
import sys
from collections import defaultdict

print ("Day7")
def fillDict(data):
    bags =  defaultdict(list)
    bagsP =  defaultdict(list)

    for i in range(len(data)):
        line = data[i]
        parentStr,childrenStr = line.split("contain")
        pColor1,pColor2,dummy = parentStr.strip().split(" ");
        rootBag = pColor1+" "+ pColor2
        children = childrenStr.split(",")
        for child in children:
            #print (child.strip())
            if not child.strip().startswith("no"):
                childBagNo,color1,color2,dummyBag = child.strip().split(" ")
                #print (color1,color2)
                childBag = color1+" "+color2
                bags[childBag].append(rootBag)
                bagsP[rootBag].append((childBag,childBagNo))

    return bagsP
    
def countRoots(bags,childBag,ident):
   sum = set()
   sum.add(childBag)
   if not childBag in bags.keys():
        return sum
   for e in bags[childBag]:
        #print(ident,e)
        child = countRoots(bags,e,ident+"-")
        #print(child)
        sum = sum.union(child)
   return sum    

def countChildren(bags,parentBag,ident):
   sum = 1
   if not parentBag in bags.keys():
        return 1
   for e in bags[parentBag]:
        factor = int(e[1])
        factor *=  countChildren(bags,e[0],ident+"-")
        print(ident,e,factor)
        sum += factor
        #print(child)
   return sum    

        
data = [line.strip() for line in open("input_day7.txt", 'r')]
#data = [line.strip() for line in open("input_day7_sample.txt", 'r')]
bags = fillDict(data) 

print(bags)
print(countChildren(bags,"shiny gold","")-1)
#bagsSet = countRoots(bags,"shiny gold","")
#print(len(bagsSet)-1)