#!/usr/bin/env python3
""" task 12 """
from pymongo import MongoClient


if __name__ == "__main__":
    """ return nginx data """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    count_documents = collection.count_documents({})
    print(f'{count_documents} logs')
    print('Methods:')
    get = list(collection.find({'method': 'GET'}))
    post = list(collection.find({'method': 'POST'}))
    put = list(collection.find({'method': 'PUT'}))
    pach = list(collection.find({'method': 'PATCH'}))
    delete = list(collection.find({'method': 'DELETE'}))
    print(f'\tmethod GET: {len(get)}')
    print(f'\tmethod POST {len(post)}')
    print(f'\tmethod PUT: {len(put)}')
    print(f'\tmethod PATCH: {len(pach)}')
    print(f'\tmethod DELETE: {len(delete)}')

    get_status = list(collection.find({'method': 'GET', 'path': '/status'}))
    print(f'{len(get_status)} status check')
