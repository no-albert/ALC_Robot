import RPi.GPIO as gpio
# import time
from tkinter import *
from tkinter import ttk

# Main Window Setup
root = Tk()
root.title("ALC Interface")

# Global Variables
mode = "No Mode Selected"
select = "ALC is Stationary"

# Initiate gpio pins & ignore warnings
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

# Motor A initialize
# Enable pins
gpio.setup(2, gpio.OUT)
gpio.setup(3, gpio.OUT)
# in1 and in2
gpio.setup(27, gpio.OUT)
gpio.setup(22, gpio.OUT)

# Motor B initialize
# Enable pins
gpio.setup(4, gpio.OUT)
gpio.setup(17, gpio.OUT)
# in1 and in2
gpio.setup(10, gpio.OUT)
gpio.setup(9, gpio.OUT)

# Activate Motor A
gpio.output(2, True)
gpio.output(3, True)

# Activate Motor B
gpio.output(4, True)
gpio.output(17, True)

# Custom motor speeds using PWM values
p1 = gpio.PWM(2, 1000)
p2 = gpio.PWM(17, 1000)
p1.start(50)
p2.start(50)
temp1 = 1

# User Defined Functions
def userclick():
    global mode
    mode = "User Control Mode Activated"
    modelabel.config(text=mode)


def autoclick():
    global mode
    mode = "Autonomous Control Mode Activated"
    modelabel.config(text=mode)


def forward_key(event):
    global select
    select = "Forward ..."
    selectlabel.config(text=select)
    # Motor A
    gpio.output(27, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    # Motor B
    gpio.output(10, gpio.LOW)
    gpio.output(9, gpio.HIGH)
    temp1 = 0


def backward_key(event):
    global select
    select = "Backward ..."
    selectlabel.config(text=select)
    # Motor A
    gpio.output(27, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    # Motor B
    gpio.output(10, gpio.HIGH)
    gpio.output(9, gpio.LOW)
    temp1 = 1


def left_key(event):
    global select
    select = "Left ..."
    selectlabel.config(text=select)
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    # Motor A
    gpio.output(27, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    # Motor B
    gpio.output(10, gpio.HIGH)
    gpio.output(9, gpio.LOW)


def right_key(event):
    global select
    select = "Right ..."
    selectlabel.config(text=select)
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    # Motor A
    gpio.output(27, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    # Motor B
    gpio.output(10, gpio.LOW)
    gpio.output(9, gpio.HIGH)


def stop_key(event):
    global select
    select = "Stop ..."
    selectlabel.config(text=select)
    # Motor A
    gpio.output(27, gpio.LOW)
    gpio.output(22, gpio.LOW)
    # Motor B
    gpio.output(10, gpio.LOW)
    gpio.output(9, gpio.LOW)


def forward():
    global select
    select = "Forward ..."
    selectlabel.config(text=select)
    # Motor A
    gpio.output(27, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    # Motor B
    gpio.output(10, gpio.LOW)
    gpio.output(9, gpio.HIGH)
    temp1 = 0


def backward():
    global select
    select = "Backward ..."
    selectlabel.config(text=select)
    # Motor A
    gpio.output(27, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    # Motor B
    gpio.output(10, gpio.HIGH)
    gpio.output(9, gpio.LOW)
    temp1 = 1


def left():
    global select
    select = "Left ..."
    selectlabel.config(text=select)
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    # Motor A
    gpio.output(27, gpio.LOW)
    gpio.output(22, gpio.HIGH)
    # Motor B
    gpio.output(10, gpio.HIGH)
    gpio.output(9, gpio.LOW)


def right():
    global select
    select = "Right ..."
    selectlabel.config(text=select)
    p1.ChangeDutyCycle(100)
    p2.ChangeDutyCycle(100)
    # Motor A
    gpio.output(27, gpio.HIGH)
    gpio.output(22, gpio.LOW)
    # Motor B
    gpio.output(10, gpio.LOW)
    gpio.output(9, gpio.HIGH)


def stop():
    global select
    select = "Stop ..."
    selectlabel.config(text=select)
    # Motor A
    gpio.output(27, gpio.LOW)
    gpio.output(22, gpio.LOW)
    # Motor B
    gpio.output(10, gpio.LOW)
    gpio.output(9, gpio.LOW)

# Widget Creations
modelabel = ttk.Label(root, text=mode)
selectlabel = ttk.Label(root, text=select)
autoButton = ttk.Button(root, text="Autonomous Mode", command=autoclick, width=50)
userButton = ttk.Button(root, text="User Mode", command=userclick, width=50)
modelabel.grid(row=4, column=1)
selectlabel.grid(row=5, column=1)
autoButton.grid(row=0, columnspan=3)
userButton.grid(row=1, columnspan=3)

# create buttons with arrows to control robot with mouse
leftButton = ttk.Button(root, text="\u2190", width=15, command=left)
rightButton = ttk.Button(root, text="\u2192", width=15, command=right)
upButton = ttk.Button(root, text="\u2191", width=15, command=forward)
downButton = ttk.Button(root, text="\u2193", width=15, command=backward)
stopButton = ttk.Button(root, text="STOP", width=15, command=stop)

# create binds for method function calls to control robot with WASD-keys
selectlabel.bind("<w>", forward_key)
selectlabel.bind("<a>", left_key)
selectlabel.bind("<s>", backward_key)
selectlabel.bind("<d>", right_key)
selectlabel.bind("<e>", stop_key)

# focus on gui window for key presses
selectlabel.focus_set()
selectlabel.bind("<1>", lambda event: selectlabel.focus_set())

# position the arrow buttons
leftButton.grid(row=3, column=0)
rightButton.grid(row=3, column=2)
upButton.grid(row=2, column=1)
downButton.grid(row=3, column=1)
stopButton.grid(row=2, column=2)

root.mainloop()
