#pip install PyQt6
#pip install pysinewave

from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit, 
    QPushButton,
    QVBoxLayout, 
    QMainWindow, 
    QWidget, 
    QLabel, 
    )
import sys

from pysinewave import SineWave
import time

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sinewave generator")
        self.generallayout = QVBoxLayout()
        centralwidget = QWidget(self)
        centralwidget.setLayout(self.generallayout)
        self.setCentralWidget(centralwidget)
        
        self.label = QLabel("freq = 440 * 2 ^ (pitch - 9)/12")
        self.generallayout.addWidget(self.label)
        
        self.display1 = QLineEdit()
        self.display1.setFixedHeight(30)
        self.display1.setPlaceholderText("initial pitch")
        self.generallayout.addWidget(self.display1)
    
        self.display2 = QLineEdit()
        self.display2.setFixedHeight(30)
        self.display2.setPlaceholderText("final pitch")
        self.generallayout.addWidget(self.display2)
    
        self.display3 = QLineEdit()
        self.display3.setFixedHeight(30)
        self.display3.setPlaceholderText("pitch per second")
        self.generallayout.addWidget(self.display3)
    
        self.display4 = QLineEdit()
        self.display4.setFixedHeight(30)
        self.display4.setPlaceholderText("time")
        self.generallayout.addWidget(self.display4)

        self.button = QPushButton("play")
        self.generallayout.addWidget(self.button)
        self.button.clicked.connect(self.playsound)
    
    
    def playsound(self):
        spitch = float(self.display1.text())
        fpitch = float(self.display2.text())
        pps= float(self.display3.text())
        lngth = float(self.display4.text())
        sinewave = SineWave(pitch = spitch, pitch_per_second = pps)
        sinewave.play()
        sinewave.set_pitch(fpitch)
        time.sleep(lngth)
        sinewave.stop()
    

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()


