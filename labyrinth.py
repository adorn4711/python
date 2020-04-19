# class for show a labyrinth
#from labyrinth import Labyrinth
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
        self.__border_y = len(self.__map)
        for y,line in enumerate(self.__map):
            self.__border_x = len(line)
            for x,col in enumerate(line):
                if col==self.__const_wall or col=="q" or col =="%" :
                    self.__map[y][x] = self.__const_wall
                if col==self.__const_bot or col=="m" or col=="P":
                    self.__map[y][x] = self.__const_bot
                    self.__bot_x = x
                    self.__bot_y = y
                    self.__start_bot=(self.__bot_x,self.__bot_y)
                    self.__path_position.append((self.__bot_x,self.__bot_y))
                if col==self.__const_princess or col=="g" or col == "." :
                    self.__map[y][x] = self.__const_princess
                    self.__princess_x = x
                    self.__princess_y = y
    def reset(self):
        for y in range(self.__border_y):
            for x in range(self.__border_x):
                if (self.__map[y][x] ==self.__const_visited):
                    self.__map[y][x] = self.__const_empty

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

    def setBotToStart(self):
        self.__map[self.__bot_y][self.__bot_x] = self.__const_visited
        (self.__bot_x,self.__bot_y)=self.__start_bot
        self.__map[self.__bot_y][self.__bot_x] = self.__const_bot
        self.__isPrincessFound = False
        self.reset()

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

    def getGrid(self):
        return self.__map

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
    def getStartBotPos(self):
            return self.__start_bot
    def getSize(self):
        return (self.__border_x,self.__border_y)

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

    def getPath(self):
        return self.__path
    def setPath(self,path):
        self.__path=path

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
    labyrinth = Labyrinth(grid)
    #labyrinth = Labyrinth([],20,7,pacman)
    labyrinth.print()
    #labyrinth.find_princess()
    #labyrinth.command("u")
    #labyrinth.print()
    #labyrinth.command("d")
    #labyrinth.print()
    #labyrinth.command("l")
    #labyrinth.print()
    #labyrinth.command("l")
    #labyrinth.print()
