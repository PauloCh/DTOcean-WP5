from .classes import DefPhase, LogPhase


def initialize_d_floating_phase(log_op, vessels, equipments):
    phase = LogPhase(121, "Installation of floating devices")

    phase.op_ve[0] = DefPhase(1, 'TransportDeck')
    phase.op_ve[0].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_DQ1"],
                                  log_op["op_DON2"],
                                  log_op["op_DF3"],
                                  log_op["op_DF4"],
                                  log_op["op_D5"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Jack-up Vessel']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Construction Support Vessel']), (2, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}
                                        
    phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}
                                        
    phase.op_ve[0].ve_combination[4] = {'vessel': [(1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}
                                        
    phase.op_ve[0].ve_combination[5] = {'vessel': [(1, vessels['Jack-up Barge']), (1, vessels['Tugboat']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}
                                        
                                        
                                        

    phase.op_ve[1] = DefPhase(2, 'TransportTowingQuay')
    phase.op_ve[1].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_DQ1"],
                                  log_op["op_DTT2"],
                                  log_op["op_DF3"],
                                  log_op["op_DF4"],
                                  log_op["op_D5"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]
                                  
    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling Vessel']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}







    phase.op_ve[2] = DefPhase(3, 'TransportTowingDryDock')
    phase.op_ve[2].op_sequence = [log_op["op1"],
                                  log_op["op2"],
                                  log_op["op3"],
                                  log_op["op4"],
                                  log_op["op5"],
                                  log_op["op_DDD1"],
                                  log_op["op_DTT2"],
                                  log_op["op_DF3"],
                                  log_op["op_DF4"],
                                  log_op["op_D5"],
                                  log_op["op6"],
                                  log_op["op7"],
                                  log_op["op8"]]


    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling Vessel']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Mulitcat'])],
                                        'equipment': [(1, equipments['Rov inspection'], 0), (1, equipments['Divers'], 0)]}



    return phase

    return phase
