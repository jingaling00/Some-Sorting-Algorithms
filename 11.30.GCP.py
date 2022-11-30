# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:47:17 2022

@author: jingy
"""

def bubbleSort(values):
    numSteps = 0
    for j in range(len(values)):
        length = len(values)-j
        for i in range(length-1):
            numSteps += 1
            if values[i] >= values[i+1]:
                values[i+1], values[i] = values[i], values[i+1]
    return values, numSteps
    
def selectionSort(values):
    numSteps = 0
    for j in range(len(values)):
        length = len(values)-j
        maxi = values[0]
        for i in range(length):
            numSteps += 1
            if values[i] >= maxi:
                maxi = values[i]
        values[values.index(maxi)], values[length-1] = values[length-1], values[values.index(maxi)]
    return values, numSteps

def insertSort(values):
    numSteps = 0
    for i in range(1,len(values)):
        key = values[i]
        j = i-1
        while j >= 0 and values[j] >= key:
            values[j+1] = values[j]
            numSteps += 1
            j-=1
        values[j+1] = key
    return values, numSteps
        