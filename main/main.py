#water price 
products = {
    "1":("coca-cola",25),
    "2":("coco",20),
    "3":("water",10),
    "4":("Green Tea",20),
    "5":("Coffee",25)
}

money = 0

def show_menu ():

    list_menu = ["1 Insert Money","2 Buy Water","3 Return Change","4 Exit","5.Show Balance"]
    print("\n === Vending Machine === ")
    #for menu list
    for item in list_menu:
        print(f"รายการ: {item}")
    print("="*30)
    
def insert_money ():
    global money
    try:
        amount  = int(input("Insert Money: "))
    except ValueError:
        print("please enter a number.")
        return
    if amount <= 0 :
        print("Invalid amount...")
        return
    
    money += amount
    show_balance()

def has_enough_money(price):
    return money >= price


def dispense_item(name,price):
    global money
    money -= price
    print(f"Dispensing {name}")


def water_menu():
    #loop show water
    for key,value in products.items():
        print(f"{key}. {value[0]} - {value[1]} Baht")

    
def buy_water():
    global money
    print("\n Available Water")
    water_menu()

    item = input("choose: ")

    if item in products:
        name , price = products[item]

        if has_enough_money(price):
            dispense_item(name,price)
            print("Enjoy your water! ") 
            show_balance()
        else:
            print("Not enough money....")

    else:
        print("Invalid selection. ")


def show_balance():
    print(f"Current balance {money} Baht")

def return_money ():
    global money
    print(f"Returned {money} Baht")
    money = 0

def main ():
    while True:
        show_menu()
        
        try:
            choice = int(input("choice: "))
        except ValueError:
            print("input number....")
            continue

        if choice  == 4:
            print("Exit choice...")
            break
        elif choice  == 1 :
            insert_money()
        elif choice == 2 :
            buy_water()
        elif choice == 3 :
            return_money()
        elif choice == 5:
            show_balance()
        else:
            print("ไม่มีอันไหนตรงเงื่อนไข")


if __name__ == "__main__":
    main()