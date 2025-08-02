coffee_menu = []

def add_coffee(coffee):
    coffee_menu.append(coffee)

def show_menu():
    print("현재 커피 메뉴:")
    for coffee in coffee_menu:
        print(coffee)
