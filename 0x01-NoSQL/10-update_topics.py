#!/usr/bin/env python3
"""task 10"""


def update_topics(mongo_collection, name, topics):
    '''func to change all topics of a school
    document based on the name'''
    new_values = {"$set": {'topics': topics}}
    mongo_collection.update_one({'name': name}, new_values)
