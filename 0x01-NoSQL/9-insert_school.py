#!/usr/bin/env python3
""" Insert new doc in a collection """


def insert_school(mongo_collection, **kwargs):
    """Inserts in school collection a document"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
