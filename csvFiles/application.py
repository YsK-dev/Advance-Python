import csv
with open("data.csv") as file:
    csvReader = csv.reader(file)
    listf=list(csvReader)
    print(len(listf)-1)

# with open("data.csv") as file:
#      csvReader = csv.reader(file)
#      colourBlack = len([row for row in csvReader if row["color"] == "Black"])
#     # print(colourBlack)


with open("data.csv", mode="r", newline='') as file:
    csvReader = csv.DictReader(file)
    cheap_products = [row for row in csvReader if int(row["offer_price"]) < 2000]
    
    for product in cheap_products:
        print(f"{product['brand']} - {product['color']} - {product['offer_price']}")
 

with open("data.csv", mode="r", newline='') as file:
    csvReader = csv.DictReader(file)
    offer_prices = [int(row["offer_price"]) for row in csvReader]
    average_price = sum(offer_prices) / len(offer_prices)
    print(f"Average offer price: {average_price:.2f}")



with open("data.csv", mode="r", newline='') as file:
    csvReader = csv.DictReader(file)
    crocs_products = [row for row in csvReader if row["brand"] == "Crocs"]
    
    for product in crocs_products:
        print(f"{product['brand']} - {product['color']} - Size: {product['size']} - Offer Price: {product['offer_price']}")
