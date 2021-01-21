from flask import Flask,render_template,request
from SerialPortInterface import SerialPortInterface
from forms import MainForm
app=Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess1'
#serialPort=None
class Helper:

        def __init__(self):
            self.serialPort=None

        def initialiseSerialPort(self, port):
            print('Initialising...')    
            self.serialPort=SerialPortInterface(port)

        def disconnectFromSerialPort(self):
            print('Port Disconnected...')
            self.serialPort.closePort()

        def runCommandAndGetOutput(self, command):
            '''if self.serialPort is None:
                self.initialiseSerialPort()'''
            return self.serialPort.executeCommand(command)

helper=Helper()
executeCommand=False
textOutput=""
@app.route("/",methods=["GET"])
def mainPage():
    return render_template('index.html',title='My Page')

@app.route("/choice",methods=["GET","POST"])
def choice():
    global executeCommand
    global textOutput
    if request.method == "POST" and request.form.get('connection')=='disconnect':
        helper.disconnectFromSerialPort()
        executeCommand=False
        return render_template('index.html')
        print('Data is {} JS0N is {}'.format(request.form.get('choice'),request.json))
    form=MainForm()
    print('FOrm exec: {} output {}'.format(executeCommand,textOutput))
    if request.method=="POST" and executeCommand == True:
       command = form.command.raw_data[0]
       textOutput+="\n"+helper.runCommandAndGetOutput(command)
       form.outputText=textOutput
       form.isConnected=True
       form.command.raw_data[0]=""
    elif request.method == "POST":
        choice=form.choice.raw_data[0]
        print(choice)
        helper.initialiseSerialPort(choice)
        form.isConnected=True
        executeCommand=True
        textOutput="Connected to "+choice+"\n"
        textOutput+="AT\n"+helper.runCommandAndGetOutput('AT')
        form.outputText=textOutput
        form.command.data=""
    return render_template('choice.html',form=form)
if __name__ == '__main__':
    initialiseSerialPort()
    app.run()
