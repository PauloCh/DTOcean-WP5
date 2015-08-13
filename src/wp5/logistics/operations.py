
"""
operations.py is the file governing the definition of the logistic operations

operations.py defines all individual logistic operations considered within the
DTOcean tool.
"""


class LogOp(object):

    def __init__(self, id, description, olc, time, cost):
        self.id = id
        self.description = description
        self.olc = olc
        self.time = time
        self.cost = cost

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


def logOp_init():

    logOp = {"op1": LogOp(10, "Mobilisation", [0, 0, 0, 0], 0, 0),
             "op2": LogOp(11, "Assembly at port", [0, 0, 0, 0], 0, 0),
             "op3": LogOp(13, "Vessel preparation and loading", [0, 0, 0, 0], 0, 0),
             "op4": LogOp(10, "Mobilisation", [0, 0, 0, 0], 0, 0),
             "op5": LogOp(15, "Seafloor and equipment preparation on-site", [0, 0, 0, 0], 0, 0),
             "op6": LogOp(16, "Transportation from site to site", [0, 0, 0, 0], 0, 0),
             "op7": LogOp(17, "Transportation from site to port", [0, 0, 0, 0], 0, 0),
             "op8": LogOp(18, "Demobilisation", [0, 0, 0, 0], 0, 0),

             "op_EI1": LogOp(20, "Cable laying", [0, 0, 0, 0], 0, 0),
             "op_EI2": LogOp(21, "Cable protection", [0, 0, 0, 0], 0, 0),

             "op_F1": LogOp(30, "Driven pile foundation seafloor penetration through drilling rig + positioning", [0, 0, 0, 0], 0, 0),
             "op_F2": LogOp(31, "Driven pile foundation seafloor penetration through hammering + positioning", [0, 0, 0, 0], 0, 0),
             "op_F3": LogOp(32, "Driven pile foundation seafloor penetration through vibro-driving + positioning", [0, 0, 0, 0], 0, 0),
             "op_F4": LogOp(33, "Gravity based foundation lowering + positioning", [0, 0, 0, 0], 0, 0),
             "op_F5": LogOp(34, "Suction caisson foundation seafloor penetration + positioning", [0, 0, 0, 0], 0, 0),
             "op_F6": LogOp(35, "Support structure positioning", [0, 0, 0, 0], 0, 0),
             "op_F7": LogOp(36, "Equipment removal and grouting", [0, 0, 0, 0], 0, 0),

             "op_M1": LogOp(40, "Driven pile anchor seafloor penetration through drilling rig + positioning", [0, 0, 0, 0], 0, 0),
             "op_M2": LogOp(41, "Driven pile anchor seafloor penetration through hammering + positioning", [0, 0, 0, 0], 0, 0),
             "op_M3": LogOp(42, "Driven pile anchor seafloor penetration through vibro-driving + positioning", [0, 0, 0, 0], 0, 0),
             "op_M4": LogOp(43, "Gravity based anchor lowering + positioning", [0, 0, 0, 0], 0, 0),
             "op_M5": LogOp(44, "Suction caisson seafloor penetration + mooring lines deployment", [0, 0, 0, 0], 0, 0),
             "op_M6": LogOp(45, "Drag-embedment anchor seafloor penetration + mooring lines deployment", [0, 0, 0, 0], 0, 0),
             "op_M7": LogOp(46, "Direct-embedment anchor seafloor penetration through suction-embedment + mooring lines deployment", [0, 0, 0, 0], 0, 0),
             "op_M8": LogOp(47, "Direct-embedment anchor seafloor penetration through jetting-embedment + mooring lines deployment", [0, 0, 0, 0], 0, 0),
             "op_M9": LogOp(48, "Direct-embedment anchor seafloor penetration through mechanical-embedment + mooring lines deployment", [0, 0, 0, 0], 0, 0),

             "op_D1": LogOp(50, "On-site posisitioning and connection of bottom-fixed device", [0, 0, 0, 0], 0, 0),
             "op_D2": LogOp(51, "On-site posisitioning and connection of floating device", [0, 0, 0, 0], 0, 0)
             }

    return logOp
