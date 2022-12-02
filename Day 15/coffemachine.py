MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_status(res):
    for key, value in res.items():
        # print(key.capitalize(), ": ", key == "water" or key == "milk" ? value + "ml": value)
        print(
            key.capitalize(), ": ", str(value) + "ml"
        ) if key == "water" or key == "milk" else print(key.capitalize(), ": ", value)
    print("\n")


def calculate_resources(res, menu, u_input):
    """Will calculate the remaining resources after making a coffe and save them to the
    dictonary"""
    for key, value in menu[u_input]["ingredients"].items():
        if res.get(key) >= value:
            quarters = float(input("How many quarters?: ")) * 0.25
            dimes = float(input("How many dimes?: ")) * 0.10
            nickles = float(input("How many nickles?: ")) * 0.05
            pennies = float(input("How many pennies?: ")) * 0.01
            money = quarters + dimes + nickles + pennies
            if money > menu[u_input]["cost"]:
                res["money"] = res["money"] + menu[u_input]["cost"]
                change = money - menu[u_input]["cost"]
                print(f"Here is your {u_input}")
                print(f"Here is your change ${change}")
                for keys, values in menu[u_input]["ingredients"].items():
                    res[keys] = res.get(keys) - values
                break
            else:
                print("Not enough money.")
                break

        else:
            print(f"Insufficient resources. You don't have enough {key}")
            break


while True:
    user_input = input(
        "What would you like? (espresso/latte/cappuccino/report/exit): "
    ).lower()
    if user_input == "report":
        check_status(resources)
        continue
    elif user_input == "espresso":
        calculate_resources(resources, MENU, user_input)
        continue
    elif user_input == "latte":
        calculate_resources(resources, MENU, user_input)
        continue
    elif user_input == "cappuccino":
        calculate_resources(resources, MENU, user_input)
        continue
    elif user_input == "exit":
        break
    else:
        print("===== Unkown command =====")
        continue
