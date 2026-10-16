import csv

totals = {}

with open("transactions.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        category = row["category"]
        amount = float(row["amount"])
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

print("Spending by category")
print("--------------------")
for category, total in totals.items():
    print(f"{category}: {total:.2f}")