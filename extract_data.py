import csv

csv_file_path = 'spotify-2023.csv'

csv_data = []

with open(csv_file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        csv_data.append(row)

header = csv_data[0]

data = csv_data[1:]

print("data:")
for row in data[:]:
    print(row)