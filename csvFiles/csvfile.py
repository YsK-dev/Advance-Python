import csv

with open("/home/ysk/Desktop/advancePython/csvFiles/p.csv") as file:
    csvReader = csv.reader(file)
    lists = list(csvReader)

    if len(lists) > 1:
        print(lists[1])  # Safe to access the second row
    else:
        print("Not enough rows in the CSV file.")

    #next(csvReader)
    #for i in csvReader:
        #print(i[0])
# DictReader
with open("/home/ysk/Desktop/advancePython/csvFiles/p.csv") as file:
    csvDictReader =csv.DictReader(file,delimiter =",")
    for i in csvDictReader:
        if i["Category"] == "Electronics" and int(i["Stock"])>220:
            print(i["ProductName"],i["Price"])
    #print(list(csvDictReader))