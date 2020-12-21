import re 
import sys
from collections import defaultdict

print ("Day17")


def read(data):
    puzzle = set()
    x,y = 0,0
    for line in data:
        for cell in line:
            if cell == '#':
                puzzle.add((x,y,0,0))
            x +=1
        x = 0    
        y +=1        
    return puzzle    

def draw(puzzle):
    if len(puzzle)==0:
        return ""
    minx,miny,minz,minw = list(puzzle)[0]
    maxx,maxy,maxz,maxw = list(puzzle)[0]
    for x,y,z,w in puzzle:
        if x<minx: minx=x
        if x>maxx: maxx=x
        if y<miny: miny=y
        if y>maxy: maxy=y
        if z<minz: minz=z
        if z>maxz: maxz=z
        if w<minw: minw=w
        if w>maxw: maxw=w
    for w in range(minw,maxw+1):
        for z in range(minz,maxz+1):
            print ("w="+str(w)+"z="+str(z))        
            for y in range(miny,maxy+1):
                line=str(y)+":"
                for x in range(minx,maxx+1):
                    if (x,y,z) in puzzle:
                        line +="#"
                    else:    
                        line +="."
                print (line)  
                  
def grow(oldGeneration):
    newGeneration = set()
    allNeighbors =set()
    for x,y,z,w in oldGeneration:
        count =0
        for dx in range(-1,2):
            for dy in range(-1,2):
                for dz in range(-1,2):
                    for dw in range(-1,2):
                        if (dx==0 and dy==0 and dz==0 and dw==0): continue
                        allNeighbors.add((x+dx,y+dy,z+dz,w+dw))
                        if (x+dx,y+dy,z+dz,w+dw) in oldGeneration:
                            count +=1
        #print(x,y,z,count)                 
        if count ==2 or count ==3:
            newGeneration.add((x,y,z,w))                    
    for x,y,z,w in allNeighbors:
        count =0
        for dx in range(-1,2):
            for dy in range(-1,2):
                for dz in range(-1,2):
                    for dw in range(-1,2):
                        if (x+dx,y+dy,z+dz,w+dw) in oldGeneration:
                            count +=1 
        if count ==3:
            newGeneration.add((x,y,z,w))                    
    return newGeneration,len(newGeneration)
        
data = [line.strip() for line in open("input_day17_sample.txt", 'r')]
data = [line.strip() for line in open("input_day17.txt", 'r')]
puzzle = read(data)
print(sorted(puzzle))
draw(puzzle)
for i in range(6):
    puzzle,numItems =  grow(puzzle)
    print(numItems)
    #draw(puzzle)
    
#print(grow(puzzle))
#data = "0,3,6"
#data = "2,1,3"
#print(solution(data))
#print (solution(data,1))    
#print (solution(data,2))    
