#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.\n")
bill_total = float(input("What was the total bill? \n"))
bill_total2 = float(round(bill_total, 2))
tip_percentage = float(input("What percentage tip would you like to give? \n"))
tip_percentage2 = float((tip_percentage) / 100)
tip_percent_print = int(tip_percentage2 * 100)
total_with_tip = (tip_percentage2 + 1) * bill_total2
people_split = input("how many people split the bill? \n")
people_split2 = float(people_split)
bill_per_person = round(total_with_tip / people_split2, 2)
print(
    f"The total bill is ${bill_total2}, the percentage we would like to give is {tip_percent_print} %, {people_split} people split the bill, the bill per person is ${bill_per_person}"
)
