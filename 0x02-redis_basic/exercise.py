#!/usr/bin/env python3
"""
exercise file contains Cache class
"""

from typing import Union
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
