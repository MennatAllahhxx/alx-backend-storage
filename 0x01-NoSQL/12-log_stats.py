#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.logs
collection = db.nginx
print("{} logs".format(collection.count_documents({})))
print("Methods:")
print("\t method GET: {}".format(collection.
                                 count_documents({"method": "GET"})))
print("\t method POST: {}".format(collection.
                                  count_documents({"method": "POST"})))
print("\t method PUT: {}".format(collection.
                                 count_documents({"method": "PUT"})))
print("\t method PATCH: {}".format(collection.
                                   count_documents({"method": "PATCH"})))
print("\t method DELETE: {}".format(collection.
                                    count_documents({"method": "DELETE"})))
print("{} status check".format(collection.
                               count_documents({
                                                "method": "GET",
                                                "path": "/status"
                                                })))
