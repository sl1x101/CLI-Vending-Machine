#main program

#water price 
water_price = {
    "1":("coca-cola",25),
    "2":("coco",20),
    "3":("water",10),
    "4":("Green Tea",20),
    "5":("Coffee",25)
}

money = 10

def show_menu ():

    list_menu = ["1 Insert Money","2 Buy Water","3 Return Change","4 Exit"]
    print("\n === Vending Machine === ")
    #for menu list
    for item in list_menu:
        print(f"รายการ: {item}")
    print("="*30)
    
def insert_money ():
    amount  = int(input("Insert Money: "))
    money += amount
    print(f"current balance : {money} Baht")
    
def buy_water():
    print("\n Available Water")

    #loop show water
    for key,value in water_price.items():
        print(f"{key}. {value[0]} - {value[1]} Baht")

    item = input("choose: ")

    if item in water_price:
        name , price = water_price[item]

        if money >= price:
            money-= price
            print(f"\nDispensing {name}...")
            print("Enjoy your water! ") 
            print(f"Remaining balance: {money} Bath")
        else:
            print("Not enough money....")

    else:
        print("Invalid selection. ")


def return_chang ():
    print(f"Returned {money} Baht")
    money = 0

def main ():
    show_menu()
    



if __name__ == "__main__":
    main()