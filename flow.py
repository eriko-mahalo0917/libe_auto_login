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
    def process(self, url: str, 
                id_method:str, id_value: str,               #IDを探すメソッド名とその値
                pass_method:str, pass_value: str,           #PASSを探すメソッド名とその値
                login_btn_method:str, login_btn_value: str  #Buttonを探すメソッド名とその値
                ):
        
        try:
            #１つ目のフロー
            #ログインサイトを開く
            self.logger.info(f"URLを開きます：{url}")
            self.chrome.get(url)
            
            
            #2つ目のフロー
            #IDを入力する
            id_text = os.getenv("ID")
            self.logger.info("IDを入力します")
            self.action_element.click_clear_input(
                get_method_name = id_method,   #メソッド名が入る
                value = id_value,              #usernameなどの値が入る
                input_text = id_text
            )
            
            
            #３つ目のフロー
            #パスワード入力
            pass_text = os.getenv("PASS")
            self.logger.info("パスワードを入力します")
            self.action_element.click_clear_input(
                get_method_name = pass_method,   #メソッド名が入る
                value = pass_value,              #passwordなどの値が入る
                input_text = pass_text
            )
            
            
            #４つ目のフロー
            #ログインボタンをクリックする
            self.logger.info("ログインボタンをクリックします")
            self.action_element.click_element(
                get_method_name = login_btn_method,
                value = login_btn_value,
            )
            
            self.logger.info("ログインに成功しました")
            
        except Exception as e:
            #要素が見つからないなどのエラーが起きたとき
            self.logger.error(f"ログインフローにエラーが発生しました\n{e}")
            
        #処理終了だけど、成功しても失敗しても処理を終了するからfinally
        finally:
            self.logger.info("ブラウザを終了します")
            self.chrome.quit()