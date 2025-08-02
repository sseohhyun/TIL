import menu
import inventory

menu.add_item("Espresso", 3000)
menu.add_item("Latte", 4000)
menu.add_item("Cappuccino", 4500)

inventory.add_stock("Espresso", 10)
inventory.add_stock("Latte", 15)
inventory.add_stock("Cappuccino", 12)

menu.show_menu()
print()
inventory.show_inventory()