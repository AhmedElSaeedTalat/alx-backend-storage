#!/usr/bin/env python3
""" 11-main """


def schools_by_topic(mongo_collection, topic):
    """ list school having a certain topic """
    return mongo_collection.find({'topics': {"$elemMatch": {"$eq": topic}}})
