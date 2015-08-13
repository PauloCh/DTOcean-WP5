
"""
phase.py is the file governing the definition of the logistic phases

"""

class LogPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.ops_sequence = {}
#        self.feasibility = feasiblity
#        self.matching = matching
#        self.v&e&p_selected = {}
#        self.schedule = {}
#        self.time = {}
#        self.cost = {}
#        self.environmental = environment
#        self.risk = risk

    def set_sequence(self, key, ops_sequence):
        self.ops_sequence[key] = ops_sequence

#    def vessel_feasiblity(self, wp1_BoM, wp2_BoM, wp3_BoM,
#                          wp4_BoM, vessels):
#        if self.id == 100 or 101 or 102:
#            deck_loading = 0
#            deck_area = 0
#        elif self.id == 110 or 111 or 112:
#            for dev in range(wp2_BoM['numUnits'].ix[0]):
#                for x in range(wp4_BoM['quantity'].ix[0]):
#                    key1 = "diameter foundation " + str(x) + " [m]"
#                    key2 = "length foundation " + str(x) + " [m]"
#                    key3 = "weight foundation " + str(x) + " [kg]"
#                    load_u_f[len(load_u_f):] = [wp4_BoM[key1].ix[0]*wp4_BoM[key2].ix[0]/wp4_BoM[key3].ix[0]]
#                    area_u_f[len(area_u_f):] = [wp4_BoM[key1].ix[0]*wp4_BoM[key2].ix[0]]
#                load_u[len(load_u):] = max(load_u_f[dev*x:(dev+1)*x])
#                area_u[len(area_u):] = sum(area_u_f[dev*x:(dev+1)*x])
#            deck_loading = max(load_u)
#            deck_area = max(area_u)
#
#        return deck_loading, deck_area


#class FeasiblityPhase(LogPhase):
#
#    def __init__(self, id, description, ops_sequence, ve_combination, feasibility):
#        super(FeasiblityPhase, self).__init__(id, description,
#                                                 ops_sequence, ve_combination)
#        self.feasibility = feasibility


class OPsequence(object):

    def __init__(self, id, description, op_sequence):
        self.id = id
        self.description = description
        self.op_sequence = op_sequence
        self.ve_combination = {}

    def set_combination(self, key, ve_combination):
        self.ve_combination[key] = ve_combination

#    def set_feasibility(self, key, vessel_funct, equipm_funct, port_funct):
#        self.vessel = vessel_funct
#        self.equipment = equipm_funct
#        self.port = port_funct

"""
#### Definition of the logistic pahase by invocaking the class LogPhase #######
# Invocation of the full list of logistic phases covered in WP5
# Explanation of the key ID numbering system implemented:
# 1st digit:  1 = Installation;
#             9 = O&M
# 2nd digit: 0 = Electrical infrastructure;
#            1 = Moorings and foundations;
#            2 = Wave and Tidal devices;
# 3rd digit: component/sub-system type - differ depending on the logistic phase
# 4th digit: method (level 1) - differ depending on the logistic phase
# 5th digit: sub-method (level 2) - differ depending on the logistic phase
####
"""

def logPhase_install_init(logOp, vessels, equipments):

    """
    1st Level - Initialize the logistic phases through LogPhase classes
    """
    logPhase_install = {'E_export' : LogPhase(100, "Installation of static subsea export power cables"),
                        'E_array'  : LogPhase(101, "Installation of static subsea inter-array power cables"),
                        'E_cp'     : LogPhase(102, "Installation of offshore electrical collection point"),

                        'F_driven'  : LogPhase(110, "Installation of driven piles foundations"),
                        'F_suction' : LogPhase(111, "Installation of suction caissons for foundation systems"),
                        'F_gravity' : LogPhase(112, "Installation of gravity based foundations"),

                        'M_drag'   : LogPhase(113, "Installation of mooring systems with drag-embedment anchors"),
                        'M_direct' : LogPhase(114, "Installation of mooring systems with direct-embedment anchors"),

                        'D_fixed'    : LogPhase(120, "Installation of bottom fixed devices"),
                        'D_floating' : LogPhase(121, "Installation of floating devices")
                        }

    """
    2nd Level - Define the diferent operations sequence for each logistic phase
    """

    logPhase_install['F_driven'].set_sequence('01', OPsequence(1,'Drilling',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F1"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_driven'].set_sequence('02', OPsequence(2,'Hammering',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F2"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_driven'].set_sequence('03', OPsequence(3,'Vibro-Pilling',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F3"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_suction'].set_sequence('01', OPsequence(1,'Suction',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F5"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_gravity'].set_sequence('01', OPsequence(1,'gravity',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F4"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_drag'].set_sequence('01', OPsequence(1,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M6"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_direct'].set_sequence('01', OPsequence(1,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_direct'].set_sequence('02', OPsequence(2,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M8"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_direct'].set_sequence('03', OPsequence(3,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M9"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['D_fixed'].set_sequence('01', OPsequence(1,'fixed',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_D1"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['D_floating'].set_sequence('01', OPsequence(1,'floating',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_D2"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    """
    3rd Level - Define the  diferent vessel and equipment combination for each logistic phase
    """

    logPhase_install['F_driven'].ops_sequence['01'].set_combination(1,
                    {'vessel':{(1, vessels['Crane Barge']), (2, vessels['Tugboat'])},
                     'equipment':(1, equipments['Hammer'])})
#    logPhase_install['F_driven'].set_combination(2, {'vessel': (1, vessels['Crane Vessel']),
#                                                       'equipment': (1, equipments['Hammer'])})
#    logPhase_install['F_driven'].set_combination(3, {'vessel': {(1, vessels['JUP Barge']), (2, vessels['Tugboat'])},
#                                                       'equipment': (1, equipments['Hammer'])})
#    logPhase_install['F_driven'].set_combination(4, {'vessel': (1, vessels['JUP Vessel']),
#                                                       'equipment': (1, equipments['Hammer'])})
#    logPhase_install['F_driven'].set_combination(5, {'vessel': {(1, vessels['Crane Barge']), (2, vessels['Tugboat'])},
#                                                       'equipment': (1, equipments['Drill Rig'])})
#    logPhase_install['F_driven'].set_combination(6, {'vessel': (1, vessels['Crane Vessel']),
#                                                       'equipment': (1, equipments['Drill Rig'])})
#    logPhase_install['F_driven'].set_combination(7, {'vessel': {(1, vessels['JUP Barge']), (2, vessels['Tugboat'])},
#                                                       'equipment': (1, equipments['Drill Rig'])})
#    logPhase_install['F_driven'].set_combination(8, {'vessel': (1, vessels['JUP Vessel']),
#                                                       'equipment': (1, equipments['Drill Rig'])})


    return logPhase_install,

def logPhase_OM_init(logOp, vessels, equipments):

    """
    Initialize the logistic phases through LogPhase classes
    """

    logPhase_OM = {'insp' : LogPhase(900, "O&M offshore intervention")}


    """
    Define the diferent operations sequence for each logistic phase
    """



    """
    Define the diferent vessel and equipment combination for each logistic phase
    """

    return logPhase_OM