import time
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import serial

root=Tk()
root.title("ESP Autostart Changer")
err=""
comliste=("COM2:","COM3:","COM4:","COM5:","COM6:")

def serialOn():
    global ser

    for comport in comliste:
        try:
            ser = serial.Serial(port=comport,baudrate=115200)
            serialopen=True
        except Exception as e:
            #print ("error open serial port: " + str(e))
            serialopen=False            
        if serialopen == True:
            time.sleep(2)
            ESPsend(chr(3))
            return (comport)
    return ("Error")
    
def ESPsend(out):
    out+="\r\n"
    out=out.encode("utf-8")
    ser.write(out)
    time.sleep(0.1)
    
def autooff():
    if ser.isOpen() == False:start()
    ESPsend("import os")
    ESPsend("os.rename('main.py','mainxxx.py')")
    hinweistxt="Autostart off"
    hinweis.config(text=hinweistxt)
    stop()
    
def autoon():
    if ser.isOpen() == False:start()
    ESPsend("import os")
    ESPsend("os.rename('mainxxx.py','main.py')")
    hinweistxt="Autostart on"
    hinweis.config(text=hinweistxt)
    stop()
    
def stop():
    ser.close()
    
def start():
    while True:
        err=serialOn()
        if err!="Error":
            statustxt="ESP connectet on: "+err
            status.config(text=statustxt)
            break
        else:
            if askyesno("No ESP found!!! Try again?"):
                pass
            else:
                exit()


#----------------------------------------------------------------------------------   
#----------  Witgets laden


   
frameButton = Frame(root)
frameButton.pack(fill='both')
button2=Button(frameButton, text="Autostart ON              ", command=autoon)
button2.pack(side="right",padx="5",pady="2")

button1=Button(frameButton, text="Autostart OFF             ", command=autooff)
button1.pack(side="right",padx="5")

hinweis = Label(root, fg = "lightgreen",bg = "gray", font = "Verdana 10 bold" )
hinweis.pack(fill='both',padx="5",pady="2")
hinweistxt="Change Autostart "
hinweis.config(text=hinweistxt)

status = Label(root)
status.pack(fill='both',padx="5",pady="2")
statustxt="                               "
status.config(text=statustxt)
#------------------------------------------------------------------------------------

start()
root.mainloop() 
