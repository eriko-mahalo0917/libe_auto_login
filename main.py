#selenium.pyからインポートしてclassを呼び出す
from selenium_manager import ChromeDriverManager, GetElement ,ActionElement


#============================================================================
#メインで実行するためのコード
if __name__=="__main__":
    #seleniumのメソッドを呼び出し、インスタンスを作成
    driver_manager = ChromeDriverManager()
    
    #①ブラウザを起動して、サイズの指定も可能
    print("ブラウザを起動します...🤖")
    driver = driver_manager.chrome_process()
    
    
    #②driverにこのサイトを開いてと命令する
    aeon_url = "https://www.aeon-kyushu.com/signin"
    #selenium_managerのここdef chrome_process(self,window_size="1000,1000"):
    driver.get(url = aeon_url)
    print(f"{aeon_url} を開きました！")
    
    
    #③ページとID入力欄などを探す専門家「GetElement」を呼ぶ
    #①で作った「driver」を渡す
    get_element = GetElement(driver=driver)
    
    
    #④操作をする専門家「ActionElement」を呼ぶ
    action_element = ActionElement()
    
    #ID入力欄を探してとお願いし、見つけた部品を変数に入れる
    id_box = get_element.get_id_element()
    #見つけたID入力欄に文字を入力してとお願いする
    action_element.input_text(element=id_box, text = "eriko.1024@icloud.com")
    print("IDを入力しました！👑")
    
    
    #パスワード入力欄を探してと命令する
    pass_box = get_element.get_pass_element()
    #見つけたパスワード入力欄に文字を入力してとお願いする
    action_element.input_text(element=pass_box, text="passeord")
    print("パスワードを入力しました。")
    
    #ログインボタンを探して
    login_btn = get_element.get_login_btn_element()
    #見つけたログインボタンをクリックしてほしいとお願いする
    action_element.click_element(element=login_btn)
    print("ログインボタンをクリックしました！🎉")
    
    
    