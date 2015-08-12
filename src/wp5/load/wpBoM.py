# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 15:26:10 2015

@author: Paulo
"""

import pandas as pd

def load_WP2_BoM(file_path):
    
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    units = excel.parse('units', header=0, index_col=0)
    position = excel.parse('position', header=0, index_col=0)

    WP2_BoM = {'numUnits': units,
               'position':  position
               }
    
    return WP2_BoM
    
    
def load_WP4_BoM(file_path):
    
    # Transform vessel database .xls into panda type
    WP4_BoM = pd.read_csv(file_path)

    return WP4_BoM