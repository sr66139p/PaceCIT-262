#imports QT6 and necessary modules
from PyQt6 import QtCore, QtGui, QtWidgets
import random
import re
import sys

def read_rand_prompt():
    #read in a random prompt from the text file
    with open("prompts.txt", "r") as prompts_file:
        prompts = prompts_file.readlines()
        rand_i = random.randint(0, len(prompts)-1)
        return prompts[rand_i]

#takes the placeholders out of the prompts and returns them
def deconstruct_prompt(prompt):
    placeholders = re.findall('{(.*?)}', prompt)
    return placeholders  

#switches between the states of this finite state program
def b_clicked():
    global state
    # handler for button
    if state == 0: # state 0
        # run state0
        state_0()
        # change state
        state = 1
    else: # state 1
        state_1()
        # change state 
        state = 0
    
#switches to state 0
def state_0():
    global prompt, ph
    clear_inputs()
    # clear output label
    outputlabel.setText("")

    # display placeholders
    prompt = read_rand_prompt()
    ph = deconstruct_prompt(prompt)
    input1.setPlaceholderText(ph[0])
    input2.setPlaceholderText(ph[1])
    input3.setPlaceholderText(ph[2])
    
#clears the text boxes
def clear_inputs():
    input1.setPlaceholderText("")
    input2.setPlaceholderText("")
    input3.setPlaceholderText("")
    input1.setText("")
    input2.setText("")
    input3.setText("")

#switches to state 1
def state_1():
    global prompt
    # get text inputs
    t1 = input1.toPlainText()
    t2 = input2.toPlainText()
    t3 = input3.toPlainText()

    # replace placeholders in prompt with inputs
    prompt = re.sub('{(.*?)}', t1, prompt, count=1)
    prompt = re.sub('{(.*?)}', t2, prompt, count=1)
    prompt = re.sub('{(.*?)}', t3, prompt, count=1)
    
    outputlabel.setText(prompt)

    clear_inputs()

#starts on state 0
state = 0
prompt = ''
ph = []

#adds window properties
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.show()
MainWindow.setObjectName("MainWindow")
MainWindow.resize(640, 480)
MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)

centralwidget = QtWidgets.QWidget(parent=MainWindow)
centralwidget.setObjectName("centralwidget")

#declares the next button
nextbutton = QtWidgets.QPushButton(parent=centralwidget)
nextbutton.setGeometry(QtCore.QRect(220, 390, 201, 51))
font = QtGui.QFont()
font.setPointSize(16)
nextbutton.setFont(font)
nextbutton.setAutoDefault(False)
nextbutton.setDefault(False)
nextbutton.setFlat(False)
nextbutton.setObjectName("nextbutton")
nextbutton.clicked.connect(b_clicked)

#Declares the 3 input boxes
input1 = QtWidgets.QTextEdit(parent=centralwidget)
input1.setGeometry(QtCore.QRect(9, 310, 203, 61))
input1.setObjectName("input1")

input2 = QtWidgets.QTextEdit(parent=centralwidget)
input2.setGeometry(QtCore.QRect(220, 310, 204, 61))
input2.setObjectName("input2")

input3 = QtWidgets.QTextEdit(parent=centralwidget)
input3.setGeometry(QtCore.QRect(430, 310, 203, 61))
input3.setObjectName("input3")

#Adds a border for the sake of visibility
border = "QWidget {border: 1px solid white; }"
input1.setStyleSheet(border)
input2.setStyleSheet(border)
input3.setStyleSheet(border)

#Declares output label
outputlabel = QtWidgets.QLabel(parent=centralwidget)
outputlabel.setGeometry(QtCore.QRect(9, 30, 622, 241))
font = QtGui.QFont()
font.setPointSize(16)
outputlabel.setFont(font)
outputlabel.setFrameShape(QtWidgets.QFrame.Shape.Box)
outputlabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
outputlabel.setWordWrap(True)
outputlabel.setObjectName("outputlabel")

MainWindow.setCentralWidget(centralwidget)
menubar = QtWidgets.QMenuBar(parent=MainWindow)
menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
menubar.setObjectName("menubar")
MainWindow.setMenuBar(menubar)

actionQuit = QtGui.QAction(parent=MainWindow)
actionQuit.setObjectName("actionQuit")

QtCore.QMetaObject.connectSlotsByName(MainWindow)

_translate = QtCore.QCoreApplication.translate
MainWindow.setWindowTitle(_translate("MainWindow", "Wacky Words"))
nextbutton.setText(_translate("MainWindow", "Next"))
outputlabel.setText(_translate("MainWindow", "Welcome to Wacky Words!"))
actionQuit.setText(_translate("MainWindow", "Quit"))

MainWindow.setTabOrder(input3, input2)
MainWindow.setTabOrder(input2, input1)
MainWindow.setTabOrder(input1, nextbutton)
MainWindow.setTabOrder(nextbutton, input3)

sys.exit(app.exec())
