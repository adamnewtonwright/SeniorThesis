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

# Remember to check your Arduino Serial Connection and make sure it matches below
arduinoData = serial.Serial('/dev/cu.usbmodem1411',9600)


def move_on(): #this simplies moves the motor, need to define direction first
    arduinoData.write(b'1')
    give = int(entry.get())
    i = 0
    while i < give:
        arduinoData.write(b'1')
        i = i + 1
def move_off():
    arduinoData.write(b'0')
def left(): #cw, here we need to set the direction pin
    arduinoData.write(b'2')
def right(): #ccw
    arduinoData.write(b'3')

control_window = tkinter.Tk()
control_window.title("Dye Laser") # Giving it a title.

btn = tkinter.Button(control_window,text="move on",command=move_on)
btn2 = tkinter.Button(control_window,text="move off",command=move_off)
btn.pack()
btn2.pack()

lefty = tkinter.Button(control_window,text="left",command=left)
lefty.pack()
righty = tkinter.Button(control_window,text="right",command=right)
righty.pack()

label = tkinter.Label(control_window, text = "Number of Steps")
entry = tkinter.Entry(control_window, bd =5)

label.pack()
entry.pack()

control_window.mainloop()


while (1==1): #infinite loop
   if (arduinoData.inWaiting()>0): #is there data, no, if yes, then continue
       myData = arduinoData.readline()
       print (myData)
