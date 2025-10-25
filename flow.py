####クラスとは再利用可能＆拡張性があること！忘れることのないように！#################
#os.getenvを利用するために！PC内の保存データを持ってくる
import os
from dotenv import load_dotenv
from logger import SimpleLogger
from selenium_manager import ChromeDriverManager, GetElement, ActionElement


load_dotenv()
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
        self.action_element = ActionElement(get_element_instance=self.get_element)
        
        
#=====================================================================
    def process(self, url: str,id_locator: str,pass_locator: str, login_btn_locator: str):
        
        #1つ目のフロー
        #ログインサイトを開く
        self.chrome.get(url)
        
        #2つ目のフロー
        #IDを入力する →　envファイルの"ID" という名前のデータを取り出してid_textへ代入
        id_text = os.getenv("ID")
        #ActionElementを呼び出す
        self.action_element.click_clear_input(locator=id_locator, input_text=id_text)
        
        
        #３つ目のフロー
        #パスワードの入力
        pass_text = os.getenv("PASS")
        self.logger.info(f"パスワードを入力します：{pass_text}")
        self.action_element.click_clear_input(locator=pass_locator, input_text=pass_text)
        
        
        #４つ目のフロー
        #ログインボタンをクリック
        #ログインできているか確認
        self.action_element.click_element(locator=login_btn_locator)
        self.logger.info(f"ログインに成功しました")
        
        #終了
        self.chrome.quit()