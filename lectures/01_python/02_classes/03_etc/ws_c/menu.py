menu = {}

def add_item(name, price):
    menu[name] = price

def show_menu():
    print("메뉴:")
    for name, price in menu.items():
        print(f"{name}: {price}원")