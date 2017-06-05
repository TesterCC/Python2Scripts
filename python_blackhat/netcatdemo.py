#!/usr/bin/env python
# coding:utf-8

# blackhat P14

import sys
import socket
import getopt
import threading
import subprocess


# define some global variable
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


