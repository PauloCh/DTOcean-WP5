from .classes import DefPhase, LogPhase


def initialize_m_drag_phase(log_op, vessels, equipments):
    phase = LogPhase(113, "Installation of mooring systems with drag-embedment anchors")

    phase.op_ve[0] = DefPhase(1, 'Deploy drag-embedment anchor')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DragEmbed"],
                                  log_op["Tensng"],
                                  log_op["PreLay"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}


    return phase
