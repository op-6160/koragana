import func
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
import clipboard


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path('../others/koragana.ui')
form_class = uic.loadUiType(form)[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        self.pushButton_copy.clicked.connect(self.btnCopy)
        self.pushButton_trans.clicked.connect(self.btnTrans)
        self.pushButton_eraser.clicked.connect(self.btnErase)
        # 화면을 보여준다.
        self.show()

    def btnCopy(self):
        cout = self.textEdit_output.toPlainText()
        print(cout)
        clipboard.copy(cout)

    def btnErase(self):
        self.textEdit_input.setText("")

    def btnTrans(self):
        self.pushButton_trans.setEnabled(False)
        input_ = self.textEdit_input.toPlainText()
        translation = func.Translation(input_)
        output = translation.x
        self.textEdit_output.setText(output)
        self.pushButton_trans.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()