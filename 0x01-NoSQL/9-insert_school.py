#!/usr/bin/env python3
""" task 9"""


def insert_school(mongo_collection, **kwargs):
    """func to insert a new document in a collection"""
    test = mongo_collection.insert_one(kwargs)
    return test.inserted_id
