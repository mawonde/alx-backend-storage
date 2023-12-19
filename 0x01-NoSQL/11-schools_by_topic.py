#!/usr/bin/env python3
"""function that returns the list
of school having a specific topic:"""


def schools_by_topic(mongo_collection, topic):
    """
    returns The list of school that having the same topics
    """
    return [i for i in mongo_collection.find({"topics": topic})]
