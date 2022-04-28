from PySide6.QtWidgets import *
from PySide6.QtGui import *
'''
Using PySide6
To make TextEditor GUI Program
Copyright HyeSu Kim
'''

# 닫기 버튼 클릭시 선택할 경우의수
class MainWindow(QMainWindow):
    def closeEvent(self,e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(win, None, "SAVE or NOT",
                                      QMessageBox.Save |
                                      QMessageBox.Discard |
                                      QMessageBox.Cancel
                                      )
#창 이름 설정
app = QApplication()
app.setApplicationName("Editor")
text = QPlainTextEdit()
#
win = MainWindow()
win.setCentralWidget(text)
# 메뉴 설정
menu = win.menuBar().addMenu("&File")
#
open_action = QAction("&Open")
#파일 열기
def open_file():
    path = QFileDialog.getOpenFileName(win, "Open File")[0]
    if path:
        text.setPlainText(open(path).read())
open_action.triggered.connect(open_file)
#단축키 설정
open_action.setShortcut(QKeySequence("Ctrl+O"))
#
menu.addAction(open_action)
#파일 경로 저장 후 일반 파일 저장 + 새롭게 저장 중 선택 가능
file_path = None
save_action = QAction("&Save")
def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path,"w") as f:
            f.write(text.toPlainText())
            #
            text.document().setModified(False)
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence("Ctrl+S"))
menu.addAction(save_action)
#
save_as_action = QAction("Save &As...")

def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(win,"Save AS")[0]
    if path:
        file_path = path
        save()
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)
# 파일 닫기
close = QAction("&Close")
close.triggered.connect(win.close)
menu.addAction(close)
win.show()
# 메모장 정보
help_menu = win.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)
#
def show_about_dialog():
    text = """<center>\
    <h1>Text Editor<h1>\
    </center>\
    <p>Version 1.2.3<br>\
    Copyright HS</p>"""
    QMessageBox.about(win,"About",text)
#
about_action.triggered.connect(show_about_dialog)
text.show()
app.exec()