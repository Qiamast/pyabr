#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Telegram or Gap channel: @pyabr
#  Telegram or Gap group:   @pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

import sys, os
from libabr import Files, Colors, Control, Res
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

files = Files()
colors = Colors()
control = Control()
res = Res()

# input box #
class MainApp (QMainWindow):
    def __init__(self,ports):
        super(MainApp, self).__init__()

        self.Backend = ports[0]
        self.Env = ports[1]
        self.Widget = ports[2]
        self.Appname = ports[3]
        self.External = ports[4]

        self.setStyleSheet('background-color: white;')
        self.Widget.SetWindowIcon(QIcon(res.get('@icon/about')))
        ## Finds ##

        self.Widget.Resize(self,int(self.Env.width()/3),100)
        self.leInput = QLineEdit()
        self.leInput.resize(int(self.Env.width()/3),50)
        f = QFont()
        f.setPointSize(12)
        self.leInput.setFont(f)
        self.layout().addWidget(self.leInput)
        self.leInput.returnPressed.connect (self.inp)
        password_hint = control.read_record ('input.password_hint','/etc/configbox')
        if password_hint=='Yes':
            self.leInput.setEchoMode(QLineEdit.Password)

        if self.External[0]=='' or self.External[0]==None:
            self.Widget.SetWindowTitle (res.get('@string/title'))
        else:
            self.Widget.SetWindowTitle (self.External[0])

        self.btnCancel = QPushButton()
        self.btnCancel.setText(res.get('@string/cancel'))
        self.btnCancel.setGeometry(0,50,int(self.Env.width()/6),50)
        self.btnCancel.clicked.connect(self.Widget.Close)
        self.layout().addWidget(self.btnCancel)

        self.btnOK = QPushButton()
        self.btnOK.clicked.connect (self.inp)
        self.btnOK.setText(res.get('@string/ok'))
        self.btnOK.setGeometry(int(self.Env.width() / 6), 50, int(self.Env.width() / 6), 50)
        self.layout().addWidget(self.btnOK)

        self.Widget.DisableFloat()

    def inp(self):
        inputx = self.leInput.text()
        self.External[1](inputx)
        self.Widget.Close()