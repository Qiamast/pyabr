#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/manijamali2003/pyabr
#
#######################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from libabr import System, Files, Script, Control, Res, App

files = Files()
control = Control()
res = Res()

class MainApp (QMainWindow):

    def __init__(self,args):
        super(MainApp, self).__init__()

        self.calendar = QCalendarWidget()
        self.calendar.setStyleSheet('background: none;')

        self.Backend = args[0]
        self.Env = args[1]
        self.Widget = args[2]
        self.AppName = args[3]
        self.External = args[4]

        self.Widget.Resize(self,int(res.etc(self.AppName,"width")),int(res.etc(self.AppName,"height")))

        self.Widget.SetWindowTitle (res.get('@string/app_name'))
        self.Widget.SetWindowIcon (QIcon(res.get(res.etc(self.AppName,"logo"))))

        ## Data base ##
        sweek = files.readall("/proc/info/sweek")

        ## Calender widget ##

        self.calendar.setFont(self.Env.font())

        ## Start week ##
        if sweek=="Sat":
            self.calendar.setFirstDayOfWeek(Qt.Saturday)
        elif sweek=="Sun":
            self.calendar.setFirstDayOfWeek(Qt.Sunday)
        elif sweek=="Mon":
            self.calendar.setFirstDayOfWeek(Qt.Monday)
        elif sweek=="Tue":
            self.calendar.setFirstDayOfWeek(Qt.Tuesday)
        elif sweek=="Wed":
            self.calendar.setFirstDayOfWeek(Qt.Wednesday)
        elif sweek=="Thu":
            self.calendar.setFirstDayOfWeek(Qt.Thursday)
        elif sweek=="Fri":
            self.calendar.setFirstDayOfWeek(Qt.Friday)

        self.calendar.setGridVisible(True) # https://www.tutorialspoint.com/pyqt/pyqt_qcalender_widget.htm

        self.setCentralWidget(self.calendar)
