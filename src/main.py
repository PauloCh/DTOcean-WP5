"""
Import databases
"""
from os import path

import pandas as pd

from wp5.load import load_vessel_data, load_equipment_data, load_port_data
from wp5.load.wp_bom import load_WP1_BoM, load_WP2_BoM
from wp5.load.wp_bom import load_WP3_BoM, load_WP4_BoM
from wp5.logistics.operations import logOp_init
from wp5.logistics.phase import logPhase_init
from wp5.installation import planning, select_port

# # Set directory paths for loading inputs (@Tecanalia)
mod_path = path.dirname(path.realpath(__file__))


def database_file(file):
    fpath = path.join('databases', '{0}'.format(file))
    db_path = path.join(mod_path, fpath)
    return db_path
"""
### Load maritime infrastructure database
"""
vessels = load_vessel_data(database_file("Vessel_Database_python.xlsx"))
equipments = load_equipment_data(database_file("Equipment_Database_python.xlsx"))
ports = load_port_data(database_file("Ports_Database2_python.xlsx"))

"""
### Load inputs from end-user and WP1, WP2, WP3 & WP6
"""
wp1_BoM = load_WP1_BoM(database_file("WP1_BoM.xlsx"),
                       database_file("VianaCastelo.csv"))
wp2_BoM = load_WP2_BoM(database_file("WP2_BoM.xlsx"))
wp3_BoM = load_WP3_BoM(database_file("WP3_BoM.xlsx"))
wp4_BoM = load_WP4_BoM(database_file("WP4_BoM.csv"))

"""
### Initialise logistic operations and logistic phases
"""
logOp = logOp_init()

logPhase_install, logPhase_OM = logPhase_init(logOp, vessels, equipments)





"""
### Determine the adequate installation logistic phase sequence
"""
install_seq = planning.install_plan(wp1_BoM, wp3_BoM, wp4_BoM)

"""
### Determine the adequate installation logistic phase sequence
"""
install_port = select_port.install_port(wp1_BoM, wp3_BoM, wp4_BoM, ports)

for x in install_seq:
    for y in install_seq[x]:
        log_phase_id = install_seq[x][y]
# ###### TO-DO-TO-DO-TO-DO-TO-DO-TO-DO-TO-DO !!!
=======
logOp = logOp_init()

logPhase_install = logPhase_install_init(logOp, vessels, equipments)
logPhase_OM = logPhase_OM_init(logOp, vessels, equipments)

>>>>>>> origin/master
deck_loading, deck_area = logPhase_install['F_driven'].vessel_feasiblity(wp1_BoM, wp2_BoM, wp3_BoM,
                                               wp4_BoM, vessels)


<<<<<<< HEAD
=======



>>>>>>> origin/master
