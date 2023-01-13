import logging
import os
import subprocess
import yaml
import pandas as pd
import datetime 
import gc
import re

def readcon(file):
    with open(file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)
            
nempty = 0
def check_col(f1,f2):
    get = True
    f1list = list(f1.columns)
    yes = 'Correct. All columns validated'
    empty = []
    for i in f2:
        if i not in f1list:
            empty.append(i)
            yes = 'Incorrect. Following columns are not in File: ' + str(empty)
            nempty += 1
        else:
            nempty = 0
            
    return yes

def check_len(f1,f2):
    lenf1 = len(f1)
    lenf2 = len(f2)
    yes = 'yup'
    if lenf1 == lenf2:
        yes = 'Both File and YAML column lengths sufficient'
    else:
        yes = 'File and YAML column lenghths unsufficient'
    return yes
