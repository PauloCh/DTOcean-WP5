from .classes import DefPhase, LogPhase


def initialize_f_gravity_phase(log_op, vessels, equipments):
    phase = LogPhase(112, "Installation of gravity based foundations")

    phase.op_ve[0] = DefPhase(1, 'Gravity based anchor installation with on deck transportation')
    phase.op_ve[0].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M4"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]


    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Construction Support Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}



                                        
                                        

    phase.op_ve[1] = DefPhase(2, 'Gravity based anchor installation with on deck transportation for array installation')
    phase.op_ve[1].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M4"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]


    phase.op_ve[1].ve_combination[0] = {'vessel': [ (1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat']) ],
                                        'equipment': [(1, equipments['divers'], 0), (1, equipments['rov'], 0) ]
                                        }

    phase.op_ve[1].ve_combination[1] = {'vessel': [ (1, vessels['Crane Barge']), (2, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [ (1, equipments['Floating crane'], 0), (1, equipments['rov'], 0) ]
                                        }

    phase.op_ve[1].ve_combination[2] = {'vessel': [ (1, vessels['Platform Support Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [(1, equipments['Floating crane'], 0), (1, equipments['rov'], 0) ]
                                        }
                                        
                                        
                                        
                                        
                                        
                                                
                                        
    phase.op_ve[2] = DefPhase(3, 'Gravity based anchor installation with towing transportation')
    phase.op_ve[2].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_M4"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]

    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(3, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}




    return phase
