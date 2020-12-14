import re 
import sys
from collections import defaultdict

print ("Day14")


def readMask(maskline):
    mask0 = ""
    mask1 = ""
    for maskbit in maskline:
        if maskbit == "X":
            mask0 += "1"
            mask1 += "0"
        if maskbit == "1":
            mask0 += "1"
            mask1 += "1"
        if maskbit == "0":
            mask0 += "0"
            mask1 += "0"
    return mask0, mask1          

def readAddressMask(address,addressMask):
    addressFloating =[]
    i = len(addressMask)-1

    for maskbit in addressMask:
        if maskbit == "X":
            p =2**i
            if len(addressFloating) >0:
                addressFloating1 =[p+i for i in addressFloating]
                addressFloating += addressFloating1
            addressFloating.append(p)
            address = address - (address & p)
        if maskbit == "1":
            p =2**i
            address = (p | address)
        i -=1
    addressFloating.append(0) 
    #print(address,sorted(addressFloating))
    addressList = [address+x for x in sorted(addressFloating)]
    #print(addressList)
    return  addressList        



def solution(data,solution):
    memory = defaultdict(list)
    for line in data:
        command,valuestr = line.split("=")
        if command.strip()=="mask":
            mask0, mask1 = readMask(valuestr.strip())
            addressmask =valuestr.strip()
            #print(mask0,mask1)
        else:    
            mem1 = command.split("[")
            mem2 = mem1[1].split("]")
            address =mem2[0]
            #print (command,memnr,valuestr)
            value = int(valuestr)
            #print (value)
            #value = (int(mask1,2) | value)
            #value = (int(mask0,2) & value)
            #print (value)
            if (solution ==1):
                value = (int(mask1,2) | value)
                value = (int(mask0,2) & value)
                memory[address]=value
            if (solution ==2):
                adressfloating = readAddressMask(int(address),addressmask)
                for j in adressfloating:
                    memory[j]=value
                  
            
    mysum = sum(memory.values())    
    return mysum




                  
data = [line.strip() for line in open("input_day14_sample.txt", 'r')]
data = [line.strip() for line in open("input_day14.txt", 'r')]

#print (solution(data,1))    
print (solution(data,2))    
