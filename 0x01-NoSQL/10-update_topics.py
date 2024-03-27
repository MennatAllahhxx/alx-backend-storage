#!/usr/bin/env python3
"""
Module contains update_topics fun
"""


def update_topics(mongo_collection, name, topics):
    """AI is creating summary for insert_school

    Args:
        mongo_collection (mongoDB collection): to insert new docs to.

    Returns:
        str: new docs id
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
