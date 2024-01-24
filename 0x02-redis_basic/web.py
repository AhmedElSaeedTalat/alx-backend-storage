#!/usr/bin/env python3
""" web.py file Task 5 """
import requests
from functools import wraps
from redis import Redis
from typing import Callable
db = Redis()


def cache_countVisited(method: Callable) -> Callable:
    """ function that caches the number of requests """
    @wraps(method)
    def wrapper(url):
        """ wrapper for the function """
        key = f'count:{url}'
        db.incr(key)
        result = method(url)
        if result:
            db.setex('result', 10, result)
        return result
    return wrapper


@cache_countVisited
def get_page(url: str) -> str:
    """ return response of request """
    res = requests.get(url)
    return res.text