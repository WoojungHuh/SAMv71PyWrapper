#!/usr/bin/env python

import serial
import sys
import subprocess

ports = []
    #Generates list of available COM ports
s = subprocess.check_output(["python", "-m", "serial.tools.list_ports"])
output = s.decode("utf-8")
lines = output.split('\n')
for line in lines:
    print(line)
    ports.append(line)
    
    #Iterates and prints parameters of available ports
ser = serial.Serial()
for i in ports:
    ser.port = i
    print(ser)
