# Program: plot_random.py

from graphics import *
from random import *
import math

def main():

    win = GraphWin("2d Random Walk", 650, 650)
    win.setCoords(-100.0,-100.0,100.0,100.0)

    # Draw the interface.

    Text(Point(-20,-70), "Enter the number of steps for the random walk: ").draw(win)
    input = Entry(Point(45,-70),10)
    input.setText("1")
    input.draw(win)

    button = Text(Point(0,-85),"Start the Simulation")
    button.draw(win)
    Rectangle(Point(-25,-90),Point(25,-80)).draw(win)

    # Wait for a mouse click.
    
    win.getMouse()

    # Change the button.

    button.setText("Simulation in Progress")

    # Get the number of steps from the Entry box.
    
    N = eval(input.getText())

    # (x, y) gives the location of the sailor. (x_new,y_new)
    # gives the new location after taking one step. r gives
    # the length of a step.

    x = 0
    y = 0
    x_new = 0
    y_new = 0

    # NB. Pick r so that it divides into 90 AND 60 to give a whole nunmber.
    # So r = 1,2,3,5,6,10,15,30 are all acceptable.

    r = 3

    # It's a bit complicated because you have to deal with the four
    # corners and the four edges separately. When the sailor gets to
    # a corner, he only has two options. At an edge, he has three options.
    # In the interior, he has four options. 

    for i in range(N):
        theta = 2*math.pi*random()
        R = 65
        D = (x_new**2+y_new**2)**0.5
        x_new = x+r*math.cos(theta)
        y_new = y+r*math.sin(theta)
        if D>R:
            x_new = x_new*R/D
            y_new = y_new*R/D
            
        p = Point(x,y)
        q = Point(x_new,y_new)
        l = Line(p,q)
        l.draw(win)
        x = x_new
        y = y_new


    # Change the button.

    button.setText("Quit")

    # Wait for click and then quit.

    win.getMouse()
    win.close()
    
if __name__=='__main__':main()
