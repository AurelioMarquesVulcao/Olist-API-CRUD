from pymongo import MongoClient
# from decouple import config
import csv


def reader_authors():
    with open("src/csv/author.csv", 'r') as file_csv:
        reader = csv.reader(file_csv, delimiter='|')
        array = []
        author = []

        for i in reader:
            array.append(i[0])

        for c in range(0, len(array)):
            author.append({'name': array[c]}) 
    return author


# print(reader_authors())

url = config('mongodb+srv://Aurelioprod:U0PWxXrhk4KmFpp4@vulcaotech-pdii4.mongodb.net/Olist?retryWrites=true&w=majority')
# print(url)
cluster = MongoClient(url)
db = cluster['Olist']
colection = db["authors"]

data = reader_authors()

colection.insert_many(data)
