#!/usr/bin/env python3
"""
Main file
"""

from typing import Any
import uuid
import redis


class Cache:
    """AI is creating summary for class Cache
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Any) -> str:
        """AI is creating summary for store

        Args:
            data (any): [description]

        Returns:
            str: [description]
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
