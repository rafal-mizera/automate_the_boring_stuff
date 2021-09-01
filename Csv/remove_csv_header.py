"""Removes first line of every csv file in current working directory"""

import csv
import os

os.makedirs("header_removed",exist_ok=True)

for filename in os.listdir("."):
    if not filename.endswith(".csv"):
        continue
    with open(filename,"r") as file:
        path = os.path.join("header_removed",filename)
        with open(path,"w",newline="") as new_file:
            print(f"Removing header from {filename}")
            csv_reader = csv.reader(file)
            csv_writer = csv.writer(new_file)
            data = list(csv_reader)
            print(f"Writing to {filename} ...")
            for row in range(1,len(data)):
                csv_writer.writerow(data[row])




