#!/usr/bin/python3
import datetime

filename="test.txt"
content = []


def getTimeSecs(preLine, nextLine):

    try:
        index = preLine.index('] ')
        nextIndex = nextLine.index('] ')
        preTime = datetime.datetime.strptime(preLine[index +2: index+ 25], '%Y-%m-%d %H:%M:%S.%f')
        nextTime = datetime.datetime.strptime(nextLine[nextIndex +2: nextIndex+ 25], '%Y-%m-%d %H:%M:%S.%f')
        return (nextTime - preTime).microseconds / 1000;
    except Exception,e:
        print e
        return 0


with open(filename, 'r') as fo:
    for line in fo.readlines():
        content.append(line.strip())


content.sort();

output="result.log"
with open(output, 'w+') as wo:
    preLine = ''
    for line in content:
        if preLine =='':
            preLine = line
        line = "["+ str(getTimeSecs(preLine, line))+"]"+line + '\n\r'
        wo.writelines(line)
        preLine = line





