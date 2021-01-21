import serial

def initialise():
    global ser
    ser=serial.Serial('/dev/ttyUSB2',115200,timeout=1)
    

def write(command):
    global ser
    command+='\r\n'
    ser.write(command.encode())

def read():
    global ser
    output=''
    a=" "
    while a!=b'':
        a=ser.readline()
        print('a is',end='')
        print(a)
        output+=a.decode('utf-8')
    return output
write('AT+COPS?')
print(read())
global ser
ser.close()
'''
ser.write('AT\r\n'.encode())
a=" "
while a!=b'':
    a=ser.readline()
    print(a)

ser.write('AT+COPS?\r\n'.encode())
a=" "
while a!=b'':
    a=ser.readline()
    print(a)'''

