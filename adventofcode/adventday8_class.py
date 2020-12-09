import re 
import sys
from collections import defaultdict

print ("Day8")
class Computer:
    def __init__(self,data):
        self.compile(data)
        self.program_copy = self.program.copy()
    
    def reset(self):
        self.program = self.program_copy.copy()
    def changeCode(self,lineNr,instruction):
        newLine = (instruction,self.program[lineNr][1])
        self.program[lineNr]=newLine
    def changeArgument(self,line,arg):
        newLine = (self.program[lineNr][0],arg)
        self.program[lineNr]=newLine
    def compile(self,data):
        self.program = []
        self.instList=defaultdict(list)
        nopList=[]
        jmpList=[]
        pc= 0
        for line in data:
           instruction,arg = line.split(" ")
           self.program.append((instruction,arg))
           self.instList[instruction].append(pc)
           pc +=1  

    def run(self):
        pc =0
        acc = 0
        visited = set()
        lenPrg=len(self.program)
        while pc<lenPrg:
            instruction,arg = self.program[pc]
            if pc in visited:
                break
            visited.add(pc)
            if instruction == "acc":
                acc += int(arg)
                pc +=1
            if instruction == "jmp":
                pc += int(arg)
            if instruction == "nop":
                pc +=1
            #print(pc,acc)    
        #print ("end:",acc)
        terminated = pc == lenPrg
        return (acc,terminated)
        
    def print(self):
        print(self.instList)

def solve(data):
  computer = Computer(data);
  lastAcc,terminated = computer.run()
  if terminated:
    return lastAcc
  for (original,replace) in [("jmp","nop"),("nop","jmp")]:     
      for i in computer.instList[original]:
        computer.reset()
        computer.changeCode(i,replace)
        lastAcc,terminated = computer.run()
        if terminated:
            return lastAcc


data = [line.strip() for line in open("input_day8.txt", 'r')]
#data = [line.strip() for line in open("input_day8_sample.txt", 'r')]
#print (data)
computer = Computer(data);
#computer.print()
print(computer.run())
print(solve(data))

