#selenium.pyからインポートしてclassを呼び出す
from selenium_manager import ChromeDriverManager, GetElement ,ActionElement
from selenium.webdriver.common.by import By

#============================================================================
#メインで実行するためのコード
if __name__=="__main__":
    #seleniumのメソッドを呼び出し、インスタンスを作成
    driver_manager = ChromeDriverManager()
    
    #①ブラウザを起動して、サイズの指定も可能
    print("ブラウザを起動します...🤖")
    driver = driver_manager.chrome_process(window_size="1500,1000")
    
    
    #②driverにこのサイトを開いてと命令する
    aeon_url = "https://www.aeon-kyushu.com/signin"
    #selenium_managerのここdef chrome_process(self,window_size="1000,1000"):
    driver.get(url = aeon_url)
    print(f"{aeon_url} を開きました！")
    
    
    #③ページとID入力欄などを探す専門家「GetElement」を呼ぶ
    #①で作った「driver」を渡す
    #get_element = GetElement(driver=driver)
    
    
    #④操作をする専門家「ActionElement」を呼ぶ
    action_element = ActionElement()
    
    #⑤ID入力欄を探してとお願いし、見つけた部品を変数に入れる　※本当のIDの名前
    id_box = driver.find_element(By.NAME, "LOGIN_ID")
    #見つけたID入力欄に文字を入力してとお願いする
    action_element.input_text(element=id_box, text = "eriko.1024@icloud.com")
    print("IDを入力しました！👑")
    
    
    #⑥パスワード入力欄を探してと命令する
    pass_box = driver.find_element(By.NAME ,"PASSWORD")
    #見つけたパスワード入力欄に文字を入力してとお願いする
    action_element.input_text(element=pass_box, text="pppppppppp")
    print("パスワードを入力しました。")
    
    #ログインボタンを探して
    login_btn = driver.find_element(By.CLASS_NAME, "btn-submit")
    #見つけたログインボタンをクリックしてほしいとお願いする
    action_element.click_element(element=login_btn)
    print("ログインボタンをクリックしました！🎉\nログイン成功！")
    
    
    #ログイン後、ユーザーがエンターを押すまでまつ
    input("ブラウザを閉じるにはエンターを教えてください：")
    
    #閉じる作業を入れる
    driver.quit()
    print("ブラウザを閉じました。")