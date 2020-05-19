import csv
import random


# I created a CSV with over 1 million authors
def create_authors():
    with open("src/csv/names.csv", 'r') as file_csv:
        reader = csv.reader(file_csv, delimiter='|')
        array = []
        author = []

        for c in range(0, 4):

            for i in reader:
                array.append(i[c])
            author += array[1::]

    # print(len(author))

    author_1KK = []
    for c in range(0, 1000100):
        author_1KK.append(random.choice(author))
    # print(author_1KK[1000000])
    return author_1KK


def create_csv():
    with open('src/csv/author.csv', 'a') as file_csv:
        write = csv.writer(file_csv, delimiter=',', lineterminator='\n')
        author = create_authors()
        for c in range(0, len(author)):
            write.writerow([author[c]])


create_csv()
