from PIL import Image, ImageOps
import mss
import mss.tools
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import time

import sys
np.set_printoptions(threshold=sys.maxsize)

import copy
import math
import cv2
import random
import keyboard












fume=[1263, 659]
gloom=[1264, 939]
coffee=[1325, 868]
marigold=[1469, 864]
magnet=[1509, 803]
goldMagnet=[1421, 944]
lily=[1179, 722]
garlic=[1367, 865]
pumkin=[1461, 790]
tallnut=[1509,722]
startingPosition=[1193,565]
allPositions=[]
theListInSelection=[fume,gloom,coffee,marigold,magnet,goldMagnet,lily,garlic,pumkin,tallnut]

fumeSlot=[1228, 477]
gloomSlot=[fumeSlot[0]+50*1, fumeSlot[1]]
coffeeSlot=[fumeSlot[0]+50*2, fumeSlot[1]]
marigoldSlot=[fumeSlot[0]+50*3, fumeSlot[1]]
magnetSlot=[fumeSlot[0]+50*4, fumeSlot[1]]
goldMagnetSlot=[fumeSlot[0]+50*5, fumeSlot[1]]
lilySlot=[fumeSlot[0]+50*6, fumeSlot[1]]
garlicSlot=[fumeSlot[0]+50*7, fumeSlot[1]]
pumkinSlot=[fumeSlot[0]+50*8, fumeSlot[1]]




def tombDetection():
    monitor = {"top": 608, "left": 1310, "width": 1705-1310, "height": 846-608}
    sct_img = sct.grab(monitor)

    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    imgToWorkWith = np.asarray(img)

    gray_image = ImageOps.grayscale(img)
    gray = np.asarray(gray_image)
    errorArray=copy.deepcopy(gray)
    # sefsef=plt.imshow(imgToWorkWith)
    # plt.show()
    tombCounter=0
    for eachRowGray in range(len(imgToWorkWith)):
        for eachColGray in range(len(imgToWorkWith[0])):
            tempThingy=math.fabs(imgToWorkWith[eachRowGray][eachColGray][0]-95)+math.fabs(imgToWorkWith[eachRowGray][eachColGray][1]-97)+math.fabs(imgToWorkWith[eachRowGray][eachColGray][2]-129)
            if tempThingy==0:
                tombCounter=tombCounter+1
    return tombCounter




for eachRow in range(6):
    tempRowPos = []
    for eachCol in range(9):

        rowNumber=startingPosition[0]+80*eachCol
        colNumber=startingPosition[1]+87*eachRow

        if eachRow==5:
            colNumber=colNumber-30
        tempRowPos.append([rowNumber,colNumber])
    allPositions.append(tempRowPos)


with mss.mss() as sct:
    time.sleep(3)
    while 1==1:
        pyautogui.click(x=1202, y=930)
        time.sleep(6)

        for selectionCounter in theListInSelection:
            pyautogui.click(x=selectionCounter[0], y=selectionCounter[1])
        time.sleep(0.5)
        pyautogui.click(x=1350, y=999)
        pyautogui.click(x=1350, y=999)
        time.sleep(3)
        randCOuntesf=0

        for eachRow in range(len(allPositions)):
            for eachCol in range(6):
                if (eachRow==2 or eachRow ==3) and eachCol!=4:
                    pyautogui.click(x=lilySlot[0], y=lilySlot[1])
                    pyautogui.click(x=allPositions[eachRow][eachCol][0], y=allPositions[eachRow][eachCol][1])


        for eachRow in range(len(allPositions)):
            for eachCol in range(4):
                pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
                pyautogui.click(x=allPositions[eachRow][eachCol][0], y=allPositions[eachRow][eachCol][1])

        def plantGloom(x,y):
            pyautogui.click(x=fumeSlot[0], y=fumeSlot[1])
            pyautogui.click(x=x, y=y)
            pyautogui.click(x=gloomSlot[0], y=gloomSlot[1])
            pyautogui.click(x=x, y=y)
            pyautogui.click(x=coffeeSlot[0], y=coffeeSlot[1])
            pyautogui.click(x=x, y=y)
            pyautogui.click(x=pumkinSlot[0], y=pumkinSlot[1])
            pyautogui.click(x=x, y=y)

        plantGloom(allPositions[1][5][0],allPositions[1][5][1])
        plantGloom(allPositions[1][6][0],allPositions[1][6][1])
        plantGloom(allPositions[1][7][0],allPositions[1][7][1])
        plantGloom(allPositions[4][5][0],allPositions[4][5][1])
        plantGloom(allPositions[4][6][0],allPositions[4][6][1])
        plantGloom(allPositions[4][7][0],allPositions[4][7][1])

        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])

        pyautogui.click(x=pumkinSlot[0], y=pumkinSlot[1])
        pyautogui.click(x=allPositions[0][4][0], y=allPositions[0][4][1])
        pyautogui.click(x=pumkinSlot[0], y=pumkinSlot[1])
        pyautogui.click(x=allPositions[5][4][0], y=allPositions[5][4][1])

        pyautogui.click(x=magnetSlot[0], y=magnetSlot[1])
        pyautogui.click(x=allPositions[1][4][0], y=allPositions[1][4][1])
        pyautogui.click(x=magnetSlot[0], y=magnetSlot[1])
        pyautogui.click(x=allPositions[4][4][0], y=allPositions[4][4][1])

        pyautogui.click(x=goldMagnetSlot[0], y=goldMagnetSlot[1])
        pyautogui.click(x=allPositions[1][4][0], y=allPositions[1][4][1])
        pyautogui.click(x=goldMagnetSlot[0], y=goldMagnetSlot[1])
        pyautogui.click(x=allPositions[4][4][0], y=allPositions[4][4][1])

        pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
        pyautogui.click(x=allPositions[0][4][0], y=allPositions[0][4][1])
        pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
        pyautogui.click(x=allPositions[5][4][0], y=allPositions[5][4][1])

        pyautogui.click(x=pumkinSlot[0], y=pumkinSlot[1])
        pyautogui.click(x=allPositions[2][5][0], y=allPositions[2][5][1])
        pyautogui.click(x=pumkinSlot[0], y=pumkinSlot[1])
        pyautogui.click(x=allPositions[3][5][0], y=allPositions[3][5][1])

        pyautogui.click(1515,1014)
        pyautogui.click(1515, 1014)
        pyautogui.moveTo(x=allPositions[4][4][0], y=allPositions[4][4][1])

        time.sleep(130)

        if tombDetection() > 1000:
            time.sleep(0.5)
            pyautogui.click(1493, y=794)
            pyautogui.click(1493, y=794)
            time.sleep(6)
            continue
        monitor = {"top": 530, "left": 1560, "width": 1897 - 1560, "height": 1006 - 530}
        sct_img = sct.grab(monitor)

        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        imgToWorkWith = np.asarray(img)

        gray_image = ImageOps.grayscale(img)
        gray = np.asarray(gray_image)
        errorArray = copy.deepcopy(gray)

        for eachRowGray in range(len(imgToWorkWith)):
            for eachColGray in range(len(imgToWorkWith[0])):
                tempThingy = math.fabs(imgToWorkWith[eachRowGray][eachColGray][0] - 254) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][1] - 247) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][2] - 110)

                if tempThingy > 80:
                    errorArray[eachRowGray][eachColGray] = 255
                else:
                    errorArray[eachRowGray][eachColGray] = 0

        summationErrorArray = copy.deepcopy(errorArray)
        for eachRowEror in range(len(errorArray)):
            for eachColEror in range(len(errorArray[0])):
                if eachRowEror > 0 and eachColEror > 0 and eachRowEror < len(errorArray) - 1 and eachColEror < len(
                        errorArray[0]) - 1:
                    tempSummer = 0
                    if errorArray[eachRowEror - 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if tempSummer > 5:
                        summationErrorArray[eachRowEror][eachColEror] = 0
                    else:
                        summationErrorArray[eachRowEror][eachColEror] = 255

        # sefesf=plt.imshow(summationErrorArray)
        # plt.show()
        # exit()
        listOfSunPixels=[]
        for eachRowSunPix in range(len(summationErrorArray)):
            for eachColSunPix in range(len(summationErrorArray[0])):
                if summationErrorArray[eachRowSunPix][eachColSunPix]==0:
                    listOfSunPixels.append([eachColSunPix+1560,eachRowSunPix+530])
        if len(listOfSunPixels)<51:
            if tombDetection() > 1000:
                time.sleep(0.5)
                pyautogui.click(1493, y=794)
                pyautogui.click(1493, y=794)
                time.sleep(6)
                continue
            else:
                time.sleep(0.5)
                pyautogui.click(1853, y=453)
                pyautogui.click(1853, y=453)
                pyautogui.click(1513, y=788)
                pyautogui.click(1513, y=788)
                pyautogui.click(1385, y=831)
                pyautogui.click(1385, y=831)
                time.sleep(6)
                continue

        listOfRnadomNumbers=[]
        listOfSunPixelsUsed = []



        for randomCOunters in range(50):
            randomsNumberNow= random.randint(0, len(listOfSunPixels))
            listOfSunPixelsUsed.append(listOfSunPixels[randomsNumberNow])
            #listOfRnadomNumbers.append()


        for eachRandomNumebr in listOfSunPixelsUsed:
            #print(listOfSunPixels[eachRandomNumebr][0],listOfSunPixels[eachRandomNumebr][1])
            pyautogui.click(x=eachRandomNumebr[0], y=eachRandomNumebr[1])

        pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
        pyautogui.click(x=allPositions[2][5][0], y=allPositions[2][5][1])
        pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
        pyautogui.click(x=allPositions[3][5][0], y=allPositions[3][5][1])

        pyautogui.click(x=lilySlot[0], y=lilySlot[1])
        pyautogui.click(x=allPositions[2][4][0], y=allPositions[2][4][1])
        pyautogui.click(x=lilySlot[0], y=lilySlot[1])
        pyautogui.click(x=allPositions[3][4][0], y=allPositions[3][4][1])
        pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
        pyautogui.click(x=allPositions[2][4][0], y=allPositions[2][4][1])
        pyautogui.click(x=marigoldSlot[0], y=marigoldSlot[1])
        pyautogui.click(x=allPositions[3][4][0], y=allPositions[3][4][1])
        time.sleep(1)
        pyautogui.click(1515,1014)
        pyautogui.click(1515, 1014)
        time.sleep(130)

        if tombDetection() > 1000:
            time.sleep(0.5)
            pyautogui.click(1493, y=794)
            pyautogui.click(1493, y=794)
            time.sleep(6)
            continue


        pyautogui.moveTo(x=allPositions[2][4][0], y=allPositions[2][4][1])
        monitor = {"top": 530, "left": 1560, "width": 1897 - 1560, "height": 1006 - 530}
        sct_img = sct.grab(monitor)

        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        imgToWorkWith = np.asarray(img)

        gray_image = ImageOps.grayscale(img)
        gray = np.asarray(gray_image)
        errorArray = copy.deepcopy(gray)

        for eachRowGray in range(len(imgToWorkWith)):
            for eachColGray in range(len(imgToWorkWith[0])):
                tempThingy = math.fabs(imgToWorkWith[eachRowGray][eachColGray][0] - 254) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][1] - 247) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][2] - 110)

                if tempThingy > 80:
                    errorArray[eachRowGray][eachColGray] = 255
                else:
                    errorArray[eachRowGray][eachColGray] = 0

        summationErrorArray = copy.deepcopy(errorArray)
        for eachRowEror in range(len(errorArray)):
            for eachColEror in range(len(errorArray[0])):
                if eachRowEror > 0 and eachColEror > 0 and eachRowEror < len(errorArray) - 1 and eachColEror < len(
                        errorArray[0]) - 1:
                    tempSummer = 0
                    if errorArray[eachRowEror - 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if tempSummer > 5:
                        summationErrorArray[eachRowEror][eachColEror] = 0
                    else:
                        summationErrorArray[eachRowEror][eachColEror] = 255

        # sefesf=plt.imshow(summationErrorArray)
        # plt.show()
        # exit()
        listOfSunPixels = []
        for eachRowSunPix in range(len(summationErrorArray)):
            for eachColSunPix in range(len(summationErrorArray[0])):
                if summationErrorArray[eachRowSunPix][eachColSunPix] == 0:
                    listOfSunPixels.append([eachColSunPix + 1560, eachRowSunPix + 530])
        if len(listOfSunPixels)<51:
            if tombDetection() > 1000:
                time.sleep(0.5)
                pyautogui.click(1493, y=794)
                pyautogui.click(1493, y=794)
                time.sleep(6)
                continue
            else:
                time.sleep(0.5)
                pyautogui.click(1853, y=453)
                pyautogui.click(1853, y=453)
                pyautogui.click(1513, y=788)
                pyautogui.click(1513, y=788)
                pyautogui.click(1385, y=831)
                pyautogui.click(1385, y=831)
                time.sleep(6)
                continue
        listOfRnadomNumbers = []
        listOfSunPixelsUsed = []
        for randomCOunters in range(50):
            randomsNumberNow = random.randint(0, len(listOfSunPixels))
            listOfSunPixelsUsed.append(listOfSunPixels[randomsNumberNow])
            # listOfRnadomNumbers.append()


        for eachRandomNumebr in listOfSunPixelsUsed:
            # print(listOfSunPixels[eachRandomNumebr][0],listOfSunPixels[eachRandomNumebr][1])
            pyautogui.click(x=eachRandomNumebr[0], y=eachRandomNumebr[1])




        pyautogui.click(1515,1014)
        pyautogui.click(1515, 1014)
        time.sleep(3)
        pyautogui.moveTo(x=allPositions[1][8][0], y=allPositions[1][8][1])

        pyautogui.click(x=fumeSlot[0] + 50 * 11, y=fumeSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        time.sleep(9)
        pyautogui.click(x=fumeSlot[0] + 50 * 11, y=fumeSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])

        time.sleep(120)
        if tombDetection() > 1000:
            time.sleep(0.5)
            pyautogui.click(1493, y=794)
            pyautogui.click(1493, y=794)
            time.sleep(6)
            continue
        pyautogui.moveTo(x=allPositions[2][4][0], y=allPositions[2][4][1])
        monitor = {"top": 530, "left": 1560, "width": 1897 - 1560, "height": 1006 - 530}
        sct_img = sct.grab(monitor)

        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        imgToWorkWith = np.asarray(img)

        gray_image = ImageOps.grayscale(img)
        gray = np.asarray(gray_image)
        errorArray = copy.deepcopy(gray)

        for eachRowGray in range(len(imgToWorkWith)):
            for eachColGray in range(len(imgToWorkWith[0])):
                tempThingy = math.fabs(imgToWorkWith[eachRowGray][eachColGray][0] - 254) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][1] - 247) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][2] - 110)

                if tempThingy > 80:
                    errorArray[eachRowGray][eachColGray] = 255
                else:
                    errorArray[eachRowGray][eachColGray] = 0

        summationErrorArray = copy.deepcopy(errorArray)
        for eachRowEror in range(len(errorArray)):
            for eachColEror in range(len(errorArray[0])):
                if eachRowEror > 0 and eachColEror > 0 and eachRowEror < len(errorArray) - 1 and eachColEror < len(
                        errorArray[0]) - 1:
                    tempSummer = 0
                    if errorArray[eachRowEror - 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if tempSummer > 5:
                        summationErrorArray[eachRowEror][eachColEror] = 0
                    else:
                        summationErrorArray[eachRowEror][eachColEror] = 255

        # sefesf=plt.imshow(summationErrorArray)
        # plt.show()
        # exit()
        listOfSunPixels = []
        for eachRowSunPix in range(len(summationErrorArray)):
            for eachColSunPix in range(len(summationErrorArray[0])):
                if summationErrorArray[eachRowSunPix][eachColSunPix] == 0:
                    listOfSunPixels.append([eachColSunPix + 1560, eachRowSunPix + 530])
        if len(listOfSunPixels)<51:
            if tombDetection() > 1000:
                time.sleep(0.5)
                pyautogui.click(1493, y=794)
                pyautogui.click(1493, y=794)
                time.sleep(6)
                continue
            else:
                time.sleep(0.5)
                pyautogui.click(1853, y=453)
                pyautogui.click(1853, y=453)
                pyautogui.click(1513, y=788)
                pyautogui.click(1513, y=788)
                pyautogui.click(1385, y=831)
                pyautogui.click(1385, y=831)
                time.sleep(6)
                continue
        listOfRnadomNumbers = []
        listOfSunPixelsUsed = []
        for randomCOunters in range(50):
            randomsNumberNow = random.randint(0, len(listOfSunPixels))
            listOfSunPixelsUsed.append(listOfSunPixels[randomsNumberNow])
            # listOfRnadomNumbers.append()

        for eachRandomNumebr in listOfSunPixelsUsed:
            # print(listOfSunPixels[eachRandomNumebr][0],listOfSunPixels[eachRandomNumebr][1])
            pyautogui.click(x=eachRandomNumebr[0], y=eachRandomNumebr[1])




        pyautogui.click(1515,1014)
        pyautogui.click(1515, 1014)
        time.sleep(10)
        pyautogui.moveTo(x=allPositions[1][8][0], y=allPositions[1][8][1])

        pyautogui.click(x=fumeSlot[0] + 50 * 11, y=fumeSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        time.sleep(9)
        pyautogui.click(x=fumeSlot[0] + 50 * 11, y=fumeSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])

        time.sleep(120)
        if tombDetection() > 1000:
            time.sleep(0.5)
            pyautogui.click(1493, y=794)
            pyautogui.click(1493, y=794)
            time.sleep(6)
            continue
        pyautogui.moveTo(x=allPositions[2][4][0], y=allPositions[2][4][1])
        monitor = {"top": 530, "left": 1560, "width": 1897 - 1560, "height": 1006 - 530}
        sct_img = sct.grab(monitor)

        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        imgToWorkWith = np.asarray(img)

        gray_image = ImageOps.grayscale(img)
        gray = np.asarray(gray_image)
        errorArray = copy.deepcopy(gray)

        for eachRowGray in range(len(imgToWorkWith)):
            for eachColGray in range(len(imgToWorkWith[0])):
                tempThingy = math.fabs(imgToWorkWith[eachRowGray][eachColGray][0] - 254) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][1] - 247) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][2] - 110)

                if tempThingy > 80:
                    errorArray[eachRowGray][eachColGray] = 255
                else:
                    errorArray[eachRowGray][eachColGray] = 0

        summationErrorArray = copy.deepcopy(errorArray)
        for eachRowEror in range(len(errorArray)):
            for eachColEror in range(len(errorArray[0])):
                if eachRowEror > 0 and eachColEror > 0 and eachRowEror < len(errorArray) - 1 and eachColEror < len(
                        errorArray[0]) - 1:
                    tempSummer = 0
                    if errorArray[eachRowEror - 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror - 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror - 1] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror] == 0:
                        tempSummer = tempSummer + 1
                    if errorArray[eachRowEror + 1][eachColEror + 1] == 0:
                        tempSummer = tempSummer + 1
                    if tempSummer > 5:
                        summationErrorArray[eachRowEror][eachColEror] = 0
                    else:
                        summationErrorArray[eachRowEror][eachColEror] = 255

        # sefesf=plt.imshow(summationErrorArray)
        # plt.show()
        # exit()
        listOfSunPixels = []
        for eachRowSunPix in range(len(summationErrorArray)):
            for eachColSunPix in range(len(summationErrorArray[0])):
                if summationErrorArray[eachRowSunPix][eachColSunPix] == 0:
                    listOfSunPixels.append([eachColSunPix + 1560, eachRowSunPix + 530])
        if len(listOfSunPixels)<51:
            if tombDetection() > 1000:
                time.sleep(0.5)
                pyautogui.click(1493, y=794)
                pyautogui.click(1493, y=794)
                time.sleep(6)
                continue
            else:
                time.sleep(0.5)
                pyautogui.click(1853, y=453)
                pyautogui.click(1853, y=453)
                pyautogui.click(1513, y=788)
                pyautogui.click(1513, y=788)
                pyautogui.click(1385, y=831)
                pyautogui.click(1385, y=831)
                time.sleep(6)
                continue
        listOfRnadomNumbers = []
        listOfSunPixelsUsed = []
        for randomCOunters in range(50):
            randomsNumberNow = random.randint(0, len(listOfSunPixels))
            listOfSunPixelsUsed.append(listOfSunPixels[randomsNumberNow])
            # listOfRnadomNumbers.append()

        for eachRandomNumebr in listOfSunPixelsUsed:
            # print(listOfSunPixels[eachRandomNumebr][0],listOfSunPixels[eachRandomNumebr][1])
            pyautogui.click(x=eachRandomNumebr[0], y=eachRandomNumebr[1])

        pyautogui.click(1515, 1014)
        pyautogui.click(1515, 1014)
        time.sleep(3)
        pyautogui.moveTo(x=allPositions[1][8][0], y=allPositions[1][8][1])

        pyautogui.click(x=fumeSlot[0] + 50 * 11, y=fumeSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[1][8][0], y=allPositions[1][8][1])
        time.sleep(9)
        pyautogui.click(x=fumeSlot[0] + 50 * 11, y=fumeSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])
        pyautogui.click(x=garlicSlot[0], y=garlicSlot[1])
        pyautogui.click(x=allPositions[4][8][0], y=allPositions[4][8][1])

        time.sleep(120)

        if tombDetection() > 1000:
            time.sleep(0.5)
            pyautogui.click(1493, y=794)
            pyautogui.click(1493, y=794)
            time.sleep(6)
            continue



        monitor = {"top": 536, "left": 1125, "width": 1907 - 1125, "height": 1027 - 536}
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

        imgToWorkWith = np.asarray(img)

        gray_image = ImageOps.grayscale(img)
        gray = np.asarray(gray_image)
        errorArray = copy.deepcopy(gray)

        for eachRowGray in range(len(imgToWorkWith)):
            for eachColGray in range(len(imgToWorkWith[0])):
                tempThingy = math.fabs(imgToWorkWith[eachRowGray][eachColGray][0] - 255) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][1] - 230) + math.fabs(
                    imgToWorkWith[eachRowGray][eachColGray][2] - 102)
                if tempThingy > 0:
                    errorArray[eachRowGray][eachColGray] = 255
                else:
                    errorArray[eachRowGray][eachColGray] = 0

        listOfPonints = []
        for eachRowGray in range(len(errorArray)):
            for eachColGray in range(len(errorArray[0])):
                if errorArray[eachRowGray][eachColGray] == 0:
                    listOfPonints.append([eachColGray + 1125, eachRowGray + 536 + 50])

        pyautogui.click(x=listOfPonints[0][0], y=listOfPonints[0][1])

        time.sleep(10)





        if keyboard.is_pressed("a"):
            print("You pressed 'a'.")
            break
#        pyautogui.press('1')


"""        [[1984, 767], [1982, 821], [2020, 790], [2033, 779], [1984, 797], [2002, 804], [1999, 826], [2027, 808],
         [2027, 793], [2017, 791], [2024, 794], [2008, 822], [2005, 755], [2001, 835], [2006, 830], [1999, 843],
         [2010, 826], [2005, 753], [1986, 838], [2026, 812], [2013, 838], [2025, 767], [2034, 751], [2019, 803],
         [2012, 786], [2022, 757], [2035, 784], [2025, 767], [1992, 762], [1998, 783], [1997, 840], [1982, 767],
         [2005, 805], [2034, 755], [1996, 853], [2018, 786], [2033, 826], [1997, 823], [1996, 773], [1997, 817],
         [2021, 829], [2013, 746], [2003, 846], [2026, 802], [1986, 770], [2010, 838], [1992, 777], [1995, 839],
         [2033, 744], [2020, 831]]

"""