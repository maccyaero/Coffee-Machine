# TODO:Ask the user which coffee do they want
#   Import coffee dictionary file
#   Search the inout in dictionary to get the details of the required coffee

# TODO: Take Money from User
#   Prompt user for how many quarter, nickels, dimes and pennies they have
#   Make Constants for all the coin values
#   Make Variables for all coin amounts
#   Using Constants and variables calculate how much money user has put in
#   If the Price is more than input value refund the money and restart the program.
#   If the price is less than equal to input value calculate change and give back.

# TODO: Calculate amount of resources left after each purchase.
#   if ingredients required are met then subtract the amount of ingredients from resources
#   if the ingredients required are not met then refund the money and end the program
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def main():
    import MENU
    import constant

    def sum_up_coins(quarters_amount, dimes_amount, nickels_amount, pennies_amount):
        cash_paid = (pennies_amount * constant.penny) + (dimes_amount * constant.dime) + \
                    (nickels_amount * constant.nickel) + (quarters_amount * constant.quarter)
        return cash_paid

    def do_we_have_enough_resources(water, milk, coffee_beans):
        remaining_water = resources["water"] - water
        remaining_milk = resources["milk"] - milk
        remaining_coffee = resources["coffee"] - coffee_beans
        if remaining_water < 0:
            print("ERR: Ran out of water")
        if remaining_milk < 0:
            print("ERR: Ran out of milk")
        if remaining_coffee < 0:
            print("ERR: Ran out of coffee beans")
        if remaining_milk < 0 or remaining_coffee < 0 or remaining_water < 0:
            return False
        else:
            return True

    def update_resources_left(water, milk, coffee_beans):
        """Takes the amount required to make a beverage and returns whether possible to make it."""
        remaining_water = resources["water"] - water
        resources["water"] = remaining_water
        remaining_milk = resources["milk"] - milk
        resources["milk"] = remaining_milk
        remaining_coffee = resources["coffee"] - coffee_beans
        resources["coffee"] = remaining_coffee

    def print_report():
        water_left = resources["water"]
        milk_left = resources["milk"]
        coffee_left = resources["coffee"]
        print(f"Water: {water_left}")
        print(f"Milk: {milk_left}")
        print(f"Coffee: {coffee_left}")

    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "report":
        print_report()
        main()
    price = MENU.MENU[coffee]["cost"]
    water_required = MENU.MENU[coffee]["ingredients"]["water"]
    milk_required = MENU.MENU[coffee]["ingredients"]["milk"]
    coffee__required = MENU.MENU[coffee]["ingredients"]["coffee"]
    print("Please insert coins.")
    no_of_quarters = float(input("how many quarters?"))
    no_of_dimes = float(input("how many dimes?"))
    no_of_nickels = float(input("how many nickels?"))
    no_of_pennies = float(input("how many pennies?\n"))
    amount_paid = sum_up_coins(no_of_quarters, no_of_dimes, no_of_nickels, no_of_pennies)
    enough_resources = do_we_have_enough_resources(water_required, milk_required, coffee__required)
    if amount_paid > price and enough_resources:
        change = round(amount_paid - price, 2)
        update_resources_left(water_required, milk_required, coffee__required)
        print(f"Here is your coffee and change of ${change}")
        main()
    elif not enough_resources:
        print("Sorry please ask reception for a refill.")
    else:
        print(f"The cash paid is not enough, {amount_paid} refunded")
        main()


main()
