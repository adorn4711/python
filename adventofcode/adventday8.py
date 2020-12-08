import re 
import sys
from collections import defaultdict

print ("Day8")
def compile(data):
    program = []
    nopList=[]
    jmpList=[]
    pc= 0
    for line in data:
       instruction,arg = line.split(" ")
       program.append((instruction,arg))
       if instruction == "jmp":
         jmpList.append(pc)
       if instruction == "nop":
         nopList.append(pc)
       pc +=1  
         
    return program,nopList,jmpList

def run(program):
    pc =0
    acc = 0
    visited = set()
    lenPrg=len(program)
    while pc<lenPrg:
        instruction,arg = program[pc]
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
        
    return acc,terminated

def solve(data):
  program,nopList,jmpList = compile(data)
  lastAcc,terminated = run(program)
  if terminated:
    return lastAcc
  for i in nopList:
    instruction,arg = program[i]
    program[i]=("jmp",arg)
    lastAcc,terminated = run(program)
    if terminated:
        return lastAcc
    program[i]=("nop",arg)
  for i in jmpList:
    instruction,arg = program[i]
    program[i]=("nop",arg)
    lastAcc,terminated = run(program)
    if terminated:
        return lastAcc
    program[i]=("jmp",arg)
        
    

data = [line.strip() for line in open("input_day8.txt", 'r')]
#data = [line.strip() for line in open("input_day8_sample.txt", 'r')]
#print (data)
program,nopList,jmpList = compile(data)
#print (program,nopList,jmpList)
#print (jmpList)

#print(run(program))
print(solve(data))