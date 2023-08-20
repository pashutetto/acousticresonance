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

import pyaudio
import wave

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("sinewave generator")
        self.generallayout = QVBoxLayout()
        centralwidget = QWidget(self)
        centralwidget.setLayout(self.generallayout)
        self.setCentralWidget(centralwidget)

        self.display1 = QLineEdit()
        self.display1.setFixedHeight(30)
        self.display1.setPlaceholderText("file name")
        self.generallayout.addWidget(self.display1)

        self.display2 = QLineEdit()
        self.display2.setFixedHeight(30)
        self.display2.setPlaceholderText("length")
        self.generallayout.addWidget(self.display2)

        self.button = QPushButton("record")
        self.generallayout.addWidget(self.button)
        self.button.clicked.connect(self.recordsound)

    def recordsound(self):
        chunk = 1024
        fs = 44100
        seconds = float(self.display2.text())
        filename = self.display1.text() + '.wav'
        p = pyaudio.PyAudio()

        stream = p.open(format = pyaudio.paInt16, 
                        channels = 1,
                        rate = fs,
                        frames_per_buffer=chunk,
                        input = True)

        frames = []

        for i in range(0, int(fs/chunk*seconds)):
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        self.label = QLabel("finish")
        self.generallayout.addWidget(self.label)

        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(fs)
        wf.writeframes(b''.join(frames))
        wf.close()

def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    main()

    