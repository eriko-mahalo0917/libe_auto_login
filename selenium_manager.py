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
        self.driver = self.chrome_process() #最後にここにって難しい
        
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
            self.logger.info(f"ドライバーの起動をします")
            chrome = webdriver.Chrome(service=service ,options=chrome_options)
            self.logger.info(f"ドライバーが起動しました")
            #この設置した設定をここで受け取ります
            return chrome
        #起動できなかった場合はこれをする
        except Exception as e:
            #エラーのログを出す
            self.logger.error(f"ドライバーの起動に失敗しました")
            #失敗したerror内容をここで出す
            self.logger.error(f"エラーの内容：{e}")
            #処理を停止
            raise
        

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#--- ② ページの部品（IDやパスワードの入力欄など）を見つけるクラスを作る ---
#WebDriverという「型」を教えるために、インポートを一つ追加　型ヒント
from selenium.webdriver.remote.webdriver import WebDriver
#これをインポートするをIDとか名前とか探せる
from selenium.webdriver.common.by import By

class GetElement:
    #初期設定をする　これも共通でログを設定
    def __init__(self,driver:WebDriver):
        #中身はさっきと一緒だけど名前を変えた方が分かりやすいから変更
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        #ライブラリから持ってきて使っていて、変数へ入れ込んでいる
        self.driver = driver
        
    #=====IDで要素を取得する機能==========
    def get_id_element(self):
        #tryの外側にinfoをおいたのは宣言自体はエラーにならないから
        self.logger.info(f"IDで要素を取得します")
        
        try:
            return self.driver.find_element(By.ID, "username")
        except Exception as e:
            self.logger.error(f"ID=username要素の取得に失敗しました")
            raise