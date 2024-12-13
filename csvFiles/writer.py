import csv

# with open("/home/ysk/Desktop/advancePython/csvFiles/p.csv","w",newline='') as file:
#     csvWriter = csv.writer(file)
#     # csvWriter.writerow(["Brand","Model"])
#     # csvWriter.writerow(["tws","jupiter"])
#     # csvWriter.writerow(["honda","pcx"])

#     csvWriter.writerows([["Brand","Model"],["tws","jupiter"],["honda","activia"]])

# with open("products","w") as file:
#     csvWriter = csv.writer(file)
#     csvWriter.writerow(["Rks","pcx"])

# with open("products.csv","r") as file:
#     csvReader = csv.reader(file)
#     with open("new-procts.csv",mode="w", newline='') as f:
#         csvWriter = csv.writer(f)
#         for prod in csvReader:
#             csvWriter.writerow([u.upper() for u in prod])   

with open("products.csv","r+") as file:
    csvReader = csv.reader(file)
    csvWriter = csv.writer(file)

    next(csvReader)

    products = [[i[0],i[1],i[2],int(i[3] * 3),i[4]] for i in csvReader]

    file.seek(0)

    csvWriter.writerow(["ProductID","ProductName","Category","Price","Stock","Description"])
    csvWriter.writerows(products)
