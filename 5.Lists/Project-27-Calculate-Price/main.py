available_parts = {
    1: "computer",
    2: "monitor",
    3: "keyboard",
    4: "mouse",
    5: "hdmi cable",
    6: "dvd drive"
}

price_quantity = {
    "computer": {"price": 500, "quantity": 10},
    "monitor": {"price": 200, "quantity": 8},
    "keyboard": {"price": 500, "quantity": 5},
    "mouse": {"price": 10, "quantity": 0},
    "hdmi cable": {"price": 20, "quantity": 7},
    "dvd drive": {"price": 50, "quantity": 5},
}

total_price = 0

while True:
    print("\nPlease add options from the list:")
    for key, value in available_parts.items():
        print(f"{key}: {value}")
    user_choice = input("> ")
    if user_choice == "0":
        break
    elif int(user_choice) in available_parts:
        selected_item = available_parts[int(user_choice)]
        if price_quantity[selected_item]["quantity"] > 0:
            total_price += price_quantity[selected_item]["price"]
            price_quantity[selected_item]["quantity"] -= 1
            print(f"Adding {selected_item}")
        else:
            print(f"{selected_item} is out of stock")
    else:
        print("Invalid input")

print(f"Total price: {total_price}")
