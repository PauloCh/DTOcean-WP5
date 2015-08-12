# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:26:10 2015

@author: Paulo
"""

import pandas as pd

def load_WP4_BoM(file_path):
    
    # Transform vessel database .xls into panda type
    WP4_BoM = pd.read_csv(file_path)

    return WP4_BoM