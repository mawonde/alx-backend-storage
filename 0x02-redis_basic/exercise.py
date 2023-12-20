#!/usr/bin/env python3
""" Remote Dictionary Service """

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts num times a function is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """behavior to function that will count"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapped


def call_history(method: Callable) -> Callable:
    """ Stores the history of inputs and outputs	"""
    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """  behavior to function that will count """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapped


def replay(fn: Callable):
    """ Displays the history of calls """
    r = redis.Redis()
    function_name = fn.__qualname__
    count = r.get(function_name)
    try:
        count = int(count.decode("utf-8"))
    except Exception:
        count = 0
    print(f"{function_name} was called {count} times:")
    inputs = r.lrange(f"{function_name}:inputs", 0, -1)
    outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    for one, two in zip(inputs, outputs):
        try:
            one = one.decode('utf-8')
        except Exception:
            one = ""
        try:
            two = two.decode('utf-8')
        except Exception:
            two = ""
        print(f"{function_name}(*{one}) -> {two}")


class Cache:
    """ implements the cache strategy """
    def __init__(self):
        """ The Constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Gets a data that will be saved """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Extracts the information saved in redis """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ takes a Parameter of  a value from redis to str """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Takes a Parameter from a value from redis to int """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
