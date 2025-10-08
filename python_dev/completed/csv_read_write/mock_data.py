import csv

def save_mock_data(filepath, header, data):
    pass

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

mock_data[1][4] = "BADGERS"
print(mock_data)