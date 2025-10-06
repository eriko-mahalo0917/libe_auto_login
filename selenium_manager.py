#インポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from logger import SimpleLogger

#クラスを作成する
class ChromeDriverManager:
    #初期設定
    def __init__(self):
        self.getLogger = SimpleLogger()
        self.logger = self.getLogger.get_logger()
        self.drive = self.chrome_process()
        
    #①設定するためのオプションを設定
    def get_chrome_options(self):
        #インスタンスを作成する
        chrome_options = Options()
        #ウィンドウのサイズのみだから
        chrome_options.add_argument("--window-size=1000,1000")
        return chrome_options
        
    #②ドライバーを生成する　ブラウザを立ち上げるみたいな？
    def chrome_process(self):
        service = Service()
        
        #①の作成したのをここで受け取る
        chrome_options = self.get_chrome_options()
        
        #エラー時はraiseで処理を停止します
        try:
            self.logger.info("ドライバーの起動をします")
            chrome = webdriver.Chrome(service=service ,options=chrome_options)
            self.logger.info("ドライバーが起動しました")
            #この設置した設定をここで受け取ります
            return chrome
        #起動できなかったのは愛
        except Exception as e:
            #エラーのログを出す
            self.logger.error(f"ドライバーの起動に失敗しました")
            #失敗したerror内容をここで出す
            self.logger.error(f"エラーの内容：{e}")
            #処理を停止
            raise