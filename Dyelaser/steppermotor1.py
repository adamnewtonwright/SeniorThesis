#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:13:09 2017

@author: adam
"""

#Donald Swen and Adam Wright
#Professor Kleinert
#Physics Research - Dye Laser Project 9-2-2016
#This program moves the stepper motor with python interface and through arduino.
#Input number of steps desired first. Choose a direction: left, right.
#Then click move on. Close program to exit and stop.
#A lot more functionality can be added, but this is the bare bones.

import serial #Import Serial Library
import time
#from Tkinter import *
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk

# Remember to check your Arduino Serial Connection and make sure it matches below
arduinoData = serial.Serial('/dev/cu.usbmodem1411',9600)


#This variable will count the total number of steps in a certain direction
total_steps = 0
localtime = time.asctime( time.localtime(time.time()) )
class Main:
    def __init__(self):

        #print the time and date
        #print(localtime)

        total_steps = 0
        # move on command
        def move_on(): #this simplies moves the motor, need to define direction first
            arduinoData.write(b'1')
            global total_steps
            give = int(entry.get())
            total_steps+=give
            # prints the number of steps moved and the total number of steps moved in a             direction
            # print(give, total_steps)
            Th.insert(tkinter.INSERT, give)
            Th.insert(tkinter.INSERT, "                         ")
            Th.insert(tkinter.INSERT, total_steps)
            Th.insert(tkinter.INSERT, "\n")
            i = 0
            while i < give:
                arduinoData.write(b'1')
                i = i + 1

        # Move off command
        def move_off():
            arduinoData.write(b'0')

        # Left Direction command
        def left(): #cw, here we need to set the direction pin
            print('Left')
            global total_steps
            total_steps = 0
            Th.insert(tkinter.INSERT, "Left")
            Th.insert(tkinter.INSERT, "\n")
            arduinoData.write(b'2')

        # Right direction command
        def right(): #ccw
            global total_steps
            total_steps = 0
            print('Right')
            Th.insert(tkinter.INSERT, "Right")
            Th.insert(tkinter.INSERT, "\n")
            arduinoData.write(b'3')


        # Main Frame
        root = tkinter.Tk()
        title = root.title("Dye Laser") # Giving it a title.
        root.geometry('625x700')


        # Text box
        T = tkinter.Text(root, height=3, width=30)
        T.pack()
        T.insert(tkinter.INSERT, localtime)
        T.insert(tkinter.INSERT, "\n")
        T.insert(tkinter.INSERT, "Select direction of Motion:")

        #Left/ right buttons
        lefty = tkinter.Button(root,text="left",command=left)
        lefty.pack()
        righty = tkinter.Button(root,text="right",command=right)
        righty.pack()

        # Text Box
        T1 = tkinter.Text(root, height=2, width=50)
        T1.pack()
        T1.insert(tkinter.INSERT, "Insert desired number of steps and press Move on:")

        #Entry widget
        label = tkinter.Label(root, text = "Number of Steps")
        entry = tkinter.Entry(root, bd =5)
        label.pack()
        entry.pack()

        #Move on/off buttons
        btn = tkinter.Button(root,text="move on",command=move_on)
        btn2 = tkinter.Button(root,text="move off",command=move_off)
        btn.pack()
        btn2.pack()

        # History Log
        Th = tkinter.Text(root, height=100, width=50)
        Th.insert(tkinter.INSERT, "                     History Log \n \n")
        Th.insert(tkinter.INSERT, "Individual Step          ")
        Th.insert(tkinter.INSERT, "Total Step \n")
        Th.pack()

        root.mainloop()

# Calling the main frame
window = Main()

# Looping through the inputs
while True:
   if (arduinoData.inWaiting()>0): #is there data, no, if yes, then continue
       myData = arduinoData.readline()
       print (myData)
