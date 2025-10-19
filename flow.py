####クラスとは再利用可能＆拡張性があること！忘れることのないように！#################

# 環境変数！このファイルの外側、PC自体に保存してあるデータを呼び出せる仕組み
import os
#selenium_managerからクラスをインポート
from selenium_manager import ChromeDriverManager, GetElement, ActionElement
#loggerをインポート
from logger import SimpleLogger


##########################################################################

class AutoLoginFlow:
    #初期設置
    def __init__(self):
        #logger　ログの設定
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        
        
        #🚀chromeの起動をここで行う
        self.driver_manager = ChromeDriverManager()
        self.chrome = self.driver_manager.chrome_process() #メソッド
        
        
        #インスタンスを作成する
        #classの中でインスタンスを準備するのはself.を付けて自分の道具として使えるようにするため
        self.get_element = GetElement(driver=self.chrome)
        self.action_element = ActionElement()
        
        
        
#########################################################################
    def process(self, url: str, id_locator: str, pass_locator: str,login_btn_locator: str):
    #3回まで繰り返して（０，１，２の３回繰り返す）
        count = 0
        while count < 3:
            try:
                #1つ目のフロー
                #ログインサイトを開く
                self.open_site(url) #別定義のところ
                #2つ目のフロー
                #IDを入力
                id_text = os.getenv("ID")
                id_box = self.get_element.get_id_element(id_locator)
                self.action_element.input_text(id_box, id_text)
            
            
                
            
                
                
    #別定義---------------------------------------------------------------
    #ここはchrome.pyのopen_siteではダメなのか？initでchromを開いているから？ ん？    
    def open_site(self, url :str):
        self.logger.info(f"ログインサイトを開きます:{url}")
        self.chrome.get(url)
        self.logger.info(f"ログインサイトを開きました")