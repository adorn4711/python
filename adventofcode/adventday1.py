print ("day1")
def calc(data):
    for i in range(len(data)):
        for j in range(i,len(data)):
            for k in range(j,len(data)):
                if int(data[i])+int(data[j])+int(data[k]) == 2020:
                    return  int(data[i])*int(data[j])*int(data[k])
        
        
data = [line.strip() for line in open("input.txt", 'r')]
#print (data)
print (calc(data))
