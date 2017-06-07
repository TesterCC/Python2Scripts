#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/53.html#mid=1713

import csv
import os
import time


# App Class
class App(object):
    def __init__(self):
        self.content = ""
        self.startTime = 0

    # Launch App
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.globalroam.android.toku/.WelcomeActivity'
        self.content = os.popen(cmd)

    # Stop App
    def StopApp(self):
        cmd = 'adb shell am force-stop com.globalroam.android.toku'
        # cmd = 'adb shell input keyevent 3'
        os.popen(cmd)

    # Get Launch Time
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(': ')[1]   # add 1 space for windows excel calc
                elaspedtime = self.startTime.replace("\n", "")    # replace for adapt winodws excel
                break
        return elaspedtime


# Controller Class
class Controller(object):


    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp", "elapsedtime")]
        self.filename = "AppLaunchTimeTest_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".csv"

    # one time test process
    def TestProcess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elapsedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        time.sleep(2)
        currenttime = self.GetCurrentTime()
        self.alldata.append((currenttime, elapsedtime))



    # run TestProcess many times
    def Run(self):
        while self.counter > 0:
            self.TestProcess()
            self.counter -= 1


    # get current timestamp
    def GetCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    # def CollectAllData(self):

    # store data
    def SaveDataToCSV(self):
        csvfile = file(self.filename, 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(3)
    controller.Run()
    controller.SaveDataToCSV()