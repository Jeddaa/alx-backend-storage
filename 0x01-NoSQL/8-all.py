#!/usr/bin/env python3
""" task 8 """


def list_all(mongo_collection):
    '''func to list all document in a collection '''
    return mongo_collection.find()
