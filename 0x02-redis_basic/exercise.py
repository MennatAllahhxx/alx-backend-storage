#!/usr/bin/env python3
"""
exercise file contains Cache class
"""

from typing import Union, Callable
import uuid
import redis


class Cache:
    """AI is creating summary for class Cache
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

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

    def get(self, key: str,
            fn: Union[Callable, None] = None) -> Union[str, bytes, int, float]:
        """AI is creating summary for get

        Args:
            key (str): key of the data
            fn (Optional[Callable]): to convert the data to the desired format
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
