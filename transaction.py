def automated_transaction():
    cents = int(input("Enter the money in cents: "))
    dollars = 0
    quaters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    cents_left = 0
    #checking if cents is greater than 100
    if cents >= 100:
        #dollars in cents
        dollars = cents // 100
        #cents left after dollars converted
        cents_left = cents % 100
    if cents:
        #if cents is greater than 25 but less than 100 e.g 35
        if cents >=25 and cents < 100:
            quaters = 1
            cents_left = cents % 25    
        if cents_left >= 25:
        #quaters in cents
            quaters = cents_left // 25
        #cents left
            cents_left %= 25
        # if cents is greater than 25 but less than 100 e.g 99 cents
        if cents >= 25 and cents < 100:
            quaters = cents // 25
        #cents left
            cents_left = cents % 25
    if cents:
        if cents >=10 and cents < 25:
            dimes = 1
            cents_left = cents % 10
        if cents_left >= 10:
        #dimes in cents
            dimes = cents_left // 10
        #cents left
            cents_left %= 10
    if cents:
        if cents >= 5 and cents < 10:
            nickels = 1
            cents_left = cents % 5
        if cents_left >=5:
        #nickels in cents
            nickels = cents_left // 5
        #cents left
            cents_left %= 5
    if cents_left >= 1:
        #pennies in cents
        pennies = cents_left
    if cents >= 1 and cents < 5:
        pennies = cents
    print(f"{dollars}d {quaters}q {dimes}d {nickels}n {pennies}p")
automated_transaction()
