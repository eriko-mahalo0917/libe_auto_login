#インポート####################################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#loggerとchromeをインポート
from logger import SimpleLogger
from chrome import ChromeManager

#############################################################################

#1つ目のフロー：ブラウザを立ち上げる
#ChromeManagerのインスタンスを呼ぶ
class ChromeDriverManager:
    def __init__(self):
        self.chrome_manager = ChromeManager()
    
    #デフォルトは1000，1000だけど、自由に設定できるようにする
    def chrome_process(self, window_size = "1000,1000"):
        service = Service()
        driver = self.chrome_manager.start_chrome(window_size=window_size)
        return driver
    
    

#２つ目のフロー
#ID、パスワードを取得
class GetElement:
    #探すためのdriverが必要だから、引数にいる
    def __init__(self, driver: WebDriver):
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        self.driver = driver
        
    #ID取得
    def get_id_element(self, id_locator: str):
        self.logger.info(f"ID='{id_locator}' で要素を取得します")
        try:
            id_element = self.driver.find_element(By.ID, id_locator)
            self.logger.info(f"ID='{id_locator}' の取得に成功しました")
            return id_element
        except Exception as e:
            self.logger.error(f"ID='{id_locator}' 要素の取得に失敗しました\nエラー内容: {e}")
            #処理停止
            raise
        
    #パスワード取得
    def get_pass_element(self, pass_locator: str):
        self.logger.info(f"PASS='{pass_locator}'の取得します")
        try:
            pass_element = self.driver.find_element(By.ID, pass_locator)
            self.logger.info(f"PASS='{pass_locator}'の取得に成功しました")
            return pass_element
        except Exception as e:
            self.logger.error(f"PASS='{pass_locator}'の要素の取得に失敗しました\nエラー内容：{e}")
            #処理停止
            raise
        
        
    #チェックボックス探す
    def get_check_box_element(self, check_locator: str):
        self.logger.info(f"チェックボックス=’{check_locator}’の要素を取得します")
        try:
            check_element = self.driver.find_element(By.ID, check_locator)
            self.logger.info(f"チェックボックス='{check_locator}' の取得に成功しました")
            return check_element
        except Exception as e:
            self.logger.error(f"チェックボックス='{check_locator}' 要素の取得に失敗しました\nエラー内容: {e}")
            #処理停止
            raise
        
    #ログインボタン探す
    def get_login_btn_element(self, login_btn_locator: str):
        self.logger.info(f"ログインボタン='{login_btn_locator}' で要素を取得します")
        try:
            btn_element = self.driver.find_element(By.ID, login_btn_locator)
            self.logger.info(f"ログインボタン='{login_btn_locator}' の取得に成功しました")
            return btn_element
        except Exception as e:
            self.logger.error(f"ログインボタン='{login_btn_locator}' の取得に失敗しました。\nエラー内容{e}")
            #処理停止
            raise
        
        
            
#３つ目のフロー
#操作してログインボタンをクリック＋自分で見つける　※※ここでGetElementを呼び出して使う※※
class ActionElement:
    def __init__(self,get_element_instance: GetElement):
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        self.get_element = get_element_instance
        
        
    #クリアしてから入力する 
    def click_clear_input(self, locator: str,input_text: str):
        #GetElementを利用してクリック・クリアを入力する
        self.logger.info(f"{locator}にテキストを入力します。")
        #空っぽの箱を用意
        
        try:
            element = self.get_element.get_id_element(locator)
            #クリックをして入力できるようにする
            element.click()
            #一旦、クリアする
            element.clear()
            #テキスト入力
            element.send_keys(input_text)
            self.logger.info(f"テキスト入力に成功しました")
        except Exception as e:
            self.logger.error(f"テキスト入力に失敗しました。\nエラー内容{e}")
            #処理停止
            raise
        
    #クリックする
    def click_element(self, locator: str):
        self.logger.info(f"{locator}の要素をクリックします")
        
        try:
            element = self.get_element.get_login_btn_element(locator)
            element.click()
            self.logger.info(f"クリックに成功しました")
        except Exception as e:
            self.logger.error(f"ID='{locator}' のクリックまたは要素検索に失敗しました。\nエラー: {e}")
            #処理停止
            raise