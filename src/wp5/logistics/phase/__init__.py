# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module governs the definition of the logistic phases. The functions included
are responsible to initialize and characterize the logistic phases both of the
installation and O&M modules. The functions return a class of each logistic phase
characterized in terms of operations sequence and vessel & equipment combination.

BETA VERSION NOTES: In this version, only two logistic phases were characterized,
one related to Moorings and Foundation Installation: Driven Pile, and another
related to Operation and Maintenance: Offshore Inspection.
"""

from .classes import LogPhase, DefPhase
from .f_driven import initialize_f_drive_phase


def logPhase_install_init(log_op, vessels, equipments):
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
    log_op : dict
     dictionnary containing all classes defining the individual logistic operations
    vessels : DataFrame
     Panda table containing the vessel database
    equipments : DataFrame
     Panda table containing the equipment database

    Returns
    -------
    logPhase_install : dict
     dictionnary containing all classes defining the logistic phases for installation
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_install = {'E_export': LogPhase(100, "Installation of static subsea export power cables"),
                        'E_array': LogPhase(101, "Installation of static subsea inter-array power cables"),
                        'E_cp': LogPhase(102, "Installation of offshore electrical collection point"),

                        'F_driven': initialize_f_drive_phase(log_op, vessels, equipments),
                        'F_suction': LogPhase(111, "Installation of suction caissons for foundation systems"),
                        'F_gravity': LogPhase(112, "Installation of gravity based foundations"),

                        'M_drag': LogPhase(113, "Installation of mooring systems with drag-embedment anchors"),
                        'M_direct': LogPhase(114, "Installation of mooring systems with direct-embedment anchors"),

                        'D_fixed': LogPhase(120, "Installation of bottom fixed devices"),
                        'D_floating': LogPhase(121, "Installation of floating devices")
                        }


    # 2nd Level - Define the diferent operations sequence and corresponding V&E combination for each Phase



    return logPhase_install


def logPhase_OM_init(log_op, vessels, equipments):
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
    log_op : dict
     dictionnary containing all classes defining the individual logistic operations
    vessels : DataFrame
     Panda table containing the vessel database
    equipments : DataFrame
     Panda table containing the equipment database

    Returns
    -------
    logPhase_OM : dict
     dictionnary containing all classes defining the logistic phases for O&M
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_OM = {'insp': LogPhase(900, "O&M top-side maintenance")}

    # 2nd Level - Define the diferent operations sequence and corresponding v&e combination for each Phase

    logPhase_OM['insp'].op_ve[0] = DefPhase(1, 'inps')

    logPhase_OM['insp'].op_ve[0].op_sequence = [log_op["op1"],
                                                log_op["op2"],
                                                log_op["op3"],
                                                log_op["op4"],
                                                log_op["op_OM1"],
                                                log_op["op7"],
                                                log_op["op8"]]

    logPhase_OM['insp'].op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['CTV'])],
                                                      'equipment': [(0, 0, 0)]}

    logPhase_OM['insp'].op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                                      'equipment': [(0, 0, 0)]}

    return logPhase_OM
