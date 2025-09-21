#ロガー：各レベル（５つ）に対して色を分ける機能を実装（カスタム）
#レベルに合わせて、記録された文字の色を変える機能
#--------------------------------------------
#Pythonの標準ライブラリ（たくさんの本棚みたいな場所）にあるモジュール（部品）を取ってきて、「logging --- Python 用のログ記録手段」をインポートして呼び出して、
# 現在のログインのエラー状況を記録し、これから書くコードを記録してくれるお道具箱的な？自動では色々してくれなくて、こっちが指示を出さなきゃいけない


# 1. 必要な部品をPythonの標準モジュールよりインポートする　loggingモジュールから、4つの部品をインポートしています。
#getLogger: 記録係　/ FileHandler: ファイルに出力する係 / Formatter: 見た目を決める係 / DEBUG: 重要度レベルの名前
from logging import getLogger, FileHandler, Formatter, DEBUG

#このloggerはログの出力を命令するオブジェクト&特殊な変数
#ログを「[レベル名] 日時 - メッセージ (ファイル名)」という詳しい形式で表示するためのformatter（見た目を決める係）を準備! ①重要度のレベル　②時間　③メッセージ　④どこのファイル
#formatterは自分で名前を決めていい変数！Formatter()でモジュールから呼び出す内容　中身の引数はテンプレートであるもの！クラスだけど、すでに作られたクラスだからclassで指定しなくていい
formatter = Formatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
#記録係を準備
logger = getLogger(__name__)
#「ログの出力先を、log.txtという名前のファイルにしてください」と指示する、ファイル出力専門の係　ここはclass
handler = FileHandler("log.txt")
#handlerさん、引数で決めたformatterの通りに表示してねということ！メソッドを呼び出している
handler.setFormatter(formatter)
#handlerの出力するレベルはすべてがいいからDEBUGのレベルを選んでいる
handler.setLevel(DEBUG)
#ここのレベルもDEBUGからの出力
logger.setLevel(DEBUG)
#これはgetLogger（）とペア的な存在！出力先をセットする！どういうこと？
logger.addHandler(handler)

logger.debug("これはデバッグログです")
logger.error("ファイルが存在していません")

#復習 呼び出し
from logging import getLogger, StreamHandler, Formatter, DEBUG

# --- ★★★ここからが色付け機能を追加する部分★★★ ---
class ColoredFormatter(Formatter):
    """ログレベルに応じて色を付けるためのカスタムFormatter"""
    COLORS = {
        'WARNING':  '\033[33m',  # 黄色
        'INFO':     '\033[32m',  # 緑色
        'DEBUG':    '\033[36m',  # 水色
        'ERROR':    '\033[31m',  # 赤色
        'RESET':    '\033[0m'    # 色をリセット
    }

    def format(self, record):
        # ログメッセージに色を付ける
        log_message = super().format(record)
        return f"{self.COLORS.get(record.levelname, self.COLORS['RESET'])}{log_message}{self.COLORS['RESET']}"
# --- ★★★ここまで★★★


#フォーマットどんな風呼び出すか？決まったclassを呼び出す レベル名前と時間とメッセージとファイル名
formatter = ColoredFormatter('[%(levelname)s] %(asctime)s - %(message)s (%(filename)s)')
#記録係の特殊な変数で呼び出す
logger = getLogger(__name__)
#ログの出力先を決める
handler = StreamHandler()
#handlerのレベルを決める
handler.setFormatter(formatter)
#
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

logger.debug("これはデバッグのログです")
logger.info("プログラムが開始しました")
logger.error("ファイルは存在しません")
logger.warning("ファイルが容量を超えました")