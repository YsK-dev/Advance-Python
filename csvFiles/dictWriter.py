import csv


with open("new-procts.csv","w") as file:
    headers =["pID","PRişko","CATEGORY","PRICE","STOCK","DESCRIPTION"]
    csvWriter = csv.DictWriter(file, headers)
    csvWriter.writeheader()
    # csvWriter.writerow(
    #     {"pID":"Rks",
    #      "PRişko":"125",
    #      "CATEGORY":"motor",
    #      "PRICE":"10032",
    #      "STOCK":"300",
    #      "DESCRIPTION":"Fast and furious"
    #       }
    # )
    # csvWriter.writerow(
    #     {"pID":"HONDA",
    #      "PRişko":"125",
    #      "CATEGORY":"motor",
    #      "PRICE":"154540032",
    #      "STOCK":"30",
    #      "DESCRIPTION":"MOney,Fast and furious"
    #       })
    
    csvWriter.writerows(
        [{"pID":"tws",
         "PRişko":"125",
         "CATEGORY":"motor",
         "PRICE":"1454032",
         "STOCK":"320",
         "DESCRIPTION":"Fast and furious"
          },
           {"pID":"YAMAHA",
         "PRişko":"125",
         "CATEGORY":"motor",
         "PRICE":"19540032",
         "STOCK":"20",
         "DESCRIPTION":"MOney,Fast and furious"
          }


        ])



