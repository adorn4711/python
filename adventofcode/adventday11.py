#import re 
#import sys
from collections import defaultdict

seats =[]
def fill(data):
    for line in data:
        seats.append([[char,-1,True] for char in line])
    #print (seats)

def getNum1():
    directions =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for x in range(len(seats)):
        for y in range(len(seats[x])):
            s=0
            for dx,dy in directions:
                if x+dx<0: continue
                if x+dx>=len(seats): continue
                if y+dy<0: continue
                if y+dy>=len(seats[x]): continue
                if seats[x+dx][y+dy][0]=='#':
                    s +=1
            if seats[x][y] != '.':
                seats[x][y][1]=s            

def getNum():
    directions =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for x in range(len(seats)):
        for y in range(len(seats[x])):
            s=0
            for dx,dy in directions:
                f =1
                found = False
                while not found and 0<=x+f*dx<len(seats) and 0<=y+f*dy<len(seats[x]):
                    if seats[x+f*dx][y+f*dy][0]=='#':
                        s +=1
                    if seats[x+f*dx][y+f*dy][0]!='.':   
                        found = True
                    f +=1        
            if seats[x][y] != '.':
                seats[x][y][1]=s            

   
def reseat():
    for x in range(len(seats)):
        for y in range(len(seats[x])):
            if seats[x][y][0] != '.':
                seats[x][y][2] = False 
                if seats[x][y][0] == 'L' and  seats[x][y][1] == 0:    
                    seats[x][y][0] = '#'
                    seats[x][y][2] = True
                else:         
                    if seats[x][y][0] == '#' and  seats[x][y][1] >=5:    
                        seats[x][y][0] = 'L'      
                        seats[x][y][2] = True
def show():
    print("-------------------------------------")
    for x in range(len(seats)):
        s =""
        for y in range(len(seats[x])):
            s += str(seats[x][y][1])
        s +="     "
        #s =""
        for y in range(len(seats[x])):
            s += str(seats[x][y][0])
        print(s)
        
            
def count():
    s =0
    changed = False
    for x in range(len(seats)):
        for y in range(len(seats[x])):
            if seats[x][y][0] != '.':
                changed = changed or seats[x][y][2]
                if seats[x][y][0] == '#' :
                    s +=1
    
    return s,changed
                
print ("Day11")


data = [(line.strip()) for line in open("input_day11.txt", 'r')]
#print (data)
#print(solve1(data))
fill(data)
changed = True
while changed:
    getNum()
    reseat()
    #show()
    s,changed =count()
    #print (s)
print ("Solution",s)    