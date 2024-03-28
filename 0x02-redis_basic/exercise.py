#!/usr/bin/env python3
"""
exercise file contains Cache class, count_call and call_history decorators
"""

from typing import Union, Callable
from functools import wraps
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """AI is creating summary for count_calls

    Args:
        method (Callable): key of the data

    Returns:
        Callable: wrapper
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """AI is creating summary for call_history

    Args:
        method (Callable): key of the data

    Returns:
        Callable: wrapper
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        ins = str(args)
        self._redis.rpush("{}:inputs".format(key), ins)
        outs = str(method(self, *args, **kwargs))
        self._redis.rpush("{}:outputs".format(key), outs)
        return outs

    return wrapper


class Cache:
    """AI is creating summary for class Cache
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """AI is creating summary for store

        Args:
            data (Union[str, bytes, int, float]): data to be set in redis

        Returns:
            str: key generated using uuid
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable, None] = None):
        """AI is creating summary for get

        Args:
            key (str): key of the data.
            fn (Union[Callable, None], optional): to convert the data to
                                                  the desired format.
                                                  Defaults to None.

        Returns:
            Union[str, bytes, int, float]: data corresponding to the key
        """
        val = self._redis.get(key)

        if fn is not None:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """AI is creating summary for get_str

        Args:
            key (str): key of the data

        Returns:
            str: retrieve data as string
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """AI is creating summary for get_int

        Args:
            key (str): key of the data

        Returns:
            int: retrieve data as int
        """
        return self.get(key, int)
