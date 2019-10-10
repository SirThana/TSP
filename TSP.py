import time
import pdb
from pudb.remote import set_trace
import pygame as pg
import random
import math
from sys import exit
from pygame.locals import *

#TODO
#   1.  Find a way to get the smallest difference between two vectors
#       When found, j looping through i, draw a line from j to the smallest i found
#       Then proceed with the next j, looping again through i || done using pythagoras


#   --> Return a list of vector points x, y
#       These vectors will have a random x & y relative to the screen size
def vectorGenerator(amountVector, width, height):
    vector = [] # x | y
    for i in range(0, amountVector):
        vector.append([random.randint(0, width), random.randint(0, height)])
    return vector


#   --> p1 and p2 are two lists with x and y cordinates
#       Returns the distance between two given points using pythagoras
def calcDistance(p1, p2):
    return int((( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5)) #Pythagoras theorem


def drawLine(vectorList):
    knownPoints = [] #Keep track of known points index
    for idx1 in range(0, len(vectorList) - 1):
        if idx1 not in knownPoints:
            if idx1 > 0:
                idx1 = vectorList.index(vectorList[idxLowVal])
            if idx1 <= len(vectorList) - 1:
                try:
                    d = calcDistance(vectorList[idx1], vectorList[idx1 + 1])
                except:
                    d = calcDistance(vectorList[idx1], vectorList[idx1])
                
            pg.draw.circle(screen, (0,255,255), (vectorList[idx1]), (5)) #make current dot blue
            pg.display.update() #refresh screen

            #Compare idx1 against all other p2's
            for idx2, p2 in enumerate(vectorList):
                while idx2 in knownPoints:
                    idx2 += 1
                if p2 != vectorList[idx1]: #Theres one iteration where they're the same, ignore that iteration
                    if calcDistance(vectorList[idx1], p2) <= d: #calcDistance and compare it to the lowest found d
                        d = calcDistance(vectorList[idx1], p2) #Not even neccesary right ?? | for comparison
                        idxLowVal = idx2 #Found a new lowest val, update the index

                    #We compared idx1 to all p2's, we can now draw shortest line
                    if idx2 == len(vectorList) - 1:
                        knownPoints.append(idxLowVal)
                        knownPoints.append(idx1)
                        pg.draw.line(screen, (30,120,10), (vectorList[idx1]), (vectorList[idxLowVal]), 2)
                        print(vectorList.index(vectorList[idx1]))
                        pg.display.update() #refresh screen


def main():
    (width, height) = (1920, 1080)
    global screen #Superscope screen

    screen = pg.display.set_mode((width, height))
    vectorList = vectorGenerator(6, width, height)
    for vector in vectorList:
        pg.draw.circle(screen, (255,0,0), (vector), (5))
    #set_trace()
    drawLine(vectorList)
    pg.display.flip()


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit(0)

main()
