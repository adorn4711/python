

def nextMove(posr, posc, board):
#print all the moves here
    #print(grid)
    firstMove="none"
    bot_x = posc
    bot_y = posr
    for y in range(len(board)):
        for x in range(len(board[y])):
            #print(x,y,grid[y][x])
            char = board[y][x]
            if (char == 'b'):
                bot_x = x
                bot_y = y
            if (char == 'd'):
                princess_x = x
                princess_y = y
    #print("Princess",princess_x,princess_y)
    #print("Bot",bot_x,bot_y)
    x_run = princess_x - bot_x
    y_run = princess_y - bot_y
    if (x_run==0 and y_run==0):
        return "CLEAN"
    #print("way",x_run,y_run)
    if(x_run>0):
        command_x="RIGHT"
    else:
        command_x="LEFT"
    for i in range(abs(x_run)):
        #print(command_x)
        return command_x
    if(y_run>0):
        command_y="DOWN"
    else:
        command_y="UP"
    for i in range(abs(y_run)):
        #print(command_y)
        return command_y
    #print("command",command_x,command_y)
#m = int(input())
#grid = []
#for i in range(0, m):
    #grid.append(input().strip())
m=3
grid =[["b","-","-"],
       ["-","-","-"],
       ["d","-","-"]
       ]
print(nextMove(0,0,grid))
