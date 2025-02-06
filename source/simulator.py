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
    print("       （ESCキー押下で管理画面に処理が進む）")
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
        else:
            print("無効なキーが押されました。")

if __name__ == "__main__":
    main()


 