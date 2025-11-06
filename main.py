#importしてくる##############################################################
from flow import AutoLoginFlow

###########################################################################
#クラスを作成＋インスタンス化
class Main:
    def __init__(self):
        self.auto_login_flow = AutoLoginFlow()
        
    def main(self):
        
        #リベのログインサイト
        libe_url = "https://libecity.com/signin"
        
        #IDの情報
        id_method = "find_by_css_selector"
        id_value = "#contents_wrap > main > div.login_tab_box.is_show > section > div:nth-child(1) > p.form_data_area > input[type=text]"
        
        #PASSの情報
        pass_method = "find_by_css_selector"
        pass_value = "input[type='password']"
        
        #ログインボタンの情報
        login_btn_method = "find_by_xpath"
        login_btn_value = '//*[@id="contents_wrap"]/main/div[1]/section/p[1]/button'
        
        self.auto_login_flow.process(
            url=libe_url,
            id_method = id_method,
            id_value = id_value,
            pass_method = pass_method,
            pass_value = pass_value,
            login_btn_method =login_btn_method,
            login_btn_value = login_btn_value
        )
            
            
#＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
    print("テストが完了しました。")
