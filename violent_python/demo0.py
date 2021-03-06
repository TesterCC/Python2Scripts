#!/usr/bin/env python
# coding:utf-8

# P6

port = 21
banner = "FreeFloat FTP Server"

print banner.upper()
print banner.lower()
print banner.replace('FreeFloat', 'Ability')
print banner.find('FTP')

print "[+] Checking for " + banner + "on port " + str(port)

# P8
portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(25)
print portList

portList.sort()
print portList
pos = portList.index(80)
print "[+] There are "+str(pos)+" ports to scan before 80."

portList.remove(443)
print portList
cnt = len(portList)
print "[+] Scanning "+str(cnt)+" Total Ports."

services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}
print services.keys()
print services.items()
print services.has_key('http')
print services['ftp']
print "[+] Found vulnerable with FTP on port "+str(services['ftp'])
