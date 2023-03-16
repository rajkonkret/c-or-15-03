import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f, delimiter=";")

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("liczba wierszy", csvreader.line_num)
print(fields)
print(rows)
print(rows[2][0])
