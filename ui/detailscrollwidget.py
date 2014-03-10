#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Shine Huang'

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui.detailw import Ui_DetailWidget
from ui.starwidget import StarWidget
from ui.reviewwidget import ReviewWidget
from ui.listitemwidget import ListItemWidget
from models.enums import (UBUNTUKYLIN_LABEL_STYLE_PATH,
                          UBUNTUKYLIN_RES_TMPICON_PATH,
                          RECOMMEND_BUTTON_PATH,
                          UBUNTUKYLIN_RES_PATH,
                          RECOMMEND_QPUSH_BUTTON_PATH)

class DetailScrollWidget(QScrollArea):
    app = ''

    def __init__(self, parent=None):
        QScrollArea.__init__(self,parent)
        self.detailWidget = QWidget()
        self.ui_init()

        self.setGeometry(QRect(40, 107, 815, 479))
        self.setWidget(self.detailWidget)

        self.ui.detailHeader.setAlignment(Qt.AlignCenter)
        self.ui.detailHeader.setText("详细信息")
        self.ui.detailHeader.lower()
        self.ui.btnCloseDetail.setText("返回")

        self.ui.btnCloseDetail.setFocusPolicy(Qt.NoFocus)
        self.ui.btnInstall.setFocusPolicy(Qt.NoFocus)
        self.ui.btnUpdate.setFocusPolicy(Qt.NoFocus)
        self.ui.btnUninstall.setFocusPolicy(Qt.NoFocus)
        self.ui.btnSshotBack.setFocusPolicy(Qt.NoFocus)
        self.ui.btnSshotNext.setFocusPolicy(Qt.NoFocus)
        self.ui.reviewListWidget.setFocusPolicy(Qt.NoFocus)
        self.ui.summary.setReadOnly(True)
        self.ui.description.setReadOnly(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.btnCloseDetail.clicked.connect(self.slot_close_detail)
        self.ui.btnInstall.clicked.connect(self.slot_click_install)
        self.ui.btnUpdate.clicked.connect(self.slot_click_update)
        self.ui.btnUninstall.clicked.connect(self.slot_click_uninstall)

        # style
        self.detailWidget.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.white)
        self.detailWidget.setPalette(palette)

        self.setAutoFillBackground(True)
        self.setPalette(palette)

        self.verticalScrollBar().setStyleSheet("QScrollBar:vertical{width:12px;background-color:black;margin:0px,0px,0px,0px;padding-top:0px;padding-bottom:0px;}"
                                               "QScrollBar:sub-page:vertical{background:qlineargradient(x1: 0.5, y1: 1, x2: 0.5, y2: 0, stop: 0 #D4DCE1, stop: 1 white);}QScrollBar:add-page:vertical{background:qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 #D4DCE1, stop: 1 white);}"
                                               "QScrollBar:handle:vertical{background:qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #CACACA, stop: 1 #818486);}QScrollBar:add-line:vertical{background-color:green;}")
        self.ui.name.setStyleSheet("QLabel{font-size:16px;font-weight:bold;}")
        self.ui.splitText1.setStyleSheet("QLabel{color:#1E66A4;font-size:16px;}")
        self.ui.splitText2.setStyleSheet("QLabel{color:#1E66A4;font-size:16px;}")
        self.ui.splitText3.setStyleSheet("QLabel{color:#1E66A4;font-size:16px;}")
        self.ui.splitLine1.setStyleSheet("QLabel{background-color:#E0E0E0;}")
        self.ui.splitLine2.setStyleSheet("QLabel{background-color:#E0E0E0;}")
        self.ui.splitLine3.setStyleSheet("QLabel{background-color:#E0E0E0;}")
        self.ui.detailHeader.setStyleSheet("QLabel{background-image:url('res/detailheadbg.png');color:black;font-size:14px;padding-top:17px;}")
        self.ui.btnCloseDetail.setStyleSheet("QPushButton{background-image:url('res/btn2-1.png');border:0px;color:#497FAB;}QPushButton:hover{background:url('res/btn2-2.png');}QPushButton:pressed{background:url('res/btn2-3.png');}")
        self.ui.candidateVersion.setStyleSheet("QLabel{color:#FF7D15;}")
        self.ui.gradeBG.setStyleSheet("QLabel{background-image:url('res/gradebg.png')}")
        self.ui.grade.setStyleSheet("QLabel{font-size:30px;color:#1E66A4;}")
        self.ui.gradeText2.setStyleSheet("QLabel{font-size:13px;}")
        self.ui.gradeText3.setStyleSheet("QLabel{font-size:13px;color:#9AA2AF;}")
        self.ui.summary.setStyleSheet("QTextEdit{border:0px;}")
        self.ui.description.setStyleSheet("QTextEdit{border:0px;}")
        self.ui.description.verticalScrollBar().setStyleSheet("QScrollBar:vertical{width:11px;background-color:black;margin:0px,0px,0px,0px;padding-top:0px;padding-bottom:0px;}"
                                                                 "QScrollBar:sub-page:vertical{background:qlineargradient(x1: 0.5, y1: 1, x2: 0.5, y2: 0, stop: 0 #D4DCE1, stop: 1 white);}QScrollBar:add-page:vertical{background:qlineargradient(x1: 0.5, y1: 0, x2: 0.5, y2: 1, stop: 0 #D4DCE1, stop: 1 white);}"
                                                                 "QScrollBar:handle:vertical{background:qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #CACACA, stop: 1 #818486);}QScrollBar:add-line:vertical{background-color:green;}")
        self.ui.sshotBG.setStyleSheet("QLabel{background-image:url('res/sshotbg.png')}")
        self.ui.btnSshotBack.setStyleSheet("QPushButton{border:0px;background-image:url('res/btn-sshot-back-1.png')}QPushButton:hover{background-image:url('res/btn-sshot-back-2')}QPushButton:pressed{background-image:url('res/btn-sshot-back-3')}")
        self.ui.btnSshotNext.setStyleSheet("QPushButton{border:0px;background-image:url('res/btn-sshot-next-1.png')}QPushButton:hover{background-image:url('res/btn-sshot-next-2')}QPushButton:pressed{background-image:url('res/btn-sshot-next-3')}")
        self.ui.reviewListWidget.setStyleSheet("QListWidget{border:0px;}QListWidget::item{height:85px;margin-top:-1px;border:0px;}")

        self.hide()

    def ui_init(self):
        self.ui = Ui_DetailWidget()
        self.ui.setupUi(self.detailWidget)

    # fill fast property, show ui, request remote property
    def showSimple(self, software):
        # clear reviews
        self.ui.reviewListWidget.clear()
        self.detailWidget.resize(805, 790)
        self.ui.reviewListWidget.resize(805, 0)

        self.app = software
        self.ui.name.setText(software.name)
        self.ui.installedVersion.setText("当前版本: " + software.installed_version)
        self.ui.candidateVersion.setText("最新版本: " + software.candidate_version)
        self.ui.summary.setText(software.summary)
        self.ui.description.setText(software.description)

        if(os.path.isfile(UBUNTUKYLIN_RES_TMPICON_PATH + software.name + ".png")):
            self.ui.icon.setStyleSheet("QLabel{background-image:url('" + UBUNTUKYLIN_RES_TMPICON_PATH + software.name + ".png')}")
        else:
            self.ui.icon.setStyleSheet("QLabel{background-image:url('" + UBUNTUKYLIN_RES_TMPICON_PATH + "default.png')}")

        size = software.packageSize
        sizek = size / 1000
        self.ui.size.setText("软件大小: " + str(sizek) + " K")

        self.ui.gradeText1.setText("我的评分: ")
        self.ui.gradeText2.setText("评分 ? 次")
        self.ui.gradeText3.setText("满分5分")
        self.ui.grade.setText(str(software.rnrStat.ratings_average))
        self.star = StarWidget('big', 4, self.detailWidget)
        self.star.move(500, 94)

        if(software.is_installed):
            self.ui.status.setStyleSheet("QLabel{background-image:url('res/installed.png')}")
            self.ui.status.show()

            if(software.is_upgradable):
                self.ui.btnInstall.setText("已安装")
                self.ui.btnUpdate.setText("可升级")
                self.ui.btnUninstall.setText("可卸载")
                self.ui.btnInstall.setEnabled(False)
                self.ui.btnUpdate.setEnabled(True)
                self.ui.btnUninstall.setEnabled(True)
                self.ui.btnInstall.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
                self.ui.btnUpdate.setStyleSheet("QPushButton{background-image:url('res/btn4-1.png');border:0px;color:white;}QPushButton:hover{background:url('res/btn4-2.png');}QPushButton:pressed{background:url('res/btn4-3.png');}")
                self.ui.btnUninstall.setStyleSheet("QPushButton{background-image:url('res/btn5-1.png');border:0px;color:white;}QPushButton:hover{background:url('res/btn5-2.png');}QPushButton:pressed{background:url('res/btn5-3.png');}")
            else:
                self.ui.btnInstall.setText("已安装")
                self.ui.btnUpdate.setText("不可升级")
                self.ui.btnUninstall.setText("可卸载")
                self.ui.btnInstall.setEnabled(False)
                self.ui.btnUpdate.setEnabled(False)
                self.ui.btnUninstall.setEnabled(True)
                self.ui.btnInstall.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
                self.ui.btnUpdate.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
                self.ui.btnUninstall.setStyleSheet("QPushButton{background-image:url('res/btn5-1.png');border:0px;color:white;}QPushButton:hover{background:url('res/btn5-2.png');}QPushButton:pressed{background:url('res/btn5-3.png');}")
        else:
            # self.ui.status.setStyleSheet("QLabel{background-image:url('res/notinstall.png')}")
            self.ui.status.hide()

            self.ui.btnInstall.setText("安装")
            self.ui.btnUpdate.setText("不可升级")
            self.ui.btnUninstall.setText("不可卸载")
            self.ui.btnInstall.setEnabled(True)
            self.ui.btnUpdate.setEnabled(False)
            self.ui.btnUninstall.setEnabled(False)
            self.ui.btnInstall.setStyleSheet("QPushButton{background-image:url('res/btn3-1.png');border:0px;color:white;}QPushButton:hover{background:url('res/btn3-2.png');}QPushButton:pressed{background:url('res/btn3-3.png');}")
            self.ui.btnUpdate.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
            self.ui.btnUninstall.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")

        self.show()

        # send request
        ################
        # div

    def add_one_review(self, review):
        count = self.ui.reviewListWidget.count()
        reviewHeight = (count + 1) * 85
        self.detailWidget.resize(805, 790 + reviewHeight)
        self.ui.reviewListWidget.resize(805, reviewHeight)

        oneitem = QListWidgetItem()
        rliw = ReviewWidget(review)
        self.ui.reviewListWidget.addItem(oneitem)
        self.ui.reviewListWidget.setItemWidget(oneitem, rliw)

    def add_sshot(self, sshot):
        onesshot = QLabel()
        onesshot.setGeometry(309, 458, 158, 120)
        # onesshot.setStyleSheet("QLabel{background-image:url('res/" + sshot. + "')}")

    def slot_close_detail(self):
        self.hide()

    def slot_click_install(self):
        self.emit(SIGNAL("clickinstall"), self.app)
        self.ui.btnInstall.setText("处理中")
        self.ui.btnInstall.setEnabled(False)

    def slot_click_update(self):
        self.emit(SIGNAL("clickupdate"), self.app)
        self.ui.btnUpdate.setText("处理中")
        self.ui.btnUpdate.setEnabled(False)

    def slot_click_uninstall(self):
        self.emit(SIGNAL("clickremove"), self.app)
        self.ui.btnUninstall.setText("处理中")
        self.ui.btnUninstall.setEnabled(False)

    def slot_work_finished(self, newPackage):
        self.app.package = newPackage
        if(self.app.mark == "install" or self.app.mark == "update"):
            self.ui.status.show()
            self.ui.btnInstall.setText("已安装")
            self.ui.btnUpdate.setText("不可升级")
            self.ui.btnUninstall.setText("可卸载")
            self.ui.btnInstall.setEnabled(False)
            self.ui.btnUpdate.setEnabled(False)
            self.ui.btnUninstall.setEnabled(True)
            self.ui.btnInstall.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
            self.ui.btnUpdate.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
            self.ui.btnUninstall.setStyleSheet("QPushButton{background-image:url('res/btn5-1.png');border:0px;color:white;}QPushButton:hover{background:url('res/btn5-2.png');}QPushButton:pressed{background:url('res/btn5-3.png');}")
        elif(self.app.mark == "remove"):
            self.ui.status.hide()
            self.ui.btnInstall.setText("安装")
            self.ui.btnUpdate.setText("不可升级")
            self.ui.btnUninstall.setText("不可卸载")
            self.ui.btnInstall.setEnabled(True)
            self.ui.btnUpdate.setEnabled(False)
            self.ui.btnUninstall.setEnabled(False)
            self.ui.btnInstall.setStyleSheet("QPushButton{background-image:url('res/btn3-1.png');border:0px;color:white;}QPushButton:hover{background:url('res/btn3-2.png');}QPushButton:pressed{background:url('res/btn3-3.png');}")
            self.ui.btnUpdate.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")
            self.ui.btnUninstall.setStyleSheet("QPushButton{background-image:url('res/btn-notenable.png');border:0px;color:#9AA2AF;}")

