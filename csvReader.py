import csv

review = []
with open('a.csv') as file:
    csvReader = csv.reader(file, delimiter=',')
    for row in csvReader:
        review.append(row)
    print(review)