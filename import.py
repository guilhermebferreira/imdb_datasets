from pymongo import MongoClient
import csv
import os
import sys
import re
import json

client = MongoClient('mongodb://root:MongoDB2019!@0.0.0.0:27017')
db = client["mydatabase"]


def find(collection, key, value):
    return collection.find({key: re.compile(value, re.IGNORECASE)})


def find_exact(collection, key, value):
    return collection.find_one({key: re.compile(value, re.IGNORECASE)})


def find_movie(value):

    pipeline = [
        {"$match": {"title": value}},
        {"$group": {"_id": "$title", "min": {"$min": "$ordering"}}}
    ]

    query = [
        {"$match":{"title":re.compile(value, re.IGNORECASE)}},
        {"$group" : {"_id" : "$titleId", "ordering" : {"$min" : "$ordering"}}}
             ]

    titles = db.titles_akas

    movies = titles.aggregate(query)

    return movies


def find_title(value):
    movies = db.titles_akas.find({'title': re.compile(value, re.IGNORECASE)})

    #print(movies.explain())

    return movies


def find_rating(value):
    return find_exact(db.title_ratings, 'tconst', value)


def csv_to_dict(collection, file):
    # client = MongoClient('mongodb://guilherme:senha!@0.0.0.0:27017')
    # db = client["mydatabase"]
    csv.field_size_limit(sys.maxsize)

    print('iniciando carregamento de %s' % file)

    with open(file) as infile:
        reader = csv.DictReader(infile, dialect='excel-tab')
        result = {}
        for row in reader:
            # print(row)
            collection.insert_one(row)
    print('%s carregado' % file)


def load_files_short():
    print("carregando conjunto de testes")
    collection = db.title_akas
    csv_to_dict(collection, "data/short.title.akas.tsv")

    collection = db.title_ratings
    csv_to_dict(collection, "data/short.title.ratings.tsv")

    collection = db.title_basics
    csv_to_dict(collection, "data/short.title.basics.tsv")



def load_files():
    collection = db.title_akas
    csv_to_dict(collection, "data/title.akas.tsv")

    collection = db.title_ratings
    csv_to_dict(collection, "data/title.ratings.tsv")

    collection = db.title_basics
    csv_to_dict(collection, "data/title.basics.tsv")


print('running pythom import')

load_files_short() #versão para testes
#load_files() #Isso pode demorar


# r = find_title("a")
#
#
# for movie in r:
#     # # print(movie)
#     id = movie.get('titleId')
#     title = movie.get('title')
#     print(movie)
#     if id:
#         rating = find_rating(id)
#         if rating:
#             rate = rating.get('averageRating')
#             if rate:
#                 print("%s - %s:" % (id, title))
#                 print(rate)
