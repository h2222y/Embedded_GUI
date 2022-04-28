from PySide6.QtWidgets import *
from PySide6.QtGui import *

# ----초기 리스트----
names = ['hyesu','donghun','hyunji','hwan'] #기존 친구 리스트
# ----함수----
def newName():
    global names
    if(line_name.text() not in names):
        bar.showMessage("환영합니다. 나의 인맥")
        names.append(line_name.text())
        print(names)
    else:
        bar.showMessage("이미 친구입니다.")
def delName():
    global names
    if(line_name.text() in names):
        bar.showMessage(line_name.text()+", 더 이상 내 친구가 아닙니다.")
        names.remove(line_name.text())
        print(names)
    else:
        bar.showMessage(line_name.text()+", 그는 내 친구가 아닙니다.")
def Exit():
    quit()

# 메인 윈도우 위젯 생성
app = QApplication()
win = QMainWindow()
# ----메뉴----
menu_bar = win.menuBar()
menu = menu_bar.addMenu("메뉴")

menuAdd = QAction("추가", win)
menuDel = QAction("제거", win)
menuClose = QAction("종료",win)
menu.addAction(menuAdd)
menu.addAction(menuDel)
menu_bar.addAction(menuClose)
# ----메인----
main = QWidget() # 메뉴와 겹치지 않도록 따로 생성
win.setCentralWidget(main)
form = QFormLayout() # form에 각각 구성요소 넣어주기
txt = QLabel("인맥을 관리합시다.")
form.addWidget(txt)
line_name = QLineEdit()
form.addRow("name", line_name)
addBtn = QPushButton("추가")
delBtn = QPushButton("제거")
lay = QHBoxLayout() #Button Layout
lay.addWidget(addBtn)
lay.addWidget(delBtn)
form.addRow(lay)
main.setLayout(form)

# ----상태바----
app.setApplicationName("My Friends")
win.resize(400,400)
bar = win.statusBar()
bar.showMessage("인맥을 관리합시다.")

# ----버튼 클릭----
addBtn.clicked.connect(newName)
delBtn.clicked.connect(delName)
menuAdd.triggered.connect(newName)
menuDel.triggered.connect(delName)
menuClose.triggered.connect(Exit)



win.show()
app.exec()
