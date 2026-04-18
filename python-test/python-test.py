# -*- coding:utf-8 -*-

import os


'''
这是个测试程序
'''


print 'hello world'


def testprint():
    print '=====main start'
    print 'main'
    print '=====main end'


def test():
    today='20210531'
    print today
    print today+"_test"

def getFilePath():
    return '/Users/apple/Documents/study/python/python-test/test.txt'

def readFile(filePath):
    f = open(filePath)
    s = 1
    for line in f.readlines():
        print line
    f.close()
    return s

def Hello():
    file = getFilePath()
    readFile(file)


if __name__ == "__main__":
    Hello()











