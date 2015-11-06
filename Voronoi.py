# Making Voronoi diagrams in the least efficient way possible

from Tkinter import *
import random, time, math

WIDTH = 400
HEIGHT = 400
size = 2


Vor= Tk()
Vor.title("Voronoi diagram")
canvas = Canvas(Vor, background="white", width=WIDTH, height=HEIGHT)
canvas.pack()


class Node():
    def __init__(self, (x, y), size, colour2):
        self.x = x
        self.y = y
        self.size = size
        self.colour = "black"
        self.colour2 = colour2

    def display(self):
        canvas.create_rectangle( (self.x ,self.y),(self.x+self.size ,self.y+self.size), fill = "black")


def random_colour():
	a = random.randint(0,255)
	b = random.randint(0,255)
	c = random.randint(0,255)
	return (a,b,c)


NodeList = []


def make_node(event):
	col = '#%02x%02x%02x' % random_colour()
	x,y = event.x,event.y
	tempnode = Node((x,y),size, col)
	tempnode.display()
	NodeList.append(tempnode)

	

def find_nearest_node(i,j,list):
	distance = 2 * WIDTH
	nearestnode = 0
	for k in range(len(list)):
		xtemp = NodeList[k].x
		ytemp = NodeList[k].y
		dist = math.sqrt( (xtemp - i)**2 + (ytemp - j)**2 )
		if dist < distance:
			distance = dist
			nearestnode = k
	
	tempcol = NodeList[nearestnode].colour2
	canvas.create_rectangle( (i ,j),(i+1, j+1), fill = tempcol, outline = tempcol)	
	


def Start():
	for i in range(0,WIDTH):
		for j in range(0,HEIGHT):
			find_nearest_node(i+1,j+1,NodeList)

	for i in range(len(NodeList)):
		NodeList[i].display()		

temp = {'quit':0}

def Quit():
	temp['quit'] += 1
	if temp['quit'] > 0:
		sys.exit()


canvas.bind("<Button-1>", make_node)


start = Button(Vor,text = "Ready?", command = Start)
start.pack(side = LEFT)
quit = Button(Vor,text = "Exit?", command = Quit)
quit.pack(side = RIGHT)



Vor.mainloop()

 