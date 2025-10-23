####クラスとは再利用可能＆拡張性があること！忘れることのないように！#################
#os.getenvを利用するために！PC内の保存データを持ってくる
import os
from logger import SimpleLogger
from selenium_manager import ChromeDriverManager, GetElement, ElementAction


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
        
        #インスタンスを作成 GetElement&ElementAction
        self.get_element = GetElement(driver = self.chrome)
        self.action_element = ElementAction()
        
        
#=====================================================================
    def process(self, url: str,id_locator: str,pass_locator: str, login_btn_locator: str):
        
        #1つ目のフロー
        #ログインサイトを開く
        self.chrome.get(url)
        
        #2つ目のフロー
        #IDを入力する →　envファイルの"ID" という名前のデータを取り出してid_textへ代入
        id_text = os.getenv("ID")
        id_element = self.get_element.get_id_element(id_locator)
        self.action_element.click_clear_input(element=id_element, text = id_text)
        
        
        #３つ目のフロー
        #パスワードの入力
        pass_text = os.getenv("PASS")
        pass_element = self.get_element.get_pass_element(pass_locator)
        self.logger.info(f"パスワードを入力します：{pass_text}")
        self.action_element.click_clear_input(element=pass_element,text = pass_text)
        
        
        #４つ目のフロー
        #ログインボタンをクリック
        #ログインできているか確認
        login_btn_element = self.get_element.get_login_btn_element(login_btn_locator)
        self.action_element.click_element(element=login_btn_element)
        self.logger.info(f"ログインに成功しました")
        
        #終了