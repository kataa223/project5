import eel
import desktop
import pos_system

ITEM_CODE = 0
ITEM_NAME = 1
ITEM_PRICE = 2

app_name="html"
end_point="index.html"
size=(700,600)

# item_master.csvの読み込み
with open("item_master.csv", "r", encoding="utf-8") as f:
    item_lines = f.read().splitlines()

# マスタ登録
item_master=[]  
for item_line in item_lines:
    item = item_line.split(",")
    item_master.append(pos_system.Item(item[ITEM_CODE], item[ITEM_NAME], item[ITEM_PRICE]))

# オーダーをインスタンス化
order = pos_system.Order(item_master)

# オーダー登録
@ eel.expose
def regist_item_run(item_code, item_number):
    order.set_item_order(item_code)                         # オーダーを追加
    order.set_item_number(item_number)                      # 個数を追加
    order.set_item_display_list(item_code, item_number)     # 表示用の商品リストを設定
    order.set_items_amount(item_code, item_number)          # 合計金額を設定
    return order.get_item_display_list()                    # 表示用の良品リストを取得

# 現時点での合計金額を取得
@ eel.expose
def get_total_current():
    return f'合計金額:{order.get_items_amount()}'

# 会計
@ eel.expose
def calc_total_run(money):
    order.set_money(int(money))     # お預かり金額を設定
    order.set_change()              # おつりを設定
    text_display = f'合計金額:{order.get_items_amount()}\nお預かり金額:{order.get_money()}\nおつり:{order.get_change()}'
    return text_display
    
# リセット
@ eel.expose
def reset_run():
    order.__init__(item_master)

desktop.start(app_name,end_point,size)