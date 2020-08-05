from tkinter import *
from time import *
import time
import sys

Movelist = {"Move1":0, "Move2": 0, "Move3":0, "Move4":0,
                "Move5":0, "Move6":0,"Move7":0, "Move8":0, "Move9":0}

WinCondition = {"X1":"", "X2":"", "X3":"", "X4":"",
                "X5":"", "X6":"","X7":"", "X8":"", "X9":"",
                "O1":"", "O2":"", "O3":"", "O4":"", "O5":"",
                "O6":"","O7":"O", "O8":"O", "O9":"O"}

errorcheck = {"X1":0, "X2":0, "X3":0, "X4":0,
                "X5":0, "X6":0,"X7":0, "X8":0, "X9":0,
                "O1":0, "O2":0, "O3":0, "O4":0,"O5":0,
                "O6":0,"O7":0, "O8":0, "O9":0}

Winner = 0
checkvalue = 0





number1 = 1
number2 = 10


def winner (WinCondition):
    if WinCondition ['X1'] and WinCondition ['X2'] and WinCondition ['X3'] == "X":
        winner = 'X'
        return winner  
    elif WinCondition ['X4'] and WinCondition ['X5'] and WinCondition ['X6'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['X7'] and WinCondition ['X8'] and WinCondition ['X9'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['X7'] and WinCondition ['X5'] and WinCondition ['X3'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['X1'] and WinCondition ['X5'] and WinCondition ['X9'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['X1'] and WinCondition ['X4'] and WinCondition ['X7'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['X3'] and WinCondition ['X6'] and WinCondition ['X9'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['X2'] and WinCondition ['X5'] and WinCondition ['X8'] == "X":
        winner = 'X'
        return winner 
    elif WinCondition ['O1'] and WinCondition ['O2'] and WinCondition ['O3'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O4'] and WinCondition ['O5'] and WinCondition ['O6'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O7'] and WinCondition ['O8'] and WinCondition ['O9'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O7'] and WinCondition ['O5'] and WinCondition ['O3'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O1'] and WinCondition ['O5'] and WinCondition ['O9'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O1'] and WinCondition ['O4'] and WinCondition ['O7'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O3'] and WinCondition ['O6'] and WinCondition ['O9'] == "O":
        winner = 'O'
        return winner 
    elif WinCondition ['O2'] and WinCondition ['O5'] and WinCondition ['O8'] == "O":
        winner = 'O'
        return winner 
    else:
        return
