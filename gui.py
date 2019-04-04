import easygui as gui
import serial as ser
import sys
import os
if gui.ccbox("open serial","yes","no"):
    gui.msgbox("serial opened","attention","OK")
    baud=gui.choicebox("please set baudrate","baudrate",("115200","9600","4800"))
    ser.baudrate=baud
    ser.port='COM3'
    print(baud)
    
    
else: 
    gui.msgbox("exit","attention","OK")
    

print("done")

