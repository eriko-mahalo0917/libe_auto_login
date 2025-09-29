#ブラウザを動かすために必要で標準ライブラリから読んでいる
from selenium import webdriver
#Optionはウィンドウのサイズを変えたいから呼んでいる
from selenium.webdriver.chrome.options import Options
#Chromeを動かすために必要な「chromedriver.exe」という小さなプログラムを、きちんと管理してくれる秘書
from selenium.webdriver.chrome.service import Service
#作成したloggerを呼び出す
from logger import SimpleLogger

#=============================================================

class ChromeManager:
    #初期設定
    def __init__(self):
        #logging.pyのSimpleLogger()呼んできている
        self.getLogger = SimpleLogger()
        #logging.pyのget_logger()を呼び出していれている
        self.logger = self.getLogger.get_logger()