import re 
import sys
print ("Day5")
    
def getSeat(data):
    highestSeat =0
    seatList =set()
    for line in data:
        binary = line.replace('F','0').replace('B','1').replace('R','1',).replace('L','0')
        currentSeat = int(binary,base = 2)
        #print(binary,currentSeat)
        if (currentSeat > highestSeat):
            highestSeat = currentSeat
        seatList.add(currentSeat)
    fullList = set()   
    for i in range(highestSeat):
        fullList.add(i)
        
    return fullList - seatList    
        
data = [line.strip() for line in open("input_day5.txt", 'r')]
#print(data)
testlist =['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']
print(getSeat(data))