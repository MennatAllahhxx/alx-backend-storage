#!/usr/bin/env python3
"""
Module contains list_all fun
"""


def list_all(mongo_collection):
    """AI is creating summary for list_all

    Args:
        mongo_collection (mongoDB collection): to list all the docs for.

    Returns:
        List: all documents in a collection
    """
    return list(mongo_collection.find({}))
