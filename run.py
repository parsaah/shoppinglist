import csv

QUIT_WORDS = ("quit", "exit", "q", "ex")
my_products = list()

class Product:
    def __init__(self, id, name, price, category, quantity):
        self.id = id
        self.name = name
        self.price = int(price)
        self.category = category
        self.quantity = int(quantity)

    def __repr__(self) -> str:
        return f"product :{self.name}, price :{self.price}, quantity : {self.quantity}"


with open('product.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        product = Product(*row)
        my_products.append(product)


class Basket:
    basket = list()

    def add_to_basket(self, my_products, user_input):
        for product in my_products:
            if user_input in product.name:
                if product.quantity == 0:
                    print("The product you want is out of stock")
                    break
                else:
                    self.basket.append(product)
                    product.quantity -= 1
                    print(f"{user_input} added in your basket, total product : {len(self.basket)}")
                    break
        else:
            print("The product you want is not available in the shop")

    def show_the_basket(self):
        if len(self.basket) == 0:
            print("Your basket is empty")
        else:
            print("Your basket :")
            for product in self.basket:
                print(product.name)

    def search_in_basket(self):
        if len(self.basket) == 0:
            print("Your basket is empty")
        else:
            searched_product = input("Enter a product ? ")
            for product in self.basket:
                if searched_product in product.name:
                    print(f"{searched_product} in your basket")
                else:
                    print(f"{searched_product} does not exist in your basket")

    def move_product(self):
        if len(self.basket) == 0:
            print("Your basket is empty")
        else:
            moved_product = input("which?")
            cel = int(input("where?"))
            for product in self.basket:
                if moved_product in product.name:
                    self.basket.remove(product)
                    self.basket.insert(cel-1, product)
                    print(f"{moved_product} moved to cel{cel}")
                    break
            else:
                print(f"{moved_product} does not exist in your basket")

    def Calculate_the_price(self):
        total_price = sum(product.price for product in self.basket)
        print(f"total price : {total_price} $")

    def remove_from_basket(self):
        if len(self.basket) == 0:
            print("Your basket is empty")
        else:
            removed_product = input("Which product ? ")
            for product in self.basket:
                if removed_product in product.name:
                    self.basket.remove(product)
                    print(f"{removed_product} removed from basket")
                else:
                    print(f"{removed_product} does not exist in your basket")

    def remove_all_basket(self):
        if len(self.basket) == 0:
            print("Your basket is empty")
        else:
            self.basket.clear()
            print("All product in your basket have been deleted")

    def pay(self):
        if len(self.basket) == 0:
            print("Your basket is empty")
        else:
            self.show_the_basket()
            self.Calculate_the_price()
            get_pay = input("For pay write paid : ")
            if get_pay == "paid":
                self.show_the_basket()
                self.Calculate_the_price()
                print("Payment successfully completed")
                print("Thank you for your purchase, hope to see you again")
                return True
            else:
                print("Payment is broken")


def help():
    print(f"You can use the words {QUIT_WORDS} to exit")
    print("You can enter 'show' to see your list")
    print("You can enter 'remove' to remove an item")
    print("You can enter 'removeall' to remove all item")
    print("You can enter 'search' to search an item")
    print("You can enter 'movement' to movement an item")
    print("You can enter 'pay' to pay")


user_basket = Basket()

while True:
    print(my_products)
    user_input = input("Enter your product to add, or enter your request :").lower()

    if user_input in QUIT_WORDS:
        user_basket.show_the_basket()
        break

    elif user_input in user_basket.basket:
        print("This product is already in your basket")

    elif user_input == "show":
        user_basket.show_the_basket()
        user_basket.Calculate_the_price()

    elif user_input == "search":
        user_basket.search_in_basket()

    elif user_input == "movement":
        user_basket.move_product()

    elif user_input == "remove":
        user_basket.remove_from_basket()

    elif user_input == "removeall":
        user_basket.remove_all_basket()

    elif user_input == "pay":
        if user_basket.pay() == True:
            with open('product.csv', mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows([header])
                for product in my_products:
                    writer.writerows([(product.id,product.name,product.price,product.category,product.quantity)])
            break

    else:
        user_basket.add_to_basket(my_products, user_input)
        user_basket.Calculate_the_price()


