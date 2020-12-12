import re 
import sys
from collections import defaultdict

print ("Day12")
def sign(x):
    if x>0: return 1
    if x<0: return -1
    return 0
class Ship:
    def __init__(self):
        self.pos_x=0
        self.pos_y=0
        self.wpos_x=10
        self.wpos_y=-1
        self.direction_x=1
        self.direction_y=0
        
    
    def north(self,distance):
        self.wpos_y -= distance
    def south(self,distance):
        self.wpos_y += distance
    def west(self,distance):
        self.wpos_x -= distance
    def east(self,distance):
        self.wpos_x += distance
    def left(self,degree):
        steps = degree//90
        for _ in range(steps):
            self.oneLeftW()
    def oneLeftW(self):
        self.right(270)
    def oneLeft(self):
        if sign(self.wpos_x) ==-1 and sign(self.wpos_y) ==0:
                self.direction_x = 0
                self.direction_y = 1
        elif sign(self.wpos_x) ==0 and sign(self.wpos_y) ==1:
                self.direction_x = 1
                self.direction_y = 0
        elif sign(self.wpos_x) ==1 and sign(self.wpos_y) ==0:
                self.direction_x = 0
                self.direction_y = -1
        elif sign(self.wpos_x) ==0 and sign(self.wpos_y) ==-1:
                self.direction_x = -1
                self.direction_y = 0
    def right(self,degree):
        steps = degree//90
        for _ in range(steps):
            self.oneRightW()
    def oneRightW(self):
        temp =self.wpos_x
        self.wpos_x =-self.wpos_y
        self.wpos_y =temp
          
    def oneRight(self):
        if self.direction_x ==-1 and self.direction_y ==0:
                self.direction_x = 0
                self.direction_y = -1
        elif self.direction_x ==0 and self.direction_y ==-1:
                self.direction_x = 1
                self.direction_y = 0
        elif self.direction_x ==1 and self.direction_y ==0:
                self.direction_x = 0
                self.direction_y = 1
        elif self.direction_x ==0 and self.direction_y ==1:
                self.direction_x = -1
                self.direction_y = 0
    def forward(self,distance):
        self.pos_x += self.wpos_x*distance 
        self.pos_y += self.wpos_y*distance 
    def backward(self,distance):
        self.pos_x -= self.direction_x*distance 
        self.pos_y -= self.direction_y*distance 
    def drive(self,command):
        cmd=command[0:1]
        if cmd == "L":
            degree = int(command[1:])
            self.left(degree)
            return (command,self.wpos_x,self.wpos_y,self.pos_x,self.pos_y)
        if cmd == "R":
            degree = int(command[1:])
            self.right(degree)
            return (command,self.wpos_x,self.wpos_y,self.pos_x,self.pos_y)
        distance = int(command[1:])
        if cmd == "N": self.north(distance)
        if cmd == "S": self.south(distance)
        if cmd == "E": self.east(distance)
        if cmd == "W": self.west(distance)
        if cmd == "F": self.forward(distance)
        if cmd == "B": self.backward(distance)
        return (command,self.wpos_x,self.wpos_y,self.pos_x,self.pos_y)
        
    def getPosition(self):
        return(self.pos_x,self.pos_y,abs(self.pos_x)+abs(self.pos_y))            
        
def drive(data):
    ship = Ship()
    for line in data:
        print(ship.drive(line))
    print (ship.getPosition())    
          
data = [line.strip() for line in open("input_day12_sample.txt", 'r')]
data = [line.strip() for line in open("input_day12.txt", 'r')]
drive(data)
#data = [line.strip() for line in open("input_day8_sample.txt", 'r')]
#print (data)
