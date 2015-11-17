# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module imports the WP5 databases required to run WP5 package.  All data
imported is translated to panda dataframes.

BETA VERSION NOTES: the module also aims to provide a buffer between the database
source and WP5 package, so it becomes simple to shift from the temporary .xlsx
and .csv files to the final SQL solution.
"""

import pandas as pd

from ..logistics import VesselType
from ..logistics import EquipmentType

def load_vessel_data(file_path):
    """Imports vessel database into panda dataframe and creates a class for each
    vessel type

    Parameters
    ----------
    file_path : string
     the folder path of the vessel database

    Returns
    -------
    vessels : dict
     dictionnary containing all classes defining the different vessel types
    """
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    pd_vessel = excel.parse('Python_Format', header=0, index_col=0)

    # Splits the pd_vessel object with the full dataset, into smaller panda
    # objects with specific vessel types. Each vessel object is initiated with
    # the vessel class: VesselType
    vessels = {'Barge': VesselType("Barge", pd_vessel[pd_vessel['Vessel type [-]'] == 'Barge']),
               'Tugboat': VesselType("Tugboat", pd_vessel[pd_vessel['Vessel type [-]'] == 'Tugboat']),
               'Crane Barge': VesselType("Crane Barge", pd_vessel[pd_vessel['Vessel type [-]'] == 'Crane barge']),
               'Crane Vessel': VesselType("Crane Vessel", pd_vessel[pd_vessel['Vessel type [-]'] == 'Crane vessel']),
               'JUP Barge': VesselType("JUP Barge", pd_vessel[pd_vessel['Vessel type [-]'] == 'JUP Barge']),
               'JUP Vessel': VesselType("JUP Vessel", pd_vessel[pd_vessel['Vessel type [-]'] == 'JUP Vessel']),
               'Anchor Handling': VesselType("AHTS", pd_vessel[pd_vessel['Vessel type [-]'] == 'AHTS']),
               'Multicat': VesselType("Multicat", pd_vessel[pd_vessel['Vessel type [-]'] == 'Multicat']),
               'AHTS': VesselType("AHTS", pd_vessel[pd_vessel['Vessel type [-]'] == 'AHTS']),
               'CLV': VesselType("CLV", pd_vessel[pd_vessel['Vessel type [-]'] == 'CLV']),
               'CLB': VesselType("CLB", pd_vessel[pd_vessel['Vessel type [-]'] == 'CLB']),
               'CTV': VesselType("CTV", pd_vessel[pd_vessel['Vessel type [-]'] == 'CTV']),
               'Construction Support Vessel': VesselType("Construction Support Vessel", pd_vessel[pd_vessel['Vessel type [-]'] == 'Construction Support Vessel']),
               'Fit for Purpose': VesselType("Fit for Purpose", pd_vessel[pd_vessel['Vessel type [-]'] == 'Fit for Purpose']),
               'Platform Support Vessel': VesselType("Platform Supply Vessel", pd_vessel[pd_vessel['Vessel type [-]'] == 'PSV']),
               'Helicopter': VesselType("Helicopter", pd_vessel[pd_vessel['Vessel type [-]'] == 'Helicopter'])
               }

    return vessels


def load_equipment_data(file_path):
    """Imports equipment database into panda dataframe    hammer = excel.parse('hammer', header=0, index_col=0)
s and creates a class for
    each equipment type

    Parameters
    ----------
    file_path : string
     the folder path of the equipment database

    Returns
    -------
    vessels : dict
     dictionnary containing all classes defining the different equipment types
    """

    # Transform Equipment database .xls into panda type
    excel = pd.ExcelFile(file_path)

    # Collect data from a particular tab
    rov = excel.parse('rov', header=0, index_col=0)
    divers = excel.parse('divers', header=0, index_col=0)
    cable_burial = excel.parse('cable_burial', header=0, index_col=0)
    excavating = excel.parse('excavating', header=0, index_col=0)
    mattress = excel.parse('mattress', header=0, index_col=0)
    rock_filter_bags = excel.parse('rock_filter_bags', header=0, index_col=0)
    split_pipe = excel.parse('split_pipe', header=0, index_col=0)
    hammer = excel.parse('hammer', header=0, index_col=0)
    drilling_rigs = excel.parse('drilling_rigs', header=0, index_col=0)
    vibro_driver = excel.parse('vibro_driver', header=0, index_col=0)

    # Define equipment types by invoking EquipmentType class
    equipments = {'rov': EquipmentType("rov", rov),
                  'divers': EquipmentType("divers", divers),
                  'cable burial': EquipmentType("cable_burial", cable_burial),
                  'excavating': EquipmentType("excavating", excavating),
                  'mattress': EquipmentType("mattress", mattress),
                  'rock filter bags': EquipmentType("rock_filter_bags", rock_filter_bags),
                  'split pipe': EquipmentType("split_pipe", split_pipe),
                  'hammer': EquipmentType("hammer", hammer),
                  'drilling rigs': EquipmentType("drilling_rigs", drilling_rigs),
                  'vibro driver': EquipmentType("vibro_driver", vibro_driver)
                 }

    return equipments


def load_port_data(file_path):
    """Imports port database into a panda table

    Parameters
    ----------
    file_path : string
     the folder path of the port database

    Returns
    -------
    vessels : dict
     dictionnary containing a panda dataframe with all ports
    """
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    ports = excel.parse('python', header=0, index_col=0)

    return ports
