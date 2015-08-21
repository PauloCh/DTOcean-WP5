# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module governs the definition of the logistic phases. The functions included
in this module are responsible to initialize and characterize the logistic phases
both of the installation and O&M modules. These functions return each logistic phase
characterized in terms of operations sequence and vesse & equipment combination.

BETA VERSION NOTES: In this version, only two logistic phases were characterized,
one related to Moorings and Foundation Installation: Driven Pile, and another
related to Operation and Maintenance: Offshore Inspection.
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
        self.sol = {}


class VE_solutions(object):

    def __init__(self, id):
        self.id = id
        self.sol_ves = {}
        self.sol_eq = {}
        self.schedule = {}
        self.cost = {}


def logPhase_install_init(logOp, vessels, equipments):
    """This function initializes and characterizes all logistic phases associated
    with the installation module. The first step uses LogPhase class to initialize
    each class with a key ID and description, the second step uses the DefPhase
    class to characterize each phase with a set of operation sequences and vessel
    and equipment combinations.
    Explanation of the key ID numbering system implemented:
     1st digit: 1 = Installation;
                9 = O&M
     2nd digit: 0 = Electrical infrastructure;
                1 = Moorings and foundations;
                2 = Wave and Tidal devices;
     3rd digit: component/sub-system type - differ depending on the logistic phase
     4th digit: method (level 1) - differ depending on the logistic phase
     5th digit: sub-method (level 2) - differ depending on the logistic phase

    Parameters
    ----------
    logOp : dict
     among other data contains the feasibility requirements of vessels
    vessels : dict
     contains data regarding the vessel and equipment combinations specific of
     each operation sequence of the logistic phase
    equipments : dict
     contains data regarding the vessel and equipment combinations specific of
     each operation sequence of the logistic phase

    Returns
    -------
    logPhase_install : class
     A dict of panda dataframes with all the feasibile vessels
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

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


    # 2nd Level - Define the diferent operations sequence and corresponding V&E combination for each Phase

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
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                               'equipment': [(1, equipments['Drill Rig'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    logPhase_install['F_driven'].op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                                               'equipment': [(1, equipments['Hammer'], 0)]
                                                               }

    return logPhase_install


def logPhase_OM_init(logOp, vessels, equipments):
    """This function initializes and characterizes all logistic phases associated
    with the O&M module. The first step uses LogPhase class to initialize
    each class with a key ID and description, the second step uses the DefPhase
    class to characterize each phase with a set of operation sequences and vessel
    and equipment combinations.
    Explanation of the key ID numbering system implemented:
     1st digit: 1 = Installation;
                9 = O&M
     2nd digit: 0 = Electrical infrastructure;
                1 = Moorings and foundations;
                2 = Wave and Tidal devices;
     3rd digit: component/sub-system type - differ depending on the logistic phase
     4th digit: method (level 1) - differ depending on the logistic phase
     5th digit: sub-method (level 2) - differ depending on the logistic phase

    Parameters
    ----------
    logOp : dict
     among other data contains the feasibility requirements of vessels
    vessels : dict
     contains data regarding the vessel and equipment combinations specific of
     each operation sequence of the logistic phase
    equipments : dict
     contains data regarding the vessel and equipment combinations specific of
     each operation sequence of the logistic phase

    Returns
    -------
    logPhase_OM : class
     A dict of panda dataframes with all the feasibile vessels
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_OM = {'insp': LogPhase(900, "O&M top-side maintenance")}


    # 2nd Level - Define the diferent operations sequence and corresponding v&e combination for each Phase

    logPhase_OM['insp'].op_ve[0] = DefPhase(1, 'inps')

    logPhase_OM['insp'].op_ve[0].op_sequence = [logOp["op1"],
                                                logOp["op2"],
                                                logOp["op3"],
                                                logOp["op4"],
                                                logOp["op_OM1"],
                                                logOp["op7"],
                                                logOp["op8"]]

    logPhase_OM['insp'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(0, 0, 0)]
                                                      }

    logPhase_OM['insp'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(0, 0, 0)]
                                                      }

    return logPhase_OM
