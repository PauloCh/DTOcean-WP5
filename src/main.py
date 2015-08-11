"""
Import databases
"""
from os import path

from wp5.load import load_vessel_data
from wp5.load import load_equipment_data
from wp5.load import load_port_data
from wp5.logistics.operations import logOp_init
from wp5.logistics.phase import logPhase_init

# # Set directory paths for loading inputs (@Tecanalia)
mod_path = path.dirname(path.realpath(__file__))

def database_file(file):
    fpath = path.join('databases', '{0}'.format(file))
    db_path = path.join(mod_path, fpath)
    return db_path

vessels = load_vessel_data(database_file("Vessel_Database_python.xlsx"))
equipments = load_equipment_data(database_file("Equipment_Database_python.xlsx"))
ports = load_port_data(database_file("Ports_Database2_python.xlsx"))

logOp = logOp_init()

logPhase_install = logPhase_init(logOp, vessels, equipments)[0]
logPhase_OM = logPhase_init(logOp, vessels, equipments)[1]