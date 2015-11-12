from .classes import DefPhase, LogPhase


def initialize_m_direct_phase(log_op, vessels, equipments):
    phase = LogPhase(114, "Installation of mooring systems with direct-embedment anchors")

    phase.op_ve[0] = DefPhase(1, 'Deploy direct-embedment anchor by suction-embedment')
    phase.op_ve[0].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M7"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}
                                        
                                        
                                        
                                  
                                  
                                  
                                        
    phase.op_ve[1] = DefPhase(2, 'Deply direct-embedment anchor by jetting-embedment')
    phase.op_ve[1].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M8"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]

    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}
                                        
                                        
         


                               
                                        
    phase.op_ve[2] = DefPhase(3, 'Deply direct-embedment anchor by mechanical-embedment')
    phase.op_ve[2].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M9"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]

    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0)]}
                                        
                                        

    return phase
