#!/usr/bin/env python

import sys
import subprocess
s = subprocess.check_output(["python", "-m", "serial.tools.list_ports"])
output = s.decode("utf-8")
lines = output.split('\n')
for line in lines:
    print(line)
