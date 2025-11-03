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
    def get_element_by_ID(self, locator: str):
        self.logger.info(f"ID='{locator}' で要素を取得します")
        try:
            id_element = self.driver.find_element(By.ID, locator)
            self.logger.info(f"ID='{locator}' の取得に成功しました")
            return id_element
        except Exception as e:
            self.logger.error(f"ID='{locator}'の取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
    
    #NAMEを取得する
    def get_element_by_name(self, locator: str):
        self.logger.info(f"NAME='{locator}'で要素を取得します")
        try:
            name_element = self.driver.find_element(By.NAME, locator)
            self.logger.info(f"NAME='{locator}' の取得に成功しました")
            return name_element
        except Exception as e:
            self.logger.error(f"NAME='{locator}' の取得に失敗しました\nエラー内容{e}")
            #処理停止
            raise
        
        
    #XPATHで取得する
    def get_element_by_xpath(self, locator: str):
        self.logger.info(f"XPath='{locator}' で要素を取得します")
        try:
            xpath_element = self.driver.find_element(By.XPATH, locator)
            self.logger.info(f"XPath='{locator}' の取得に成功しました")
            return xpath_element
        except Exception as e:
            self.logger.error(f"XPath='{locator}' 要素の取得に失敗しました\nエラー内容: {e}")
            #処理停止
            raise
        
        
    #CSS_SELECTORで取得
    def get_element_by_css_selector(self, locator: str):
        self.logger.info(f"CSS_SELECTOR='{locator}' で要素を取得します")
        try:
            css_selector_element = self.driver.find_element(By.CSS_SELECTOR, locator)
            self.logger.info(f"CSS_SELECTOR='{locator}' で取得に成功しました")
            return css_selector_element
        except Exception as e:
            self.logger.error(f"CSS_SELECTOR='{locator}' で要素に失敗しました")
            #処理停止
            raise
        
        
    #TAG_NAMEを取得する
    def get_element_by_tag_name(self, locator: str):
        self.logger.info(f"TAG_NAME='{locator}' で要素を取得します")
        try:
            tag_name_element = self.driver.find_element(By.TAG_NAME, locator)
            self.logger.info(f"TAG_NAME='{locator}' で取得に成功しました")
            return tag_name_element
        except Exception as e:
            self.logger.error(f"TAG_NAME='{locator}' で取得に失敗しました")
            #処理停止
            raise
    
    
    #LINK_TEXTを取得する
    def get_by_link_text(self, locator: str):
        self.logger.info(f"LINK_NAME='{locator}' で要素を取得します")
        try:
            link_text_element = self.driver.find_element(By.LINK_TEXT, locator)
            self.logger.info(f"LINK_NAME='{locator}' で取得に成功しました")
            return link_text_element
        except Exception as e:
            self.logger.error(f"LINK_NAME='{locator}' で取得に失敗しました")
            #処理停止
            raise
        
    
    #CLASS_NAMEを取得する
    def get_element_by_class_name(self, locator: str):
        self.logger.info(f"CLASS_NAME='{locator}' で要素を取得します")
        try:
            class_name_element = self.driver.find_element(By.CLASS_NAME, locator)
            self.logger.info(f"CLASS_NAME='{locator}' で取得に成功しました")
            return class_name_element
        except Exception as e:
            self.logger.error(f"CLASS_NAME='{locator}' で取得に失敗しました")
            #処理停止
            raise
        
        
#３つ目のフロー
##操作してログインボタンをクリック＋自分で見つける　※※ここでGetElementを呼び出して使う※※
class ActionElement:
    def __init__(self,get_element_instance: GetElement):
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        self.get_element_instance = get_element_instance
        
    
    #click_clear_inputとclick_elementで取得する共通部分
    def get_element(self, method_name: str, locator: str):
        self.logger.info("要素を取得します")
        get_method = getattr(self.get_element_instance, method_name)
        element =   get_method(locator)
        self.logger.info("要素を取得しました")
        return element
    
        
    #クリアをしてから入力する
    def click_clear_input(self, method_name: str, locator: str, input_text: str):
        self.logger.info("テキストを入力します。")
        try:
            #共通の呼び出す
            element = self.get_element(method_name, locator)
            #操作する部分
            element.click()
            element.clear()
            element.send_keys(input_text)
            self.logger.info(f"{method_name}で取得した要素に '{input_text}' を入力しました")
        except Exception as e:
            self.logger.error("テキスト入力に失敗しました\ｎ{e}")
            #処理停止
            raise
        
        
    #クリックをする
    def click_element(self, method_name: str, locator: str):
        self.logger.info("要素をクリックします")
        try:
            #共通の呼び出す
            element = self.get_element(method_name, locator)
            #操作する部分
            element.click()
            self.logger.info(f"{method_name}で取得した要素をクリックしました")
        except Exception as e:
            self.logger.error(f"クリックに失敗しました\n{e}")
            #処理停止
            raise