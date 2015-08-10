# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:57:12 2015

@author: WavEC - Offshore Renewables
email: boris.teillant@wavec.org / paulo@wavec.org

main.py is the main file of the WP5 module within the suite of design tools
developped under the EU FP7 DTOcean project. main.py returns the installation
schedule, cost, environmental impact and risk value. It embodies the logistic
functions providing the estimated performance of the logistic phases not only
for the installation phase but also for the O&M service life.

main.py is primarily composed of three sub-modules:
1-Logistic requirements and pre-defined logistic phase:
2-Selection of the maritime infrastructure:
3-Performance assessment of the logistic phase:

Parameters
----------
logOpID : integer
 ID number identifying the type of marine operation
environmentData : array
 array containing the environmental resource database
technologyData : array
 array containing the technology database
vesselsData : array
 array containing the vessels database
equipmentData : array
 array containing the equipment database
portsData : array
 array containing the ports database
inputFromEndUser : array
 array containing theprescribed end-user inputs

Returns
-------

Examples
--------
>>> WP5()


See also: ...

                       DTOcean project
                    http://www.dtocean.eu

                   WavEC Offshore Renewables
                    http://www.wavsec.org/en


"""
"""
Import databases
"""
from os import path

from load import environment, load_csv, equipment, vessel, port, phaseSeq
"""
Import classes
"""
from logPhaseClass import LogPhase
from logOpClass import LogOp
from vesselClass import VesselType
from equipmentClass import Equipment
"""
Import logistic functions
"""
from installation import planning, select_port
from characterization import predefined, requirements # will be modified
from selection import select, match # will be modified
from assessment.schedule import scheduleLog
from assessment.cost import costLog
"""
#### Definition of the logistic pahase by invocaking the class LogPhase ###
# Invocation of the full list of logistic phases covered in WP5
# Explanation of the key ID numbering system implemented:
# 1st digit:  1 = Installation; 9 = O&M
# 2nd digit: 0 = Electrical infrastructure; 1 = Moorings and foundations;
#            2 = wave or tidal devices
# 3rd digit: component/sub-system type - differ depending on the logistic phase
# 4th digit: method (level 1) - differ depending on the logistic phase
# 5th digit: sub-method (level 2) - differ depending on the logistic phase
"""
lg1 = LogPhase(100, "Installation of static subsea export power cables", {}, {})
lg2 = LogPhase(101, "Installation of static subsea inter-array power cables", {}, {})
lg3 = LogPhase(102, "Installation of offshore electrical collection point", {}, {})
lg4 = LogPhase(110, "Installation of driven piles foundations", {}, {})
lg5 = LogPhase(111, "Installation of suction caissons for foundation systems", {}, {})
lg6 = LogPhase(112, "Installation of gravity based foundations", {}, {})
lg7 = LogPhase(113, "Installation of mooring systems with drag-embedment anchors", {}, {})
lg8 = LogPhase(114, "Installation of mooring systems with direct-embedment anchors", {}, {})
lg9 = LogPhase(120, "Installation of bottom fixed devices", {}, {})
lg10 = LogPhase(121, "Installation of floating devices", {}, {})
lg11 = LogPhase(900, "O&M offshore intervention", {}, {})
# to be added (if needed): electrical connectors, mooring systems with 
# piles/GBS/suction caissons
"""
#### Definition of the logistic operations by invocaking the class LogOp ###
# Invocation of the full list of individual logistic operations covered in WP5
# Explanation of the key ID numbering system implemented:
# 1st digit:  1 = General individual operation shared with all/most logistic phases;
#             2 = Specialized individual operation for the installation of electrical infrastructure;
#             3 = Specialized individual operation for the installation of foundations;
#             4 = Specialized individual operation for the installation of moorings;
#             5 = Specialized individual operation for the installation of tidal or wave energyd devices;
#             6 = Specialized individual operation for inspection activities;
#             7 = Specialized individual operation for on-site maintenance interventions;
#             8 = Specialized individual operation for port-based maintenance interventions;
# 2nd digit: simple counter to discriminate between different individual
#            operations within the same category defined by the 1st digit
"""
lio1 = LogOp(10, "Mobilisation", [0, 0, 0, 0], 0, 0)
lio2 = LogOp(11, "Assembly at port", [0, 0, 0, 0], 0, 0)
lio3 = LogOp(13, "Vessel preparation and loading", [0, 0, 0, 0], 0, 0)
lio4 = LogOp(14, "Transportation from port to site", [0, 0, 0, 0], 0, 0)
lio5 = LogOp(15, "Seafloor and equipment preparation on-site", [0, 0, 0, 0], 0, 0)
lio6 = LogOp(16, "Transportation from site to site", [0, 0, 0, 0], 0, 0)
lio7 = LogOp(17, "Transportation from site to port", [0, 0, 0, 0], 0, 0)
lio8 = LogOp(18, "Demobilisation", [0, 0, 0, 0], 0, 0)

lio_EI1 = LogOp(20, "Cable laying", [0, 0, 0, 0], 0, 0)
lio_EI1 = LogOp(21, "Cable protection", [0, 0, 0, 0], 0, 0)

lio_F1 = LogOp(30,
               "Driven pile foundation seafloor penetration through drilling rig + positioning",
               [0, 0, 0, 0], 0, 0)
lio_F2 = LogOp(31, "Driven pile foundation seafloor penetration through hammering + positioning", [0, 0, 0, 0], 0, 0)
lio_F3 = LogOp(32, "Driven pile foundation seafloor penetration through vibro-driving + positioning", [0, 0, 0, 0], 0, 0)
lio_F4 = LogOp(33, "Gravity based foundation lowering + positioning", [0, 0, 0, 0], 0, 0)
lio_F5 = LogOp(34, "Suction caisson foundation seafloor penetration + positioning", [0, 0, 0, 0], 0, 0)
lio_F6 = LogOp(35, "Support structure positioning", [0, 0, 0, 0], 0, 0)
lio_F7 = LogOp(36, "Equipment removal and grouting", [0, 0, 0, 0], 0, 0)

lio_M1 = LogOp(40, "Driven pile anchor seafloor penetration through drilling rig + positioning", [0, 0, 0, 0], 0, 0)
lio_M2 = LogOp(41, "Driven pile anchor seafloor penetration through hammering + positioning", [0, 0, 0, 0], 0, 0)
lio_M3 = LogOp(42, "Driven pile anchor seafloor penetration through vibro-driving + positioning", [0, 0, 0, 0], 0, 0)
lio_M4 = LogOp(43, "Gravity based anchor lowering + positioning", [0, 0, 0, 0], 0, 0)
lio_M5 = LogOp(44, "Suction caisson seafloor penetration + mooring lines deployment", [0, 0, 0, 0], 0, 0)
lio_M6 = LogOp(45, "Drag-embedment anchor seafloor penetration + mooring lines deployment", [0, 0, 0, 0], 0, 0)
lio_M7 = LogOp(46, "Direct-embedment anchor seafloor penetration through suction-embedment + mooring lines deployment", [0, 0, 0, 0], 0, 0)
lio_M8 = LogOp(47, "Direct-embedment anchor seafloor penetration through jetting-embedment + mooring lines deployment", [0, 0, 0, 0], 0, 0)
lio_M9 = LogOp(48, "Direct-embedment anchor seafloor penetration through mechanical-embedment + mooring lines deployment", [0, 0, 0, 0], 0, 0)

lio_D1 = LogOp(50, "On-site posisitioning and connection of bottom-fixed device", [0, 0, 0, 0], 0, 0)
lio_D2 = LogOp(51, "On-site posisitioning and connection of floating device", [0, 0, 0, 0], 0, 0)
"""
#### Definition of the operation sequences for each logistic phase ###
#lg1.sequence[01] = {1: LogOp(01, "Mobilisation", 0,0,0)}
#
#lg1.sequence[01].update({2: LogOp(01, "transportation",0,0,0)})
#lg1.sequence[02] = LogOp(01, "transportation",0,0,0)
#lg1.sequence[02][1].id
#lg1.sequence[02][1].description
"""
lg4.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_F1, lio_F7, lio6, lio7, lio8]
lg4.ops_sequence[02] = [lio1, lio2, lio3, lio4, lio5, lio_F2, lio_F7, lio6, lio7, lio8]
lg4.ops_sequence[03] = [lio1, lio2, lio3, lio4, lio5, lio_F3, lio_F7, lio6, lio7, lio8]

lg5.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_F5, lio_F7, lio6, lio7, lio8]

lg6.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_F4, lio_F7, lio6, lio7, lio8]

lg7.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_M6, lio6, lio7, lio8]

lg8.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_M7, lio6, lio7, lio8]
lg8.ops_sequence[02] = [lio1, lio2, lio3, lio4, lio5, lio_M8, lio6, lio7, lio8]
lg8.ops_sequence[03] = [lio1, lio2, lio3, lio4, lio5, lio_M9, lio6, lio7, lio8]

lg9.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_F6, lio_F7, lio6, lio7, lio8]

lg10.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_F6, lio_D1, lio6, lio7, lio8]

lg11.ops_sequence[01] = [lio1, lio2, lio3, lio4, lio5, lio_F6, lio_D2, lio6, lio7, lio8]

"""
### Loading inputs ###
"""
# # Set directory paths for loading inputs (@Tecanalia)
mod_path = path.dirname(path.realpath(__file__))


def database_file(file):
    fpath = path.join('databases', '{0}'.format(file))
    db_path = path.join(mod_path, fpath)
    return db_path

# # Load data provided by end-user/WP1
# Load environment data - only metocean sample data is currently available!
    # bathymetry and soil conditions data are missing but will be required!
environment_data = environment.load_data(database_file(
    "VianaCastelo.csv"))
# device type can be "floating" or "bottom fixed"
end_user_inputs = {'device_type': "bottom fixed",
                   'device_length': 100,
                   'device_height': 8,
                   'device_width': 8,
                   'device_drymass': 150000}
# # Load data provided by WP2 (sample data was provided by Francesco Ferri)
#if wp2_df is not None:
#    WP2_outputs = {'WP2': wp2_df}
#else:
wp2_outputs = {'NumOFunits': 4,
               'Position': {'Device0': (0, 0, 30),
                            'Device1': (100, 0, 30),
                            'Device2': (0, 100, 30),
                            'Device3': (100, 100, 30)}}
# # Load data provided by WP3
#if wp3_df is not None:
#    WP3_outputs = {'WP2': wp3_df}
#else:
wp3_outputs = {'electrical layout': "type 1"}
# # Load data provided by WP4 (sample data was provided by Sam Weller)
#if wp4_df is not None:
#    WP4_outputs = {'WP4': wp4_df}
#else:
wp4_outputs = load_csv.load_data_csv(database_file("pileinstallation.csv"))
# # Load WP5 databases
# Load vessel database
vessel_data = vessel.load_data(database_file(
    "Vessel_Database_python.xlsx"))
# Load equipment database
# equipment_data = equipment.load_data(database_file(
#    "Equipment_Database_python.xlsx"))
hammer, drilling_rig = equipment.load_data(database_file(
    "Equipment_Database_python.xlsx"))
# Load port database
port_data = port.load_data(database_file(
    "Ports_Database2_python.xlsx"))
# Load Logistic Phase Sequence data
logSeq_data = phaseSeq.load_data(database_file(
    "InterPhasingSequencing_python.xlsx"))
"""
### Define vessel types by invoking VesselType class
"""
vt1 = VesselType("vt1", "Tug boat", vessel_data[vessel_data['Vessel Type'] == 'Tug'])
vt2 = VesselType("vt2", "Crane barge", vessel_data[vessel_data['Vessel Type'] == 'Crane Barge'])
vt3 = VesselType("vt3", "Crane vessel", vessel_data[vessel_data['Vessel Type'] == 'Crane Vessel'])
vt4 = VesselType("vt4", "Jack-up barge", vessel_data[vessel_data['Vessel Type'] == 'Jack-up barge'])
vt5 = VesselType("vt5", "Jack-up vessel", vessel_data[vessel_data['Vessel Type'] == 'Jack-up vessel'])
vt6 = VesselType("vt6", "AHTS", vessel_data[vessel_data['Vessel Type'] == 'AHTS'])
vt7 = VesselType("vt7", "Multicat", vessel_data[vessel_data['Vessel Type'] == 'Multicat'])
"""
### Define equipment types by invoking Equipment class
"""
eq1 = Equipment("eq1", "hammer", hammer)
eq2 = Equipment("eq2", "drilling rig", drilling_rig)
"""
#### Definition of the V&E combinations for each logistic phase ###
#vesselType = Vessel(01,"vessel",all_vessel)
# vt1= VesselType(01,"CLV",*panda)
"""
lg4.ve_combination[01] = {'vessel': {(1, vt2.id), (2, vt1.id)}, 'equipment': (1, eq1.id)}
lg4.ve_combination[02] = {1: (1, vt3.id), 2: (1, eq1.id)}
lg4.ve_combination[03] = {1: {(1, vt4.id), (2, vt1.id)}, 2: (1, eq1.id)}
lg4.ve_combination[04] = {1: (1, vt5.id), 2: (1, eq1.id)}
lg4.ve_combination[05] = {1: {(1, vt2.id), (2, vt1.id)}, 2: (1, eq2.id)}
lg4.ve_combination[06] = {1: (1, vt3.id), 2: (1, eq2.id)}
lg4.ve_combination[07] = {1: {(1, vt4.id), (2, vt1.id)}, 2: (1, eq2.id)}
lg4.ve_combination[08] = {1: (1, vt5.id), 2: (1, eq2.id)}

lg5.ve_combination[01] = {1: {(1, vt2.id), (2, vt1.id)}}
lg5.ve_combination[02] = {1: (1, vt3.id)}
lg5.ve_combination[03] = {1: {(1, vt4.id), (2, vt1.id)}}
lg5.ve_combination[04] = {1: (1, vt5.id)}
lg5.ve_combination[05] = {1: {(1, vt2.id), (2, vt1.id)}}
lg5.ve_combination[06] = {1: (1, vt3.id)}
lg5.ve_combination[07] = {1: {(1, vt4.id), (2, vt1.id))}
lg5.ve_combination[08] = {1: (1, vt5.id)}

lg6.ve_combination[01] = {1: {(1, vt2.id), (2, vt1.id)}}
lg6.ve_combination[02] = {1: (1, vt3.id)}
lg6.ve_combination[03] = {1: {(1, vt4.id), (2, vt1.id)}}
lg6.ve_combination[04] = {1: (1, vt5.id)}
lg6.ve_combination[05] = {1: {(1, vt2.id), (2, vt1.id)}}
lg6.ve_combination[06] = {1: (1, vt3.id)}
lg6.ve_combination[07] = {1: {(1, vt4.id), (2, vt1.id))}
lg6.ve_combination[08] = {1: (1, vt5.id)}
"""
### Define comprehensive list of logistic interphase sequences
"""
# Dictionaries are great to access data of different hierarchy types such as
# the interphase sequence one, an example is shown bellow.
# e.g. logPhaseSeq['Dev 1']['EL 2']['FT 2']
# Probably not needed in the end!!!
#logPhaseSeq = {'Dev 1': {'EL 1': {'FT 1': logSeq_data,
#                                  'FT 2': logSeq_data,
#                                  'FT 3': logSeq_data,
#                                  'FT 4': logSeq_data,
#                                  'FT 5': logSeq_data,
#                                  'FT 6': logSeq_data},
#                         'EL 2': {'FT 1': logSeq_data,
#                                  'FT 2': logSeq_data,
#                                  'FT 3': logSeq_data,
#                                  'FT 4': logSeq_data,
#                                  'FT 5': logSeq_data,
#                                  'FT 6': logSeq_data},
#                         'EL 3': {'FT 1': logSeq_data,
#                                  'FT 2': logSeq_data,
#                                  'FT 3': logSeq_data,
#                                  'FT 4': logSeq_data,
#                                  'FT 5': logSeq_data,
#                                  'FT 6': logSeq_data},
#                         'EL 4': {'FT 1': logSeq_data,
#                                  'FT 2': logSeq_data,
#                                  'FT 3': logSeq_data,
#                                  'FT 4': logSeq_data,
#                                  'FT 5': logSeq_data,
#                                  'FT 6': logSeq_data},
#                         },
#               }
"""
### Determine the adequate installation logistic phase sequence
"""
install_seq = planning.install_plan(end_user_inputs, wp3_outputs, wp4_outputs)
"""
### Determine the adequate installation logistic phase sequence
"""
# ###### TO-DO-TO-DO-TO-DO-TO-DO-TO-DO-TO-DO !!!
install_port = select_port.install_port((end_user_inputs, wp3_outputs, wp4_outputs))

#
## # assess sequentially each logistic phase of the installation process
#for x in install_seq:
#    
#    # Execute WP5 functions sequentially
#    log_pre_sol = predefined.predef_sol_log(log_phase_id)
#    log_req = requirements.logistic_requirements(log_phase_id,
#                                                 environment_data,
#                                                 technology_data)
#
#    equipSol = select.equipmentSelecLog(log_pre_sol, log_req, equipment_data)
#    vesselSol = select.vesselSelecLog(log_pre_sol, log_req, vessel_data)
#    portSol = select.portSelecLog(log_pre_sol, log_req, port_data)
#
#    log_sol = match.matching(equipSol,vesselSol,portSol)
#
#    log_sched = scheduleLog.schedule_log(log_phase_id,
#                                         log_sol,
#                                         environment_data,
#                                         distances)
#                                         
#    log_cost = costLog.cost_log(log_phase_id, log_sol, log_sched)
#
#    # TODO
#    # log_envir = environmentLog()
#    # logRisk = riskLogistics()
#
#    return (environment_data,
#            technology_data,
#            equipment_data,
#            vessel_data,
#            log_pre_sol,
#            log_req,
#            equipSol,
#            vesselSol,
#            portSol,
#            log_sol,
#            log_sched,
#            log_cost) # for visualization purposes
    
    

