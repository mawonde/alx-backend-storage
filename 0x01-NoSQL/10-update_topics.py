#!/usr/bin/env python3
""" update a document """


def update_topics(mongo_collection, name, topics):
    """Function that Updates a document by name """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
