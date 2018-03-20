#!/usr/bin/env python
# coding:utf-8

# blackhat P14-P21

import os
import sys
import socket
import getopt
import threading
import subprocess

# print(os.path.basename(__file__))   # get current filename
# print(os.path.basename(sys.argv[0]))
script_name = os.path.basename(__file__)


# define some global variable
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


def useage():
    print(">>>>>>>MFC Pentest Net Tool<<<<<<<")
    print("")
    print("Usage: {0} -t target_host -p port".format(script_name))
    print("")
    print("-l --listen                 - listen on [host]:[port] for incomming connections")
    print("-e --execute=file_to_run    - execute the given file upon receiving a connection")
    print("-c --command                - initialize a command shell")
    print("-u --upload=destination     - upon receiving connection upload a file and write to [destination]")
    print("")
    print("Examples: ")
    print("{0} -t 192.168.0.1 -p 5555 -l -c".format(script_name))
    print("{0} -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe".format(script_name))
    print("{0} -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\"".format(script_name))
    print("echo 'ABCDEFGHI' | ./{0} -t 192.168.11.12 -p 135".format(script_name))
    sys.exit(0)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        useage()

    # get command -var
    # try:
        # opts, args = getopt.getopt(sys.argv[1:], "hel:t:p:cu:", [])
    pass    #P15


if __name__ == '__main__':
    useage()




