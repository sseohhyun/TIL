# inventory.py
inventory = {}

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item(item, quantity):
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
        else:
            print(f"재고가 부족합니다. 현재 {item}의 재고: {inventory[item]}")
    else:
        print(f"{item}은(는) 재고에 없습니다.")

def get_inventory():
    return inventory