from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()
window.setWindowTitle('Языки программирования')
window.resize(400, 500)

button1 = QLabel('PHP')
button2 = QLabel('JavaScript')
button3 = QLabel('Python')
button4 = QLabel('Pascal')
button5 = QLabel('SQL')
button6 = QLabel('C++')

layout_main = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(button1, alignment = Qt.AlignCenter)
layoutH1.addWidget(button2, alignment = Qt.AlignCenter)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH2.addWidget(button4, alignment = Qt.AlignCenter)
layoutH3.addWidget(button5, alignment = Qt.AlignCenter)
layoutH3.addWidget(button6, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
window.setLayout(layout_main)
window.show()
app.exec_() 