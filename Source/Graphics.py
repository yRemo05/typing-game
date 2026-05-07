from PyQt5 import QtCore, QtGui, QtWidgets
from json import load

class GUI(QtWidgets.QMainWindow):
    def __init__(self,wordBuffer:int=5,minutes:int=1):

        
        self.WordsLabelText = "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;{0}\">{1}</span></p><p align=\"center\"><span style=\" font-size:22pt;\"><br/></span></p></body></html>"
        self.TimeLeftLabelText = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">TIME : {0}</span></p></body></html>"
        self.WPMLabelText = "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">WPM :{0}</span></p></body></html>"
        self.AccuracyLabelText = "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ACCURACY :{0}</span></p></body></html>"
        self.KeysHitLabelText = "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">KEYS HIT:{0}</span></p></body></html>"
        self.correctWLabelText = "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CORRECT WORDS :{0}</span></p></body></html>"
        self.validKeys = [QtCore.Qt.Key.Key_A,QtCore.Qt.Key.Key_B,QtCore.Qt.Key.Key_C,QtCore.Qt.Key.Key_D,QtCore.Qt.Key.Key_E,
             QtCore.Qt.Key.Key_F,QtCore.Qt.Key.Key_G,QtCore.Qt.Key.Key_H,QtCore.Qt.Key.Key_I,QtCore.Qt.Key.Key_J,
             QtCore.Qt.Key.Key_K,QtCore.Qt.Key.Key_L,QtCore.Qt.Key.Key_M,QtCore.Qt.Key.Key_N,QtCore.Qt.Key.Key_O,
             QtCore.Qt.Key.Key_P,QtCore.Qt.Key.Key_Q,QtCore.Qt.Key.Key_R,QtCore.Qt.Key.Key_S,QtCore.Qt.Key.Key_T,
             QtCore.Qt.Key.Key_U,QtCore.Qt.Key.Key_V,QtCore.Qt.Key.Key_W,QtCore.Qt.Key.Key_X,QtCore.Qt.Key.Key_Y,
             QtCore.Qt.Key.Key_Z]

        self.wordBuffer = wordBuffer
        self.time = minutes*60
        self.isTimerActive = False
        self.timer = None
        self.counters = [0,0,0] # 0 : Correct typed  1 : Mistyped  2 : Keys pressed
        self.currentRound = []


        file = open("Data\\words.json","r")
        self.wordsList = load(file)["Words"]
        file.close()
        self.currentRound = self.fetch_next_round()
        

        super().__init__()
        self.setWindowTitle("Typing Game")
        self.resize(1006, 697)
        self.setStyleSheet("background-color : rgb(80,80,80);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.WordsLabel1 = QtWidgets.QLabel(self.wordText(self.currentRound[0]),self.centralwidget)
        #self.WordsLabel.setGeometry(QtCore.QRect(20, 100, 961, 161))
        self.WordsLabel1.setGeometry(QtCore.QRect(5, 100, 961, 161))
        self.WordsLabel2 = QtWidgets.QLabel(self.wordText(self.currentRound[1]),self.centralwidget)
        self.WordsLabel2.setGeometry(QtCore.QRect(15, 100, 961, 161))
        self.WordsLabel3 = QtWidgets.QLabel(self.wordText(self.currentRound[2]),self.centralwidget)
        self.WordsLabel3.setGeometry(QtCore.QRect(25, 100, 961, 161))
        self.WordsLabel4 = QtWidgets.QLabel(self.wordText(self.currentRound[3]),self.centralwidget)
        self.WordsLabel4.setGeometry(QtCore.QRect(35, 100, 961, 161))
        self.WordsLabel5 = QtWidgets.QLabel(self.wordText(self.currentRound[4]),self.centralwidget)
        self.WordsLabel5.setGeometry(QtCore.QRect(45, 100, 961, 161))
        self.InputLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.InputLineEdit.installEventFilter(self)
        self.InputLineEdit.setGeometry(QtCore.QRect(20, 290, 961, 61))
        self.InputLineEdit.setStyleSheet("border : 5px solid rgba(0, 0, 0, 0);\n"
"border-radius:5px;\n"
"border-color:rgb(3, 148, 138);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"")
        self.ResetButton = QtWidgets.QPushButton("RESET",self.centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(690, 540, 270, 50))
        self.ResetButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(220, 220, 75, 255), stop:1 rgba(56, 202, 68, 255));\n"
"border : 2px solid rgb(0,0,0);\n"
"border-radius:10px;\n"
"border-color : rgb(150,150,150);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(56, 202, 68, 255), stop:1 rgba(220, 220, 75, 255));\n"
"}\n"
"")
        self.TimeLeftLabel = QtWidgets.QLabel(self.TimeLeftLabelText,self.centralwidget)
        self.TimeLeftLabel.setGeometry(QtCore.QRect(690, 470, 270, 51))
        self.WPMLabel = QtWidgets.QLabel(self.WPMLabelText,self.centralwidget)
        self.WPMLabel.setGeometry(QtCore.QRect(40, 400, 500, 50))
        self.WPMLabel.setStyleSheet("border : 5px solid rgba(0, 0, 0, 0);\n"
"border-radius:5px;\n"
"border-color:rgb(150,150,150);")
        self.AccuracyLabel = QtWidgets.QLabel(self.AccuracyLabelText,self.centralwidget)
        self.AccuracyLabel.setGeometry(QtCore.QRect(40, 520, 500, 50))
        self.AccuracyLabel.setStyleSheet("border : 5px solid rgba(0, 0, 0, 0);\n"
"border-radius:5px;\n"
"border-color:rgb(150,150,150);")
        self.KeysHitLabel = QtWidgets.QLabel(self.KeysHitLabelText,self.centralwidget)
        self.KeysHitLabel.setGeometry(QtCore.QRect(40, 460, 500, 50))
        self.KeysHitLabel.setStyleSheet("border : 5px solid rgba(0, 0, 0, 0);\n"
"border-radius:5px;\n"
"border-color:rgb(150,150,150);")
        self.correctWLabel = QtWidgets.QLabel(self.correctWLabelText.format(str(self.counters[0])),self.centralwidget)
        self.correctWLabel.setGeometry(QtCore.QRect(40, 580, 500, 50))
        self.correctWLabel.setStyleSheet("border : 5px solid rgba(0, 0, 0, 0);\n"
"border-radius:5px;\n"
"border-color:rgb(150,150,150);")
        self.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self)

    def fetch_next_round(self):
        words = []
        for index in range(self.wordBuffer):
                if self.wordsList:
                        words.append(self.wordsList.pop(0))
        return words

    def refreshWordLabels(self):
        labels = [self.WordsLabel1, self.WordsLabel2, self.WordsLabel3, self.WordsLabel4, self.WordsLabel5]
        for index, label in enumerate(labels):
                if index < len(self.currentRound):
                        label.setText(self.wordText(self.currentRound[index]))
                else:
                        label.clear()
    
    def wordText(self,text:str,status:bool=None):
        if status is None:
                return self.WordsLabelText.format("",text)
        if status == True:
                return self.WordsLabelText.format(" color:#159813;",text)
        if status == False:
                return self.WordsLabelText.format(" color:#982f31;",text)
          

    def eventFilter(self, obj, event):
        if obj is self.InputLineEdit and event.type() == QtCore.QEvent.Type.KeyPress:
                return self.returnEvent(event)

        return super().eventFilter(obj, event)

    def returnEvent(self,event):
        if not self.InputLineEdit.hasFocus():
                return False

        if self.timer is None or not self.timer.isActive():
                self.startTimer()

        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Space:
                # Enter or space submits the current word before the key is inserted.
                if self.InputLineEdit.text() == self.currentRound[0]:
                        self.correctWLabel.setText(self.correctWLabelText.format(str(self.counters[0] + 1)))
                        self.counters[0] += 1 # word was typed correctly.
                else:
                        self.counters[1] += 1 # word was not typed correctly.
                        #self.wordsList.append()

                self.InputLineEdit.clear() # Clear the input line and get it ready for the next word typing.
                self.currentRound.pop(0)
                if self.wordsList:
                        self.currentRound.append(self.wordsList.pop(0))
                self.refreshWordLabels()

                return True

        if event.key() in self.validKeys:
                self.counters[2] += 1
                self.KeysHitLabel.setText(self.KeysHitLabelText.format(str(self.counters[2])))

        return False

    def refreshPage(self,wordList:list):
        self.WordsLabelText.format("".join(word for word in wordList))
        self.WordsLabel.setText(self.WordsLabelText)

    def showTimeLeft(self):
        self.oMinutes -= 1
        if self.oMinutes != 0: 
                self.TimeLeftLabel.setText(self.TimeLeftLabelText.format(str(self.oMinutes)))
        else:
                self.TimeLeftLabel.setText(self.TimeLeftLabelText.format("-FINISH-"))
                self.WPMLabel.setText(self.WPMLabelText.format(str( (self.counters[0]+self.counters[1])*60/5*self.time)))
                self.AccuracyLabel.setText(self.AccuracyLabelText.format(str(self.counters[0]/(self.counters[0]+self.counters[1])*100)))
                self.timer.stop()
                self.tm = QtCore.QTimer(self)
                self.tm.timeout.connect(self._enableLineEdit)
                self.InputLineEdit.setEnabled(False)
                self.tm.start(300)


    def _enableLineEdit(self):
        self.InputLineEdit.setEnabled(True)
        self.tm.stop()

    def startTimer(self):
        self.timer = QtCore.QTimer(self)
        self.oMinutes = self.time
        self.TimeLeftLabel.setText(self.TimeLeftLabelText.format(str(self.time)))
        self.timer.timeout.connect(self.showTimeLeft)
        self.timer.start(100)


if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    ui = GUI()
    ui.show()
    app.exec()
