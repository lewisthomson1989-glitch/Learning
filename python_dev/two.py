import csv

filename = "themis.csv"
with open(f"csv_read_write/{filename}", 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  
    column_index = header.index('debtorspostcode') 

    postcode = [row[column_index] for row in reader]
   
record = print(f"Record 5's postcode is: {postcode[4]}")

record_number = 5

with open(f"csv_read_write/{filename}", 'r') as file:
    csv_reader = csv.reader(file)
    for index, row in enumerate(csv_reader):
        if index == record_number:
            print(row) 
            break