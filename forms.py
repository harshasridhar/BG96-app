
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, TextField,HiddenField
import listSerialPorts as ls
class MainForm(FlaskForm):
        choicesDict=ls.getPorts()
        choices=[ (value['port'], key)for key,value in choicesDict.items()]
        choice=SelectField('Choice',choices=choices)
        submit=SubmitField('Connect to Serial Port')
        isConnecting=False
        isConnected=False
        outputText=""
        execute=SubmitField("Execute Command")
        command=TextField(render_kw={'placeholder':'enter command'})
        hidden=HiddenField()
        executeCommand=False
