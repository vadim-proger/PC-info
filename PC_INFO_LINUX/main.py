import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_Dialog

def get_info():
    info = ui.comboBox.currentText()
    
    if info == "Host_info":
        information = subprocess.getoutput("hostnamectl")
    elif info == "CPU":
        information = subprocess.getoutput("lscpu")
    elif info == "Memory":
        information = subprocess.getoutput("free -h")
    elif info == "Distribution":
        information = subprocess.getoutput("lsb_release -a")
    elif info == "Core":
        information = subprocess.getoutput("uname -a")
    elif info == "Architecture":
        information = subprocess.getoutput("arch")
    elif info == "Disk space":
        information = subprocess.getoutput("df -h")
    elif info == "USB":
        information = subprocess.getoutput("lsusb")
    elif info == "Network interfaces":
        information = subprocess.getoutput("ifconfig")
    elif info == "GPU":
        information = subprocess.getoutput("lspci | grep -i vga")
    elif info == "Audio":
        information = subprocess.getoutput("lspci | grep -i audio")

    ui.textBrowser.setText(information)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.pushButton.clicked.connect( get_info )
    sys.exit(app.exec_())
