import os
import csv

filename = "themis.csv"
with open(f"csv_read_write/{filename}", 'r') as file:
        first_line = file.readline().strip()
        postcode = first_line.split(",")
        print(postcode[7])        


with open(f"csv_read_write/{filename}", 'r') as file:
        record = csv.DictReader(file) 
        for row in record:
            postcode = print(row["debtorspostcode"])
            
