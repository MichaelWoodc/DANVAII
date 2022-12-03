# works as of november 22, 2022
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on September 19, 2022, at 11:12
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import fillpdf
from fillpdf import fillpdfs
from PIL import Image, ImageDraw, ImageFont

expInfo = {'session': '001', 'participant': '', 'age': '', 'gender': '', 'ethnicity': ''}

# This is a before experiment comment in the code section of the readymessage section

# Let's initialize some numbers for loops
dictionaryloop = 0
dictionaryloop2 = 0

#Let's make some lists and dictionaries to store all of the variables we will place into our PDF
danvasubtest = 'Adult'
data_dict = {}
stimsList = {}
correctAnswers = {}
incorrectAnswers = {}
errorList = []
NamesCorrectAnswers = {}
intensity = ''
gender = ''
genderOfAnswer = ''
intensityOfAnswer = ''
correctAnswerForString = ''


# This is a begin experiment comment in the code section of the readymessage section
highIntensityErrors = 0
lowIntensityErrors = 0
errorList = []
skippedErrors = 0
errorsByMisjudgement = 0
totalErrors = 0
totalerrors = 0
happyHighIntensityErrors = 0
happyLowIntensityErrors = 0
sadHighIntensityErrors = 0
sadLowIntensityErrors = 0
angryHighIntensityErrors = 0
angryLowIntensityErrors = 0
fearfulHighIntensityErrors = 0
fearfulLowIntensityErrors = 0
happyErrors = 0
sadErrors = 0
angryErrors = 0
fearfulErrors = 0
lowIntensityErrors = 0
misattributedHappySad = 0
misattributedHappyAngry = 0
misattributedHappyFearful = 0
misattributedSadHappy = 0
misattributedSadAngry = 0
misattributedSadFearful = 0
misattributedAngryHappy = 0
misattributedAngrySad = 0
misattributedAngryFearful = 0
misattributedFearfulHappy = 0
misattributedFearfulSad = 0
misattributedFearfulAngry = 0
maleHappyErrors = 0
maleSadErrors = 0
maleAngryErrors = 0
maleFearfulErrors = 0
maleTotalErrors = 0
femaleHappyErrors = 0
femaleSadErrors = 0
femaleAngryErrors = 0
femaleFearfulErrors = 0
femaleTotalErrors = 0


# This is to set the number of the trial for scoring the right data

dictionarydefinitions = ["skippedErrors","totalErrors","totalerrors","happyHighIntensityErrors","happyLowIntensityErrors",
                         "sadHighIntensityErrors","sadLowIntensityErrors","angryHighIntensityErrors",
                         "angryLowIntensityErrors","fearfulHighIntensityErrors","fearfulLowIntensityErrors",
                         "happyErrors","sadErrors","angryErrors","fearfulErrors","lowIntensityErrors",
                         "highIntensityErrors","misattributedHappySad","misattributedHappyAngry",
                         "misattributedHappyFearful","misattributedSadHappy","misattributedSadAngry",
                         "misattributedSadFearful","misattributedAngryHappy","misattributedAngrySad",
                         "misattributedAngryFearful","misattributedFearfulHappy","misattributedFearfulSad",
                         "misattributedFearfulAngry","errorsByMisjudgement","danvasubtest","maleHappyErrors",
                         "maleSadErrors","maleAngryErrors","maleFearfulErrors","maleTotalErrors",
                         "femaleHappyErrors","femaleSadErrors","femaleAngryErrors","femaleFearfulErrors","femaleTotalErrors",
                         "totalErrors1","totalErrors2","happyErrors2","sadErrors2","angryErrors2","fearfulErrors2",]
# this is a comment "before experiment"


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'blockedTrials'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': '', 'age': '', 'gender': '', 'ethnicity': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\micha\\1 CODE\\DANVA\\DANVA\\.vscode\\2_template demographics inside psychopy builder_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-0.396,-0.396,-0.396], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "readyMessage"
readyMessageClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text="I am going to show you some people's faces and I want you to tell me how they feel. I want you to tell me if they are happy, sad, angry, or fearful (scared). Let's get started.\n(Esc will quit, laptops may require clicking quit button)\n\n\nPress any key to continue",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
starttest = keyboard.Keyboard()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', units='height', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(0.6936,0.4704),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.6), units=None,
    labels=["HAPPY", "SAD", "ANGRY", "FEARFUL"], ticks=(1, 2, 3, 4), granularity=1,
    style=['rating'], styleTweaks=[], opacity=1,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Arial', labelHeight=0.05,
    flip=False, ori=0, depth=-1, readOnly=False)
next_button = visual.TextStim(win=win, name='next_button',
    text='CONTINUE',
    font='Arial',
    pos=(.7, -0.6), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
mouse_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_2.mouseClock = core.Clock()
# this is a begin experiment comment

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "readyMessage"-------
continueRoutine = True
# update component parameters for each repeat
starttest.keys = []
starttest.rt = []
_starttest_allKeys = []
# setup some python lists for storing info about the mouse
gotValidClick = False  # until a click is received
# This is a begin routine comment in the code section of the readymessage section
# keep track of which components have finished
readyMessageComponents = [Instructions, starttest, mouse]
for thisComponent in readyMessageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
readyMessageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "readyMessage"-------
while continueRoutine:
    # get current time
    t = readyMessageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=readyMessageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *starttest* updates
    waitOnFlip = False
    if starttest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        starttest.frameNStart = frameN  # exact frame index
        starttest.tStart = t  # local t and not account for scr refresh
        starttest.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(starttest, 'tStartRefresh')  # time at next scr refresh
        starttest.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(starttest.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(starttest.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if starttest.status == STARTED and not waitOnFlip:
        theseKeys = starttest.getKeys(keyList=None, waitRelease=False)
        _starttest_allKeys.extend(theseKeys)
        if len(_starttest_allKeys):
            starttest.keys = _starttest_allKeys[-1].name  # just the last key pressed
            starttest.rt = _starttest_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in readyMessageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "readyMessage"-------
for thisComponent in readyMessageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "readyMessage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
EmotionTests = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('facesBlock.csv'),
    seed=None, name='EmotionTests')
thisExp.addLoop(EmotionTests)  # add the loop to the experiment
thisEmotionTest = EmotionTests.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEmotionTest.rgb)
if thisEmotionTest != None:
    for paramName in thisEmotionTest:
        exec('{} = thisEmotionTest[paramName]'.format(paramName))

for thisEmotionTest in EmotionTests:
    currentLoop = EmotionTests
    # abbreviate parameter names if possible (e.g. rgb = thisEmotionTest.rgb)
    if thisEmotionTest != None:
        for paramName in thisEmotionTest:
            exec('{} = thisEmotionTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(stimFile)
    slider.reset()
    # setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # this is a begin routine comment   
    # keep track of which components have finished
    trialComponents = [image, slider, next_button, mouse_2]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *slider* updates
        if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *next_button* updates
        if next_button.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_button.frameNStart = frameN  # exact frame index
            next_button.tStart = t  # local t and not account for scr refresh
            next_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_button, 'tStartRefresh')  # time at next scr refresh
            next_button.setAutoDraw(True)
        # *mouse_2* updates
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(next_button)
                        clickableList = next_button
                    except:
                        clickableList = [next_button]
                    for obj in clickableList:
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        #this is an "each frame" comment
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    EmotionTests.addData('image.started', image.tStartRefresh)
    EmotionTests.addData('image.stopped', image.tStopRefresh)
    EmotionTests.addData('slider.response', slider.getRating())
    EmotionTests.addData('slider.rt', slider.getRT())
    EmotionTests.addData('slider.started', slider.tStartRefresh)
    EmotionTests.addData('slider.stopped', slider.tStopRefresh)
    EmotionTests.addData('next_button.started', next_button.tStartRefresh)
    EmotionTests.addData('next_button.stopped', next_button.tStopRefresh)
    # store data for EmotionTests (TrialHandler)
    x, y = mouse_2.getPos()
    buttons = mouse_2.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(next_button)
            clickableList = next_button
        except:
            clickableList = [next_button]
        for obj in clickableList:
            if obj.contains(mouse_2):
                gotValidClick = True
                mouse_2.clicked_name.append(obj.name)
    EmotionTests.addData('mouse_2.x', x)
    EmotionTests.addData('mouse_2.y', y)
    EmotionTests.addData('mouse_2.leftButton', buttons[0])
    EmotionTests.addData('mouse_2.midButton', buttons[1])
    EmotionTests.addData('mouse_2.rightButton', buttons[2])
    if len(mouse_2.clicked_name):
        EmotionTests.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
    EmotionTests.addData('mouse_2.started', mouse_2.tStart)
    EmotionTests.addData('mouse_2.stopped', mouse_2.tStop)
    # this is an "end routine" comment in the trial section
    
    
    
        
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'EmotionTests'


for i in currentLoop.trialList : 
    
    # Let's do the basic things first:
    stimsList['stim' + str(dictionaryloop)] = (currentLoop.trialList[dictionaryloop]['stimFile'])
    if thisExp.entries[dictionaryloop + 1]['slider.response'] == None:
        skippedErrors = skippedErrors + 1
    
    # Let's concact a string to fill in the correct answer with intensity and gender column, we'll start with emotion
    if currentLoop.trialList[dictionaryloop]['correctAnswer'] == 1:
        correctAnswerForString = 'Happy '
    elif currentLoop.trialList[dictionaryloop]['correctAnswer'] == 2:
        correctAnswerForString = 'Sad '
    elif currentLoop.trialList[dictionaryloop]['correctAnswer'] == 3:
        correctAnswerForString = 'Angry '
    elif currentLoop.trialList[dictionaryloop]['correctAnswer'] == 4:
        correctAnswerForString = 'Fearful '
    else:
        pass
    # Now let's grab the intensity
    if  currentLoop.trialList[dictionaryloop]['intensity'] == 1:
        intensityOfAnswer = 'Low '
        
    elif currentLoop.trialList[dictionaryloop]['intensity'] == 2:
        intensityOfAnswer = 'High '
    else:
        pass
    # Now let's grab the gender:
    if  currentLoop.trialList[dictionaryloop]['stimuliGender'] == 1:
        genderOfAnswer = 'Female'
    elif currentLoop.trialList[dictionaryloop]['stimuliGender'] == 2:
        genderOfAnswer = 'Male'
    else:
        pass
    # Now let's plug that into the PDF
    correctAnswers['correctAnswer'+ str(dictionaryloop)] = (correctAnswerForString) + (intensityOfAnswer) + (genderOfAnswer)

    if thisExp.entries[dictionaryloop + 1]['slider.response'] != currentLoop.trialList[dictionaryloop]['correctAnswer']:
        totalErrors = totalErrors+1
        response = thisExp.entries[dictionaryloop+1]['slider.response']
        # this will give us the errors
        correctAnswerKey = currentLoop.trialList[dictionaryloop]['correctAnswer']
        
        if currentLoop.trialList[dictionaryloop]['stimuliGender'] == 1:
            maleTotalErrors = maleTotalErrors + 1
        elif currentLoop.trialList[dictionaryloop]['stimuliGender'] == 2:
            femaleTotalErrors = femaleTotalErrors + 1
        else:
            pass
        
        
        
        if  currentLoop.trialList[dictionaryloop]['intensity'] == 1:
            lowIntensityErrors = lowIntensityErrors + 1
        elif currentLoop.trialList[dictionaryloop]['intensity'] == 2:
            highIntensityErrors = highIntensityErrors + 1
        else:
            pass        
        
        if correctAnswerKey == 1:
            happyErrors = happyErrors + 1
            #correctAnswers['correctAnswer'+ str(dictionaryloop)] = 'Happy'
            if  currentLoop.trialList[dictionaryloop]['intensity'] == 1:
                happyLowIntensityErrors = happyLowIntensityErrors + 1
            elif currentLoop.trialList[dictionaryloop]['intensity'] == 2:
                happyHighIntensityErrors = happyHighIntensityErrors + 1
            else:
                pass        

            if response == 2:
                misattributedHappySad = misattributedHappySad + 1
            elif response == 3:
                misattributedHappyAngry = misattributedHappyAngry + 1
            elif response == 4:
                misattributedHappyFearful = misattributedHappyFearful + 1
            else:
                pass
            if currentLoop.trialList[dictionaryloop]['stimuliGender'] == 1:
                maleHappyErrors = maleHappyErrors + 1
            elif currentLoop.trialList[dictionaryloop]['stimuliGender'] == 2:
                femaleHappyErrors = femaleHappyErrors + 1
            else: 
                pass
            
        if correctAnswerKey == 2:
            sadErrors = sadErrors + 1
            if  currentLoop.trialList[dictionaryloop]['intensity'] == 1:
                sadLowIntensityErrors = sadLowIntensityErrors + 1     
            elif currentLoop.trialList[dictionaryloop]['intensity'] == 2:
                sadHighIntensityErrors = sadHighIntensityErrors + 1                
            else:
                pass

            if response == 1:
                misattributedSadHappy = misattributedSadHappy + 1
            elif response == 3:
                misattributedSadAngry = misattributedSadAngry + 1
            elif response == 4:
                misattributedSadFearful = misattributedSadFearful + 1
            else:
                pass
            
            if currentLoop.trialList[dictionaryloop]['stimuliGender'] == 1:
                maleSadErrors = maleSadErrors + 1
            elif currentLoop.trialList[dictionaryloop]['stimuliGender'] == 2:
                femaleSadErrors = femaleSadErrors + 1
            else: 
                pass
            
        if correctAnswerKey == 3:
            angryErrors = angryErrors + 1
            if  currentLoop.trialList[dictionaryloop]['intensity'] == 1:
                angryLowIntensityErrors = angryLowIntensityErrors + 1        
            elif currentLoop.trialList[dictionaryloop]['intensity'] == 2:
                angryHighIntensityErrors = angryHighIntensityErrors + 1                
            else:
                pass
            
            if response == 1:
                misattributedAngryHappy = misattributedAngryHappy + 1
            elif response == 2:
                misattributedAngrySad = misattributedAngrySad + 1
            elif response == 4:
                misattributedAngryFearful = misattributedAngryFearful + 1
            else:
                pass
            
            if currentLoop.trialList[dictionaryloop]['stimuliGender'] == 1:
                maleAngryErrors = maleAngryErrors + 1
            elif currentLoop.trialList[dictionaryloop]['stimuliGender'] == 2:
                femaleAngryErrors = femaleAngryErrors + 1
            else: 
                pass
            
        if correctAnswerKey == 4:
            fearfulErrors = fearfulErrors + 1
            if  currentLoop.trialList[dictionaryloop]['intensity'] == 1:
                fearfulLowIntensityErrors = fearfulLowIntensityErrors + 1
            elif currentLoop.trialList[dictionaryloop]['intensity'] == 2:
                fearfulHighIntensityErrors = fearfulHighIntensityErrors + 1
            else:
                pass
            
            if response == 1:
                misattributedFearfulHappy = misattributedFearfulHappy + 1
            elif response == 2:
                misattributedFearfulSad = misattributedFearfulSad + 1
            elif response == 3:
                misattributedFearfulAngry = misattributedFearfulAngry + 1
            else:
                pass
            
            if currentLoop.trialList[dictionaryloop]['stimuliGender'] == 1:
                maleFearfulErrors = maleFearfulErrors + 1
            elif currentLoop.trialList[dictionaryloop]['stimuliGender'] == 2:
                femaleFearfulErrors = femaleFearfulErrors + 1
            else:
                pass
            
        else:
            pass

        if response == 1:
            incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Happy'        
        elif response == 2:
            incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Sad'
        elif response == 3:
            incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Angry'
        elif response == 4:
            incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Fearful'
        else:
            incorrectAnswers['incorrectAnswer'+ str(dictionaryloop)] = 'Skipped'
    
    dictionaryloop = dictionaryloop + 1

totalerrors = totalErrors
errorsByMisjudgement = totalErrors - skippedErrors

totalErrors1 = totalerrors
totalErrors2 = totalerrors
happyErrors2 = happyErrors
sadErrors2 = sadErrors
angryErrors2 = angryErrors
fearfulErrors2 = fearfulErrors

for i in (dictionarydefinitions):
    data_dict [dictionarydefinitions[dictionaryloop2]] = (eval(dictionarydefinitions[dictionaryloop2]))
    # I have no idea what I was doing with the below.  It should probably just go in the other section
    # stimsList['stim'+str((dictdefincr2 - 1))] = (currentLoop.trialList[(dictdefincr2)-1]['stimFile'])
    dictionaryloop2 = dictionaryloop2 + 1


data_dict.update(stimsList)
data_dict.update(expInfo)
data_dict.update(incorrectAnswers)
data_dict.update(correctAnswers)



# "this is an end experiment comment

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)




happycolor = "#00FF00"
sadcolor = "#0000FF"
angrycolor = "#FF0000"
fearfulcolor = "#FFFF00"
malecolor = "#0000FF"
femalecolor = "#FF0000"

widthmain = 480
heightmain = 30

totalerrorsincrement = widthmain/24

widthmisattributions = 378
heightmisattributions = 20
errorsincrementmisattribute = widthmisattributions/18
misattributionerrorsincrement = widthmisattributions/18

widthgendererrors = 378
errorsincrementgender = widthgendererrors/24
gendererrorsincrement = widthgendererrors/24

shape = [(0, 0), (widthmain, heightmain)]

happystartx = 0
happyendx = (happyErrors * totalerrorsincrement)
sadstartx = happyendx
sadendx = sadstartx + (sadErrors * totalerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (angryErrors * totalerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (fearfulErrors * totalerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmain)]
sadrectangle = [(sadstartx,0),(sadendx,heightmain) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmain)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmain)]
  
# creating new Image object
totalerrorsgraph = Image.new("RGB", (widthmain, heightmain),color = "#FFFFFF")




# create rectangle image for happy errors
happyerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
saderrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
angryerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)
fearfulerrorsrectangle = ImageDraw.Draw(totalerrorsgraph)

happyerrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
saderrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryerrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulerrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

# totalerrorsgraph.show()
totalerrorsgraph.save("graphPictures/totalerrorsgraph.jpg")

#create picture for happy misattributions

happystartx = 0
happyendx = (0) # only since we're on the happy misattributions graph
sadstartx = happyendx
sadendx = sadstartx + (misattributedHappySad * misattributionerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (misattributedHappyAngry * misattributionerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (misattributedHappyFearful * misattributionerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


  # creating new Image object
happyMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
sadErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
angryErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)
fearfulErrorsrectangle = ImageDraw.Draw(happyMisattributionsGraph)

sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

# happyMisattributionsGraph.show()
happyMisattributionsGraph.save("graphPictures/happyMisattributions.jpg")

happystartx = 0
happyendx = (misattributedSadHappy * misattributionerrorsincrement) 
sadstartx = happyendx
sadendx = sadstartx # only since we're on the sad misattributions graph
angrystartx = sadendx
angryendx = angrystartx + (misattributedSadAngry * misattributionerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (misattributedSadFearful*misattributionerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


  # creating new Image object
sadMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)
angryErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)
fearfulErrorsrectangle = ImageDraw.Draw(sadMisattributionsGraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

# sadMisattributionsGraph.show()
sadMisattributionsGraph.save("graphPictures/sadMisattributions.jpg")

happystartx = 0
happyendx = happystartx + (misattributedAngryHappy * misattributionerrorsincrement) 
sadstartx = happyendx
sadendx = sadstartx + (misattributedAngrySad * misattributionerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx # only since we're on the Angry misattributions graph
fearfulstartx = angryendx
fearfulendx = fearfulstartx + (misattributedAngryFearful * misattributionerrorsincrement)

happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


  # creating new Image object
angryMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)
sadErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)
fearfulErrorsrectangle = ImageDraw.Draw(angryMisattributionsGraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
fearfulErrorsrectangle.rectangle(fearfulrectangle, fill =fearfulcolor, outline=None)

# angryMisattributionsGraph.show()
angryMisattributionsGraph.save("graphPictures/angryMisattributions.jpg")

happystartx = 0
happyendx = (misattributedFearfulHappy * misattributionerrorsincrement) 
sadstartx = happyendx
sadendx = sadstartx + (misattributedFearfulSad*misattributionerrorsincrement)
angrystartx = sadendx
angryendx = angrystartx + (misattributedFearfulAngry*misattributionerrorsincrement)
fearfulstartx = angryendx
fearfulendx = fearfulstartx # because we are making the fearful graph


happyrectangle = [(0, 0), (happyendx , heightmisattributions)]
sadrectangle = [(sadstartx,0),(sadendx,heightmisattributions) ]
angryrectangle = [(angrystartx,0), (angryendx, heightmisattributions)]
fearfulrectangle = [(fearfulstartx,0), (fearfulendx,heightmisattributions)]


# creating new Image object
fearfulMisattributionsGraph = Image.new("RGB", (widthmisattributions, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
happyErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph)
sadErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph)
angryErrorsrectangle = ImageDraw.Draw(fearfulMisattributionsGraph)

happyErrorsrectangle.rectangle(happyrectangle, fill =happycolor, outline=None)
sadErrorsrectangle.rectangle(sadrectangle, fill =sadcolor, outline=None)
angryErrorsrectangle.rectangle(angryrectangle, fill =angrycolor, outline=None)

# fearfulMisattributionsGraph.show()
fearfulMisattributionsGraph.save("graphPictures/fearfulMisattributions.jpg")

# Gender Errors Graph
malestartx = 0
maleendx = malestartx + (maleTotalErrors * errorsincrementgender) 
femalestartx = maleendx
femaleendx = femalestartx + (femaleTotalErrors * errorsincrementgender)

malerectangle = [(0, 0), (maleendx , heightmisattributions)]
femalerectangle = [(femalestartx,0),(femaleendx,heightmisattributions) ]

# creating new Image object
genderErrorsGraph = Image.new("RGB", (widthgendererrors, heightmisattributions),color = "#FFFFFF")

# create rectangle image for happy Errors
maleTotalErrorsrectangle = ImageDraw.Draw(genderErrorsGraph)
femaleTotalErrorsrectangle = ImageDraw.Draw(genderErrorsGraph)


maleTotalErrorsrectangle.rectangle(malerectangle, fill =malecolor, outline=None)
femaleTotalErrorsrectangle.rectangle(femalerectangle, fill =femalecolor, outline=None)

# genderErrorsGraph.show()
genderErrorsGraph.save("graphPictures/errorsbygender.jpg")



# data_dict
# Now let's insert the images

fillpdfs.place_image('graphPictures/totalerrorsgraph.jpg', 124, 769, 'blankDocumentNumberLine.pdf', 'pdfMagic/completed.pdf', 1, width=636, height=165)

# These were the values before changing to the document with the number lines
page2GraphStart = 120
# page2GraphWidth = 283
# page2GraphHeight = 15

happygraphstarty = 161
#The following are for the other graphs
fillpdfs.place_image('graphPictures/happyMisattributions.jpg', page2GraphStart, happygraphstarty, 'pdfMagic/completed.pdf', 'pdfMagic/completed1.pdf', 2, width=widthmisattributions, height=heightmisattributions)
fillpdfs.place_image('graphPictures/sadMisattributions.jpg', page2GraphStart, happygraphstarty-43, 'pdfMagic/completed1.pdf', 'pdfMagic/completed2.pdf', 2, width=widthmisattributions, height=heightmisattributions)
fillpdfs.place_image('graphPictures/angryMisattributions.jpg', page2GraphStart, happygraphstarty-85, 'pdfMagic/completed2.pdf', 'pdfMagic/completed3.pdf', 2, width=widthmisattributions, height=heightmisattributions)
fillpdfs.place_image('graphPictures/fearfulMisattributions.jpg', page2GraphStart, happygraphstarty-126, 'pdfMagic/completed3.pdf', 'pdfMagic/completed4.pdf', 2, width=widthmisattributions, height=heightmisattributions)
fillpdfs.place_image('graphPictures/errorsbygender.jpg',page2GraphStart, happygraphstarty-238, 'pdfMagic/completed4.pdf', 'pdfMagic/completed.pdf', 2, width=widthmisattributions, height=heightmisattributions)

fillpdfs.write_fillable_pdf('pdfMagic/completed.pdf', 'completed.pdf', data_dict, flatten=False)
os.startfile('completed.pdf')



logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()