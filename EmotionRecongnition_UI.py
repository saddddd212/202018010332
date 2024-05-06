# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmotionRecongnition_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(600, 645)
        MainWindow.setMaximumSize(QtCore.QSize(820, 645))
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("\n"
"#QInputDialog{border-image: url(:/newPrefix/images_test/light.png);}\n"
"\n"
"QMenuBar{border-color:transparent;}\n"
"QToolButton[objectName=pushButton_doIt]{\n"
"border:5px;}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:hover {\n"
"image:url(:/newPrefix/images_test/run_hover.png);}\n"
"\n"
"QToolButton[objectName=pushButton_doIt]:pressed {\n"
"image:url(:/newPrefix/images_test/run_pressed.png);}\n"
"\n"
"QScrollBar:vertical{\n"
"background:transparent;\n"
"padding:2px;\n"
"border-radius:8px;\n"
"max-width:14px;}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"background:#9acd32;\n"
"min-height:50px;\n"
"border-radius:8px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover{\n"
"background:#9eb764;}\n"
"\n"
"QScrollBar::handle:vertical:pressed{\n"
"background:#9eb764;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"background:none;\n"
"}\n"
"                               \n"
"QScrollBar::sub-page:vertical{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"background:none;}\n"
"                                 \n"
"QScrollBar::sub-line:vertical{\n"
"background:none;\n"
"}\n"
"QScrollArea{\n"
"border:0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"background:transparent;\n"
"padding:0px;\n"
"border-radius:6px;\n"
"max-height:12px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"background:#9acd32;\n"
"min-width:50px;\n"
"border-radius:6px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed{\n"
"background:#9eb764;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:horizontal{\n"
"background:none;\n"
"}\n"
"QScrollBar::add-line:horizontal{\n"
"background:none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"background:none;\n"
"}\n"
"QToolButton::hover{\n"
"border:0px;\n"
"} ")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(8, 30, 425, 47))
        self.label_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(22)
        font.setItalic(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_title.setText("表情识别系统")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_useTime = QtWidgets.QLabel(self.centralwidget)
        self.label_useTime.setGeometry(QtCore.QRect(122, 218, 103, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_useTime.setFont(font)
        self.label_useTime.setObjectName("label_useTime")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(446, 118, 375, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(8, 360, 420, 280))
        self.label_face.setMinimumSize(QtCore.QSize(420, 280))
        self.label_face.setMaximumSize(QtCore.QSize(420, 280))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(:/newPrefix/icons/scan.png);")
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        self.label_face.setObjectName("label_face")
#         self.textEdit_model = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEdit_model.setGeometry(QtCore.QRect(58, 126, 360, 30))
#         self.textEdit_model.setMinimumSize(QtCore.QSize(360, 30))
#         self.textEdit_model.setMaximumSize(QtCore.QSize(360, 30))
#         font = QtGui.QFont()
#         font.setFamily("华文仿宋")
#         font.setPointSize(12)
#         self.textEdit_model.setFont(font)
#         self.textEdit_model.setStyleSheet("background-color: transparent;\n"
# "border-color: rgb(0, 0, 0);\n"
# "color: rgb(0, 0, 0);")
#         self.textEdit_model.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_model.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_model.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
#         self.textEdit_model.setReadOnly(True)
#         self.textEdit_model.setObjectName("textEdit_model")
#         self.toolButton_file = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton_file.setGeometry(QtCore.QRect(8, 242, 50, 40))
#         self.toolButton_file.setMinimumSize(QtCore.QSize(50, 39))
#         self.toolButton_file.setMaximumSize(QtCore.QSize(50, 40))
#         self.toolButton_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.toolButton_file.setAutoFillBackground(False)
#         self.toolButton_file.setStyleSheet("background-color: transparent;")
#         self.toolButton_file.setText("")
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/recovery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.toolButton_file.setIcon(icon)
#         self.toolButton_file.setIconSize(QtCore.QSize(40, 40))
#         self.toolButton_file.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
#         self.toolButton_file.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
#         self.toolButton_file.setAutoRaise(False)
#         self.toolButton_file.setArrowType(QtCore.Qt.NoArrow)
#         self.toolButton_file.setObjectName("toolButton_file")
#         self.textEdit_camera = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEdit_camera.setGeometry(QtCore.QRect(58, 188, 360, 30))
#         self.textEdit_camera.setMinimumSize(QtCore.QSize(360, 30))
#         self.textEdit_camera.setMaximumSize(QtCore.QSize(360, 30))
#         font = QtGui.QFont()
#         font.setFamily("华文仿宋")
#         font.setPointSize(12)
#         self.textEdit_camera.setFont(font)
#         self.textEdit_camera.setStyleSheet("background-color: transparent;\n"
# "border-color: rgb(0, 0, 0);\n"
# "color: rgb(0, 0, 0);")
#         self.textEdit_camera.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_camera.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_camera.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
#         self.textEdit_camera.setReadOnly(True)
#         self.textEdit_camera.setObjectName("textEdit_camera")
#         self.textEdit_pic = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEdit_pic.setGeometry(QtCore.QRect(58, 248, 360, 30))
#         self.textEdit_pic.setMinimumSize(QtCore.QSize(360, 30))
#         self.textEdit_pic.setMaximumSize(QtCore.QSize(360, 30))
#         font = QtGui.QFont()
#         font.setFamily("华文仿宋")
#         font.setPointSize(12)
#         self.textEdit_pic.setFont(font)
#         self.textEdit_pic.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.textEdit_pic.setStyleSheet("background-color: transparent;\n"
# "border-color: rgb(0, 0, 0);\n"
# "color: rgb(0, 0, 0);")
#         self.textEdit_pic.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_pic.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_pic.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
#         self.textEdit_pic.setReadOnly(True)
#         self.textEdit_pic.setObjectName("textEdit_pic")
#         self.pushButton_model = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_model.setGeometry(QtCore.QRect(60, 120, 93, 41))
#         self.pushButton_model.setText("选择模型")
        self.pushButton_camera = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_camera.setGeometry(QtCore.QRect(70, 140, 93, 41))
        self.pushButton_camera.setText("选择摄像头")
        self.pushButton_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_file.setGeometry(QtCore.QRect(210, 140, 93, 41))
        self.pushButton_file.setText("选择图片")
        self.pushButton_video = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_video.setGeometry(QtCore.QRect(350, 140, 93, 41))
        self.pushButton_video.setText("选择视频")

        # self.toolButton_camera = QtWidgets.QToolButton(self.centralwidget)
        # self.toolButton_camera.setGeometry(QtCore.QRect(8, 178, 50, 45))
        # self.toolButton_camera.setMinimumSize(QtCore.QSize(50, 39))
        # self.toolButton_camera.setMaximumSize(QtCore.QSize(50, 45))
        # self.toolButton_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.toolButton_camera.setAutoFillBackground(False)
        # self.toolButton_camera.setStyleSheet("background-color: transparent;")
        # self.toolButton_camera.setText("")
        # icon1 = QtGui.QIcon()
        # icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/g1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.toolButton_camera.setIcon(icon1)
        # self.toolButton_camera.setIconSize(QtCore.QSize(50, 39))
        # self.toolButton_camera.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        # self.toolButton_camera.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # self.toolButton_camera.setAutoRaise(False)
        # self.toolButton_camera.setArrowType(QtCore.Qt.NoArrow)
        # self.toolButton_camera.setObjectName("toolButton_camera")
        # self.toolButton_model = QtWidgets.QToolButton(self.centralwidget)
        # self.toolButton_model.setGeometry(QtCore.QRect(8, 116, 50, 40))
        # self.toolButton_model.setMinimumSize(QtCore.QSize(0, 0))
        # self.toolButton_model.setMaximumSize(QtCore.QSize(50, 40))
        # self.toolButton_model.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.toolButton_model.setAutoFillBackground(False)
        # self.toolButton_model.setStyleSheet("background-color: transparent;")
        # self.toolButton_model.setText("")
        # icon2 = QtGui.QIcon()
        # icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/folder_web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.toolButton_model.setIcon(icon2)
        # self.toolButton_model.setIconSize(QtCore.QSize(40, 40))
        # self.toolButton_model.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        # self.toolButton_model.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # self.toolButton_model.setAutoRaise(False)
        # self.toolButton_model.setArrowType(QtCore.Qt.NoArrow)
        # self.toolButton_model.setObjectName("toolButton_model")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(186, 224, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        # self.line_2 = QtWidgets.QFrame(self.centralwidget)
        # self.line_2.setGeometry(QtCore.QRect(180, 300, 373, 21))
        # self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(180, 288, 223, 43))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.label_outputResult = QtWidgets.QLabel()
        self.label_outputResult.setGeometry(QtCore.QRect(466, 386, 300, 250))
        self.label_outputResult.setMinimumSize(QtCore.QSize(300, 250))
        self.label_outputResult.setMaximumSize(QtCore.QSize(300, 250))
        self.label_outputResult.setStyleSheet("border-image: url(:/icons/ini1.png);")
        self.label_outputResult.setText("")
        self.label_outputResult.setObjectName("label_outputResult")
        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(120, 290, 97, 51))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(16)
        self.label_scanResult.setFont(font)
        self.label_scanResult.setObjectName("label_scanResult")
#         self.textEdit_video = QtWidgets.QTextEdit(self.centralwidget)
#         self.textEdit_video.setGeometry(QtCore.QRect(56, 310, 360, 30))
#         self.textEdit_video.setMinimumSize(QtCore.QSize(360, 30))
#         self.textEdit_video.setMaximumSize(QtCore.QSize(360, 30))
#         font = QtGui.QFont()
#         font.setFamily("华文仿宋")
#         font.setPointSize(12)
#         self.textEdit_video.setFont(font)
#         self.textEdit_video.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.textEdit_video.setStyleSheet("background-color: transparent;\n"
# "border-color: rgb(0, 0, 0;\n"
# "color: rgb(0, 0, 0);")
#         self.textEdit_video.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_video.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
#         self.textEdit_video.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
#         self.textEdit_video.setReadOnly(True)
#         self.textEdit_video.setObjectName("textEdit_video")
#         self.toolButton_video = QtWidgets.QToolButton(self.centralwidget)
#         self.toolButton_video.setGeometry(QtCore.QRect(6, 302, 50, 40))
#         self.toolButton_video.setMinimumSize(QtCore.QSize(50, 39))
#         self.toolButton_video.setMaximumSize(QtCore.QSize(50, 40))
#         self.toolButton_video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
#         self.toolButton_video.setAutoFillBackground(False)
#         self.toolButton_video.setStyleSheet("background-color: transparent;")
#         self.toolButton_video.setText("")
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/pai.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.toolButton_video.setIcon(icon3)
#         self.toolButton_video.setIconSize(QtCore.QSize(40, 40))
#         self.toolButton_video.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
#         self.toolButton_video.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
#         self.toolButton_video.setAutoRaise(False)
#         self.toolButton_video.setArrowType(QtCore.Qt.NoArrow)
#         self.toolButton_video.setObjectName("toolButton_video")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionGoogle_Translate = QtWidgets.QAction(MainWindow)
        self.actionGoogle_Translate.setObjectName("actionGoogle_Translate")
        self.actionHTML_type = QtWidgets.QAction(MainWindow)
        self.actionHTML_type.setObjectName("actionHTML_type")
        self.actionsoftware_version = QtWidgets.QAction(MainWindow)
        self.actionsoftware_version.setObjectName("actionsoftware_version")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "表情识别"))
        self.label_title.setToolTip(_translate("MainWindow", "Test Result Helper 3.3.10 author：WuXian （2019.3.13）"))
        # self.label_useTime.setText(_translate("MainWindow", "<html><head/><body><p>用时：</p></body></html>"))
        self.label_useTime.setText(_translate("MainWindow", "用时："))
        self.label_face.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/icons/scan.png\"/></p></body></html>"))
#         self.textEdit_model.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#070707;\">选择模型</span></p></body></html>"))
#         self.textEdit_camera.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#0b0b0b;\">选择摄像头</span></p></body></html>"))
#         self.textEdit_pic.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#090909;\">选择图片</span></p></body></html>"))
        self.label_time.setText(_translate("MainWindow", "0 s"))
        self.label_result.setText(_translate("MainWindow", "None"))
        # self.label_scanResult.setText(_translate("MainWindow", "<html><head/><body><p>结果：</p></body></html>"))
        self.label_scanResult.setText(_translate("MainWindow", "结果："))
#         self.textEdit_video.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
# "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
# "p, li { white-space: pre-wrap; }\n"
# "</style></head><body style=\" font-family:\'华文仿宋\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
# "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#070707;\">选择视频</span></p></body></html>"))
        self.actionGoogle_Translate.setText(_translate("MainWindow", "Google Translate"))
        self.actionHTML_type.setText(_translate("MainWindow", "HTML type"))
        self.actionsoftware_version.setText(_translate("MainWindow", "software version"))

import image1_rc
