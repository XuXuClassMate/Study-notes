# -*- coding:utf-8 -*-


class App:
    name=""
    time=""
    s1=0.0
    s2=0.0
    s3=0.0
    s4=0.0
    s5=0.0

    resultAppList = []

    def __init__(self,name,time,s1,s2,s3,s4,s5):
        self.name=name
        self.time=time
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5


'''
[
app1,
app1,
app2,
app3
..
]
'''
def readData():
    app1 = App("1", "20210501", 1.0, 1.0, 1.0, 1.0, 1.0)
    result = [app1]
    return result


"""
"""
def handle(appList):
    result = appList
    return result


"""
app1:[startapp1,endapp1] 
==>
app1:[start,start+1,...start+n,end]
"""
def hanldeApp(appStart, appEnd):
    resultList = []

    startTime=appStart.time
    endTime=appEnd.time

    for i in endTime-startTime:
        name = appStart.name
        #[1.0,1.2,1.4,1.6,1.8,2.0]
        s1Array = calcS(appStart.s1, appEnd.s1)
        s3Array = calcS(appStart.s3, appEnd.s3)
        s2Array = calcS(appStart.s2, appEnd.s2)

    return resultList


def calcS(start, end):
    avg = (end-start)/5
    avg = avg + random()
    return [start,start + avg, start + 2*avg, start + 3*avg, start + 4*avg, end]


def random():
    return 0.01


"""
[app1,
app2,
app3]
"""
def writeData(appList):
    for app in appList:
        print '{},{},{},{},{},{},{}'.format(app.name, app.time, app.s1 ,app.s2 , app.s3 , app.s4 , app.s5)


def main():

    # 读出数据
    readList = readData()

    #补数处理
    writeList = handle(readList)


    # 写数据到文件
    writeData(writeList)



if __name__ == "__main__":

    main()