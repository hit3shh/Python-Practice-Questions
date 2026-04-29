# '''
# Tray 1:  Snacks
# Tray 2:  Beverages
# Tray 4:  Chocolates

# process:
# 1- select tray (1,2,3,0)   # 0 for exit
# let i select tray1:

# 2- shows items such as:
#         a. Lays  20
#         b. Uncle chips  30
#         c. Doritos   40
#     choose items (a,b,c)

# 3- want to stay on same tray  (y/n):

# 1: Tray1
# 2: Tray2
# 3: Tray3

# 4- Select a tray (1,2,3,0):

# output:    

# 1: total bill amount
# 2: Items Dispatched


# '''


# def display_tray(tray_name, items):
#     print(f"\n--- {tray_name} ---")
#     for key, item in items.items():
#         print(f"{key}. {item['name']} - Rs.{item['price']}")

# def vending_machine():
#     trays = {
#         '1': {'name': 'Snacks', 'items': {'a': {'name': 'Lays', 'price': 20}, 'b': {'name': 'Uncle Chips', 'price': 30}, 'c': {'name': 'Doritos', 'price': 40}}},
#         '2': {'name': 'Beverages', 'items': {'a': {'name': 'Coke', 'price': 50}, 'b': {'name': 'Pepsi', 'price': 45}, 'c': {'name': 'Sprite', 'price': 40}}},
#         '3': {'name': 'Chocolates', 'items': {'a': {'name': 'Dairy Milk', 'price': 40}, 'b': {'name': 'KitKat', 'price': 30}, 'c': {'name': 'Munch', 'price': 20}}}
#     }

#     total_bill = 0
#     dispatched_items = []

#     while True:
#         print("\n--- Select a Tray ---")
#         for tray_num, tray_data in trays.items():
#             print(f"{tray_num}: {tray_data['name']}")
#         print("0: Exit")

#         tray_choice = input("Enter your tray choice (1, 2, 3, or 0 to exit): ").strip()

#         if tray_choice == '0':
#             break
#         elif tray_choice in trays:
#             current_tray_name = trays[tray_choice]['name']
#             current_tray_items = trays[tray_choice]['items']

#             while True:
#                 display_tray(current_tray_name, current_tray_items)
#                 item_choice = input(f"Choose an item from {current_tray_name} (a, b, c) or 'back' to choose another tray: ").strip().lower()

#                 if item_choice == 'back':
#                     break
#                 elif item_choice in current_tray_items:
#                     selected_item = current_tray_items[item_choice]
#                     total_bill += selected_item['price']
#                     dispatched_items.append(selected_item['name'])
#                     print(f"Added {selected_item['name']} to your cart. Current bill: Rs.{total_bill}")
#                 else:
#                     print("Invalid item choice. Please try again.")

#                 continue_tray = input("Do you want to select another item from this tray? (y/n): ").strip().lower()
#                 if continue_tray != 'y':
#                     break
#         else:
#             print("Invalid tray choice. Please try again.")

#     print("\n--- Transaction Summary ---")
#     print(f"Total Bill Amount: Rs.{total_bill}")
#     if dispatched_items:
#         print("Items Dispatched:")
#         for item in dispatched_items:
#             print(f"- {item}")
#     else:
#         print("No items were purchased.")
#     print("Thank you for using the vending machine!")

# # Run the vending machine
# vending_machine()


