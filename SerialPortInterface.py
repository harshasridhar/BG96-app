import serial
class SerialPortInterface:


    def __init__(self, port='/dev/ttyUSB2', baudRate=115200):
        self.serialPort = serial.Serial(port, baudRate, timeout=1)

    def getResponseViaSerialPort(self):
        output=''
        a=" "
        while a!=b'':
            a=self.serialPort.readline()
            output+=a.decode('utf-8')
        return output

    def executeCommand(self,command='AT'):
        command += '\r\n'
        self.serialPort.write(command.encode())
        return str(self.getResponseViaSerialPort()).replace('\r\n','\n')

    def closePort(self):
        self.serialPort.close()

    def __del__(self):
        self.closePort()
