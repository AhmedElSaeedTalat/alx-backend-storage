#!/usr/bin/env python3
""" Write a Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """
        list all documents
        Args:
            mongo_collection: passed collection
        Return - found documents in the passed collection
    """
    documents = list(mongo_collection.find())
    if len(documents) > 0:
        return documents
    return []
