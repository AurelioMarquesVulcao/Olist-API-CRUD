from pymongo import MongoClient
from decouple import config
import csv


def reader_authors():
    with open("src/csv/author.csv", 'r') as file_csv:
        reader = csv.reader(file_csv, delimiter='|')
        array = []
        author = []

        for i in reader:
            array.append(i[0])

        for c in range(0, len(array)):
            author.append({'_id': c, 'name': array[c]}) 
    return author


# print(reader_authors())

url = config('ACCESS_DB', cast=str)
# print(url)
cluster = MongoClient(url)
db = cluster['Olist']
colection = db["authors"]

data = reader_authors()

colection.insert_many(data)
