import re 
import sys
from collections import defaultdict

print ("Day16")

def read(data):
    section =0
    formats=[]
    nearbyList=[]
    for line in data:
        if len(line)==0: continue
        if line == "your ticket:":
            section =1
            continue
        if line == "nearby tickets:":
            section =2
            continue
        if section == 0:
            #print(section,line)
            r = line.split(":")
            f = r[1].split("or")
            n1 = f[0].strip().split("-")
            n2 = f[1].strip().split("-")
            formats.append((int(n1[0]),int(n1[1]),int(n2[0]),int(n2[1])))
        if section ==1:
            myTicket = line.strip().split(",")    
        if section ==2:
            nearby = line.strip().split(",")
            value=[nearby]
            emptySet = set()
            value.append(emptySet)
            nearbyList.append(value)    
    return formats,myTicket,nearbyList

def solution(formats,nearby):
    for ticket in nearby:
        for ticketDataStr in ticket[0]:
            ticketData = int(ticketDataStr)
            pos =0
            for min1,max1,min2,max2 in formats:
                #print(min1,max1,min2,max2,ticketData)
                if min1 <=ticketData<=max1:
                    ticket[1].add(pos)
                if min2 <=ticketData<=max2:
                    ticket[1].add(pos)
                pos +=1     
        if len(ticket[1])==0:    
            nearby.remove(ticket)
    return nearby
                  
data = [line.strip() for line in open("input_day16_sample.txt", 'r')]
#data = [line.strip() for line in open("input_day16.txt", 'r')]

formats,myTicket,nearby = read(data)
print(formats)
print(myTicket)
print(nearby)
print( solution(formats,nearby))
#data = "0,3,6"
#data = "2,1,3"
#print(solution(data))
#print (solution(data,1))    
#print (solution(data,2))    
