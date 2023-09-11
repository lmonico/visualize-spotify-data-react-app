import csv
import json

csv_file_path = 'spotify-2023.csv'

csv_data = []

with open(csv_file_path, mode='r', newline='') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        csv_data.append(row)

header = csv_data[0]

data = csv_data[1:]

count = 0

for element in data:
    print(element)
    count = count +1

json_filename = 'spotify_list.json'

with open(json_filename, 'w') as json_file:
    json.dump(data, json_file)