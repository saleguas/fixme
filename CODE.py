#!/usr/bin/python

#############################################################
#|
#|  Obviously the code below is incorrect and will not function correctly.
#|  Try to see what the issue may be. Thought I'm listing some simple commands for Python3, try going on
#|  https://www.geeksforgeeks.org/python-3-basics/ 
#|  to learn more
#|
#|  How to import stuff:
#|  import <module>
#|
#|  How to create a function:
#|  def <name>():
#|     <code here>
#|
#|  How to print something:
#|  print("<type stuff here>")
#|
#|  How to commentate:
#|  # <Commentary>
#|
#############################################################
#| 
#| Please fix, commentate, and edit any code under the line below!
#| 
#############################################################

import os
import sys
import platform
import time
import datetime


#the function uses the "os" module to get a result of either, linux1, linux2, darwin, or win32
def get_platform():
    platforms = {
        'linux1' : 'Linux', #if the platform gets linux1, call it "Linux"
        'linux2' : 'Linux', #if the platform gets linux2, call it " linux
        'darwin' : 'Mac OS X', #if the platform gets dawrin, call it "Mac OS X"
        'win32' : 'Windows' #  if the platform gets Windows, call it "win32"
    }


print("Welcome! Here's your system information! /n")

print("Your Local Time Zone: " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))#Local time zone

print("your platform         " + str(get_platform()))

print("Release Version       " + platform.release()) # gives the platform's machine

print("System:               " + platform.system()) #nothing

print("Machine:              " + platform.machine()) #gives the release version


