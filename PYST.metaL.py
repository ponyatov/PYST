## @file
## @brief meta: Smalltalkish in Python

from metaL import *

p = Project(
    title='''Smalltalkish in Python''',
    about='''
* https://twitter.com/dponyatov/status/1445456570389729283
''') \
    | Python() \
    | ST()

p.sync()
