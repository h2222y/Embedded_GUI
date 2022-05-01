"""
Using PySide6
Make Couple Predict Program
Make UI by using Qt Designer
Copyright HyeSu Kim
"""

from PySide6.QtWidgets import *
from predict_ui import Ui_MyWindow
import hashlib

class MyApp(QMainWindow,Ui_MyWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()
    def main(self):
        pass
    # ----UI 창 clear 함수 구현----
    def clear(self):
        self.textBox1.clear()
        self.textBox2.clear()
        self.spinBox.clear()
    # ----나의 이름과 상대방의 이름을 hashlib를 이용하여 숫자로 변환하고, 확률을 구해 커플이 될 확률을 구해보자----
    def check(self):
        str1= self.textBox1.text()
        str2=self.textBox2.text()
        hashCode1 = hashlib.sha256(str1.encode()).hexdigest()
        hashCode2 = hashlib.sha256(str2.encode()).hexdigest()

        sum1 = int(hashCode1, 16) + int(hashCode2, 16)
        sum2 = self.spinBox.value() * 777
        result = (sum1 + sum2) % 101

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Warning Warning!!")
        msg.setText("NASA 공식에 의해, " + str(result) + \
                    "% 확률로 커플이 됩니다.")
        msg.exec()
    # ----창 닫기 함수----
    def bye(self):
        self.close()

app =QApplication()
win = MyApp()
win.show()
app.exec()