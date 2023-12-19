#!/usr/bin/env python3
""" a Python function that lists
all documents in a collection"""

import pymongo


def list_all(mongo_collection):
    """ Return an empty list if no document """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
