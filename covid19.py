####### WELCOME TO 2120 CORONA PROJECT#############
# Watch this video to get started:
# https://youtu.be/C9kdfxAWvQ0
#
# You will need the us_covid.txt data file in the same folder.
# The format of each data line is as follows:
# Lat,Date,Case,Long,Country/Region,Province/State
# Lat: latitude
# Date: a date between 2020-01-22 and 2020-04-07
# Case: the number of confirmed cases on that date
# Long: longitude
#
# Find each TODO comment in order and write your code below it.
# Do not erase comments.
# Do not write/modify code elsewhere.
# Note: Use tab to indent.
###################################################

# set up graphics and other libraries.
from tkinter import *
from time import sleep
from math import log
window = Tk()
canvas = Canvas(window, width=500, height=500, background="black")
canvas.pack()

#CUSTOM FUNCTIONS DEFINITIONS
def buildDates():
    date_list = []
    
    for d in range(22, 32):
        date = "2020-01-"
        if d < 10:
            
            date += "0"
        date_list += [date + str(d)]

    

    for d in range(1, 30):
       date = "2020-02-"
       if d < 10:
         date += "0"
       date_list += [date + str(d)]
        





 

    for d in range(1, 32):
       date = "2020-03-"
       if d < 10:
         date += "0"
       date_list += [date + str(d)]







    for d in range(1, 8):
       date = "2020-04-"
       if d < 10:
         date += "0"
       date_list += [date + str(d)]


  
    return date_list



def getDateFromLine(aLine):
  aList = aLine.split(",")
  return (aList[1])





def getCases(aLine):
  aList = aLine.split(",")
  return (int(aList[2]))







def getLatFromLine(aLine):
  aLine = aLine.split(",")
  return float(aLine[0])





def getLongFromLine(aLine):
  aLine = aLine.split(",")
  return float(aLine[3])






def calcXCoord(aLine):
    long = getLongFromLine(aLine)
    x = (long + 150) * 500/100
    return int(x)
    



def calcYCoord(aLine):
    lat = getLatFromLine(aLine)
    y = (500 - (lat * 500/75))
    return int(y)








def drawInfection(oneLine):
    x = calcXCoord(oneLine)
    y = calcYCoord(oneLine)
    c = getCases(oneLine)
    if c > 0:
        r = log(c)
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="white", width=0)

def drawMapForDate(searchDate):
    
    f = open("us_covid.txt")
    covid = f.read()
    covidList = covid.split("\n")
    for line in covidList:
        date = getDateFromLine(line)
        if date == searchDate:
        	drawInfection(line)




    
    return




#MAIN CODE HERE
for day in buildDates():
    drawMapForDate(day)

    # grey rectangle behind date display
    canvas.create_rectangle(200, 15, 300, 35, fill="grey")
    # date display
    canvas.create_text(250, 25, text=day)

    # wait 0.25 seconds before drawing next frame
    sleep(0.25)
    canvas.update()

#finishing the drawing app
mainloop()