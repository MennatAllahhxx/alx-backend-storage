#!/usr/bin/env python3
"""
Module contains schools_by_topic fun
"""


def schools_by_topic(mongo_collection, topics: str):
    """AI is creating summary for schools_by_topic

    Args:
        mongo_collection (collection): to be searched through
        topics (str): topics to be used for search
    """
    return mongo_collection.find({"topics": topics})
