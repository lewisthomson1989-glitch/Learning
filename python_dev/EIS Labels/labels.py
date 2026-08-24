from os import read
import csv



def read_file(filename:str, filetype:str) -> list:
   
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

filename = "python_dev/EIS Labels/eis000_14915 - Copy.csv"