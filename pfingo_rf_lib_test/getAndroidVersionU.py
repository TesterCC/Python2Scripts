#coding:utf-8


import os


def checkDeviceConnect():

    try:
        normal = 'device\n'
        result = os.popen("adb devices")

        deviceStatus = result.readlines()[1].split("\t")[1]

        if deviceStatus == normal:
            print "Device is Online"
            return True
        else:
            print "Device Connect Status is abnormal, please check it: ", deviceStatus
            return False

    except Exception, e:
        print "Device Connect Fail:", e
        return False


def getDeviceSerialNum():
    result = os.popen("adb devices")
    deviceSerialNum = result.readlines()[1].split("\t")[0]
    print deviceSerialNum
    return getDeviceSerialNum


def getDeviceBrand():
    #执行获取进程的命令
    result = os.popen("adb shell cat /system/build.prop | grep product.brand")
    #获取product.brand
    getvalue = result.readlines()[0].split("=")[1]
    print(getvalue)
    return getvalue


if __name__ == "__main__":
    checkDeviceConnect()
    getDeviceSerialNum()
    getDeviceBrand()

