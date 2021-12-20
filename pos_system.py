import datetime
        
### 検索用関数
def find_item(item_master, item_code):
    for i, item in enumerate(item_master):
        if item.get_item_code() == item_code:
            return i
    
### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_item_code(self):
        return self.item_code
    
    def get_price(self):
        return self.price
    
    def get_item_name(self):
        return self.item_name

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list = []
        self.item_number_list = []
        self.item_display_list = ""
        self.amount = 0
        self.money = 0
        self.change = 0
        self.item_master = item_master
    
    # オーダーを設定
    def set_item_order(self,item_code):
        self.item_order_list.append(item_code)
    
    # 個数を設定
    def set_item_number(self,item_number):
        self.item_number_list.append(item_number)
        
    # 合計金額を設定
    def set_items_amount(self, item_code, item_number):
        num = find_item(self.item_master, item_code)
        self.amount += int(self.item_master[num].get_price()) * int(item_number)
    # 合計金額を取得
    def get_items_amount(self):
        return self.amount
        
    # お預かり金額を設定
    def set_money(self, money):
        self.money = money
    # お預かり金額取得
    def get_money(self):
        return self.money
    
    # 表示用の商品一覧を設定    
    def set_item_display_list(self, item_code, item_number):
        num = find_item(self.item_master, item_code)
        self.item_display_list += f'商品コード:{item_code}, 商品名:{self.item_master[num].get_item_name()}, 価格:{self.item_master[num].get_price()}, 個数:{item_number}\n'
    # 表示用の商品一覧を取得    
    def get_item_display_list(self):
        return self.item_display_list
    
    # おつりを設定
    def set_change(self):
        self.change = self.money - self.amount
    # おつり取得
    def get_change(self):
        return self.change
    
