import pandas as pd

from ..logistics import VesselType
from ..logistics import EquipmentType

"""
### Set of functions to load data from database folder into panda tables
"""


# # Imports data from vessels
def load_vessel_data(file_path):
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    pd_vessel = excel.parse('Python_Format', header=0, index_col=0)

    """
    ### Define vessel types by invoking VesselType class
    """
    vessels = {'Tugboat': VesselType("Tug boat", pd_vessel[pd_vessel['Vessel Type'] == 'Tug']),
               'Crane Barge': VesselType("Crane barge", pd_vessel[pd_vessel['Vessel Type'] == 'Crane Barge']),
               'Crane Vessel': VesselType("Crane vessel", pd_vessel[pd_vessel['Vessel Type'] == 'Crane Vessel']),
               'JUP Barge': VesselType("Jack-up barge", pd_vessel[pd_vessel['Vessel Type'] == 'Jack-up barge']),
               'JUP Vessel': VesselType("Jack-up vessel", pd_vessel[pd_vessel['Vessel Type'] == 'Jack-up vessel']),
               'Anchor Handling': VesselType("Anchor Handling (AHTS or AHT)", pd_vessel[pd_vessel['Vessel Type'] == 'AHTS']),
               'Multicat': VesselType("Multicat", pd_vessel[pd_vessel['Vessel Type'] == 'Multicat']),
               'CLV': VesselType("Cable Laying Vessel", pd_vessel[pd_vessel['Vessel Type'] == 'CLV']),
               'CLB': VesselType("Cable Laying Barge", pd_vessel[pd_vessel['Vessel Type'] == 'CLB']),
               'CTV': VesselType("Crew Transfer Vessel", pd_vessel[pd_vessel['Vessel Type'] == 'CTV'])
               }

    return vessels


def load_equipment_data(file_path):
    # Transform Equipment database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    hammer = excel.parse('hammer', header=0, index_col=0)
    drillingRig = excel.parse('drilling rig', header=0, index_col=0)

    """
    ### Define equipment types by invoking EquipmentType class
    """
    equipments = {'Hammer': EquipmentType("Hammer", hammer),
                  'Drill Rig': EquipmentType("Drilling Rig", drillingRig)
                  }

    return equipments


def load_port_data(file_path):
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    ports = excel.parse('python', header=0, index_col=0)

    return ports
