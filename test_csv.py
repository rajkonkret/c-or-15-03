import csv

# , ;  tab
# radek, zosia, krzysiek

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Sanchit', 'COE', '2', '9.1']  # przykład jak dane wygladaja w pythonie dla pojedynczego wiersza

# wymagany sposob podania danych przez biblioteke csv
my_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': "2"},
    {'branch': 'COs', 'cgpa': '6.1', 'name': 'Koral', 'year': "3"},
    {'branch': 'BOL', 'cgpa': '2.1', 'name': 'Greg', 'year': "1"}
]
file = 'records.csv'

with open(file, 'w', newline="") as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)
# ctrl shift f = wyszukiwarka w plikach
