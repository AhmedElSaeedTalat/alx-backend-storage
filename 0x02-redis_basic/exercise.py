#!/usr/bin/env python3
"""
store data file
"""
import redis
import uuid
from typing import Union


class Cache:
    """ class to cache """
    def __init__(self):
        """ instantiate a class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            stores date
            Args:
                data: passed data to be stored
            Return - random key used to store data
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
