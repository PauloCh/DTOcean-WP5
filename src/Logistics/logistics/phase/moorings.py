from .classes import DefPhase, LogPhase


def initialize_moorings_phase(log_op, vessels, equipments):
    phase = LogPhase(114, "Installation of mooring systems with direct-embedment anchors")

    phase.op_ve[0] = DefPhase(1, 'Deploy direct-embedment anchor by suction-embedment')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DirecSuct"],
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
                                        
                                        
                                        
                                  
                                  
                                  
                                        
    phase.op_ve[1] = DefPhase(2, 'Deploy direct-embedment anchor by jetting-embedment')
    phase.op_ve[1].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DirecJet"],
                                  log_op["Tensng"],
                                  log_op["PreLay"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}
                                        
                                        
         


                               
                                        
    phase.op_ve[2] = DefPhase(3, 'Deploy direct-embedment anchor by mechanical-embedment')
    phase.op_ve[2].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DirecMech"],
                                  log_op["Tensng"],
                                  log_op["PreLay"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}
                                        


    phase.op_ve[3] = DefPhase(4, 'Deploy drag-embedment anchor')
    phase.op_ve[3].op_sequence = [log_op["Mob"],
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

    phase.op_ve[3].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[3].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[3].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}



    phase.op_ve[4] = DefPhase(5, 'Installation of suction caissons')
    phase.op_ve[4].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["SuctCais"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]


    phase.op_ve[4].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[4].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[4].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[4].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}


    return phase
