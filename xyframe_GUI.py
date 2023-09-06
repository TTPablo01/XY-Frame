#########################################################################################
#
# Program  : xyframe_GUI.py
# Version  : 0.0.0.20
#
# Author   : Pablo Cordoba 
# Updated  : 06/09/2023 at 16:30
# Function : GUI for the XY Frame 
#
# Copyright: IGS / Tubetech Industrial Ltd. 2023.
#
# Dependencies (Python files):
#            xyframe_mc5005.py
#            xyframe_motors.py
#
#########################################################################################

#import xyframe_motors as m ### dependicies
#import xyframe_mc5005 as mc


import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image 
import time




###### MAIN SCREEN ######
class MainWindow:
    def __init__(self,master):

        s = ttk.Style()
        s.theme_use("default")
        s.configure("TProgressbar", thickness=50)

        self.master = master
        self.controls = None
        self.ControlsValue = None
 
        self.frame = tk.Frame(self.master, width=1500, height=1000)
        self.frame.pack()

        """
        self.ImageFrame = tk.Frame(self.frame, width=400, height=150, bg='black')
        self.ImageFrame.place(anchor='sw', x=100, y=1000)

        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("logo.png"))

        # Create a Label Widget to display the Image
        self.label = tk.Label(self.ImageFrame, image = img)
        self.label.pack()

        """


    def PowerOn(self):
        PowerOnFrame = tk.Frame(self.frame, height=1000, width=1500)
        PowerOnFrame.pack()
        PowerOnMessage = tk.Label(PowerOnFrame, text="POWERING ON...")
        PowerOnMessage.config(font=('Arial',40, 'bold'))
        PowerOnMessage.place(x = 540 , y = 300)
        
        ProgressBar = ttk.Progressbar(PowerOnFrame, orient='horizontal', mode='indeterminate', length=500)
        ProgressBar.place(x = 500 , y = 450)
        ProgressBar.start()

        self.buttonControls = tk.Button(self.frame, text="Controls",height= 1, width=7, font=('Arial',20, 'bold'), command=self.OpenControls)
        self.buttonControls.place(x=1300, y=900)

        PowerOnFrame.after(3000, PowerOnFrame.destroy)

        
         

    def EstablishConnection(self):
        EstablishConnectionFrame = tk.Frame(self.frame, height=1000, width=1500)
        EstablishConnectionFrame.pack()
        
        message = tk.Label(EstablishConnectionFrame, text="XY FRAME NOT DETECTED")
        message.config(font=('Arial',40, 'bold'))
        message.place(x = 435 , y = 200)

        message2 = tk.Label(EstablishConnectionFrame, text=" Press the ESTABLISH CONNECTION button once the machine has been \nplugged or POWER OFF the device.")
        message2.config(font=('Arial',25, 'bold'))
        message2.place(x = 165 , y = 350)

        buttonEstablish = tk.Button(EstablishConnectionFrame, text="ESTABLISH \n CONNECTION",height= 2, width=12, font=('Arial',20, 'bold'),bg = "white", fg = "black" )
        buttonEstablish.place(x=500, y=500)

        buttonPowerOff = tk.Button(EstablishConnectionFrame, text="POWER \n OFF",height= 2, width=12, font=('Arial',20, 'bold'),bg = "white", fg = "black", command = root.destroy)
        buttonPowerOff.place(x=800, y=500)

        self.buttonControls = tk.Button(self.frame, text="Controls",height= 1, width=7, font=('Arial',20, 'bold'), command=self.OpenControls)
        self.buttonControls.place(x=1300, y=900)

        #EstablishConnectionFrame.after(5000, EstablishConnectionFrame.destroy)

        





        """
        top = tk.Toplevel(self.master)
        top.geometry("750x250")
        tk.Label(tk.CENTER, text= "Establishing connection with frame...", font=('Arial 18 bold')).place(x=150,y=80)
        """

   

    def ButtonSelection(self,ButtonPressed):

        if ButtonPressed == 'UP':


        elif ButtonPressed == 'DOWN':
            

        elif ButtonPressed == 'LEFT':


        elif ButtonPressed == 'RIGHT':


        elif ButtonPressed == 'ENTER':


        
        

    def update(self, n):
        self.ControlsValue = n
        
    
    def OpenControls(self):
        self.controls = ControlsWindow(self.update)

   

    
root = tk.Tk()
root.geometry("1500x1000") # Set window size
root.title("XY Frame GUI")
window = MainWindow(root)


window.PowerOn()
window.EstablishConnection()





try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)

finally:
    # Keep windows visible 
    root.mainloop()


"""
 
main = tk.Tk() # Main window creation

main.geometry("1500x1000") # Set window size

# Set window title
main.title("XY Frame GUI")

frame = tk.Frame(main, width=400, height=150)
frame.pack()
frame.place(anchor='sw', x=100, y=1000)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("logo.png"))

# Create a Label Widget to display the text or Image
label = tk.Label(frame, image = img)
label.pack()

message = tk.Label(main, text="XY FRAME NOT DETECTED")
message.config(font=('Arial',40, 'bold'))
message.place(x = 435 , y = 200)

message2 = tk.Label(main, text=" Press the ESTABLISH CONNECTION button once the machine has been \nplugged or POWER OFF the device.")
message2.config(font=('Arial',25, 'bold'))
message2.place(x = 165 , y = 350)

def establishConnection():

    top = tk.Toplevel(main)
    top.geometry("750x250")
    tk.Label(centre, text= "Establishing", font=('Arial 18 bold')).place(x=150,y=80)

def on_right(e):
    global buttonPowerOff
    buttonPowerOff.focus_set()
    

def on_left(e):
    global buttonEstablish
    buttonEstablish.focus_set()


buttonEstablish = tk.Button(main, text="ESTABLISH \n CONNECTION",height= 2, width=12, font=('Arial',20, 'bold'),bg = "white", fg = "black" )
buttonEstablish.place(x=500, y=500)
buttonEstablish.bind("<Right>", on_right)
buttonEstablish.bind("<FocusIn>", lambda e: buttonEstablish.configure(bg = "black", fg = "white"))
buttonEstablish.bind("<FocusOut>", lambda e: buttonEstablish.configure(bg = "white", fg = "black"))
buttonEstablish.focus_set() #Setting default focus to button1

buttonPowerOff = tk.Button(main, text="POWER \n OFF",height= 2, width=12, font=('Arial',20, 'bold'),bg = "white", fg = "black" )
buttonPowerOff.place(x=800, y=500)
buttonPowerOff.bind("<FocusIn>", lambda e: buttonPowerOff.configure(bg = "black", fg = "white"))
buttonPowerOff.bind("<FocusOut>", lambda e: buttonPowerOff.configure(bg = "white", fg = "black"))
buttonPowerOff.bind("<Left>", on_left)



###### CONTROLS SCREEN ######

controls = tk.Toplevel() # Control window creation

controls.geometry("1700x1000") # Set window size

# Set window title
title = tk.Label(controls, text="XY Frame Controls")
title.config(font=('Arial',40))
title.pack()

# Buttons 
buttonCLose = tk.Button(controls, text="Close",height= 1, width=5, font=('Arial',20), command= controls.destroy)
buttonCLose.place(x=1570, y=900)

buttonEnter = tk.Button(controls, text="ENTER",height= 1, width=7, font=('Arial',20 , 'bold'), bg='green')
buttonEnter.place(x=1300, y=400)

buttonUp = tk.Button(controls, text="↑",height= 1, width=7, font=('Arial',20 , 'bold'),bg = "white", fg = "black")
buttonUp.place(x=1300, y=300)

buttonDown = tk.Button(controls, text="↓",height= 1, width=7, font=('Arial',20 , 'bold'), bg = "white", fg = "black")
buttonDown.place(x=1300, y=500)

ButtonLeft = tk.Button(controls, text="←",height= 1, width=7, font=('Arial',20 , 'bold'), bg = "white", fg = "black")
ButtonLeft.place(x=1150, y=400)

buttonRight = tk.Button(controls, text="→",height= 1, width=7, font=('Arial',20 , 'bold'), bg = "white", fg = "black")
buttonRight.place(x=1450, y=400)


buttonStop = tk.Button(controls, text="STOP",height= 1, width=7, font=('Arial',20 , 'bold'), bg = "white", fg = "black")
buttonStop.place(x=200, y=700)

buttonPause = tk.Button(controls, text="PAUSE",height= 1, width=7, font=('Arial',20 , 'bold'), bg = "white", fg = "black")
buttonPause.place(x=400, y=700)

ButtonReset = tk.Button(controls, text="RESET",height= 1, width=7, font=('Arial',20 , 'bold'), bg = "white", fg = "black")
ButtonReset.place(x=600, y=700)

buttonES = tk.Button(controls, text="EMERGENCY\n STOP",height= 2, width=10, font=('Arial',20 , 'bold'), bg='red')
buttonES.place(x=800, y=700)

# Code needed to avoid blurry text on different OS
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)

finally:
    # Keep windows visible 
    main.mainloop()
    controls.mainloop()
 
 """       














