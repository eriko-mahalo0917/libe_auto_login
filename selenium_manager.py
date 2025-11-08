####クラスとは再利用可能＆拡張性があること！忘れることのないように！#################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

#loggerとchromeをインポート
from logger import SimpleLogger
from chrome import ChromeManager

#ランダムスリープのためにインポート
import time
import random #ランダムな数値を生成するライブラリ

###########################################################################
#ランダムスリープを追加
class RandomSleeper:
    #人間っぽくランダムに待機時間を持たせる
    def __init__(self):
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        
    def sleep_time(self, min_time: float = 1.0, max_time: float = 3.0):
        #ランダムモジュールの関数
        wait_time = random.uniform(min_time,max_time)
        #import timeのメソッドで一時停止させる
        time.sleep(wait_time)    

###########################################################################
#１つ目のフロー
# ブラウザを立ち上げる
class ChromeDriverManager:
    def __init__(self):
        self.chrome_manager = ChromeManager()
        
    def chrome_process(self, window_size = "1000,1000"):
        service = Service()
        driver = self.chrome_manager.start_chrome(window_size=window_size)
        return driver
    

#2つ目のフロー
#要素を取得する
class GetElement:
    def __init__(self, driver: WebDriver):
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        self.driver = driver
        
    #IDを取得する
    def find_by_id(self, value: str):
        self.logger.info(f"ID='{value}' で要素を取得します")
        try:
            id_element = self.driver.find_element(By.ID, value)
            self.logger.info(f"ID='{value}' の取得に成功しました")
            return id_element
        except Exception as e:
            self.logger.error(f"ID='{value}'の取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
    
    #NAMEを取得する
    def find_by_name(self, value: str):
        self.logger.info(f"NAME='{value}'で要素を取得します")
        try:
            name_element = self.driver.find_element(By.NAME, value)
            self.logger.info(f"NAME='{value}' の取得に成功しました")
            return name_element
        except Exception as e:
            self.logger.error(f"NAME='{value}' の取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
        
    #XPATHで取得する
    def find_by_xpath(self, value: str):
        self.logger.info(f"XPath='{value}' で要素を取得します")
        try:
            xpath_element = self.driver.find_element(By.XPATH, value)
            self.logger.info(f"XPath='{value}' の取得に成功しました")
            return xpath_element
        except Exception as e:
            self.logger.error(f"XPath='{value}' 要素の取得に失敗しました\nエラー内容: {e}")
            #処理停止
            raise
        
        
    #CSS_SELECTORで取得
    def find_by_css_selector(self, value: str):
        self.logger.info(f"CSS_SELECTOR='{value}' で要素を取得します")
        try:
            css_selector_element = self.driver.find_element(By.CSS_SELECTOR, value)
            self.logger.info(f"CSS_SELECTOR='{value}' で取得に成功しました")
            return css_selector_element
        except Exception as e:
            self.logger.error(f"CSS_SELECTOR='{value}' で要素に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
        
    #TAG_NAMEを取得する
    def find_by_tag_name(self, value: str):
        self.logger.info(f"TAG_NAME='{value}' で要素を取得します")
        try:
            tag_name_element = self.driver.find_element(By.TAG_NAME, value)
            self.logger.info(f"TAG_NAME='{value}' で取得に成功しました")
            return tag_name_element
        except Exception as e:
            self.logger.error(f"TAG_NAME='{value}' で取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
    
    
    #LINK_TEXTを取得する
    def find_by_link_text(self, value: str):
        self.logger.info(f"LINK_TEXT='{value}' で要素を取得します")
        try:
            link_text_element = self.driver.find_element(By.LINK_TEXT, value)
            self.logger.info(f"LINK_TEXT='{value}' で取得に成功しました")
            return link_text_element
        except Exception as e:
            self.logger.error(f"LINK_TEXT='{value}' で取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
    
    #CLASS_NAMEを取得する
    def find_by_class_name(self, value: str):
        self.logger.info(f"CLASS_NAME='{value}' で要素を取得します")
        try:
            class_name_element = self.driver.find_element(By.CLASS_NAME, value)
            self.logger.info(f"CLASS_NAME='{value}' で取得に成功しました")
            return class_name_element
        except Exception as e:
            self.logger.error(f"CLASS_NAME='{value}' で取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
        
#３つ目のフロー
##操作してログインボタンをクリック＋自分で見つける　※※ここでGetElementを呼び出して使う※※
class ActionElement:
    def __init__(self,get_element_instance: GetElement):
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        self.get_element_instance = get_element_instance
        #random_sleeperのインスタンスを作成
        self.random_sleeper = RandomSleeper()
        
    
    #click_clear_inputとclick_elementで取得する共通部分
    def get_element(self, get_method_name: str, value: str):
        self.logger.info("要素を取得します")
        find_method = getattr(self.get_element_instance, get_method_name)
        element =   find_method(value)
        self.logger.info("要素を取得しました")
        return element
    
        
    #クリアをしてから入力する
    def click_clear_input(self, get_method_name: str, value: str, input_text: str):
        self.logger.info("テキストを入力します。")
        try:
            #共通の呼び出す
            element = self.get_element(get_method_name, value)
            
            #サイトを表示した後に待機時間
            self.random_sleeper.sleep_time() #初期値のままで今回はやってみる
            
            #操作する部分
            element.click()
            element.clear()
            element.send_keys(input_text)
            
            #入力後に待機時間を設置
            self.random_sleeper.sleep_time() #初期値のままで今回はやってみる
            
            self.logger.info(f"{get_method_name}で取得した要素に '{input_text}' を入力しました")
        except Exception as e:
            self.logger.error(f"テキスト入力に失敗しました\n{e}")
            #処理停止
            raise
        
        
    #クリックをする
    def click_element(self, get_method_name: str, value: str):
        self.logger.info("要素をクリックします")
        try:
            #共通の呼び出す
            element = self.get_element(get_method_name, value)
            
            #クリックする前に待機時間を設置
            self.random_sleeper.sleep_time() #初期値のままで今回はやってみる
            
            #操作する部分
            element.click()
            self.logger.info(f"{get_method_name}で取得した要素をクリックしました")
        except Exception as e:
            self.logger.error(f"クリックに失敗しました\n{e}")
            #処理停止
            raise