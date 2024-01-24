#!/usr/bin/env python3
"""
store data file
"""
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """
            get stored value
            Args:
                key: key for value stored to retrieve
                fn: callable of a function
            Return - data stored
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ parametrize Cache.get with string conversion """
        return self.get(key, lambda val: val.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """ parametrize Cache.get with int conversion """
        return self.get(key, lambda val: int(val.decode('utf-8')))
