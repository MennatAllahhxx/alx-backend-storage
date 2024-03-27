#!/usr/bin/env python3
"""
Module contains update_topics fun
"""

from typing import List


def update_topics(mongo_collection, name:str, topics: List[str]):
    """AI is creating summary for update_topics

    Args:
        mongo_collection (collection): to update docs in.
        name (str): name of the doc
        topics (List[str]): topics to be updated
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
