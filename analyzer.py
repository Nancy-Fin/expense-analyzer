import csv

with open("transactions.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["date"], row["category"], row["amount"])