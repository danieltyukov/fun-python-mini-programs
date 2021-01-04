from graphics import *

##This program produces a horizontal bar chart of student exam scores

def main():
    win = GraphWin("Student Score Graph", 600, 400)
    win.setCoords(40.0, 0.0, 110.0, 10.0)
    win.setBackground('LemonChiffon')
    inFileName = input('Where is the file stored')
    inFile = open(inFileName, 'r')
    y = 8
    i = 1

    vline = Line(Point(0, 10), Point(0, 0))
    vline.draw(win)
    hline = Line(Point(-40, 1.3), Point(110, 1.3))
    hline.draw(win)
    scoretxt = Text(Point(-21, 1), 'exam score')
    scoretxt.setFill('blue')
    scoretxt.draw(win)
    x = 10
    for i in range(10):
        numtxt = Text(Point(x, 1), '%d' % x)
        numtxt.setFill('blue')
        numtxt.draw(win)
        x = x + 10

    for line in inFile.readlines():
        parts = line.split(':')
        student1 = ''.join(parts[:1])
        student1 = student1.rjust(16)
        score = parts[-1]
        score = int(score)
        txt = Text(Point(-21, y), student1)
        txt.setFill('navy')
        txt.draw(win)

        rect = Rectangle(Point(0, y + 0.3), Point(score, y - 0.3))
        rect.setFill('green')
        rect.draw(win)
        sctxt = Text(Point(5, y), score).draw(win)

        i = i + 0.1
        y = y - 1
        if score < 90:
            rect.setFill('cyan')
        if score < 80:
            rect.setFill('orange')
        if score < 70:
            rect.setFill('yellow')
        if score < 60:
            rect.setFill('red')

    message = Text(Point(45, 9.4), 'Click anywhere to quit')
    message.setFill('red')
    message.draw(win)
    win.getMouse()
    win.close()


main()