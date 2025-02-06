def main():
    while True:
        print_title_screen()
        user_input = input()
        
        if user_input.lower() == 'q':
            break
        elif user_input.lower() == 'esc':
            selected_items = purchase_products()
            total = calculate_total(selected_items)
            print(f"商品       数量")
            for item in selected_items:
                print(f"{item['name']} {selected_items.count(item)}")
            print(f"合計{total}円")
            take_payment(total)
        else:
            print("無効なキーです。")

if __name__ == '__main__':
    main()