from .classes import DefPhase, LogPhase


def initialize_d_fixed_phase(log_op, vessels, equipments):
    phase = LogPhase(120, "Installation of bottom fixed devices")

    phase.op_ve[0] = DefPhase(1, 'TransportDeck')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["DeckTrans"],
                                  log_op["PosBFdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['JUP Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Construction Support Vessel']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}
                                        
    phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}
                                        
    phase.op_ve[0].ve_combination[4] = {'vessel': [(1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}
                                        
    phase.op_ve[0].ve_combination[5] = {'vessel': [(1, vessels['JUP Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}
                                        
                                        
                                        

    phase.op_ve[1] = DefPhase(2, 'TransportTowingQuay')
    phase.op_ve[1].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["TowTrans"],
                                  log_op["PosBFdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]
                                  
    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}







    phase.op_ve[2] = DefPhase(3, 'TransportTowingDryDock')
    phase.op_ve[2].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["TowTrans"],
                                  log_op["PosBFdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]


    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}



    return phase
