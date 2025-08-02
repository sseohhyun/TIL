inventory = {}

def add_stock(name, quantity):
    inventory[name] = quantity

def show_inventory():
    print("재고:")
    for name, quantity in inventory.items():
        print(f"{name}: {quantity}개")