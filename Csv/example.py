import csv

with open("example.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
#     example_data = list(csv_reader)
#     # print(example_data)
#     # print(example_data[0][0])
#     # print(example_data[2][1])
    for row in csv_reader:
        print("Row #" + str(csv_reader.line_num) + " " + str(row))

# csv_file = open("example.csv")
# csv_reader = csv.reader(csv_file)
#
# for row in csv_reader:
#          print("Row #" + str(csv_reader.line_num) + " " + str(row))

# output_csv = open("output.csv","w",newline="")
# output_writer = csv.writer(output_csv)
# output_writer.writerow(["bacon","ham","eggs","spam"])
# output_writer.writerow(["Hello World!","bacon","ham","eggs","spam"])
# output_writer.writerow([1,2,3,4,5])
# output_csv.close()

# output_csv = open("output.tsv","w",newline="")
# csv_writer = csv.writer(output_csv,delimiter="\t",lineterminator="\n\n")
# csv_writer.writerow(["bacon","ham","eggs","spam"])
# csv_writer.writerow(["Hello World!","bacon","ham","eggs","spam"])
# csv_writer.writerow([1,2,3,4,5])
# output_csv.close()
