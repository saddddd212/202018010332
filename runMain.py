# -*- coding: utf-8 -*-
"""
点击运行主程序runMain.py
"""


import warnings
import os
# 忽略警告  
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings(action='ignore')
from EmotionRecongnition import Emotion_MainWindow
from sys import argv, exit
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(argv)

    window = QMainWindow()
    ui = Emotion_MainWindow(window)

    window.show()
    exit(app.exec_())
