from labyrinth import Labyrinth
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
            #self.__labyrinth.print()
            return False
        self.__visited.add(self.__labyrinth.getPos())
        self.__labyrinth.print()
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
            print("Move back",lastCommand,status)
            self.__labyrinth.print()




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

    pacman2 ="""%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%------------%%------------%
%-%%%%-%%%%%-%%-%%%%%-%%%%-%
%.%%%%-%%%%%-%%-%%%%%-%%%%-%
%-%%%%-%%%%%-%%-%%%%%-%%%%-%
%--------------------------%
%-%%%%-%%-%%%%%%%%-%%-%%%%-%
%-%%%%-%%-%%%%%%%%-%%-%%%%-%
%------%%----%%----%%------%
%%%%%%-%%%%%-%%-%%%%%-%%%%%%
%%%%%%-%%%%%-%%-%%%%%-%%%%%%
%%%%%%-%------------%-%%%%%%
%%%%%%-%-%%%%--%%%%-%-%%%%%%
%--------%--------%--------%
%%%%%%-%-%%%%%%%%%%-%-%%%%%%
%%%%%%-%------------%-%%%%%%
%%%%%%-%-%%%%%%%%%%-%-%%%%%%
%------------%%------------%
%-%%%%-%%%%%-%%-%%%%%-%%%%-%
%-%%%%-%%%%%-%%-%%%%%-%%%%-%
%---%%----------------%%---%
%%%-%%-%%-%%%%%%%%-%%-%%-%%%
%%%-%%-%%-%%%%%%%%-%%-%%-%%%
%------%%----%%----%%------%
%-%%%%%%%%%%-%%-%%%%%%%%%%-%
%------------P-------------%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%"""

    #print(pacman)
    #labyrinth = Labyrinth(grid)
    editor = False
    editor = True
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
        #labyrinth = Labyrinth([],28,27,pacman2)
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
