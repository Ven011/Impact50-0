#!/usr/bin/env python3
#Author Nikolas Francis
#Created 1/13/2016
#Updated 1/15/2016
#Company Bluefish Concepts
#Screen Resolution is 1024x600
#This is a game for the Impact 50-0
#impact is the font

from tkinter import *
import time, os.path, random, queue, serial

windowState = "startScreen"
root = Tk()
frame = Frame(root)
root.attributes('-fullscreen', True)
root.geometry('1024x600') 	
root.configure(background='black')
ser = serial.Serial("/dev/ttyUSB0")
q = queue.Queue()

TitleGreen = "#%02x%02x%02x" % (124, 150, 71)
TextBlue = "#%02x%02x%02x" % (63, 129, 186)
TextRed = "#%02x%02x%02x" % (189, 59, 25)
TextOrange = "#%02x%02x%02x" % (247, 150, 70)

gameSelected = -1

trainingGame = 1

trainingDuration = 3
trainingDurationText = (str)(trainingDuration) + " minutes"
trainingDurationTextStrVar = StringVar()
trainingDurationTextStrVar.set(trainingDurationText)

gameTime = 0;
gameTimetStrVar = StringVar()
gameTimetStrVar.set((str)(gameTime))

rounds = 3

roundDifficulty = -1

#Game Global Variables

totalPunches = 0
totalPunchesStrVar = StringVar()
totalPunchesStrVar.set((str)(totalPunches))

punchesLanded = 0
punchesLandedStrVar = StringVar()
punchesLandedStrVar.set((str)(punchesLanded))

hitsTaken = 0
hitsTakenStrVar = StringVar()
hitsTakenStrVar.set((str)(hitsTaken))

pausedBoolean = False
running = False

def callback():
 	print("Dr. Butts")

root.after(1000,callback)
def prepScreen():
	global root, frame	
	root.configure(background='black')	
	frame.destroy()
	frame = Frame(root)
	frame.configure(background='black')
	frame.pack(expand=YES, fill=BOTH)
	
def loadWindow():
	prepScreen()
	if windowState == "gameScreen":
		gameScreen()
	elif windowState == "gameScreenRounds":
		gameScreenRounds()
	elif windowState == "startScreen":
		startScreen()
	elif windowState == "gameSelectScreen":
		gameSelectScreen()
	elif windowState == "trainingSelectScreen":
		trainingSelectScreen()
	elif windowState == "roundsSelectScreen":
		roundsSelectScreen()
	elif windowState == "difficultySelectScreen":
		difficultySelectScreen()
	elif windowState == "trainingDurationScreen":
		trainingDurationScreen()

def startScreen():
	global frame, bgImage
	bgImage = PhotoImage(file="Impact_50.0screen1_START.GIF")	
	b = Button(frame,image=bgImage, command=toGameSelectScreen)
	b.config(width=1024, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def gameSelectScreen():
	global frame, bgImageGSS, trainingBtn, roundsBtn, goBtn
	bgImageGSS = PhotoImage(file="Impact_50.0screen2.gif")	
	HS1 = Label(frame, justify=LEFT, image=bgImageGSS)
	HS1.place(x=0,y=0, anchor=NW, width=1024, height=600)

	if gameSelected == -1:

		trainingButtonFrame=Frame(frame)
		trainingButtonFrame.config(bg="Green",width=874,height=300)#1024x600
		trainingButtonFrame.place(x=0, y=0, anchor=NW)
		trainingButtonFrame.grid_propagate(False)

		trainingBtn = PhotoImage(file="Impact_50.0screen2.1.gif")	
		b = Button(trainingButtonFrame, command=trainingBtnClicked, image=trainingBtn)
		b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		roundsButtonFrame=Frame(frame)
		roundsButtonFrame.config(width=874,height=300)#1024x600
		roundsButtonFrame.place(x=0, y=300, anchor=NW)
		roundsButtonFrame.grid_propagate(False)

		roundsBtn = PhotoImage(file="Impact_50.0screen2.2.gif")
		b = Button(roundsButtonFrame, command=roundsBtnClicked, image=roundsBtn)
		b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)
	
	elif gameSelected == 0:

		trainingButtonFrame=Frame(frame)
		trainingButtonFrame.config(bg="Green",width=874,height=300)#1024x600
		trainingButtonFrame.place(x=0, y=0, anchor=NW)
		trainingButtonFrame.grid_propagate(False)

		trainingBtn = PhotoImage(file="Impact_50.0screen2T.1.gif")	
		b = Button(trainingButtonFrame, command=trainingBtnClicked, image=trainingBtn)
		b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		roundsButtonFrame=Frame(frame)
		roundsButtonFrame.config(width=874,height=300)#1024x600
		roundsButtonFrame.place(x=0, y=300, anchor=NW)
		roundsButtonFrame.grid_propagate(False)

		roundsBtn = PhotoImage(file="Impact_50.0screen2.2.gif")
		b = Button(roundsButtonFrame, command=roundsBtnClicked, image=roundsBtn)
		b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif gameSelected == 1:

		trainingButtonFrame=Frame(frame)
		trainingButtonFrame.config(bg="Green",width=874,height=300)#1024x600
		trainingButtonFrame.place(x=0, y=0, anchor=NW)
		trainingButtonFrame.grid_propagate(False)

		trainingBtn = PhotoImage(file="Impact_50.0screen2.1.gif")
		b = Button(trainingButtonFrame, command=trainingBtnClicked, image=trainingBtn)
		b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		roundsButtonFrame=Frame(frame)
		roundsButtonFrame.config(width=874,height=300)#1024x600
		roundsButtonFrame.place(x=0, y=300, anchor=NW)
		roundsButtonFrame.grid_propagate(False)

		roundsBtn = PhotoImage(file="Impact_50.0screen2R.1.gif")
		b = Button(roundsButtonFrame, command=roundsBtnClicked, image=roundsBtn)
		b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)	


	goButtonFrame=Frame(frame)
	goButtonFrame.config(width=150,height=600)#1024x600
	goButtonFrame.place(x=1024-150, y=0, anchor=NW)
	goButtonFrame.grid_propagate(False)

	goBtn = PhotoImage(file="Impact_50.0screenGoButton1.gif")	
	b = Button(goButtonFrame, command=toNextGame, image=goBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def roundsBtnClicked():
	global frame, trainingBtn, roundsBtn, gameSelected

	trainingButtonFrame=Frame(frame)
	trainingButtonFrame.config(bg="Green",width=874,height=300)#1024x600
	trainingButtonFrame.place(x=0, y=0, anchor=NW)
	trainingButtonFrame.grid_propagate(False)

	trainingBtn = PhotoImage(file="Impact_50.0screen2.1.gif")
	b = Button(trainingButtonFrame, command=trainingBtnClicked, image=trainingBtn)
	b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	roundsButtonFrame=Frame(frame)
	roundsButtonFrame.config(width=874,height=300)#1024x600
	roundsButtonFrame.place(x=0, y=300, anchor=NW)
	roundsButtonFrame.grid_propagate(False)

	roundsBtn = PhotoImage(file="Impact_50.0screen2R.1.gif")
	b = Button(roundsButtonFrame, command=roundsBtnClicked, image=roundsBtn)
	b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)	

	gameSelected = 1

def trainingBtnClicked():
	global trainingBtn, roundsBtn, gameSelected

	trainingButtonFrame=Frame(frame)
	trainingButtonFrame.config(bg="Green",width=874,height=300)#1024x600
	trainingButtonFrame.place(x=0, y=0, anchor=NW)
	trainingButtonFrame.grid_propagate(False)

	trainingBtn = PhotoImage(file="Impact_50.0screen2T.1.gif")	
	b = Button(trainingButtonFrame, command=trainingBtnClicked, image=trainingBtn)
	b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	roundsButtonFrame=Frame(frame)
	roundsButtonFrame.config(width=874,height=300)#1024x600
	roundsButtonFrame.place(x=0, y=300, anchor=NW)
	roundsButtonFrame.grid_propagate(False)

	roundsBtn = PhotoImage(file="Impact_50.0screen2.2.gif")
	b = Button(roundsButtonFrame, command=roundsBtnClicked, image=roundsBtn)
	b.config(width=874, height=300, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	gameSelected = 0

def trainingSelectScreen():
	global frame, bgImageTSS, selectBtn, goBtn, backBtn, trainingGame
	bgImageTSS = PhotoImage(file="Impact_50.0screen3_TRAINING1.gif")	
	HS1 = Label(frame, justify=LEFT, image=bgImageTSS)
	HS1.place(x=0,y=0, anchor=NW, width=1024, height=600)


	if trainingGame == 1:
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING1.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingGame == 2:
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING2.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingGame == 3:
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING3.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingGame == 4:
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING4.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	backBtnFrame=Frame(frame)
	backBtnFrame.config(width=150,height=600)#1024x600
	backBtnFrame.place(x=0, y=0, anchor=NW)
	backBtnFrame.grid_propagate(False)

	backBtn = PhotoImage(file="Impact_50.0screenBackButton.gif")	
	b = Button(backBtnFrame, command=toGameSelectScreen, image=backBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	goButtonFrame=Frame(frame)
	goButtonFrame.config(width=150,height=600)#1024x600
	goButtonFrame.place(x=1024-150, y=0, anchor=NW)
	goButtonFrame.grid_propagate(False)

	goBtn = PhotoImage(file="Impact_50.0screenGoButton1.gif")
	b = Button(goButtonFrame, command=toTrainingDurationScreen, image=goBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def roundsSelectScreen():
	global frame, bgImageTSS, selectBtn, goBtn, backBtn, rounds
	bgImageTSS = PhotoImage(file="Impact_50.0screen3_ROUNDS.gif")	
	HS1 = Label(frame, justify=LEFT, image=bgImageTSS)
	HS1.place(x=0,y=0, anchor=NW, width=1024, height=600)


	if rounds == 3:
		currentRound = 1
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS3.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif rounds == 6:
		currentRound = 1
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS6.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif rounds == 10:
		currentRound = 1
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS10.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif rounds == 12:
		currentRound = 1
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS12.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	backBtnFrame=Frame(frame)
	backBtnFrame.config(width=150,height=600)#1024x600
	backBtnFrame.place(x=0, y=0, anchor=NW)
	backBtnFrame.grid_propagate(False)

	backBtn = PhotoImage(file="Impact_50.0screenBackButton.gif")	
	b = Button(backBtnFrame, command=toGameSelectScreen, image=backBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	goButtonFrame=Frame(frame)
	goButtonFrame.config(width=150,height=600)#1024x600
	goButtonFrame.place(x=1024-150, y=0, anchor=NW)
	goButtonFrame.grid_propagate(False)

	goBtn = PhotoImage(file="Impact_50.0screenGoButton1.gif")
	b = Button(goButtonFrame, command=toDifficultySelectScreen, image=goBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def trainingDurationScreen():
	global frame, bgImageTSS, selectBtn, goBtn, backBtn, trainingDuration
	bgImageTSS = PhotoImage(file="Impact_50.0screen4_DURATION.gif")	
	HS1 = Label(frame, justify=LEFT, image=bgImageTSS)
	HS1.place(x=0,y=0, anchor=NW, width=1024, height=600)


	if trainingDuration == 3:
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration3.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 5:
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration5.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 10:
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration10.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 20:
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration20.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 30:
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration30.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	backBtnFrame=Frame(frame)
	backBtnFrame.config(width=150,height=600)#1024x600
	backBtnFrame.place(x=0, y=0, anchor=NW)
	backBtnFrame.grid_propagate(False)

	backBtn = PhotoImage(file="Impact_50.0screenBackButton.gif")	
	b = Button(backBtnFrame, command=toNextGame, image=backBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	goButtonFrame=Frame(frame)
	goButtonFrame.config(width=150,height=600)#1024x600
	goButtonFrame.place(x=1024-150, y=0, anchor=NW)
	goButtonFrame.grid_propagate(False)

	goBtn = PhotoImage(file="Impact_50.0screenGoButton2.gif")
	b = Button(goButtonFrame, command=toGameScreen, image=goBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def difficultySelectScreen():
	global frame, bgImageTSS, beginnerBtn, intermediateBtn, hardcoreBtn, goBtn, backBtn, roundDifficulty
	bgImageTSS = PhotoImage(file="Impact_50.0screen4_LEVELS.gif")	
	HS1 = Label(frame, justify=LEFT, image=bgImageTSS)
	HS1.place(x=0,y=0, anchor=NW, width=1024, height=600)

	if roundDifficulty == -1:
		beginnerBtnFrame=Frame(frame)
		beginnerBtnFrame.config(bg="Green",width=724,height=201)#1024x600
		beginnerBtnFrame.place(x=150, y=0, anchor=NW)
		beginnerBtnFrame.grid_propagate(False)

		beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVELSBeginner1.gif")	
		b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
		b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		intermediateBtnFrame=Frame(frame)
		intermediateBtnFrame.config(bg="Green",width=724,height=200)#1024x600
		intermediateBtnFrame.place(x=150, y=201, anchor=NW)
		intermediateBtnFrame.grid_propagate(False)

		intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVELSIntermediate1.gif")	
		b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
		b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		hardcoreBtnFrame=Frame(frame)
		hardcoreBtnFrame.config(bg="Green",width=724,height=199)#1024x600
		hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
		hardcoreBtnFrame.grid_propagate(False)

		hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVELSHard1.gif")	
		b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
		b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif roundDifficulty == 1:
		beginnerBtnFrame=Frame(frame)
		beginnerBtnFrame.config(bg="black",width=724,height=201)#1024x600
		beginnerBtnFrame.place(x=150, y=0, anchor=NW)
		beginnerBtnFrame.grid_propagate(False)

		beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVEL1beginnerGREEN.gif")	
		b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
		b.config(width=723, height=200, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		intermediateBtnFrame=Frame(frame)
		intermediateBtnFrame.config(bg="black",width=724,height=200)#1024x600
		intermediateBtnFrame.place(x=150, y=201, anchor=NW)
		intermediateBtnFrame.grid_propagate(False)

		intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVELSIntermediate1.gif")	
		b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
		b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		hardcoreBtnFrame=Frame(frame)
		hardcoreBtnFrame.config(bg="black",width=724,height=199)#1024x600
		hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
		hardcoreBtnFrame.grid_propagate(False)

		hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVELSHard1.gif")	
		b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
		b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif roundDifficulty == 2:
		beginnerBtnFrame=Frame(frame)
		beginnerBtnFrame.config(bg="black",width=724,height=201)#1024x600
		beginnerBtnFrame.place(x=150, y=0, anchor=NW)
		beginnerBtnFrame.grid_propagate(False)

		beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVELSBeginner1.gif")	
		b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
		b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		intermediateBtnFrame=Frame(frame)
		intermediateBtnFrame.config(bg="black",width=724,height=200)#1024x600
		intermediateBtnFrame.place(x=150, y=201, anchor=NW)
		intermediateBtnFrame.grid_propagate(False)

		intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVEL2interYELLOW.gif")	
		b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
		b.config(width=724, height=200, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		hardcoreBtnFrame=Frame(frame)
		hardcoreBtnFrame.config(bg="black",width=724,height=199)#1024x600
		hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
		hardcoreBtnFrame.grid_propagate(False)

		hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVELSHard1.gif")	
		b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
		b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif roundDifficulty == 3:
		beginnerBtnFrame=Frame(frame)
		beginnerBtnFrame.config(bg="Green",width=724,height=201)#1024x600
		beginnerBtnFrame.place(x=150, y=0, anchor=NW)
		beginnerBtnFrame.grid_propagate(False)

		beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVELSBeginner1.gif")	
		b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
		b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		intermediateBtnFrame=Frame(frame)
		intermediateBtnFrame.config(bg="Green",width=724,height=200)#1024x600
		intermediateBtnFrame.place(x=150, y=201, anchor=NW)
		intermediateBtnFrame.grid_propagate(False)

		intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVELSIntermediate1.gif")	
		b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
		b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

		hardcoreBtnFrame=Frame(frame)
		hardcoreBtnFrame.config(bg="Green",width=724,height=199)#1024x600
		hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
		hardcoreBtnFrame.grid_propagate(False)

		hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVEL3hardRED.gif")	
		b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
		b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	backBtnFrame=Frame(frame)
	backBtnFrame.config(width=150,height=600)#1024x600
	backBtnFrame.place(x=0, y=0, anchor=NW)
	backBtnFrame.grid_propagate(False)

	backBtn = PhotoImage(file="Impact_50.0screenBackButton.gif")	
	b = Button(backBtnFrame, command=toNextGame, image=backBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	goButtonFrame=Frame(frame)
	goButtonFrame.config(width=150,height=600)#1024x600
	goButtonFrame.place(x=1024-150, y=0, anchor=NW)
	goButtonFrame.grid_propagate(False)

	goBtn = PhotoImage(file="Impact_50.0screenGoButton2.gif")
	b = Button(goButtonFrame, command=toGameScreen, image=goBtn)
	b.config(width=150, height=600, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def trainingButtonHelper():
	global frame, selectBtn, trainingGame 

	if trainingGame == 1:
		trainingGame += 1
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING2.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingGame == 2:
		trainingGame += 1
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING3.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingGame == 3:
		trainingGame += 1
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING4.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingGame == 4:
		trainingGame = 1
		selectBtn = PhotoImage(file="Impact_50.0screen3_TRAINING1.1.gif")
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="Green",width=723,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)

		b = Button(selectButtonFrame, command=trainingButtonHelper, image=selectBtn)
		b.config(width=723, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

def trainingDurationButtonHelper():
	global trainingDuration, frame, selectBtn

	if trainingDuration == 3:
		trainingDuration += 2
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration5.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 5:
		trainingDuration += 5
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration10.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 10:
		trainingDuration += 10
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration20.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 20:
		trainingDuration += 10
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration30.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif trainingDuration == 30:
		trainingDuration = 3
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=150, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenDuration3.gif")	
		b = Button(selectButtonFrame, command=trainingDurationButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

def roundsButtonHelper():
	global frame, selectBtn, rounds, currentRound

	if rounds == 3:
		rounds += 3
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS6.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif rounds == 6:
		rounds += 4
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS10.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif rounds == 10:
		rounds += 2
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS12.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	elif rounds == 12:
		rounds = 3
		selectButtonFrame=Frame(frame)
		selectButtonFrame.config(bg="black",width=724,height=300)#1024x600
		selectButtonFrame.place(x=149, y=300, anchor=NW)
		selectButtonFrame.grid_propagate(False)
		
		selectBtn = PhotoImage(file="Impact_50.0screenROUNDS3.gif")	
		b = Button(selectButtonFrame, command=roundsButtonHelper, image=selectBtn)
		b.config(width=724, height=300, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

	

def beginnerButtonHelper():
	global roundDifficulty, frame, beginnerBtn, intermediateBtn, hardcoreBtn
	roundDifficulty = 1

	beginnerBtnFrame=Frame(frame)
	beginnerBtnFrame.config(bg="black",width=724,height=201)#1024x600
	beginnerBtnFrame.place(x=150, y=0, anchor=NW)
	beginnerBtnFrame.grid_propagate(False)

	beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVEL1beginnerGREEN.gif")	
	b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
	b.config(width=723, height=200, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	intermediateBtnFrame=Frame(frame)
	intermediateBtnFrame.config(bg="black",width=724,height=200)#1024x600
	intermediateBtnFrame.place(x=150, y=201, anchor=NW)
	intermediateBtnFrame.grid_propagate(False)

	intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVELSIntermediate1.gif")	
	b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
	b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	hardcoreBtnFrame=Frame(frame)
	hardcoreBtnFrame.config(bg="black",width=724,height=199)#1024x600
	hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
	hardcoreBtnFrame.grid_propagate(False)

	hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVELSHard1.gif")	
	b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
	b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def intermediateButtonHelper():
	global roundDifficulty, frame, beginnerBtn, intermediateBtn, hardcoreBtn
	roundDifficulty = 2

	beginnerBtnFrame=Frame(frame)
	beginnerBtnFrame.config(bg="black",width=724,height=201)#1024x600
	beginnerBtnFrame.place(x=150, y=0, anchor=NW)
	beginnerBtnFrame.grid_propagate(False)

	beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVELSBeginner1.gif")	
	b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
	b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	intermediateBtnFrame=Frame(frame)
	intermediateBtnFrame.config(bg="black",width=724,height=200)#1024x600
	intermediateBtnFrame.place(x=150, y=201, anchor=NW)
	intermediateBtnFrame.grid_propagate(False)

	intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVEL2interYELLOW.gif")	
	b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
	b.config(width=724, height=200, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	hardcoreBtnFrame=Frame(frame)
	hardcoreBtnFrame.config(bg="black",width=724,height=199)#1024x600
	hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
	hardcoreBtnFrame.grid_propagate(False)

	hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVELSHard1.gif")	
	b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
	b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def hardcoreButtonHelper():
	global roundDifficulty, frame, beginnerBtn, intermediateBtn, hardcoreBtn
	roundDifficulty = 3

	beginnerBtnFrame=Frame(frame)
	beginnerBtnFrame.config(bg="Green",width=724,height=201)#1024x600
	beginnerBtnFrame.place(x=150, y=0, anchor=NW)
	beginnerBtnFrame.grid_propagate(False)

	beginnerBtn = PhotoImage(file="Impact_50.0screen4_LEVELSBeginner1.gif")	
	b = Button(beginnerBtnFrame, command=beginnerButtonHelper, image=beginnerBtn)
	b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	intermediateBtnFrame=Frame(frame)
	intermediateBtnFrame.config(bg="Green",width=724,height=200)#1024x600
	intermediateBtnFrame.place(x=150, y=201, anchor=NW)
	intermediateBtnFrame.grid_propagate(False)

	intermediateBtn = PhotoImage(file="Impact_50.0screen4_LEVELSIntermediate1.gif")	
	b = Button(intermediateBtnFrame, command=intermediateButtonHelper, image=intermediateBtn)
	b.config(width=724, height=201, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	hardcoreBtnFrame=Frame(frame)
	hardcoreBtnFrame.config(bg="Green",width=724,height=199)#1024x600
	hardcoreBtnFrame.place(x=150, y=401, anchor=NW)
	hardcoreBtnFrame.grid_propagate(False)

	hardcoreBtn = PhotoImage(file="Impact_50.0screen4_LEVEL3hardRED.gif")	
	b = Button(hardcoreBtnFrame, command=hardcoreButtonHelper, image=hardcoreBtn)
	b.config(width=724, height=199, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

def gameScreen():
	import serial, random, threading
	from timeit import default_timer as timer
	print("GameScreen")
	global frame, totalPunchesStrVar, punchesLandedStrVar, hitsTakenStrVar, trainingGame, trainingDuration, tP, pL
	global hT, bodyImg, upBtn, downBtn, pPBtn, cancelBtn, gameTime, gameTimetStrVar, currentRound
	global totalPunches, punchesLanded, hitsTaken

	pL = PhotoImage(file="Impact_50.0screenGamePL.gif")	
	HS1 = Label(frame, justify=LEFT, image=pL)
	HS1.place(x=0,y=200, anchor=NW, width=202, height=201)

	HS1 = Label(frame, justify=LEFT, textvariable=punchesLandedStrVar, bg='black', fg='white')
	labelfont = ('impact', 30)
	HS1.config(font=labelfont)      
	HS1.place(x=101,y=300, anchor=CENTER, width=150, height=75)

	hT = PhotoImage(file="Impact_50.0screenGameHT.gif")	
	HS1 = Label(frame, justify=LEFT, image=hT)
	HS1.place(x=0,y=401, anchor=NW, width=202, height=199)

	HS1 = Label(frame, justify=LEFT, textvariable=hitsTakenStrVar, bg='black', fg='white')
	labelfont = ('impact', 30)
	HS1.config(font=labelfont)      
	HS1.place(x=101,y=500, anchor=CENTER, width=150, height=75)

	if gameSelected == 0:
		bodyImg = PhotoImage(file="Impact_50.0screenGAMEtraining.gif")	
		HS1 = Label(frame, justify=LEFT, image=bodyImg)
		HS1.place(x=200,y=0, anchor=NW, width=624, height=600)

	elif gameSelected == 1:	
		currentRound = 1	
		bodyImg = PhotoImage(file="Impact_50.0screenGAMEr"+ (str)(currentRound)+".gif")	
		HS1 = Label(frame, justify=LEFT, image=bodyImg)
		HS1.place(x=200,y=0, anchor=NW, width=624, height=600)

	upBtnFrame=Frame(frame)
	upBtnFrame.config(width=200,height=150)#1024x600
	upBtnFrame.place(x=1024-200, y=0, anchor=NW)
	upBtnFrame.grid_propagate(False)

	upBtn = PhotoImage(file="Impact_50.0screenGameSpdUP.gif")
	b = Button(upBtnFrame, command=upSpeed, image=upBtn)
	b.config(width=200, height=150, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	downBtnFrame=Frame(frame)
	downBtnFrame.config(width=200,height=150)#1024x600
	downBtnFrame.place(x=1024-200, y=150, anchor=NW)
	downBtnFrame.grid_propagate(False)

	downBtn = PhotoImage(file="Impact_50.0screenGameSpdDOWN.gif")
	b = Button(downBtnFrame, command=downSpeed, image=downBtn)
	b.config(width=200, height=150, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	pPBtnFrame=Frame(frame)
	pPBtnFrame.config(width=200,height=151, bg='black')#1024x600
	pPBtnFrame.place(x=1024-200, y=300, anchor=NW)
	pPBtnFrame.grid_propagate(False)

	pPBtn = PhotoImage(file="Impact_50.0screenGamePAUSE.gif")
	b = Button(pPBtnFrame, command=pauseResumeGame, image=pPBtn)
	b.config(width=199, height=151, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	cancelBtnFrame=Frame(frame)
	cancelBtnFrame.config(width=200,height=149, bg='black')#1024x600
	cancelBtnFrame.place(x=1024-200, y=451, anchor=NW)
	cancelBtnFrame.grid_propagate(False)

	cancelBtn = PhotoImage(file="Impact_50.0screenGameCancel.gif")
	b = Button(cancelBtnFrame, command=cancelGameScreen, image=cancelBtn)
	b.config(width=200, height=149, borderwidth=0, highlightthickness=0)
	b.place(x=0, y=0)

	#BEGIN GAME HERE
	if gameSelected == 0:
		totalPunches = 0
		punchesLanded = 0
		hitsTaken = 0
		totalPunchesStrVar.set((str)(totalPunches))
		punchesLandedStrVar.set((str)(punchesLanded))
		hitsTakenStrVar.set((str)(hitsTaken))
		gameTime = trainingDuration * 60
		t = threading.Thread(target=trainingThread)
		t.start()
	if gameSelected == 1:
		totalPunches = 0
		punchesLanded = 0
		hitsTaken = 0
		totalPunchesStrVar.set((str)(totalPunches))
		punchesLandedStrVar.set((str)(punchesLanded))
		hitsTakenStrVar.set((str)(hitsTaken))
		gameTime = 180
		t = threading.Thread(target=roundsThread)
		t.start()
		root.after(100, check_queue)

	if gameTime >= 60:
		m, s = divmod(gameTime, 60)
		gameTimetStrVar.set("%d:%02d" % (m, s))
	else:
		gameTimetStrVar.set((str)(gameTime))

	
	puregreen = "#%02x%02x%02x" % (0, 255, 0)
	HS1 = Label(frame, justify=CENTER, textvariable=gameTimetStrVar, bg=puregreen, fg='white')
	labelfont = ('impact', 120)
	HS1.config(font=labelfont)      
	HS1.place(x=512,y=400, anchor=CENTER, width=550, height=300)
	

def trainingThread():
	import serial
	global running, pausedBoolean, gameTime, gameTimetStrVar, trainingGame
	global totalPunches, punchesLanded, totalPunchesStrVar, punchesLandedStrVar
	global ser
	running = True

	#-----Game Settings--------------------------------------
	frequency = 10
	litTimeMax = 200
	litTimeMin = 100

	CDMax = 20
	CDMin = 10

	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

	pausedBoolean = False
	ser = serial.Serial("/dev/ttyUSB0")
	#ser = serial.Serial("COM41")
	ser.baudrate = 9600
	ser.timeout = 0.25
	pads = 4
	upTime = [-1] * pads
	counter = 0
	aTargetLit = False
	global trainingDuration
	time.sleep(2.1)
	if trainingDuration == 3:
		msg = "tm"
		ser.write(bytes(msg.encode('ascii')))
	elif trainingDuration == 5:
		msg = "tm"
		ser.write(bytes(msg.encode('ascii')))
	elif trainingDuration >= 10:
		msg = "tf"
		ser.write(bytes(msg.encode('ascii')))
	while(running):
		while(pausedBoolean):
			print("Game Paused")
			time.sleep(.1)
		#print("Tick")
		#-------------------Game Logic--------------------------------
		
		if trainingGame == 3 or trainingGame == 4: 
			pad = 1
			#subtract one second from Uptime also check if Target is up.
			if upTime[pad -1] == 0:
				#Turn Pad OFF
				msg = (str)(pad) + "o"
				ser.write(bytes(msg.encode('ascii')))
				print(msg)
				aTargetLit = False
			elif upTime[pad -1] < 0 and aTargetLit == False: 		
				#Pad is off, 
				# if target isn't lit, roll to see if it lights up.
				if random.randint(0, 600) <= frequency:
					#roll another number to determine the Light's up Time
					upTime[pad -1] = random.randint(litTimeMin, litTimeMax)
					#Transmit the color to the Pad
					msg = (str)(pad) + "g"
					aTargetLit = True
					ser.write(bytes(msg.encode('ascii')))
					print(msg)
			upTime[pad -1] -= 1;

		if trainingGame == 2 or trainingGame == 4: 
			pad = 2
			#subtract one second from Uptime also check if Target is up.		
			if upTime[pad -1] == 0:
				#Turn Pad OFF
				msg = (str)(pad) + "o"
				ser.write(bytes(msg.encode('ascii')))
				print(msg)
				aTargetLit = False
			elif upTime[pad -1] < 0 and aTargetLit == False:
				#Pad is off, 
				# if target isn't lit, roll to see if it lights up.
				if random.randint(0, 600) <= frequency:
					#roll another number to determine the Light's up Time
					upTime[pad -1] = random.randint(litTimeMin, litTimeMax)
					#Transmit the color to the Pad
					msg = (str)(pad) + "g"
					aTargetLit = True
					ser.write(bytes(msg.encode('ascii')))
					print(msg)
			upTime[pad -1] -= 1;

		if trainingGame == 2 or trainingGame == 4: 
			pad = 3
			#subtract one second from Uptime also check if Target is up.		
			if upTime[pad -1] == 0:
				#Turn Pad OFF
				msg = (str)(pad) + "o"
				ser.write(bytes(msg.encode('ascii')))
				print(msg)
				aTargetLit = False
			elif upTime[pad -1] < 0 and aTargetLit == False:
				#Pad is off, 
				# if target isn't lit, roll to see if it lights up.
				if random.randint(0, 600) <= frequency:
					#roll another number to determine the Light's up Time
					upTime[pad -1] = random.randint(litTimeMin, litTimeMax)
					#Transmit the color to the Pad
					msg = (str)(pad) + "g"
					aTargetLit = True
					ser.write(bytes(msg.encode('ascii')))
					print(msg)
			upTime[pad -1] -= 1;

		if trainingGame == 3 or trainingGame == 4: 
			pad = 4
			#subtract one second from Uptime also check if Target is up.		
			if upTime[pad -1] == 0:
				#Turn Pad OFF
				msg = (str)(pad) + "o"
				ser.write(bytes(msg.encode('ascii')))
				print(msg)
				aTargetLit = False
			elif upTime[pad -1] < 0 and aTargetLit == False:
				#Pad is off, 
				# if target isn't lit, roll to see if it lights up.
				if random.randint(0, 600) <= frequency:
					#roll another number to determine the Light's up Time
					upTime[pad -1] = random.randint(litTimeMin, litTimeMax)
					#Transmit the color to the Pad
					msg = (str)(pad) + "g"
					aTargetLit = True
					ser.write(bytes(msg.encode('ascii')))
					print(msg)
			upTime[pad -1] -= 1;


		#----------------Input Processing
		if ser.inWaiting() > 0:
			input = ser.read(size=1).decode("utf-8")
			if input == '1':
				print("one Hit Detected!")
				if upTime[0] > 0:
					#pad is On Turn off and stuff
					upTime[0] = -1
					msg = (str)(1) + "o"
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					aTargetLit = False
					punchesLandedStrVar.set((str)(punchesLanded))

				totalPunches += 1
				totalPunchesStrVar.set((str)(totalPunches))
				root.update()

			elif input == '2':
				print("two Hit Detected!")
				if upTime[1] > 0:
					#pad is On Turn off and stuff
					upTime[1] = -1
					msg = (str)(2) + "o"
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					aTargetLit = False
					punchesLandedStrVar.set((str)(punchesLanded))

				totalPunches += 1
				totalPunchesStrVar.set((str)(totalPunches))
				root.update()
			elif input == '3':
				print("three Hit Detected!")
				if upTime[2] > 0:
					#pad is On Turn off and stuff
					upTime[2] = -1
					msg = (str)(3) + "o"
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					aTargetLit = False
					punchesLandedStrVar.set((str)(punchesLanded))

				totalPunches += 1
				totalPunchesStrVar.set((str)(totalPunches))
				root.update()
			elif input == '4':
				print("four Hit Detected!")
				if upTime[3] > 0:
					#pad is On Turn off and stuff
					upTime[3] = -1
					msg = (str)(4) + "o"
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					aTargetLit = False
					punchesLandedStrVar.set((str)(punchesLanded))

				totalPunches += 1
				totalPunchesStrVar.set((str)(totalPunches))
				root.update()
			elif input != "":
				print(input)

		
		if counter > 9:
			counter = 0
			gameTime = gameTime - 1
			if gameTime >= 60:
				m, s = divmod(gameTime, 60)
				gameTimetStrVar.set("%d:%02d" % (m, s))
			else:
				gameTimetStrVar.set((str)(gameTime))

		counter += 1
		if gameTime == 0:
			running = False
			root.update()
		if running == True:
			root.update()
			time.sleep(.1)

	#turn All Pads off
	#Turn Pad OFF
	msg = (str)(1) + "o"
	ser.write(bytes(msg.encode('ascii')))
	msg = (str)(2) + "o"
	ser.write(bytes(msg.encode('ascii')))
	msg = (str)(3) + "o"
	ser.write(bytes(msg.encode('ascii')))
	msg = (str)(4) + "o"
	ser.write(bytes(msg.encode('ascii')))
	ser.close()

def on_main_thread(func):
	global q
	q.put(func)

def check_queue():
	global q
	while True:
		if q.empty() != True:
			task = q.get(block=False)
		else: 
			break;
		root.after_idle(task)
	root.after(250, check_queue)

def updateBgImage():
	global bodyImg, frame, currentRound
	print("Potateo")
	bodyImg = PhotoImage(file="Impact_50.0screenGAMEr"+ (str)(currentRound)+".gif")	
	HS1 = Label(frame, justify=LEFT, image=bodyImg)
	HS1.place(x=200,y=0, anchor=NW, width=624, height=600)

	puregreen = "#%02x%02x%02x" % (0, 255, 0)
	HS1 = Label(frame, justify=CENTER, textvariable=gameTimetStrVar, bg=puregreen, fg='white')
	labelfont = ('impact', 120)
	HS1.config(font=labelfont)      
	HS1.place(x=512,y=400, anchor=CENTER, width=550, height=300)

def breakBgImage():
	global bodyImg, frame, currentRound
	print("Potateo")
	bodyImg = PhotoImage(file="Impact_50.0screenGAMEbreak.gif")	
	HS1 = Label(frame, justify=LEFT, image=bodyImg)
	HS1.place(x=200,y=0, anchor=NW, width=624, height=600)

	myRed = "#%02x%02x%02x" % (236, 28, 36)
	HS1 = Label(frame, justify=CENTER, textvariable=gameTimetStrVar, bg=myRed, fg='white')
	labelfont = ('impact', 120)
	HS1.config(font=labelfont)      
	HS1.place(x=512,y=400, anchor=CENTER, width=550, height=300)

def updateTime():
	global gameTime, gameTimetStrVar
	print("time Updated")
	if gameTime >= 60:
		m, s = divmod(gameTime, 60)
		gameTimetStrVar.set("%d:%02d" % (m, s))
	else:
		gameTimetStrVar.set((str)(gameTime))

def updateTotalPunches():
	global totalPunches, totalPunchesStrVar
	print("totalPunches Updated")
	totalPunchesStrVar.set((str)(totalPunches))

def updatePunchesLanded():
	global punchesLanded, punchesLandedStrVar
	print("punchesLanded Updated")
	punchesLandedStrVar.set((str)(punchesLanded))

def updateHitsTaken():
	global hitsTaken, hitsTakenStrVar
	print("hitsTakenStrVar Updated")
	hitsTakenStrVar.set((str)(hitsTaken))

def roundsThread():
	import serial
	global running, pausedBoolean, gameTime, gameTimetStrVar, rounds
	global totalPunches, punchesLanded, totalPunchesStrVar, punchesLandedStrVar
	global hitsTaken, hitsTakenStrVar, currentRound, frame, bodyImg, q, ser, currentRound
	running = True
	currentRound = 1

	pausedBoolean = False

	#ser = serial.Serial("COM41")
	ser = serial.Serial("/dev/ttyUSB0")
	ser.baudrate = 9600
	ser.timeout = 0.25
	time.sleep(2.1)
	global ser
	if roundDifficulty == 1:
		msg = "tm"
		ser.write(bytes(msg.encode('ascii')))

	elif roundDifficulty == 2:
		msg = "tm"
		ser.write(bytes(msg.encode('ascii')))

	elif roundDifficulty == 3:
		msg = "tf"
		ser.write(bytes(msg.encode('ascii')))

	while(currentRound <= rounds and running):
		#print("Tick")
		#-------------------Game Logic--------------------------------
		#round--------------------------------------------------------
		on_main_thread(updateBgImage)
		time.sleep(1)
		roundGame()	
		currentRound += 1

		if currentRound <= rounds and running:
			#break--------------------------------------------------------
			on_main_thread(breakBgImage)
			time.sleep(1)
			breakGame()

	ser.close()

def roundGame():
	global running, pausedBoolean, gameTime, gameTimetStrVar
	global totalPunches, punchesLanded, totalPunchesStrVar, punchesLandedStrVar
	global hitsTaken, hitsTakenStrVar, currentRound, frame, bodyImg, q, ser

	gameTime = 180
	on_main_thread(updateTime)
	counter = 0
	pads = 4
	upTime = [0] * pads
	colors = ['o', 'o', 'o', 'o']
	counter = 0
	aTargetLit = False

	#-----Game Settings--------------------------------------
	easyFrequency = 10
	easyLitTimeMax = 200
	easyLitTimeMin = 100
	easyRatio = .25

	intermediateFrequency = 20
	intermediateLitTimeMax = 100
	intermediateLitTimeMin = 50
	intermediateRatio = .5

	hardcoreFrequency = 50
	hardcoreLitTimeMax = 50
	hardcoreLitTimeMin = 25
	hardcoreRatio = 1

	#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	if roundDifficulty == 1:
		frequency = easyFrequency
		litTimeMax = easyLitTimeMax
		litTimeMin = easyLitTimeMin
		ratio = easyRatio

	elif roundDifficulty == 2:
		frequency = intermediateFrequency
		litTimeMax = intermediateLitTimeMax
		litTimeMin = intermediateLitTimeMin
		ratio = intermediateRatio

	elif roundDifficulty == 3:
		frequency = hardcoreFrequency
		litTimeMax = hardcoreLitTimeMax
		litTimeMin = hardcoreLitTimeMin
		ratio = hardcoreRatio
	print("Starting Round " + (str)(currentRound))

	while(running and gameTime > 0):
		while(pausedBoolean):
			print("Game Paused")
			time.sleep(.1)
		#print("tack")	


		#Round Logic -------------------------------------------
		for pad in range (1,5):
				#subtract one second from Uptime also check if Target is up.		
				if upTime[pad -1] == 0:
					#Turn Pad OFF increase Hits taken if yellow and display red
					if colors[pad-1] == 'y':
						msg = (str)(pad) + "r"
						ser.write(bytes(msg.encode('ascii')))
						hitsTaken += 1
						on_main_thread(updateHitsTaken)
						aTargetLit = False
					else:
						msg = (str)(pad) + "o"
						ser.write(bytes(msg.encode('ascii')))
						aTargetLit = False
					print(msg)
				elif upTime[pad -1] < 0 and aTargetLit == False:
					#Pad is off, 
					# if target isn't lit, roll to see if it lights up.
					#Roll to determine color
					if random.randint(0, 100) <= ratio * 100:
						msg = (str)(pad) + "y"
						colors[pad -1] = 'y'
					else:
						msg = (str)(pad) + "g"
						colors[pad -1] = 'g'
					if random.randint(0, 600) <= frequency:
						#roll another number to determine the Light's up Time
						upTime[pad -1] = random.randint(litTimeMin, litTimeMax)
						#Transmit the color to the Pad
						ser.write(bytes(msg.encode('ascii')))
						print(msg)						
						aTargetLit = True
				upTime[pad -1] -= 1;



		#----------------Input Processing
		if ser.inWaiting() > 0:
			input = ser.read(size=1).decode("utf-8")
			if input == '1':
				print("one Hit Detected!")
				if upTime[0] > 0:
					#pad is On Turn off and stuff
					upTime[0] = -1
					msg = (str)(1) + "o"
					aTargetLit = False
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					on_main_thread(updatePunchesLanded)

				totalPunches += 1
				on_main_thread(updateTotalPunches)

			elif input == '2':
				print("two Hit Detected!")
				if upTime[1] > 0:
					#pad is On Turn off and stuff
					upTime[1] = -1
					msg = (str)(2) + "o"
					aTargetLit = False
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					on_main_thread(updatePunchesLanded)

				totalPunches += 1
				on_main_thread(updateTotalPunches)

			elif input == '3':
				print("three Hit Detected!")
				if upTime[2] > 0:
					#pad is On Turn off and stuff
					upTime[2] = -1
					msg = (str)(3) + "o"
					aTargetLit = False
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					on_main_thread(updatePunchesLanded)

				totalPunches += 1
				on_main_thread(updateTotalPunches)

			elif input == '4':
				print("four Hit Detected!")
				if upTime[3] > 0:
					#pad is On Turn off and stuff
					upTime[3] = -1
					msg = (str)(4) + "o"
					aTargetLit = False
					ser.write(bytes(msg.encode('ascii')))
					punchesLanded += 1
					on_main_thread(updatePunchesLanded)

				totalPunches += 1
				on_main_thread(updateTotalPunches)
			elif input != "":
				print(input)

		if counter > 9:
			counter = 0
			gameTime = gameTime - 1
			if gameTime >= 60:
				m, s = divmod(gameTime, 60)
				gameTimetStrVar.set("%d:%02d" % (m, s))
			else:
				if roundDifficulty == 3:
					frequency += 2
					if gameTime <= 30 and gameTime > 15:
						litTimeMax = 25
						litTimeMin = 12
					elif gameTime < 15:
						litTimeMax = 12
						litTimeMin = 6
				on_main_thread(updateTime)

		counter += 1
		time.sleep(.1)

	#turn All Pads off
	#Turn Pad OFF
	msg = (str)(1) + "o"
	ser.write(bytes(msg.encode('ascii')))
	msg = (str)(2) + "o"
	ser.write(bytes(msg.encode('ascii')))
	msg = (str)(3) + "o"
	ser.write(bytes(msg.encode('ascii')))
	msg = (str)(4) + "o"
	ser.write(bytes(msg.encode('ascii')))


def breakGame():
	global gameTimetStrVar, pausedBoolean, running, frame, gameTime
	print("A Break")
	gameTime = 60
	while(gameTime > 0 and running):
		while(pausedBoolean):
			print("Game Paused")
			time.sleep(.1)
		on_main_thread(updateTime)
		time.sleep(1)
		gameTime -= 1
		print("Tock")


def toTrainingDurationScreen():
	global windowState
	print("toTrainingDurationScreen Clicked")
	windowState = "trainingDurationScreen"
	loadWindow()

def toGameSelectScreen():
	global windowState
	print("gameSelectScreen Clicked")
	windowState = "gameSelectScreen"
	loadWindow()

def toDifficultySelectScreen():
	global windowState
	print("toDifficultySelectScreen Clicked")
	windowState = "difficultySelectScreen"
	loadWindow()

def toGameScreen():
	global windowState, gameSelected, roundDifficulty
	print("toGameScreen Clicked")
	if gameSelected == 1:
		if roundDifficulty != -1:
			windowState = "gameScreen"
			loadWindow()
	elif gameSelected == 0:
		windowState = "gameScreen"
		loadWindow()

def toNextGame():
	global windowState, gameSelected
	print("toNextGame Clicked")

	if gameSelected == 0:
		windowState = "trainingSelectScreen"
		loadWindow()
	elif gameSelected == 1:
		windowState = "roundsSelectScreen"
		loadWindow()

def pauseResumeGame():
	global frame, pPBtn, pausedBoolean, ser
	if pausedBoolean == False:

		pausedBoolean = True
		msg = "to"
		ser.write(bytes(msg.encode('ascii')))
		pPBtnFrame=Frame(frame)
		pPBtnFrame.config(width=200,height=151, bg='white')#1024x600
		pPBtnFrame.place(x=1024-200, y=300, anchor=NW)
		pPBtnFrame.grid_propagate(False)

		pPBtn = PhotoImage(file="Impact_50.0screenGameRESUME.gif")
		b = Button(pPBtnFrame, command=pauseResumeGame, image=pPBtn)
		b.config(width=200, height=149, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=1)

	else:
		pausedBoolean = False

		pPBtnFrame=Frame(frame)
		pPBtnFrame.config(width=200,height=151, bg='black')#1024x600
		pPBtnFrame.place(x=1024-200, y=300, anchor=NW)
		pPBtnFrame.grid_propagate(False)

		pPBtn = PhotoImage(file="Impact_50.0screenGamePAUSE.gif")
		b = Button(pPBtnFrame, command=pauseResumeGame, image=pPBtn)
		b.config(width=199, height=151, borderwidth=0, highlightthickness=0)
		b.place(x=0, y=0)

def cancelGameScreen():
	global windowState, gameSelected, running, pausedBoolean, ser
	print("cancelGameScreen Clicked")
	running = False
	pausedBoolean = False
	msg = "to"
	ser.write(bytes(msg.encode('ascii')))

	if gameSelected == 0:
		windowState = "trainingDurationScreen"
		loadWindow()
	elif gameSelected == 1:
		windowState = "difficultySelectScreen"
		loadWindow()
def upSpeed():	
	global ser
	msg = "tu"
	ser.write(bytes(msg.encode('ascii')))
def downSpeed():	
	global ser
	msg = "td"
	ser.write(bytes(msg.encode('ascii')))

loadWindow()
root.mainloop()
print('Bluefish Concepts')
