list = []
list.append('dupa')
list.append('ddd')

list.sort(cmp=None, key=None, reverse=False)

import string
import hashlib, hmac

print hashlib.sha256("udacity").hexdigest()

a = str("a,434").split(",")

print hmac.new("sec", "dupa").hexdigest()

import random

print string.letters

a = ""
for i in range(5):
    a += random.choice(string.letters)

print a

cookie_params = {'cookie_name': "a",
                 'cookie_value':"b",
                 'path':"c"}
print "%(cookie_name)s=%(cookie_value)s;  Path=%(path)s" % cookie_params

import urllib2

www = urllib2.urlopen("http://www.example.com")

print www.headers

cache = {}

cache[(1,2)] = "dupa"

print cache.keys()

print hash(repr(2))
print hash(repr(2))

import time
from datetime import datetime, timedelta

d = datetime.now()
time.sleep(10)
d2 = datetime.now()




dt = d2 - d
print dt.total_seconds()





#    print item
