from .classes import DefPhase, LogPhase


def initialize_f_suction_phase(log_op, vessels, equipments):
    phase = LogPhase(111, "Installation of suction caissons for foundation systems")

    phase.op_ve[0] = DefPhase(1, 'Suction')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["SuctCais"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]


    #??????????????????????????
    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}


    return phase
