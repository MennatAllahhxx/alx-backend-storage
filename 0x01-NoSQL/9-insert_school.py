#!/usr/bin/env python3
"""
Module contains insert_school fun
"""


def insert_school(mongo_collection, **kwargs):
    """AI is creating summary for insert_school

    Args:
        mongo_collection (mongoDB collection): to insert new docs to.

    Returns:
        str: new docs id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
