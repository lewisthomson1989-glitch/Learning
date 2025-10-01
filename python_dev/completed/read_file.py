import os
import csv

def read_file(filename, filetype):
    """
    (Richer functionality over os.read(), specifically built for CSV.)
    TODO: Check the filetype. Use the correct library for the correct file.
    TODO: Read from flat text file, using std lib's os.read()
    """
    contents = None
    if filetype == "txt" or filetype == "csv":
        with open(f"csv_read_write/{filename}", 'r') as f:

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


f = "themis.csv"
t = "csv"


result = read_file(f, t)
print(type(result))
print(len(result))
print(result)