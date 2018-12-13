#!/usr/bin/env python2

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   ITALIC = '\033[3m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def printb(str):
    print(color.BOLD + str + color.END)

def printitb(str):
    print(color.BOLD + color.ITALIC + str + color.END)

def printit(str):
    print(color.ITALIC + str + color.END)

def printu(str):
    print(color.UNDERLINE + str + color.END)
