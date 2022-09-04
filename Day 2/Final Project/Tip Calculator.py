print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip_per = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
num_of_people = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round((total + total * tip_per) / num_of_people, 2)}")
