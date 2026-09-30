
Initial_conditions = {
    "coffee": 100,
    "water": 300,
    "milk":300,
    "money": 0
}

coffe_costs = {
    "latte": 2.50,
    "espresso": 1.50,
    "cappucino": 3.00
}
recepies = {
    "latte": {
        "required_coffee": 24,
        "required_water": 250,
        "required_milk": 150
    },
    "espresso": {
        "required_coffee": 18,
        "required_water": 50,
        "required_milk": 0 
    },
    "cappucino": {
        "required_coffee": 24,
        "required_water": 250,
        "required_milk": 100 
    }
}

def check_for_materials(what_the_user_wanted):
    if Initial_conditions["coffee"] < recepies[what_the_user_wanted]["required_coffee"]:
        print(f"Amount of coffee insufficient, sorry for the incovenience")
        return  False
    elif Initial_conditions["milk"] < recepies[what_the_user_wanted]["required_milk"]:
        print(f"Amount of milk unsufficient, sorry for the incovenience")
        return  False
    elif Initial_conditions["water"] < recepies[what_the_user_wanted]["required_water"]:
        print(f"Amount of water insufficient, sorry for the incovenience")
        return  False
    
def money_check(current_money , choice_of_beverage):
        if current_money > coffe_costs[choice_of_beverage]:
            amount_to_be_refunded = current_money - coffe_costs[choice_of_beverage]
            Initial_conditions["money"] += coffe_costs[choice_of_beverage]
            print(f"You have overpaid!, here is you're change of {amount_to_be_refunded}€")
            return True
        elif current_money < coffe_costs[choice_of_beverage]:
            print(f"You do not have enough money for {choice_of_beverage}")
            return False

def modify_materials(choice_of_beverage):
    Initial_conditions["coffee"] -= recepies[choice_of_beverage]["required_coffee"]
    Initial_conditions["milk"] -= recepies[choice_of_beverage]["required_milk"]
    Initial_conditions["water"] -= recepies[choice_of_beverage]["required_water"]
    return Initial_conditions
"""
    Recepies for the coffes

    Latte:
    250 g water
    150 ml milk
    24 g coffe
    Espresso:
    50 ml water
    18 g coffe
    Cappucino:
    250 ml water
    100 ml milk
    24 g Coffe
"""

def coffe_machine():
    machine_work = True
    while machine_work != False:
        user_choice = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
        if user_choice == "off":
            machine_work = False
            return machine_work
        elif user_choice == "report":
            print(f"Water: {Initial_conditions['water']}ml\nMilk: {Initial_conditions['milk']}ml\nCoffee: {Initial_conditions['coffee']}g\nMoney: {Initial_conditions['money']}€")
  
        else:     
            status_materials = check_for_materials(user_choice)
            if status_materials is False:
                return
            else:
                num_1e = int(input("Number of 1 euro's you would like to deposit: "))
                num_2e = int(input("Number of 2 euro's you would like to deposit: ")) * 2
                num_050e = int(input("Number of 0.50 euro's you would like to deposit: ")) * 0.50
                num_020e = int(input("Number of 0.20 euro's you would like to deposit: ")) * 0.20                        
                num_010e = int(input("Number of 0.10 euro's you would like to deposit: ")) * 0.10
                current_money = num_1e + num_2e + num_050e + num_020e + num_010e
                status_money = money_check(current_money , user_choice)
                if status_money is False:
                    Initial_conditions["money"] -= current_money
                    return
                elif status_money is True:
                    modify_materials(user_choice)
                    print(f"Here is your {user_choice}, Enjoy!")
         # WIll come back whe return function is implemented
                




coffe_machine()                    