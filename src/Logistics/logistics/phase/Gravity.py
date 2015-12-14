from .classes import DefPhase, LogPhase


def initialize_gravity_phase(log_op, vessels, equipments, MF_outputs):
    phase = LogPhase(112, "Installation of gravity based foundations")

    phase.op_ve[0] = DefPhase(1, 'Gravity based anchor installation with on deck transportation')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["GBSpos"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]


    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Construction Support Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}



                                        
                                        

    phase.op_ve[1] = DefPhase(2, 'Gravity based anchor installation with on deck transportation for array installation')
    phase.op_ve[1].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["GBSpos"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]


    phase.op_ve[1].ve_combination[0] = {'vessel': [ (1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat']) ],
                                        'equipment': [(1, equipments['divers'], 0), (1, equipments['rov'], 0) ]
                                        }

    phase.op_ve[1].ve_combination[1] = {'vessel': [ (1, vessels['Crane Barge']), (2, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [ (1, equipments['rov'], 0) ]
                                        }

    phase.op_ve[1].ve_combination[2] = {'vessel': [ (1, vessels['Platform Support Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [(1, equipments['rov'], 0) ]
                                        }
                                        
                                        
                                        
                                        
                                        
                                                
                                        
    phase.op_ve[2] = DefPhase(3, 'Gravity based anchor installation with towing transportation')
    phase.op_ve[2].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["GBSpos"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(3, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}




    return phase
