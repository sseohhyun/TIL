import inventory

inventory.add_item('apple', 10)
inventory.add_item('banana', 5)

inventory.remove_item('apple', 3)

current_inventory = inventory.get_inventory()
print("현재 재고:")
for item, quantity in current_inventory.items():
    print(f"{item}: {quantity}")