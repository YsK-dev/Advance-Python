import csv

with open("products.csv") as file:
    csvReader = csv.reader(file)
    print(csvReader)