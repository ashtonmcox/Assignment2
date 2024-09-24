class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        dollars = int(input("how many dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        return dollars + .5 * (half_dollars) + .25 * (quarters) + .5 * (nickels)

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        change = float(coins) - float(cost)
        if change < 0:
            print("Sorry, that's not enough money. Money refunded")
            return False
        else:
            print("Here is $" + str(change) + " in change")
            return True
