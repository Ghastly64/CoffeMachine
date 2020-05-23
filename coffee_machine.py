money = 550
water = 400
milk = 540
bean = 120
d_cups = 9


class CoffeeMachine:
    def __init__(self, input1):
        self.input1 = input1

    def input(self, input1):
        self.input1 = input1
        if self.input1 == 'buy':
            buy()
        if self.input1 == 'fill':
            fill()
        if self.input1 == 'take':
            take()
        if self.input1 == 'remaining':
            stats()
        if self.input1 == 'exit':
            exit()


cm = CoffeeMachine(1)


def buy():
    global money
    global water
    global milk
    global bean
    global d_cups
    print("\nWhat type of coffee would you like?")
    cof_type = input(" 1-Espresso, 2-Latte, 3-Cappuccino, back to go to main menu")
    if cof_type == '1':
        if water >= 250 and bean >= 16 and d_cups >= 1:
            print("We have enough resources, here is your Espresso")
            water = water - 250
            bean = bean - 16
            d_cups = d_cups - 1
            money = money + 4
        else:
            print("Sorry the machine needs a restock")
    if cof_type == '2':
        if water >= 350 and bean >= 20 and d_cups >= 1 and milk >= 75:
            print("We have enough resources, here is your Latte")
            water = water - 350
            milk = milk - 75
            bean = bean - 20
            d_cups = d_cups - 1
            money = money + 7
        else:
            print("Sorry the machine needs a restock")
    if cof_type == '3':
        if water >= 200 and bean >= 12 and d_cups >= 1 and milk >= 100:
            print("We have enough resources, here is your Cappuccino")
            water = water - 200
            milk = milk - 100
            bean = bean - 12
            d_cups = d_cups - 1
            money = money + 6
        else:
            print("Sorry the machine needs a restock")
    if cof_type == 'back':
        print("Heading back")


def fill():
    global money
    global water
    global milk
    global bean
    global d_cups
    water_add = input("how many ml of water would you like to add?")
    water = water + int(water_add)
    milk_add = input("how many ml of milk would you like to add?")
    milk = milk + int(milk_add)
    bean_add = input("how many g of coffee beans would you like to add?")
    bean = bean + int(bean_add)
    d_cups_add = input("how many disposable cups would you like to add?")
    d_cups = d_cups + int(d_cups_add)


def take():
    global money
    global water
    global milk
    global bean
    global d_cups
    print("You have taken " + str(money) + " dollars out of the machine")
    money = 0
    print("The coffee machine has: ")


def stats():
    print("The coffee machine has: ")
    print("\n" + str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(bean) + " of coffee beans")
    print(str(d_cups) + " of disposable cups")
    print("$" + str(money) + " of money")


while True:
    xx = input()
    cm.input(xx)
