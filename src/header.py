
import urllib2
import sys
import os
import pymongo
import re

instance = ""

def getServerStatus():
    if 'MONGOURI' in os.environ:
        c = pymongo.MongoClient(os.environ['MONGOURI'])
    else:
        c = pymongo.MongoClient()
    return c.admin.command('serverStatus', workingSet=True)
