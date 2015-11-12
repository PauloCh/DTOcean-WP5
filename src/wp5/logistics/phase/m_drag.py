from .classes import DefPhase, LogPhase


def initialize_m_drag_phase(log_op, vessels, equipments):
    phase = LogPhase(113, "Installation of mooring systems with drag-embedment anchors")

    phase.op_ve[0] = DefPhase(1, 'Deploy drag-embedment anchor')
    phase.op_ve[0].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M6"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}
                                        

    return phase
