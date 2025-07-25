import csv

with open('movie_cast.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader :
        if int(row['order']) >= 2 :
            print(row['name'])



