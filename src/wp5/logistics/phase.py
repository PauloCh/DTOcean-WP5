
"""
phase.py is the file governing the definition of the logistic phases

"""


class LogPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.op_ve = {}
#        self.feasibility = feasiblity
#        self.matching = matching
#        self.v&e&p_selected = {}
#        self.schedule = {}
#        self.time = {}
#        self.cost = {}
#        self.environmental = environment
#        self.risk = risk


class DefPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.op_sequence = {}
        self.ve_combination = {}


"""
#### Definition of the logistic pahase by invoking the class LogPhase #######
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
    logPhase_install = {'E_export': LogPhase(100, "Installation of static subsea export power cables"),
                        'E_array': LogPhase(101, "Installation of static subsea inter-array power cables"),
                        'E_cp': LogPhase(102, "Installation of offshore electrical collection point"),

                        'F_driven': LogPhase(110, "Installation of driven piles foundations"),
                        'F_suction': LogPhase(111, "Installation of suction caissons for foundation systems"),
                        'F_gravity': LogPhase(112, "Installation of gravity based foundations"),

                        'M_drag': LogPhase(113, "Installation of mooring systems with drag-embedment anchors"),
                        'M_direct': LogPhase(114, "Installation of mooring systems with direct-embedment anchors"),

                        'D_fixed': LogPhase(120, "Installation of bottom fixed devices"),
                        'D_floating': LogPhase(121, "Installation of floating devices")
                        }

    """
    2nd Level - Define the diferent operations sequence and corresponding v&e combination for each Phase
    """

    logPhase_install['F_driven'].op_ve[0] = DefPhase(1, 'Drilling')
    logPhase_install['F_driven'].op_ve[1] = DefPhase(2, 'Hammering')
    logPhase_install['F_driven'].op_ve[2] = DefPhase(3, 'Vibro Pilling')


    logPhase_install['F_driven'].op_ve[0].op_sequence = [logOp["op1"],
                                                                    logOp["op2"],
                                                                    logOp["op3"],
                                                                    logOp["op4"],
                                                                    logOp["op5"],
                                                                    logOp["op_F1"],
                                                                    logOp["op_F7"],
                                                                    logOp["op6"],
                                                                    logOp["op7"],
                                                                    logOp["op8"]]

    logPhase_install['F_driven'].op_ve[1].op_sequence = [logOp["op1"],
                                                         logOp["op2"],
                                                         logOp["op3"],
                                                         logOp["op4"],
                                                         logOp["op5"],
                                                         logOp["op_F2"],
                                                         logOp["op_F7"],
                                                         logOp["op6"],
                                                         logOp["op7"],
                                                         logOp["op8"]]

    logPhase_install['F_driven'].op_ve[2].op_sequence = [logOp["op1"],
                                                         logOp["op2"],
                                                         logOp["op3"],
                                                         logOp["op4"],
                                                         logOp["op5"],
                                                         logOp["op_F3"],
                                                         logOp["op_F7"],
                                                         logOp["op6"],
                                                         logOp["op7"],
                                                         logOp["op8"]]

    logPhase_install['F_driven'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Drill Rig'])]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                               'equipment': [(1, equipments['Drill Rig'])]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Drill Rig'])]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                               'equipment': [(1, equipments['Drill Rig'])]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Hammer'])]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                               'equipment': [(1, equipments['Hammer'])]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Hammer'])]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                               'equipment': [(1, equipments['Hammer'])]
                                                               }


    return logPhase_install


def logPhase_OM_init(logOp, vessels, equipments):

    """
    Initialize the logistic phases through LogPhase classes
    """

    logPhase_OM = {'insp': LogPhase(900, "O&M offshore intervention")}

    return logPhase_OM
