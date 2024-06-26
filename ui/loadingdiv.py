#!/usr/bin/python3
# -*- coding: utf-8 -*-

### BEGIN LICENSE

# Copyright (C) 2013 National University of Defense Technology(NUDT) & Kylin Ltd

# Author:
#     Shine Huang<shenghuang@ubuntukylin.com>
# Maintainer:
#     Shine Huang<shenghuang@ubuntukylin.com>

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 3, as published
# by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranties of
# MERCHANTABILITY, SATISFACTORY QUALITY, or FITNESS FOR A PARTICULAR
# PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models.enums import UBUNTUKYLIN_RES_PATH
from models.globals import Globals

import gettext
gettext.textdomain("ubuntu-kylin-software-center")
_ = gettext.gettext

class LoadingDiv(QWidget):

    ngif = []
    currentpage = 0

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # self.switchTimer = QTimer(self)
        # self.switchTimer.timeout.connect(self.slot_switch_animation_step)

        #self.setWindowTitle("银河麒麟软件商店")
        self.setWindowTitle(_("Galaxy kylin softare store"))

        # self.load_png()

        # launch loading
        if(parent == None):
            desktopw = QDesktopWidget()
            self.dwidth = desktopw.screenGeometry().width()
            self.dheight = desktopw.screenGeometry().height()
            self.px = self.dwidth / 2 - Globals.MAIN_WIDTH / 2
            self.py = self.dheight / 2 - Globals.MAIN_HEIGHT / 2
            self.setGeometry(int(self.px), int(self.py),int(Globals.MAIN_WIDTH), int(Globals.MAIN_HEIGHT))
        # normal loading
        else:
            self.setGeometry(0, 0, int(Globals.MAIN_WIDTH), int(Globals.MAIN_HEIGHT))


        self.gif = QMovie(UBUNTUKYLIN_RES_PATH + "loadgif.gif")
        self.loadinggif = QLabel(self)
        self.loadinggif.setGeometry(int(Globals.MAIN_WIDTH / 2 - 350 / 2),int(Globals.MAIN_HEIGHT / 2 - 350 / 2), 350, 350)
        self.loadinggif.setMovie(self.gif)


        # self.loadingtext = QLabel(self)
        # self.loadingtext.setGeometry()

        self.raise_()
        self.hide()

    # def load_png(self):
    #     for i in range(1, 18):
    #         img = QPixmap("res/loading/" + str(i) + ".png")
    #         self.ngif.append(img)
    #
    # def slot_switch_animation_step(self):
    #     if(self.currentpage == 17):
    #         self.currentpage = 1
    #
    #     self.loadinggif.setPixmap(self.ngif[self.currentpage])
    #
    #     self.currentpage = self.currentpage + 1

    # def start_loading(self):
    #     # self.loadingtext.setText(loadingText)
    #     self.currentpage = 0
    #     self.switchTimer.start(200)
    #     self.show()
    #
    # def stop_loading(self):
    #     self.switchTimer.stop()
    #     self.hide()
    def start_loading(self):
        self.gif.start()
        self.show()

    def stop_loading(self):
        self.gif.stop()
        self.hide()


class MiniLoadingDiv(QWidget):

    # parent of the request component
    parent_ = ''

    x_ = ''
    y_ = ''
    width_ = ''
    height_ = ''

    def __init__(self, onwhich, parent=None, offsetx=0, offsety=0):
        QWidget.__init__(self, parent)

        # self.parent_ = parent
        self.x_ = onwhich.x()
        self.y_ = onwhich.y()
        self.width_ = onwhich.width()
        self.height_ = onwhich.height()

        self.setGeometry(int(self.x_), int(self.y_), int(self.width_), int(self.height_))

        self.gif = QMovie(UBUNTUKYLIN_RES_PATH + "loading.gif")
        self.loadinggif = QLabel(self)
        self.loadinggif.setGeometry(int(self.width_ / 2 - 50) + int(offsetx), int(self.height_ / 2 - 25) + int(offsety), 50, 50)
        self.loadinggif.setMovie(self.gif)
        # self.loadingtext = QLabel(self)
        # self.loadingtext.setGeometry(self.loadinggif.x() + 25 - 150, self.loadinggif.y() + 55, 300, 20)
        # self.loadingtext.setAlignment(Qt.AlignCenter)
        self.raise_()
        self.hide()

    def start_loading(self):
        self.gif.start()
        self.show()

    def stop_loading(self):
        self.gif.stop()
        self.hide()
