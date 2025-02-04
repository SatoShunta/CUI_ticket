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