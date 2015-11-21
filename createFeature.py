#!/usr/bin/env python3

import sys
from decimal import *
import math
import copy
import os

pathName=sys.argv[1]
what_=sys.argv[2]

v=os.listdir(pathName)
v.sort()

#first one so not storing speaker.


for filename in v:
    if(what_=="baseline"):
        os.system("python3 create_baseline_features.py "+ pathName+filename)
    else:
        os.system("python3 create_advanced_features.py "+ pathName+filename)





