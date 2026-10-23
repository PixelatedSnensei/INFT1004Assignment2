

BALLSMAX = 30
RACKETSMAX = 20
BIKESMAX = 15
TENTSMAX = 25


hi iiii

stockMax = {"balls": 20, "rackets": 20, "bikes": 15, "tents": 25}
stockCurrent = {"balls": 0, "rackets": 0, "bikes": 0, "tents": 0}
stockHired = {"balls": 0, "rackets": 0, "bikes": 0, "tents": 0}
stockLoaned = {"balls": 0, "rackets": 0, "bikes": 0, "tents": 0}

def main():
    stockInitial = open("HireInventory.csv", "r")
    
    while True:
        menuDisplay()
        command = input("What would you like to do?: ").strip().lower()
        if command == "help!":
            continue
        elif command == "stock":
            print("\n")
            for key, value in stockCurrent.items():
                print(f'{key}: {value}')
        elif command == "hire":
            print("\n")
            () = hireItem()
        elif command == "return":
            print("\n")
            (
                ballsCurrent,
                racketsCurrent,
                bikesCurrent,
                tentsCurrent,
                ballsLoaned,
                racketsLoaned,
                bikesLoaned,
                tentsLoaned,
            ) = returnItem(
                ballsCurrent,
                racketsCurrent,
                bikesCurrent,
                tentsCurrent,
                ballsLoaned,
                racketsLoaned,
                bikesLoaned,
                tentsLoaned,
            )
        elif command == "restock":
            print("\n")
            ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent = (
                restockItem(
                    ballsCurrent,
                    racketsCurrent,
                    bikesCurrent,
                    tentsCurrent,
                    ballsLoaned,
                    racketsLoaned,
                    bikesLoaned,
                    tentsLoaned,
                )
            )
        elif command == "hired":
            print("\n")
            displayHired(ballsHired, racketsHired, bikesHired, tentsHired)
        elif command == "exit":
            print("\n")
            print("Thank you, bye!")
            return
        else:
            print("\n")
            print("Error: invalid command")


def hireItem(
    ballsCurrent,
    racketsCurrent,
    bikesCurrent,
    tentsCurrent,
    ballsLoaned,
    racketsLoaned,
    bikesLoaned,
    tentsLoaned,
    ballsHired,
    racketsHired,
    bikesHired,
    tentsHired,
):
    item = (
        itemTaker(
            "What item would you like to hire?: "
        )
    )
    if item == "balls":
        if ballsCurrent == 0:
            print(f"Error: there are no {item} in stock")
        else:
            ballsCurrent -= 1
            ballsHired += 1
            ballsLoaned += 1
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        print("Successfully hired!")
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
            ballsHired,
            racketsHired,
            bikesHired,
            tentsHired,
        )
    elif item == "rackets":
        if racketsCurrent == 0:
            print(f"Error: there are no {item} in stock")
        else:
            racketsCurrent -= 1
            racketsHired += 1
            racketsLoaned += 1
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        print("Successfully hired!")
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
            ballsHired,
            racketsHired,
            bikesHired,
            tentsHired,
        )
    elif item == "bikes":
        if bikesCurrent == 0:
            print(f"Error: there are no {item} in stock")
        else:
            bikesCurrent -= 1
            bikesHired += 1
            bikesLoaned += 1
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        print("Successfully hired!")
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
            ballsHired,
            racketsHired,
            bikesHired,
            tentsHired,
        )
    elif item == "tents":
        if tentsCurrent == 0:
            print(f"Error: there are no {item} in stock")
        else:
            tentsCurrent -= 1
            tentsHired += 1
            tentsLoaned += 1
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        print("Successfully hired!")
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
            ballsHired,
            racketsHired,
            bikesHired,
            tentsHired,
        )


def returnItem(
    ballsCurrent,
    racketsCurrent,
    bikesCurrent,
    tentsCurrent,
    ballsLoaned,
    racketsLoaned,
    bikesLoaned,
    tentsLoaned,
):
    item = itemTaker(
        "What item would you like to return?: "
    )
    if item == "balls":
        if ballsLoaned == 0:
            print(f"Error: all {item} are back at the hire desk")
        else:
            ballsCurrent += 1
            ballsLoaned -= 1
            print("\n")
            print("Successfully returned!")
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
        )
    elif item == "rackets":
        if racketsLoaned == 0:
            print(f"Error: all {item} are back at the hire desk")
        else:
            racketsCurrent += 1
            racketsLoaned -= 1
            print("\n")
            print("Successfully returned!")
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
        )
    elif item == "bikes":
        if bikesLoaned == 0:
            print(f"Error: all {item} are back at the hire desk")
        else:
            bikesCurrent += 1
            bikesLoaned -= 1
            print("\n")
            print("Successfully returned!")
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
        )
    elif item == "tents":
        if tentsLoaned == 0:
            print(f"Error: all {item} are back at the hire desk")
        else:
            tentsCurrent += 1
            tentsLoaned -= 1
            print("\n")
            print("Successfully returned!")
            displayCurrent(
                ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
            )
        return (
            ballsCurrent,
            racketsCurrent,
            bikesCurrent,
            tentsCurrent,
            ballsLoaned,
            racketsLoaned,
            bikesLoaned,
            tentsLoaned,
        )


def restockItem(
    ballsCurrent,
    racketsCurrent,
    bikesCurrent,
    tentsCurrent,
    ballsLoaned,
    racketsLoaned,
    bikesLoaned,
    tentsLoaned,
):
    displayCurrent(ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent)
    restockCapacity = BALLSMAX - ballsCurrent - ballsLoaned
    if restockCapacity == 0:
        print("Balls are already at maximum capacity")
    else:
        print(
            f"Restock {restockCapacity} balls to reach maximum capacity"
        )
        quantity = quantityTaker(
            "How many balls would you like to restock?: ", 0, restockCapacity
        )
        ballsCurrent += quantity
    restockCapacity = RACKETSMAX - racketsCurrent - racketsLoaned
    if restockCapacity == 0:
        print("Rackets are already at maximum capacity")
    else:
        print(f"Restock {restockCapacity} rackets to reach maximum capacity")
        quantity = quantityTaker(
            "How many rackets would you like to restock?: ", 0, restockCapacity
        )
        racketsCurrent += quantity
    restockCapacity = BIKESMAX - bikesCurrent - bikesLoaned
    if restockCapacity == 0:
        print("Bikes are already at maximum capacity")
    else:
        print(f"Restock {restockCapacity} bikes to reach maximum capacity")
        quantity = quantityTaker(
            "How many bikes would you like to restock?: ", 0, restockCapacity
        )
        bikesCurrent += quantity
    restockCapacity = TENTSMAX - tentsCurrent - tentsLoaned
    if restockCapacity == 0:
        print("Tents are already at maximum capacity")
    else:
        print(f"Restock {restockCapacity} tents to reach maximum capacity")
        quantity = quantityTaker(
            "How many tents would you like to restock?: ", 0, restockCapacity
        )
        tentsCurrent += quantity
    print("\n")
    print("Successfully restocked!")
    displayCurrent(
        ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
    )
    return ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent


def displayHired(
    ballsHired, racketsHired, bikesHired, tentsHired
):
    print(
        f"Total hires this session: \n"
        f"balls = {ballsHired} \n"
        f"rackets = {racketsHired} \n"
        f"bikes = {bikesHired} \n"
        f"tents = {tentsHired}"
    )


def initialise_inventory():
    while True:
        balls = quantityTaker(
            "Input starting number of balls: ", 0, BALLSMAX
        )
        rackets = quantityTaker(
            "Input starting number of rackets: ", 0, RACKETSMAX
        )
        bikes = quantityTaker("Input starting number of bikes: ", 0, BIKESMAX)
        tents = quantityTaker("Input starting number of tents: ", 0, TENTSMAX)
        if check_inventory_limit(
            balls, rackets, bikes, tents
        ):
            return (
                balls,
                rackets,
                bikes,
                tents,
            )
        print("Error: each amount must be between 0 and its maximum")


def check_inventory_limit(
    balls, rackets, bikes, tents
):
    if balls < 0 or balls > BALLSMAX:
        return False
    if rackets < 0 or rackets > RACKETSMAX:
        return False
    if bikes < 0 or bikes > BIKESMAX:
        return False
    if tents < 0 or tents > TENTSMAX:
        return False
    return True


def itemTaker(
    prompt,
):
    while True:
        item = input(prompt).strip().lower()
        if (
            item != "balls"
            and item != "rackets"
            and item != "bikes"
            and item != "tents"
        ):
            print("Error: must be balls, rackets, bikes, or tents")
            continue
        return item


def quantityTaker(
    prompt, low, high
):
    while True:
        try:
            quantity = int(input(prompt).strip().lower())
        except ValueError:
            print(f"Error: must be an integer between {low} and {high}")
            continue
        if not (low <= quantity <= high):
            print(f"Error: must be an integer between {low} and {high}")
            continue
        return quantity


def displayCurrent(
    ballsCurrent, racketsCurrent, bikesCurrent, tentsCurrent
):
    percentBalls = (
        ballsCurrent / BALLSMAX
    )
    percentRackets = racketsCurrent / RACKETSMAX
    percentBikes = bikesCurrent / BIKESMAX
    percentTents = tentsCurrent / TENTSMAX
    print(
        f"Balls: {ballsCurrent}/{BALLSMAX} - {percentBalls:.0%} - Status: {statusCheck(percentBalls)}"
    )
    print(
        f"Rackets: {racketsCurrent}/{RACKETSMAX} - {percentRackets:.0%} - Status: {statusCheck(percentRackets)}"
    )
    print(
        f"Bikes: {bikesCurrent}/{BIKESMAX} - {percentBikes:.0%} - Status: {statusCheck(percentBikes)}"
    )
    print(
        f"Tents: {tentsCurrent}/{TENTSMAX} - {percentTents:.0%} - Status: {statusCheck(percentTents)}"
    )


def statusCheck(
    percent,
):
    if percent < 0.50:
        return "Low"
    elif percent < 0.75:
        return "OK"
    elif percent <= 1.00:
        return "High"


def menuDisplay():
    print(
        "\n"
        "1. help! = see the list of commands \n"
        "2. stock = see the current stock of equipment \n"
        "3. hire = hire out an item \n"
        "4. return = return an item \n"
        "5. restock = add new items back to the current stock \n"
        "6. hired = see how many times each item has been hired \n"
        "7. exit = exit the program"
        "\n"
    )


main()
