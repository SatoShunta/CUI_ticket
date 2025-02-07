import os

# 商品リスト
products = {
    1: {"name": "特製ラーメン", "price": 1000},
    2: {"name": "醤油ラーメン", "price": 780},
    3: {"name": "しおラーメン", "price": 880},
    4: {"name": "ごはん", "price": 150}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title_screen():
    clear_screen()
    print("***********************")
    print(" 券売機シミュレータ")
    print("***********************")
    print("Please Enter (Enterキー押下で画面がクリアされて処理が進む）")
    print("       （Sキー押下で管理画面に処理が進む）")
    print("       （qキー押下でシミュレータ終了）")

def display_product_menu():
    print("\n商品      金額")
    print("=======================")
    for id, product in products.items():
        print(f"{id}. {product['name']} {product['price']}円")
    print("———")
    print("購入する商品番号(支払いに進む場合はc)> ", end="")

def process_purchase():
    cart = {}
    total_price = 0
    
    while True:
        display_product_menu()
        choice = input()

        if choice == 'c':  # 支払いに進む
            break
        elif choice.isdigit() and int(choice) in products:
            product_id = int(choice)
            if product_id in cart:
                cart[product_id] += 1
            else:
                cart[product_id] = 1
            total_price += products[product_id]["price"]
        else:
            print("商品番号またはcを指定してください。")
    
    if cart:
        print("\n商品       数量")
        for id, quantity in cart.items():
            print(f"{id}.{products[id]['name']}   {quantity}")
        print(f"===\n")
        print(f"合計{total_price}円")
        return total_price
    return 0

def process_payment(total_price):
    while True:
        print("現金を投入してください>", end=" ")
        try:
            money = int(input())
            if money <= 0:
                print("正の金額を投入してください。")
                continue
            if money < total_price:
                print("金額が不足しています。")
                return False
            print(f"ご購入ありがとうございます。おつり{money - total_price}円です。")
            return True
        except ValueError:
            print("無効な金額が入力されました。")

def display_admin_menu():
    while True:
        clear_screen()
        print("****** 管理画面 ******")
        print("1. 商品リスト表示")
        print("2. 商品追加")
        print("3. 商品削除")
        print("4. 商品価格変更")
        print("5. 戻る")
        choice = input("選択してください: ")

        if choice == "1":
            display_product_list()
        elif choice == "2":
            add_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            update_product_price()
        elif choice == "5":
            break
        else:
            print("無効な入力です。")
        input("Enterキーで続行...")

def display_product_list():
    print("\n商品リスト:")
    for id, product in products.items():
        print(f"{id}: {product['name']} - {product['price']}円")

def add_product():
    name = input("追加する商品の名前: ")
    while True:
        try:
            price = int(input("価格: "))
            break
        except ValueError:
            print("無効な価格です。整数を入力してください。")
    product_id = max(products.keys()) + 1
    products[product_id] = {"name": name, "price": price}
    print(f"{name} を追加しました。")

def remove_product():
    display_product_list()
    try:
        product_id = int(input("削除する商品ID: "))
        if product_id in products:
            del products[product_id]
            print("商品を削除しました。")
        else:
            print("無効なIDです。")
    except ValueError:
        print("無効な入力です。")

def update_product_price():
    display_product_list()
    try:
        product_id = int(input("価格を変更する商品ID: "))
        if product_id in products:
            new_price = int(input("新しい価格: "))
            products[product_id]["price"] = new_price
            print("価格を更新しました。")
        else:
            print("無効なIDです。")
    except ValueError:
        print("無効な入力です。")

def main():
    while True:
        display_title_screen()
        key = input()

        if key == "q":  # 終了
            break
        elif key == "":  # Enterキー押下
            total_price = process_purchase()
            if total_price > 0:
                if process_payment(total_price):
                    input("\nEnterキーでタイトル画面に戻る")
            else:
                input("\nEnterキーでタイトル画面に戻る")
        elif key == "s":  # ESCキー押下
            display_admin_menu()
        else:
            print("無効なキーが押されました。")

if __name__ == "__main__":
    main()
