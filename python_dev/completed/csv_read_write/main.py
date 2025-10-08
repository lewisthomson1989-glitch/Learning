# NOTE: flat file is a text file of any format, eg, log file, most importantly CSV file.
# NOTE: Remember your imports.
from os import read
import csv

def read_file(filename:str, filetype:str) -> list:
    """
    (Richer functionality over os.read(), specifically built for CSV.)
    TODO: Check the filetype. Use the correct library for the correct file.
    TODO: Read from flat text file, using std lib's os.read()
    """
    contents = None
    if filetype == "txt" or filetype == "csv":
        with open(f"{filename}", 'r') as f:

            if filetype == "txt":
                contents = f.read()
            
            elif filetype == "csv":
                contents = []
                records = csv.reader(f)
                for record in records:
                    contents.append(record)
    else:
        print(f"Extension not recognised: {filetype}")
    return contents



def print_text_contents():
    """
    Nothing to do here, just some notes for observability.
    """
    filename = "csv_read_write/walkerlove.txt" # NOTE: Avoid naming a variable "file", it's a keyword in the std lib, and will cause probems.
    contents = read_file(filename, "txt")
    print(contents)
    # No return; remember, keep functions simple, one job per function.

def get_postcode(record:list[str]) -> str:
    """
    TODO: Think about string slicing, you can do it on a list.
    Use field headings row to figure out which field is postcode.
    """
    
#    filename = "themis.csv"
#    with open(f"csv_read_write/{filename}", 'r') as file:
#        reader = csv.reader(file)
#        header = next(reader)
#    postcode = print(header[7:8])
#    return postcode
    return record[7]

    

def save_mock_data(filepath, header, data):
    pass

###

# print_text_contents() doesn't return anything, it's just a function that carries out a task, we just need to call it.
print_text_contents()

###

records = read_file("csv_read_write/themis.csv", "csv")
print(records[0][0])
# NOTE: No need for a function here, slicing can achieve this.
# TODO: Print record n of CSV. (Of a given number, eg n = 5, print line 5.)
filename = "themis.csv"
record_number = 5


with open(f"csv_read_write/{filename}", 'r') as file:
    csv_reader = csv.reader(file)
    for index, row in enumerate(csv_reader):
        if index == record_number:
            print(row) 
            break

###
with open(f"csv_read_write/{filename}", 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  
    column_index = header.index('debtorspostcode') 

    postcode = [row[column_index] for row in reader]
   
#record = print(f"Record 5's postcode is: {postcode[4]}")
# Print fifth record's postcode.
# NOTE: DO the fork for this in the function that's being called.
print(records[4])
postcode = get_postcode(records[4])  # Programming starts at zero, fifth record = 4.
print(f"Record 5's postcode is: {postcode}")

###

# TODO: Print number of fields per record, and number of records in data.
# NOTE: This can be figured out with slicing, and the std lib len() function.
num_records = len(records)
num_fields_per_record = len(records[0])
print(f"Num records in data: {num_records}, num fields per record: {num_fields_per_record}")

###

# TODO: Take mocked data, use std lib's csv library to write (save) to a new CSV file.
# NOTE: DO it in the called function.
mock_header = ["Recip_name", "Street", "City", "County", "Postcode", "Account_number"]
mock_data = [
    ["Joe Bloggs", "1 Park Avenue", "Edinburgh", "Midlothian", "EH12 3AB", "12345"],
    ["Sally Smith", "37 Grove Street", "Glasgow", "", "G3 9ZZ", "98765"],
    ["AB Sample", "99 Sample Street", "Sample Town", "Sampleshire", "AB99 9AB", "XXXXX"]
]

with open("mock_data.csv", 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(mock_header)
    csvwriter.writerows(mock_data)

save_mock_data("mock_data.csv", mock_header, mock_data)
 