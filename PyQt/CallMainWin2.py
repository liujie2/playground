import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainForm2 import Ui_MainWindow
from ChildrenForm02 import Ui_Form

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # self.child = children() # 生成窗口实例self.child
        self.child = ChildrenForm()

        # 菜单点击事件，当单击关闭菜单时的连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)
        # 菜单点击事件，当单击打开菜单时的连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)
        # 单击actionTst, 子窗口就会显示在主窗口MainGridLayout中
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        # 添加子窗口
        self.MainGridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "~/", "All File(*.*);;Text File(*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())
