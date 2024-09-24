import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance =Cashier()




def main():
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        if choice in recipes:
            check_resources = sandwich_maker_instance.check_resources(recipes[choice]["ingredients"])
            if check_resources:
                coins = cashier_instance.process_coins()
                payment = cashier_instance.transaction_result(coins, recipes[choice]["cost"])
                if payment:
                    sandwich_maker_instance.make_sandwich(choice, recipes[choice]["ingredients"])
                    print()

        elif choice == "off":
            print("shutting off")
            break
        elif choice == "report":
            print("Bread: " + str(sandwich_maker_instance.machine_resources["bread"]) + " slice(s)")
            print("Ham: " + str(sandwich_maker_instance.machine_resources["ham"]) + " slice(s)")
            print("Cheese: " + str(sandwich_maker_instance.machine_resources["cheese"]) + " slice(s)")
        else:
            print("invalid choice")


if __name__=="__main__":
    main()
