print ("Day3")
def countTree(data,right,down):
    tree =0
    x =0
    i = 0
    while i<len(data):
        line = data[i]
        l = len(line)
        #print (l)
        if (line[x]=='#'):
            tree +=1
        x = (x +right) % l
        #print (line)    
        i +=down
    return tree
    
    
        
        
data = [line.strip() for line in open("input_day3.txt", 'r')]
#print (data)
count =1
count *= countTree(data,1,1)
count *= countTree(data,3,1)
count *= countTree(data,5,1)
count *= countTree(data,7,1)
count *= countTree(data,1,2)
print(count)