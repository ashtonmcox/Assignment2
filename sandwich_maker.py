
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, ingredients_needed in ingredients.items():
            if self.machine_resources[ingredient] < ingredients_needed:
                print("Sorry there is not enough " + ingredient)
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, ingredients_needed in order_ingredients.items():
            self.machine_resources[ingredient] -= ingredients_needed
        print(sandwich_size + " sandwich is ready. Bon appetit!")