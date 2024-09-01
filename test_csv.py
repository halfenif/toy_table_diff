import csv



with open('data_sample/LEFT.csv', 'r', encoding="UTF-8", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    for row in reader:
        

        for col in row:
            print(col, type(col))

