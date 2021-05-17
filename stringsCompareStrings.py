import openpyxl
import os
from pathlib import Path
import xlsxwriter

path1 = '/Users/h0057/Desktop/VT/VantageFX/en.lproj/Localizable.strings'
path2 = '/Users/h0057/Desktop/VT/VantageFX/fr.lproj/Localizable.strings'

data1 = []
data2 = []

def removeSpecialCharacter(text, special):
    result = ''
    isSet = False
    startIdx = 0
    endIdx = 0 

    for i in range(0, len(text)):
        char = text[i]
        if char == '"':
            if isSet == False: 
                startIdx = i+1
                isSet = True
                continue
            else:
                endIdx = i 
    
    result = text[startIdx:endIdx]
    return result

def readFileFromPath(path):
    file = open(path, 'r')
    lines = file.readlines()
    keys = []
    for line in lines:
        arr = line.split('=')
        if len(arr) == 2:
            key = arr[0]
            key = removeSpecialCharacter(key, '"')
            keys.append(key)
        else:
            print(line)
    return keys

def comparaTwoFile():
    data1 = readFileFromPath(path1)
    data2 = readFileFromPath(path2)

    for key1 in data1: 
        isExist = False
        for key2 in data2:
            if key2 == key1:
                isExist = True
                break
        if isExist == False:
            print(key1)

comparaTwoFile()