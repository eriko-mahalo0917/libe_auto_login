#インポートしてくる
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#loggerを呼ぶ
from logger import SimpleLogger

#クラスを作成する
class ChromeManager:
    #コンストラクタで初期設定　ログの部分
    def __init__(self):
        #loggerの準備をする
        self.getLogger = SimpleLogger()
        self.logger = self.getLogger.get_logger()
        
    #①ブラウザの設定を決める
    def get_chrome_options(self):
        #ライブラリにあるものでインスタンスを作成
        chrome_options = Options()
        #ウィンドウサイズ
        chrome_options.add_argument("--window-size=840,600")
        #ポジションの場所
        chrome_options.add_argument("--window-position=0,0")
        return chrome_options
    
    #②ブラウザを起動する機能
    def start_chrome(self):
        service = Service()
        #①で作成したものよ呼び出し、変数へ代入　自分自身の機能を呼び出すからself　※インストラクタじゃない
        chrome_options =  self.get_chrome_options()
        
        try:
            self.logger.info(f"これからブラウザを起動します")
            chrome = webdriver.Chrome(service=service ,options=chrome_options)
            self.logger.info(f"ブラウザを起動できました")
            return chrome
        
        except Exception as e:
            self.logger.error(f"ブラウザを起動できませんでした")
            #失敗したから、実行をストップ！
            raise
        
    #③サイトを開く
    def open_site(self,url):
        #②をここで呼び出す
        chrome = self.start_chrome()
        self.logger.info(f"これからサイトを立ち上げます")
        chrome.get(url)
        self.logger.info(f"サイトを立ち上げました:{url}")
        
#実際に動かすための命令 インスタンスを作成
chrome_manager = ChromeManager()
yahoo_url = "https://www.yahoo.co.jp"
chrome_manager.open_site(url=yahoo_url)