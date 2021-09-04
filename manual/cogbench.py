import numpy as np
import matplotlib.pyplot as plt
import string
import random
from fuzzywuzzy import fuzz, process
import time

from utils import load, pickle, save
from test import Test
from alternation import Alternation

main_database = load()
class Device:
    def __init__(self, name, device_type=None, screen_width=None, screen_height=None):
        self.name = name
        self.device_type = device_type
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.created = time.time()

class Session:
    def __init__(self, db=None):
        if db is None:
            db = main_database
        self.database = db
        self.opened = time.time()

    def end(self):
        self.closed = time.time()





# test_hierarchy = dict(
#     typing=dict(
#         alternation=alternation,
#         random=random_keys,
#     )
# )
tests = [Alternation]
test_names = [t.__name__.lower() for t in tests]

# TODO: move functions to a class (?)
def handle_command(sess=None, database=None):
    command = input().split()
    lead = command[0].lower()
    save(sess=main_database)
    matches = list(filter(lambda x: lead in x, test_names))
    # if lead in test_names:
    if matches:
        test_name = matches[0]
        test = tests[test_names.index(test_name)]()
        if database:
            database.tests.append(test)
        else:
            print('Warning: no database currently loaded; test will not be saved')
        test.run()
        save(sess=database)
