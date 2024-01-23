#!/usr/bin/env python3
""" task 12 """
from pymongo import MongoClient


def display_nginx():
    """ display data of nginx """
    client = MongoClient('localhost', 27017)
    collection = client.logs.nginx
    count_documents = collection.count_documents({})
    print(count_documents, 'logs')
    print('Methods:')
    get = list(collection.find({'method': 'GET'}))
    post = list(collection.find({'method': 'POST'}))
    put = list(collection.find({'method': 'PUT'}))
    pach = list(collection.find({'method': 'PATCH'}))
    delete = list(collection.find({'method': 'DELETE'}))
    print('\tmethod GET:', len(get))
    print('\tmethod POST', len(post))
    print('\tmethod PUT:', len(put))
    print('\tmethod PATCH:', len(pach))
    print('\tmethod DELETE:', len(delete))

    get_status = list(collection.find({'method': 'GET', 'path': '/status'}))
    print(len(get_status), 'status check')


if __name__ == "__main__":
    display_nginx()
