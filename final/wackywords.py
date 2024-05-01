import sys
from PyQt6 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("main.ui")
window.show()
app.exec()

word1 = 'Word 1'
word2 = 'Word 2'
word3 = 'Word 3'
