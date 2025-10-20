#インポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#WebDriverという「型」を教えるために、インポートを一つ追加　型ヒント
from selenium.webdriver.remote.webdriver import WebDriver
#これをインポートするをIDとか名前とか探せる
from selenium.webdriver.common.by import By
from logger import SimpleLogger
from chrome import ChromeManager

#クラスを作成する
class ChromeDriverManager:
    #初期設定
    def __init__(self):
        self.chrome_manager = ChromeManager()
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ここはコンストラクタで呼び出してChromeManagerを利用するからいらなくなった場所！！
        
    #①設定するためのオプションを設定
    #def get_chrome_options(self):
        #インスタンスを作成する
        #chrome_options = Options()
        #ウィンドウのサイズのみだから
        #chrome_options.add_argument("--window-size=1000,1000")
        #return chrome_options
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    #②ドライバーを生成する　ブラウザを立ち上げるみたいな？
    def chrome_process(self,window_size="1000,1000"):
        service = Service()
        
        #コンストラクタで呼んだchromeManagerを利用する
        #これは設定機能が入ったメソッドを呼び出している
        driver = self.chrome_manager.start_chrome(window_size=window_size)
        return driver
        
        
#~~~~~~~~~~~~~~~~Chrome.pyのstart_chromeメソッドにtryとexceptが入っているからいらなくなった~~
        #エラー時はraiseで処理を停止します
        #try:
            #self.logger.info(f"ドライバーの起動をします")
            #chrome = webdriver.Chrome(service=service ,options=chrome_options)
            #self.logger.info(f"ドライバーが起動しました")
            #この設置した設定をここで受け取ります
            #return chrome
        #起動できなかった場合はこれをする
        #except Exception as e:
            #エラーのログを出す
            #self.logger.error(f"ドライバーの起動に失敗しました\nエラーの内容：{e}")
            #処理を停止
            #raise
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
#--- ② ページの部品（IDやパスワードの入力欄など）を見つけるクラスを作る ---


class GetElement:
    #初期設定をする　これも共通でログを設定
    def __init__(self,driver:WebDriver):
        #中身はさっきと一緒だけど名前を変えた方が分かりやすいから変更
        self.getLogger_set_up = SimpleLogger()
        self.logger = self.getLogger_set_up.get_logger()
        #ライブラリから持ってきて使っていて、変数へ入れ込んでいる
        self.driver = driver
        
        
    #=====IDで要素を取得する機能==========
    #id_locator: str: 「探してほしいIDの名前（文字列=str）」を受け取るための「箱（引数）」
    def get_id_element(self, id_locator: str):
        #tryの外側にinfoをおいたのは宣言自体はエラーにならないから
        self.logger.info(f"ID='{id_locator}'で要素を取得します")
        #driver.find_elementはライブラリにあるメソッド
        try:
            #探して取得する
            id_element = self.driver.find_element(By.ID, id_locator)
            self.logger.info(f"ID='{id_locator}'の取得に成功しました")
            return id_element
        
        #起動できなかったらこれをする
        except Exception as e:
            self.logger.error(f"ID='{id_locator}'要素の取得に失敗しました\nエラーの内容：{e}")
            #処理停止
            raise
        
             
    #======NAMEを取得する機能============
    #(name_locator: str)
    def get_pass_element(self, name_locator: str):
        #ログを出力
        self.logger.info(f"NAME=’{name_locator}’要素を取得します")
        try:
            name_element = self.driver.find_element(By.NAME, name_locator)
            self.logger.info(f"NAME='{name_locator}'要素の取得に成功しました")
            return name_element
        
        #起動できなかったらこれをする
        except Exception as e:
            self.logger.error(f"NAME='{name_locator}'要素の取得に失敗しました\nエラーの内容：{e}")
            #処理停止
            raise
        
        
    #=======XPATHを取得する機能============
    #(xpath_locator: str)
    def get_xpath_element(self, xpath_locator: str):
        self.logger.info(f"XPATH='{xpath_locator}'で要素を取得します")
        try:
            #このパスはパスワードじゃないよ！//input「ページ上にある、チャックボックスを探して
            #ログインを維持するチェックボックスとか、次回からID笑楽のチェックボックスとか
            xpath_element = self.driver.find_element(By.XPATH, xpath_locator) 
            self.logger.info(f"XPATH='{xpath_locator}' チェックボックス要素を取得しました")
            return xpath_element
        
        #起動できなかったらこれをする
        except Exception as e:
            self.logger.error(f"XPATH= '{xpath_locator}'チェックボックス要素の取得に失敗しました\nエラーの内容：{e}")
            #処理停止
            raise
        
        
    
    #=======ログインボタンを見つける機能==========
    #def get_login_btn_element(self):
        #ログを出力する
        #self.logger.info(f"IDで'login-button'要素を取得します")
        #try:
            #IDのログインボタンを探してほしいってお願いしている
            #login__btn_element = self.driver.find_element(By.ID, 'login-button')
            #ログを出力する
            #self.logger.info(f"ID='login-button'要素の取得に成功しました")
            #return login__btn_element
        #失敗した場合はこれをする
        #except Exception as e:
            #self.logger.error(f"ID='login-button'要素の取得に失敗しました")
            #処理停止
            #raise
        

#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝     

from selenium.webdriver.remote.webelement import WebElement


#クラスを作成する
class ActionElement:
    #初期設定でログを設定
    def __init__(self):
        #中身はさっきと一緒だけど名前を変えた方が分かりやすいから変更
        self.getLogger_action = SimpleLogger()
        self.logger = self.getLogger_action.get_logger()
        
    
    # 入力・クリック操作が定する WebElement = 型ヒント str = 型ヒントで文字列にする
    #elementは対象の部品、ID入力欄とか
    #textは入力したい文字で、userIDとか
    def input_text(self, element: WebElement, text: str):
        self.logger.info(f"テキスト'{text}'を入力します")
    
        try:
            #既に入っている文字を消す
            element.clear()
            #文字を打ち込みしてと命令
            element.send_keys(text)
            self.logger.info(f"テキストの入力に成功しました")
        except Exception as e:
            #失敗したらこれをしてほしい
            self.logger.error(f"文字の入力に失敗しました\nエラーの内容：{e}")
            #処理停止
            raise
    
    
    def click_element(self, element: WebElement):
        #ログを出す
        self.logger.info(f"要素をクリックします")
        try:
            #クリックするよとメソッドを呼んでいる
            element.click()
            self.logger.info(f"要素のクリックに成功しました")
        except Exception as e:
            #失敗したらの処理
            self.logger.error(f"要素のクリックに失敗しました\nエラーの内容：{e}")
            raise
