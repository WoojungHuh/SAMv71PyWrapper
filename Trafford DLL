import serial
import subproc

activeport = input('Select COM port:')
ser = serial.Serial()
ser.baudrate = 38400
ser.port = activeport
ser.open()


ser.flushInput()
res = ser.read(2618).decode('utf-8')
print(res)

if ser.inWaiting() > 0:
    ser.flushInput()
ser.timeout = 1.

s = input('Enter command or press quit: ') + '\r'
while s != 'quit' + '\r': 
    b = bytearray()
    cm = s.encode('utf-8')
    ser.write(cm)
    cmd = ser.read(1054).decode('utf-8')
    print(cmd)
    s = input('Enter command or press quit: ') + '\r'

ser.close()

   
