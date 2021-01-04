from graphics import *
from math import sqrt
def main():
    win = GraphWin('Draw a Triangle',200,200)
    win = GraphWin('Draw a Triangle')
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), 'Click On three POINTS')
    message.draw(win)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    triangle = Polygon(p1, p2)
    triangle.setOutline('cyan')
    triangle.draw(win)
    print('p1 X: ',p1.getX())
    print('p1 Y: ',p1.getY())
    print('p2 X: ',p2.getX())
    print('p2 Y: ',p2.getY())
    x1=p1.getX()
    x2=p2.getX()
    y1=p1.getY()
    y2=p1.getY()
    dx=x2 - x1
    dy=y2 - y1
    print('dx: ',dx)
    print('dy: ',dy)
    print('slope: ',dy/dx)
    length=sqrt(dx**2+dy**2)
    print('Length',length)

    message.setText('Click Anywhere to quit')
    win.getMouse()
