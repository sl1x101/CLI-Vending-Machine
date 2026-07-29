#main program

#water price 
water_price = {
    "1":("coca-cola",25),
    "2":("coco",20),
    "3":("water",10),
    "4":("Green Tea",20),
    "5":("Coffee",25)
}

money = 0

def show_menu ():

    list_menu = ["1 Insert Money","2 Buy Water","3 Return Change","4 Exit"]
    print("\n === Vending Machine === ")
    #for menu list
    for item in list_menu:
        print(f"รายการ: {item}")
    print("="*30)
    
def insert_money ():
    global money
    amount  = int(input("Insert Money: "))
    money += amount
    print(f"current balance : {money} Baht")

def has_enough_money(price):
    global money
    return money >= price

def water_menu():
    #loop show water
    for key,value in water_price.items():
        print(f"{key}. {value[0]} - {value[1]} Baht")

    
def buy_water():
    global money
    print("\n Available Water")
    water_menu()

    item = input("choose: ")

    if item in water_price:
        name , price = water_price[item]

        if has_enough_money(price):
            money-= price
            print(f"\nDispensing {name}...")
            print("Enjoy your water! ") 
            print(f"Remaining balance: {money} Bath")
        else:
            print("Not enough money....")

    else:
        print("Invalid selection. ")


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
        else:
            print("ไม่มีอันไหนตรงเงื่อนไข")


if __name__ == "__main__":
    main()