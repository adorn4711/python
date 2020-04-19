class Labyrinth(object):



    def __init__(self,grid =[],len_x =0,len_y=0,str =""):
        if (len(grid)>0):
            self.__map = grid
        if (len(str)>0):
            self.fill_grid(len_x,len_y,str)

        self.__init_fields()

    def __init_fields(self):
        self.__const_bot ="b"
        self.__const_princess ="p"
        self.__const_empty = "-"
        self.__const_wall = "#"
        self.__const_border = "##"
        self.__const_visited = "."
        self.__direction = "u"
        self.__moves =0
        self.__path = []
        self.__path_position =[]

        self.__bot_x = -1
        self.__bot_y = -1
        self.__princess_x = -1
        self.__princess_y = -1
        self.__testedField =self.__const_bot
        self.__isPrincessFound = False
        self.normalize()

    def fill_grid(self,len_x,len_y,str):
        self.__map = []
        pos=0
        for y in range(len_y):
            line = []
            for x in range(len_x):
                char =str[pos]
                if (char =="\n"):
                    pos +=1
                    char =str[pos]
                line.append(char)
                pos +=1
            self.__map.append(line)

    def normalize(self):
        x=0
        y=0
        for line in self.__map:
            x=0
            for col in line:
                if col==self.__const_wall or col=="q" or col =="%" :
                    self.__map[y][x] = self.__const_wall
                if col==self.__const_bot or col=="m" or col=="P":
                    self.__map[y][x] = self.__const_bot
                    self.__bot_x = x
                    self.__bot_y = y
                    self.__path_position.append((self.__bot_x,self.__bot_y))
                if col==self.__const_princess or col=="g" or col == "." :
                    self.__map[y][x] = self.__const_princess
                    self.__princess_x = x
                    self.__princess_y = y

                x +=1
            y +=1
        self.__border_x =x
        self.__border_y =y

    def down(self):
        moveSuccessful = False
        self.__direction = "d"
        if self.__bot_y < self.__border_y -1:
            moveSuccessful = self.__move(0,1)
        else:
            self.__setBorder()
        return moveSuccessful

    def up(self):
        moveSuccessful = False
        self.__direction = "u"
        if self.__bot_y > 0:
            moveSuccessful = self.__move(0,-1)
        else:
            self.__setBorder()
        return moveSuccessful

    def right(self):
        moveSuccessful = False
        self.__direction = "r"
        if self.__bot_x < self.__border_x -1:
            moveSuccessful = self.__move(1,0)
        else:
            self.__setBorder()
        return moveSuccessful

    def left(self):
        moveSuccessful = False
        self.__direction = "l"
        if self.__bot_x > 0:
            moveSuccessful = self.__move(-1,0)
        else:
            self.__setBorder()
        return moveSuccessful


    def __move(self,x,y):
        self.__map[self.__bot_y][self.__bot_x] = self.__const_visited
        self.__bot_x +=x
        self.__bot_y +=y
        self.check()
        moveSuccessful =self.canIMove()
        if (moveSuccessful):
            self.__moves +=1
            self.__path.append(self.__direction)
            self.__path_position.append((self.__bot_x,self.__bot_y))
        else:
            self.__bot_x -=x
            self.__bot_y -=y
        self.__map[self.__bot_y][self.__bot_x] = self.__const_bot
        return moveSuccessful

    def __setBorder(self):
        self.__testedField = self.__const_border

    def check(self):
        self.__testedField = self.__map[self.__bot_y][self.__bot_x]
        if (not self.isPrincessFound() ):
            self.__isPrincessFound = self.__testedField == self.__const_princess
            if (self.__isPrincessFound):
                self.__path_position.append((self.__bot_x,self.__bot_y))


    def canIMove(self):
        return self.__testedField == self.__const_empty or self.__testedField == self.__const_visited

    def isPrincessFound(self):
        return self.__isPrincessFound

    def isVisited(self):
        return self.__testedField == self.__const_visited


    def command(self,command):
        self.__direction = command
        if (command == "l"):
            return self.left()
        if (command == "r"):
            return self.right()
        if (command == "u"):
            return self.up()
        if (command == "d"):
            return self.down()

    def nextPosition(self,command):
        if (command == "l"):
            return (self.__bot_x-1,self.__bot_y)
        if (command == "r"):
            return (self.__bot_x+1,self.__bot_y)
        if (command == "u"):
            return (self.__bot_x,self.__bot_y-1)
        if (command == "d"):
            return (self.__bot_x,self.__bot_y+1)

    def move(self):
        self.command(self.__direction)
        return self.canIMove()

    def move_back(self,command):
        if (command == "l"):
            return self.right()
        if (command == "r"):
            return self.left()
        if (command == "u"):
            return self.down()
        if (command == "d"):
            return self.up()



    def turn(self):
        if (self.__direction == "r"):
            self.__direction = "d"
        elif (self.__direction == "d"):
            self.__direction = "l"
        elif (self.__direction == "l"):
            self.__direction = "u"
        elif (self.__direction == "u"):
            self.__direction = "r"
    def turn_anti_clock(self):
        if (self.__direction == "r"):
            self.__direction = "u"
        elif (self.__direction == "u"):
            self.__direction = "l"
        elif (self.__direction == "l"):
            self.__direction = "d"
        elif (self.__direction == "d"):
            self.__direction = "r"

    def getPos(self):
        return (self.__bot_x,self.__bot_y)

    def print(self):
        print("####")
        self.print_labyrinth()
        self.print_bot()


    def print_labyrinth(self):
        for line in self.__map:
            print(line)
    def print_bot(self):
        print("{0:d} Bot({1:d},{2:d},{3:s})".format(self.__moves,self.__bot_x ,self.__bot_y,self.__direction))
        print("Path",self.__path)
        print("Path position",self.__path_position)
    def print_position_path(self):
        print(len(self.__path_position))
        for pos in self.__path_position:
            print(pos[1],pos[0])

    def getMoves(self):
        return self.__moves

        def find_princess(self):
            self.move()
            self.print()
            moves=0
            while (not self.isPrincessFound()  and self.getMoves() <100):
                if (not self.canIMove()):
                    self.turn()
                    self.print_bot()
                self.move()
                self.print()



class DFS_search:
    def __init__(self,labyrinth):
        self.__labyrinth = labyrinth
        self.__future_way = []
        self.__visited = set()

    def print(self):
        self.__labyrinth.print()

    def print_position_path(self):
        self.__labyrinth.print_position_path()

    def find_princess(self):
            self.__labyrinth.move()
            self.__labyrinth.print()
            while (not self.__labyrinth.isPrincessFound()  and self.__labyrinth.getMoves() <100):
                if (not self.__labyrinth.canIMove()):
                    self.__labyrinth.turn()
                    self.__labyrinth.print_bot()
                self.__labyrinth.move()
                self.__labyrinth.print()
    def add(self,way):
        self.__future_way += [char for char in way]
        print(self.__future_way)


    def move(self,level = 0,lastCommand="k"):
        if (self.__labyrinth.getPos() in self.__visited):
            #print("Move back uuu",lastCommand,self.__labyrinth.move_back(lastCommand))
            self.__labyrinth.print()
            return False
        self.__visited.add(self.__labyrinth.getPos())
        #self.__labyrinth.print()
        if (self.__labyrinth.getMoves()<100):
            #print("Level",level,self.__visited)
            for command in ['r','u','l','d']:
                #print("try",command)
                nextPos = self.__labyrinth.nextPosition(command)
                if (not nextPos in  self.__visited):
                    canIMove = self.__labyrinth.command(command)
                    if (self.__labyrinth.isPrincessFound()):
                        #print("Level",level,"Princess found")
                        return True
                    if (canIMove):
                        if (self.move(level+1,command)):
                            return True
            status = self.__labyrinth.move_back(lastCommand)
            #print("Move back",lastCommand,status)
            #self.__labyrinth.print()




if __name__ == '__main__':
    #m = int(input())
    #grid = []
    #for i in range(0, m):
        #grid.append(input().strip())
    #m=3
    grid =[["-","-","-","-"],
       ["-","m","#","-"],
       ["p","-","-","-"]
       ]

    pacman ="""%%%%%%%%%%%%%%%%%%%%
%--------------%---%
%-%%-%%-%%-%%-%%-%-%
%--------P-------%-%
%%%%%%%%%%%%%%%%%%-%
%.-----------------%
%%%%%%%%%%%%%%%%%%%%"""
    #print(pacman)
    #labyrinth = Labyrinth(grid)
    editor = False
    #editor = True
    if (not editor):
        bot_x,bot_y = map(int, input().split())
        princess_x,princess_y = map(int, input().split())
        border_x,border_y = map(int, input().split())
        grid =[]
        for i in range(border_x):
            line = []
            for ch in input():
                line.append(ch)
            grid.append(line)
        #print(grid)
        labyrinth = Labyrinth(grid)
    else:
        labyrinth = Labyrinth([],20,7,pacman)
    dfsSearch = DFS_search(labyrinth)
    #dfsSearch.add("ldru")
    dfsSearch.move()
    dfsSearch.print_position_path()


    #dfsSearch.print()
    #dfsSearch.move()
    #dfsSearch.find_princess()
    #labyrinth.command("u")
    #labyrinth.print()
    #labyrinth.command("d")
    #labyrinth.print()
    #labyrinth.command("l")
    #labyrinth.print()
    #labyrinth.command("l")
    #labyrinth.print()
