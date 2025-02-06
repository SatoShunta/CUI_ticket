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