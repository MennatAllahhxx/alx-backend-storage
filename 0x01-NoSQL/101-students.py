#!/usr/bin/env python3
"""
Module contains top_students fun
"""


def top_students(mongo_collection):
    """AI is creating summary for top_students

    Args:
        mongo_collection (collection): collection to be sorted

    Returns:
        collection: all students sorted by average score
    """
    return mongo_collection.aggregate([
            { "$project": {
                    "name": "$name",
                    "averageScore": {"$avg":"$topics.score" }
                }
            },
            {
                "$sort": {"averageScore": -1}
            }
    ])
