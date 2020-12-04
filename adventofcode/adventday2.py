print ("Hello World")
def findPassword(data):
    valid = 0;
    for i in range(len(data)):
    #for i in range(1):
        line = data[i]
        x = line.split()
#        print (x)
        r = x[0].split("-")
        letter = x[1][0:1]
        count = x[2].count(letter)
#        print (r[0],r[1],letter,count)
        password = x[2]
#        print(password)
#        print (int(r[0])-1)
#        print ("pos2")
#        print (int(r[1])-1)
        pos1valid = password[int(r[0])-1]==letter
        pos2valid = password[int(r[1])-1]==letter
        if (pos1valid and not pos2valid):
            valid +=1
        if (pos2valid and not pos1valid):
            valid +=1
    return valid
    
        
        
data = [line.strip() for line in open("input_day2.txt", 'r')]
#print (data)
print(findPassword(data))