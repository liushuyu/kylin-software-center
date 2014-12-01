#!/usr/bin/python
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


import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.uktliw import Ui_TaskLIWidget
from models.enums import Signals,AptActionMsg,PkgStates
from models.enums import UBUNTUKYLIN_RES_ICON_PATH
from utils import commontools
from utils.debfile import DebFile


class TaskListItemWidget(QWidget):
    app = ''
    finish = False

    def __init__(self, app, parent=None, isdeb=False):
        QWidget.__init__(self,parent)
        self.ui_init()
        self.app = app
        self.parent = parent

        self.ui.size.setAlignment(Qt.AlignCenter)
        self.ui.btnCancel.setFocusPolicy(Qt.NoFocus)
        self.ui.status.setAlignment(Qt.AlignTop)
        self.ui.status.setWordWrap(True)
        self.ui.progressBar.lower()

        self.ui.progresslabel.setFocusPolicy(Qt.NoFocus)
        self.ui.progresslabel.setStyleSheet("QLabel{font-size:13px;color:#888888;}")
        self.ui.progresslabel.setText("")

        self.ui.name.setStyleSheet("QLabel{font-size:14px;font-weight:bold;}")
        self.ui.btnCancel.setStyleSheet("QPushButton{background-image:url('res/delete-normal.png');border:0px;}QPushButton:hover{background:url('res/delete-hover.png');}QPushButton:pressed{background:url('res/delete-pressed.png');}")
        self.ui.progressBar.setStyleSheet("QProgressBar{background-color:#F4F8FB;border:0px;border-radius:0px;color:#1E66A4;}"
                                          "QProgressBar:chunk{background-color:#5DC4FE;}")#text-align:right;

        self.ui.btnCancel.clicked.connect(self.slot_click_cancel)
        self.connect(self.parent,Signals.apt_process_finish,self.slot_work_finished)

        # this is deb file task
        if(isdeb == True or isinstance(app,DebFile)):
            if app.status == PkgStates.INSTALLING:#"installing":
                self.ui.name.setText("安装 "+app.name)
            if app.status == PkgStates.REMOVING:#"uninstalling":
                self.ui.name.setText("卸载 "+app.name)
            if app.status == PkgStates.UPGRADING:#"upgrading":
                self.ui.name.setText("升级 "+app.name)

            sizek = app.installedsize
            if(sizek <= 1024):
                self.ui.size.setText(str(sizek) + " KB")
            else:
                self.ui.size.setText(str('%.2f'%(sizek/1024.0)) + " MB")
            img = QPixmap(UBUNTUKYLIN_RES_ICON_PATH + "default.png")
            # img = img.scaled(32, 32)
            self.ui.icon.setPixmap(img)
        else:
            iconpath = commontools.get_icon_path(app.name)
            img = QPixmap(iconpath)
            # img = img.scaled(32, 32)
            self.ui.icon.setPixmap(img)
            if app.status == PkgStates.INSTALLING:#"installing":
                self.ui.name.setText("安装 "+app.name)
            if app.status == PkgStates.REMOVING:#"uninstalling":
                self.ui.name.setText("卸载 "+app.name)
            if app.status == PkgStates.UPGRADING:#"upgrading":
                self.ui.name.setText("升级 "+app.name)

            size = app.packageSize
            sizek = size / 1024
            if(sizek < 1024):
                self.ui.size.setText(str(sizek) + " KB")
            else:
                self.ui.size.setText(str('%.2f'%(sizek/1024.0)) + " MB")

        self.ui.progressBar.setRange(0,100)
        self.ui.progressBar.reset()
        self.ui.progresslabel.setText("")
        self.ui.status.setText("等待中......")

    def ui_init(self):
        self.ui = Ui_TaskLIWidget()
        self.ui.setupUi(self)
        self.show()

    def status_change(self, processtype, percent, msg):
        if(self.finish == False):
            text = ''
            if(processtype == 'fetch'):
                text = "正在下载: "
                if percent >= 100:
                    #text = "下载完成，开始安装..."
                    self.ui.progressBar.reset()
                    self.ui.progresslabel.setText("")
                    self.ui.status.setText("下载完成，开始安装...")
                    return
                else:
                    self.ui.progressBar.setValue(percent)
                    # self.ui.progresslabel.setText(self.ui.progressBar.value())
                    self.ui.progresslabel.setText(str('%.0f' % percent) + '%')
            elif(processtype == 'apt'):
                text = "正在执行: "
                if percent >= 100:
                    text = "安装完成"
                    self.ui.progressBar.setValue(percent)
                    # self.ui.progresslabel.setText(self.ui.progressBar.value())
                    self.ui.progresslabel.setText(str('%.0f' % percent) + '%')
                else:
                    self.ui.progressBar.setValue(percent)
                    # self.ui.progresslabel.setText(self.ui.progressBar.value())
                    self.ui.progresslabel.setText(str('%.0f' % percent) + '%')

            self.ui.status.setText(msg)

    def slot_work_finished(self, pkgname, action):
        if self.app.name == pkgname and self.finish == False:
            self.ui.progressBar.setValue(100)
            self.ui.progresslabel.setText("")
            self.ui.status.setText(AptActionMsg[action]+"已经完成")
            self.finish = True

    def slot_click_cancel(self):
        if(self.finish == True):
            self.emit(Signals.task_remove, self.app)
        else:
            self.emit(Signals.task_cancel, self.app.name)