from graphics import *

# import dialog box for opening file
from tkinter.filedialog import askopenfilename


def main():
    print("This program creates a histogram from a file of grades.")
    print("Please select the file containing the grades.")
    print()

    # get the file name
    infileName = askopenfilename()

    # create empty list to store scores
    scores = []
    # open and read file
    infile = open(infileName, "r")
    # process each line of the input file
    for line in infile:
        # get the score from line by removing newline character
        score = line[:-1]
        # store score by appending to scores list
        scores.append(score)
    # close file
    infile.close()

    # verify list of scores
    print("Verifying scores")
    verifyscores = " ".join(scores)
    print(verifyscores, end='\n')
    print()

    # create empty list to store score counts
    scorecounts = []
    # count the number of occurences of each score and store in a new list
    for i in range(11):
        scorecheck = str(i)
        scorecount = verifyscores.count(scorecheck)
        scorecounts.append(scorecount)
    # Question: Why does count() method not work when looping through the list of items
    # after they are converted from str to int? The scorecounts list ends up empty.

    # verify list of score counts
    print("Verifying score counts")
    strscorecounts = []
    for intscorecount in scorecounts:
        strscorecount = str(intscorecount)
        strscorecounts.append(strscorecount)
    verifyscorecounts = " ".join(strscorecounts)
    print("counts", verifyscorecounts, end='\n')
    print("scores", "0 1 2 3 4 5 6 7 8 9 10", end='\n')
    print()

    # creates graphics window
    histogram = GraphWin("Histogram", 400, 200)
    histogram.setBackground("yellow")
    # sets coordinates to simplify drawing of images
    # note that yur is determined by number of scores + 10
    histogram.setCoords(0, 0, 115, (len(scores) + 10))

    # use loop to create graphical template for histogram
    for j in range(11):
        bar = Rectangle(Point((5 + (10 * j)), 5), Point((10 + (10 * j)), (scorecounts[j] + 5)))
        bar.setFill("red")
        bar.setWidth(3)
        bar.setOutline("blue")
        bar.draw(histogram)
        label = Text(Point((7 + (10 * j)), 2), str(j))
        label.draw(histogram)

    print("Histogram has been created.")
    print("Click anywhere on yellow window to close.")
    histogram.getMouse()
    histogram.close()


main()
