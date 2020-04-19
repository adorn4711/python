import tkinter as tk
from labyrinth import Labyrinth
from dfs_search import DFS_search

class Labyrinth_field:

    def __init__(self,window,type,pos):
        self.CONST_BOT ="b"
        self.CONST_PRINCESS ="p"
        self.CONST_EMPTY = "-"
        self.CONST_WALL = "#"
        self.CONST_VISITED = "."
        path ="C:\\Users\\Andreas\\Documents\\python\\images\\"
        self.__images={}

        self.__images[self.CONST_BOT] = tk.PhotoImage(file=path+"onePacman.png")
        self.__images[self.CONST_PRINCESS] = tk.PhotoImage(file=path+"varroa.png")
        self.__images[self.CONST_WALL] = tk.PhotoImage(file=path+"honigtropfen.png")
        self.__images[self.CONST_VISITED] = tk.PhotoImage(file=path+"honigtropfen.png")
        self.__images[self.CONST_EMPTY] = tk.PhotoImage(file=path+"honigtropfen.png")


        self.__text = tk.StringVar()
        self.__pos = pos
        self.__widget=tk.Label(window,width=32,height=32,textvariable=self.__text)
        self.__widget.grid(row=pos[1],column=pos[0])
        self.change_type(type)

    def deleteVisited(self):
        if (self.__type ==self.CONST_VISITED):
            self.change_type(self.CONST_EMPTY)

    def change_type(self,new_type):
        self.__type = new_type;
        self.__text.set("")

        self.__widget.config(image = self.__images[self.__type])
        self.__widget.photo_ref=self.__images[self.__type]
        if self.__type == self.CONST_EMPTY:
            self.__widget.grid_remove()
        else:
            self.__widget.grid()

    def print(self):
        print(self.__pos)


class Labyrinth_graphik:
    def __init__(self):
        self.__root =  tk.Tk()
        #self.__label = Label(self.__root,text="Hello World")
        #self.__label.pack()
        self.__map = []
        self.__labyrinth=[[]]

    def load_labyrinth(self,labyrinth):
        self.__labyrinth = labyrinth
        self.__noCommand = None;
        for i_y,line in enumerate(labyrinth.getGrid()):
            self.__map.append([])
            for i_x,fieldList in enumerate(line):
                field = Labyrinth_field(self.__root,fieldList,(i_x,i_y))
                self.__map[i_y].append(field)
        self.__start_bot=self.__labyrinth.getPos()
        myButton=tk.Button(self.__root,text="NextStep",command=self.nextStep)
        size=self.__labyrinth.getSize();
        myButton.grid(row=size[0]+1,column=0,columnspan=size[1])

    def storePath(self):
        self.__path =list(self.__labyrinth.getPath())
    def setBotToStart(self):
        oldPos = self.__labyrinth.getPos()
        newPos = self.__labyrinth.getStartBotPos()
        self.bot_move(oldPos,newPos)
        self.__labyrinth.setBotToStart()
        (border_x,border_y)=self.__labyrinth. getSize()
        for y in range(border_y):
            for x in range(border_x):
                self.__map[y][x].deleteVisited()


    def bot_move(self,oldPos,newPos):
        feld =self.__map[oldPos[1]][oldPos[0]]
        self.__map[oldPos[1]][oldPos[0]].change_type(feld.CONST_EMPTY)
        self.__map[newPos[1]][newPos[0]].change_type(feld.CONST_BOT)

    def command(self,command):
        oldPos = self.__labyrinth.getPos()
        #print("OldPos:",oldPos)
        canIMove = self.__labyrinth.command(command)
        if (canIMove):
            self.bot_move(oldPos,self.__labyrinth.getPos())
        #print("newPos:",self.__labyrinth.getPos())


    def mainloop(self):
        self.__root.mainloop()
    def nextStep(self):
        commandList = self.__path
        if (self.__noCommand == None):
            self.__noCommand=0
        if (self.__noCommand< len(commandList)):
            #print(commandList)
            self.command(commandList[self.__noCommand])
            if (self.__labyrinth.isPrincessFound()):
                print("Princess found")
            print(len(commandList),self.__noCommand,commandList[self.__noCommand])
            self.__noCommand +=1
        else:
            print("Princess found in graphic")




if __name__ == '__main__':
    grid =[["-","-","-","-","-"],
       ["-","m","#","-","-"],
       ["p","-","-","-","-"]
       ]
    pacman ="""%%%%%%%%%%%%%%%%%%%%
%--------------%---%
%-%%-%%-%%-%%-%%-%-%
%--------P-------%-%
%%%%%%%%%%%%%%%%%%-%
%.-----------------%
%%%%%%%%%%%%%%%%%%%%"""

    #labyrinth = Labyrinth(grid)
    labyrinth = Labyrinth([],20,7,pacman)
    #l_graphik.bot_move((1,1),(0,1))
    dfsSearch = DFS_search(labyrinth)
    #dfsSearch.add("ldru")
    dfsSearch.move()
    dfsSearch.print_position_path()
    path = labyrinth.getPath();

    l_graphik = Labyrinth_graphik()
    l_graphik.load_labyrinth(labyrinth)
    l_graphik.storePath()
    l_graphik.setBotToStart()
    l_graphik.mainloop()
