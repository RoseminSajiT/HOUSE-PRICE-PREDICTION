import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'House predictor'
        self.left =110
        self.top = 110
        self.width = 1200
        self.height = 720
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox

        self.house = QLabel(self)
        self.house.move(150, 70)
        self.house.resize(900, 40)
        self.house.setFont(QFont('Arial', 20))
        self.house.setText("HOUSE PRICE PREDICTION USING MACHINE LEARNING")

        self.bed = QLabel(self)
        self.bed.move(250, 200)
        self.bed.resize(750, 40)
        self.bed.setFont(QFont('Arial', 15))
        self.bed.setText("Enter the number of bedrooms :")
        self.textbox = QLineEdit(self)
        self.textbox.move(700, 200)
        self.textbox.resize(180, 40)

        self.bath = QLabel(self)
        self.bath.move(250,300)
        self.bath.resize(750, 40)
        self.bath.setFont(QFont('Arial', 15))
        self.bath.setText("Enter the number of bathrooms :")
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(700, 300)
        self.textbox1.resize(180, 40)

        self.bed = QLabel(self)
        self.bed.move(250,400)
        self.bed.resize(750, 40)
        self.bed.setFont(QFont('Arial', 15))
        self.bed.setText("Enter the sqft in areas :")
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(700, 400)
        self.textbox2.resize(180, 40)

        self.bed = QLabel(self)
        self.bed.move(120, 580)
        self.bed.resize(750, 40)
        self.bed.setFont(QFont('Arial', 15))
        self.bed.setText("PREDICTED PRICE OF YOUR DREAM HOUSE IS")
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(750, 580)
        self.textbox3.resize(180, 40)

        # Create a button in the window
        self.button = QPushButton('PREDICT', self)
        self.button.move(500, 500)
        self.button.resize(180, 40)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()


    def on_click(self):
        a = []
        model = joblib.load('House.joblib')
        bedroom = self.textbox.text()
        a.append(bedroom)
        bathroom = self.textbox1.text()
        a.append(bathroom)
        total = self.textbox2.text()
        a.append(total)
        b = np.array(a, dtype=float)
        c = model.predict([b])
        c = str(c)
        print(c)
        self.textbox.setText("")
        self.textbox1.setText("")
        self.textbox2.setText("")
        self.textbox3.setText(c)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())