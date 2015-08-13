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
    vessels = {'Tugboat': VesselType("vt1", "Tug boat", pd_vessel[pd_vessel['Vessel Type'] == 'Tug']),
               'Crane Barge': VesselType("vt2", "Crane barge", pd_vessel[pd_vessel['Vessel Type'] == 'Crane Barge']),
               'Crane Vessel': VesselType("vt3", "Crane vessel", pd_vessel[pd_vessel['Vessel Type'] == 'Crane Vessel']),
               'JUP Barge': VesselType("vt4", "Jack-up barge", pd_vessel[pd_vessel['Vessel Type'] == 'Jack-up barge']),
               'JUP Vessel': VesselType("vt5", "Jack-up vessel", pd_vessel[pd_vessel['Vessel Type'] == 'Jack-up vessel']),
               'Anchor Handling': VesselType("vt6", "Anchor Handling (AHTS or AHT)", pd_vessel[pd_vessel['Vessel Type'] == 'AHTS']),
               'Multicat': VesselType("vt7", "Multicat", pd_vessel[pd_vessel['Vessel Type'] == 'Multicat']),
               'CLV': VesselType("vt8", "Cable Laying Vessel", pd_vessel[pd_vessel['Vessel Type'] == 'CLV']),
               'CLB': VesselType("vt8", "Cable Laying Barge", pd_vessel[pd_vessel['Vessel Type'] == 'CLB']),
               'CTV': VesselType("vt8", "Crew Transfer Vessel", pd_vessel[pd_vessel['Vessel Type'] == 'CTV'])
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
    equipments = {'Hammer': EquipmentType("et1", "Hammer", hammer),
                  'Drill Rig': EquipmentType("et1", "Drilling Rig", drillingRig)
                  }

    return equipments


def load_port_data(file_path):
    # Transform vessel database .xls into panda type
    excel = pd.ExcelFile(file_path)
    # Collect data from a particular tab
    ports = excel.parse('python', header=0, index_col=0)

    return ports
