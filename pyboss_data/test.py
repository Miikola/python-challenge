import csv
import os

url = os.path.join("data/employee_data1.csv")

with open(url, newline="") as csvdata:
    reader = csv.DictReader(csvdata)

    print(reader)

    for row in reader:
        print(row)