import serial.tools.list_ports
def getPorts():
    ports = serial.tools.list_ports.comports()
    portinfo={}
    for port, desc, hwid in sorted(ports):
	#print("{}: {} [{}]".format(port, desc, hwid))
        portinfo[desc+" ["+port+"]"]={'port':port,'hwid':hwid}
    return portinfo
