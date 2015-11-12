from .classes import DefPhase, LogPhase


def initialize_f_suction_phase(log_op, vessels, equipments):
    phase = LogPhase(111, "Installation of suction caissons for foundation systems")

    phase.op_ve[0] = DefPhase(1, 'Suction')
    phase.op_ve[0].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M5"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]


    #??????????????????????????
    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['Drill Rig'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                        'equipment': [(1, equipments['Drill Rig'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['Drill Rig'], 0)]}

    phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                        'equipment': [(1, equipments['Drill Rig'], 0)]}


    return phase
