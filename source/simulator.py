def purchase_products():
    selected_items = []
    while True:
        display_products()
        choice = input("購入する商品番号(支払いに進む場合はc)>")
        
        if choice == 'c':
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(products):
                selected_items.append(products[choice - 1])
            else:
                print("商品番号またはcを指定してください。")
        else:
            print("商品番号またはcを指定してください。")
    
    return selected_items

def calculate_total(selected_items):
    total = sum(item['price'] for item in selected_items)
    return total

def take_payment(total):
    while True:
        try:
            payment = float(input(f"現金を投入してください>"))
            if payment < total:
                print("金額が不足しています。")
                break
            elif payment <= 0:
                print("正の金額を入力してください。")
                break
            else:
                change = payment - total
                print(f"おつり{int(change)}円です。")
                break
        except ValueError:
            print("無効な入力です。再度入力してください。")
# 画面クリア関数
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 商品一覧表示関数
def display_products():
    print("======= 商品一覧 =======")
    print("商品      単価  販売数  売上金額")
    print("=======================")
    for i, product in enumerate(products):
        print(f"{i+1}.{product['name']:<8}{product['price']:>5}円{product['sales']:>4}{product['revenue']:>8}円")
    print("---")
    total_revenue = sum(product['revenue'] for product in products)
    print(f"総売上金額 {total_revenue:>8}円")
    print("===")

# 売上リセット関数
def reset_sales():
    for product in products:
        product['sales'] = 0
        product['revenue'] = 0
    print("売上をリセットしました。")

# 価格変更関数
def change_price():
    display_products()
    while True:
        try:
            product_num = int(input("価格を変更する商品の番号を入力してください。>"))
            if 1 <= product_num <= len(products):
                break
            else:
                print("有効な商品番号を入力してください。")
        except ValueError:
            print("数値を入力してください。")

    while True:
        try:
            new_price = int(input("変更金額を入力してください。>"))
            if new_price >= 0:
                break
            else:
                print("0以上の金額を入力してください。")
        except ValueError:
            print("数値を入力してください。")

    print(f"【{product_num}.{products[product_num-1]['name']} {new_price}円】に変更します。")
    confirmation = input("よろしいですか(Y/N）>")
    if confirmation.upper() == 'Y':
        products[product_num-1]['price'] = new_price
        print("変更しました。")
    else:
        print("変更をキャンセルしました。")

# 管理メニュー関数
def display_admin_menu():
    while True:
        display_products()
        print("=== 管理メニュー ===")
        print("1. 売上をリセットする")
        print("2. 商品の価格を変更する")
        print("3. 管理画面を終了する")
        print("---")

        while True:
            try:
                choice = int(input("管理コード入力:"))
                if 1 <= choice <= 3:
                    break
                else:
                    print("有効なメニュー番号を入力してください。")
            except ValueError:
                print("数値を入力してください。")

        if choice == 1:
            reset_sales()
        elif choice == 2:
            change_price()
        elif choice == 3:
            break
            
import os

products = [
    {"name": "特製ラーメン", "price": 1000, "quantity": 0},
    {"name": "醤油ラーメン", "price": 780, "quantity": 0},
    {"name": "しおラーメン", "price": 880, "quantity": 0},
    {"name": "ごはん", "price": 150, "quantity": 0}
]

def print_title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("***********************")
    print(" 券売機シミュレータ ")
    print("***********************")
    print("Please Enter (Enterキー押下で画面がクリアされて処理が進む）")
    print("（ESCキー押下で管理画面に処理が進む）")
    print("（qキー押下でシミュレータ終了）")

def display_products():
    print("商品      金額")
    print("=======================")
    for i, product in enumerate(products, start=1):
        print(f"{i}.{product['name']} {product['price']}円")
