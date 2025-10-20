####クラスとは再利用可能＆拡張性があること！忘れることのないように！#################
#os.getenvを利用するために！PC内の保存データを持ってくる
import os
from logger import SimpleLogger
from selenium_manager import ChromeDriverManager, GetElement, ActionElement


##########################################################################
#classを作成する
class AutoLoginFlow:
    #初期設定
    def __init__(self):
        
        #loggerを呼び出してログを利用できるようにする
        self.get_logger_setup = SimpleLogger()
        self.logger = self.get_logger_setup.get_logger()
        
        
        #chromeを起動をここで行う
        self.chrome_manager = ChromeDriverManager()
        self.chrome = self.chrome_manager.chrome_process() #メソッド
        
        
        #インスタンスを作成する
        #classの中でインスタンスを準備するのはself.を付けて自分の道具として使えるようにするため
        self.get_element = GetElement(driver=self.chrome)
        self.action_element = ActionElement()
        
        
##########################################################################
    def process(self, url: str, id_locator: str, pass_locator: str, login_btn_locator: str):
        #１つ目のフロー
        #サイトを開く
        self.chrome.get(url)
        
        #2つ目のフロー
        #IDを入力する　※環境変数という特別な場所からIDという名前を探してきて
        id_text = os.getenv("ID")
        #IDを探して持ってきて
        id_element = self.get_element.get_id_element(id_locator)
        #IDを入力して打ち込んで
        self.action_element.input_text(id_element,id_text)
        
        