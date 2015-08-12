"""
Import databases
"""
from os import path

import pandas as pd

from wp5.load import load_vessel_data, load_equipment_data, load_port_data
from wp5.load.wpBoM import load_WP1_BoM, load_WP2_BoM, load_WP3_BoM, load_WP4_BoM
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

WP1_BoM = load_WP1_BoM(database_file("WP1_BoM.xlsx"),database_file("VianaCastelo.csv"))
WP2_BoM = load_WP2_BoM(database_file("WP2_BoM.xlsx"))
WP3_BoM = load_WP3_BoM(database_file("WP3_BoM.xlsx"))
WP4_BoM = load_WP4_BoM(database_file("WP4_BoM.csv"))



