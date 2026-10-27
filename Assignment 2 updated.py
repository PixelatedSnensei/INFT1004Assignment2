import csv
import sys

def main(): #I have written out all 6 commands that we need to make
    stock, stock_max = load_inventory_from_csv() #Loads the current available stock level and the maximum stock level
    while True:
        menu()
        print()
        command = input("What would you like to do?: ").strip().lower()
        print()
        if command == "1":
            display_current_stock(stock)
        elif command == "2":
            add_new_category(stock, stock_max)
        elif command == "3":
            hire_out_or_return_items(stock, stock_max)
        elif command == "4":
            stock_analysis(stock, stock_max)
        elif command == "5":
            save_changes_to_csv(stock)
        elif command == "6":
            quit(stock)
        else:
            print("Error: invalid command")

def display_current_stock(stock):
    print()
    for key, value in stock:
        print(f"{key}: {value}")

def load_inventory_from_csv():
    stock = {}
    with open("HiredInventory.csv", mode="r", encoding="utf-8") as inventory:
        reader = csv.DictReader(inventory)
        for row in reader:
            stock[row["Category"]] = int(row["Count"])
    stock_max = stock.copy()
    return stock, stock_max

def add_new_category(stock, stock_max):
    while True:
        item = new_item_taker(stock)
        quantity = quantity_taker(None, None)   
        if quantity > 0:
            stock[item] = quantity
            stock_max[item] = quantity
            display_current_stock()
            return stock, stock_max
        print("Error: quantity must be a positive integer")

def hire_out_or_return_items(stock, stock_max):
    display_current_stock()
    action = input("Hire (H) or return (R)?: ").lower()
    if action == "h"
        hire_item(stock, stock_max)
        return stock, stock_max
    elif action == "r"
        return_item(stock)
        return stock
    else:
        print("Error: please type H or R")

def hire_item(stock):
    if sum(stock.values()) == 0: #Checks if there are any items available to hire
        print("Error: no hires available")
        return
    while True:
        item = current_item_taker(stock)
        if stock[item] > 0:
            quantity = quantity_taker()
            if 0 < quantity <= stock[item]:
                stock[item] -= quantity
                print(f"Hired {quantity} {item}. {item} remaining: {stock[item]}")
                return stock
            print(f"Error: quantity must be a positive integer and less than or equal to {stock[item]}")
            continue
        print(f"Error: no {item} available")

def return_item(stock, stock_max):
    while True:
        item = new_item_taker(stock)
        quantity = quantity_taker(1, stock_max[item])
        if quantity > 0:
            stock[item] += quantity
            print(f"Returned{quantity} {item}. {item} remaining: {stock[item]}")
            return stock
        print("Error: quantity must be a positive integer")

def stock_analysis(stock, stock_max):
    print("Stock Analysis:")
    for key, value in stock.items()
        print(f"{key}: {value}/{stock_max[key]} available")
        print()
    total_items = sum(stock.values())
    print(f"Total items available: {total_items}")
    status_check()

def status_check()
    for key, value in stock.items
        decimal = value/stock_max[key]
        if decimal < 0.5:
            status = "Low"
        elif decimal < 0.75:
            status = "OK"
        else:
            status = "High"
        print(f"{key}: {value}/{stock_max[key]} - Status: {status}")
        


def save_changes_to_csv(stock):
    try:
        with open("HiredInventory.csv", mode="w", newline="", encoding="utf-8") as inventory:
                writer = csv.writer(inventory)
                writer.writerow(["Category", "Count"])
                writer.writerows(stock.items)
        print("Changes successfully saved")
    except FileNotFoundError:
        print("File was not found")
    except OSError as error:
        print(f"Error: {error}")

def quit(stock):
    save_changes_to_csv(stock)
    sys.exit("Bye!")           
        

def current_item_taker(stock):
    while True:
        item = input("What item?: ")
        for key in stock:
            if item == key:
                return key
        print(f"Error: item must be one of: \n {'\n'.join(stock)}")

def new_item_taker(stock,): #Takes item and checks if it already exists.
    while True:
        exists = False
        item = input("What item?: ")
        if item == "":
            print("Error: name can not be empty")
            continue
        for key in stock:
            if item == key:
                exists = True
        if exists:
            print(f"Error: {item} already exist")
        else:
            return item
                
def quantity_taker(l):
    while True:
        try:
            quantity = int(input("How many?: ").strip()
        except ValueError:
            print(f"Error: must be a postive integer")
            continue
        return quantity


def menu():
    print(
        "1. Display Current Stock \n"
        "2. Add New Category \n"
        "3. Hire Out or Return Items \n"
        "4. Stock Analysis \n"
        "5. Save Changes to CSV \n"
        "6. Quite \n"
    )


main()
