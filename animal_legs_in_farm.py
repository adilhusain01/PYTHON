def calculate_total_legs(chickens, cows, pigs):
    chicken_legs = 2 * chickens
    cow_legs = 4 * cows
    pig_legs = 4 * pigs

    total_legs = chicken_legs + cow_legs + pig_legs

    return total_legs

chickens = int(input("Enter the number of chickens: "))
cows = int(input("Enter the number of cows: "))
pigs = int(input("Enter the number of pigs: "))

total_legs = calculate_total_legs(chickens, cows, pigs)

print(f"The total number of legs for {chickens} chickens, {cows} cows, and {pigs} pigs is: {total_legs}")
