import keyboard as kb
import os
import datetime

class Count_Data:
    name = ""
    key = ""
    count = 0

Count_Datas = {}

def CreateCountData(name,key):
    data = Count_Data()
    data.name = name
    data.key = key
    Count_Datas[name] = data

    kb.add_hotkey("ctrl + "+key,lambda : Count(name,-1))
    kb.add_hotkey(key,lambda : Count(name,1))

def Count(name,amount):
    Count_Datas[name].count += amount
    if Count_Datas[name].count < 0: 
        Count_Datas[name].count = 0
    RefreshScreen()


def RefreshScreen():
    text = "Increase - Button\nDecrease - CTRL + Button\nSave - Space\n\n"

    for data in Count_Datas.values():   
        text+= f"|{data.key}- {data.name}: {data.count}|\n"

    os.system('cls')
    print(text)


def SaveCounters():
    path = "Counter_Save.csv"

    # check if file exists
    if not os.path.isfile(path):
        file = open(path,"w")
        file.write("")
        file.close()

    # get column names and date
    date = str(datetime.datetime.now())
    line = date
    Column_Names = "Date"
    for data in Count_Datas.values():
        line += f",{data.count}"
        Column_Names += f",{data.name}"
    Column_Names +="\n"

    # get the first line
    file = open(path,"r")
    file.readline()
    Remainder = file.read()
    file.close()

    # change the first line
    file = open(path,"w")
    file.write(Column_Names + Remainder)
    file.close()

    # append the new save
    file = open(path,"a")

    file.write(line+"\n")
    file.close()
    print("-- Saved --")

kb.add_hotkey("space",SaveCounters)