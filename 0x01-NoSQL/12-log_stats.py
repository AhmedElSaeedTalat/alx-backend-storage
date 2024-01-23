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
    get = collection.count_documents({'method': 'GET'})
    post = collection.count_documents({'method': 'POST'})
    put = collection.count_documents({'method': 'PUT'})
    pach = collection.count_documents({'method': 'PATCH'})
    delete = collection.count_documents({'method': 'DELETE'})
    print(f'\tmethod GET: {get}')
    print(f'\tmethod POST {post}')
    print(f'\tmethod PUT: {put}')
    print(f'\tmethod PATCH: {pach}')
    print(f'\tmethod DELETE: {delete}')

    get_status = collection.count_documents({'method': 'GET',
                                             'path': '/status'})
    print(f'{get_status} status check')
