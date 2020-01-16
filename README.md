# SAMv71PyWrapper

Scope: Simple Python script for SAMv71 CLI via COM PORT interface with DLL for automated read/write capability.

Usage Guide (Terminal.py) NOT NECESSARY, PERIPHERAL TESTING SCRIPT
  -Download and Install com0com for Windows users
  -Confirm COM devices 3-6 are working properly "Device Manager/Ports (COM and LPT)" (If not, Update driver)
  -Open 2 separate instances of terminal.py in python console/command line
  -Name COM ports COM3, COM4, Open ports
  
 Main:
  -run Python subproc.py to verify COM port connections and parameters are correct
  -run Trafford.DLL as py file, (not finished yet)select function from printed library
  -If error returns "COM port access denied", verify Device is enabled in Device Manager. If enabled, and error persists, disable device and reenable. System will require restart. 
  - When run via PC Command line, press hard reset on SAMV71 board. 

Com0Com Download for Windows:
https://sourceforge.net/projects/com0com/

The Null-modem emulator (com0com) is a kernel-mode virtual serial port driver for Windows. You can create an unlimited number of virtual COM port pairs and use any pair to connect one COM port based application to another. The HUB for communications (hub4com) allows to receive data and signals from one COM or TCP port, modify and send it to a number of other COM or TCP ports and vice versa.

Pyserial download:
https://pypi.org/project/pyserial/

  pip install pyserial 
