#!/usr/bin/env python
# coding:utf-8

# http://coding.imooc.com/lesson/53.html#mid=1713
# WINDOWS,need change elasped time to number in wps excel
# Calculate elapsed time

import csv
import os
import time
from datetime import datetime


# App Class
class App(object):

    def __init__(self):
        self.content = ""
        self.startTime = 0
        # self.package_name = 'com.globalroam.android.toku'
        # self.launch_activity = '.WelcomeActivity'

# cmp=com.globalroam.pfingo/.ui.WelcomeActivity
        self.package_name = 'com.globalroam.pfingo'
        self.launch_activity = '.ui.WelcomeActivity'


    # Launch App
    def LaunchApp(self):
        # cmd = 'adb shell am start -W -n com.globalroam.android.toku/.WelcomeActivity'
        cmd = 'adb shell am start -W -n ' + self.package_name + '/' + self.launch_activity
        self.content = os.popen(cmd)



    # Stop App
    def StopApp(self):
        # cmd = 'adb shell am force-stop com.globalroam.android.toku'
        cmd = 'adb shell am force-stop ' + self.package_name
        # cmd = 'adb shell input keyevent 3'
        os.popen(cmd)


# Controller Class
class Controller(object):


    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp", "elapsedtime")]
        self.filename = "AppLaunchTimeTestMethod2_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".csv"


    def TestProcess(self):

        self.getCalculateTime()   # include launch app and calculate elapsed time

        time.sleep(3)

        self.app.StopApp()

        time.sleep(2)



    def getCalculateTime(self):

        timebeforelaunch = datetime.now()
        self.app.LaunchApp()
        timeafterlaunch = datetime.now()

        timestamp = timeafterlaunch - timebeforelaunch
        elapsedtime = timestamp.microseconds    # Number of microseconds (>= 0 and less than 1 second).
        print elapsedtime
        return self.alldata.append((timestamp, elapsedtime))


    # run TestProcess many times
    def Run(self):
        while self.counter > 0:
            self.TestProcess()
            self.counter -= 1


    # store data
    def SaveDataToCSV(self):
        csvfile = file(self.filename, 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(5)
    controller.Run()
    controller.SaveDataToCSV()