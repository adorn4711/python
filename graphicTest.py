from tkinter import *
import numpy as np
import cv2
import glob
import os

root = Tk()
path ="C:\\Users\\Andreas\\Documents\\python\\"
logo = PhotoImage(file=path+"Pacman_Tileset.png")
canvas = Canvas(root,  width=400, height=400)
canvas.pack()
#dir = "."
#pathname = os.path.join(dir, "*" + ".png")
#print(glob.glob(pathname))
#img = PhotoImage(file=path+"Pacman_Tileset.png")
image = cv2.imread(path+"Pacman_Tileset.png")
#image = cv2.imread(path+"pacman.ico")
startX=47
startY=0
new_width=40
new_height=42
endX=startX+new_width
endY=startY+new_height
currentTile = image[startY:endY, startX:endX]
cv2.imshow('image',image)
#cv2.imshow('image',currentTile)
#cv2.imwrite('onePacman.png',currentTile)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
#Bcanvas.create_image(10, 10, anchor=NW, image=image)
#canvas.create_image(img,(10,10),(20,20),(30,30),(40,40))
#myLabel = Label(root,image=logo)
#myLabel.pack()

#root.mainloop()
