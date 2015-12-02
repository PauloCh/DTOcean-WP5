from .classes import DefPhase, LogPhase


def initialize_devices_phase(log_op, vessels, equipments):
    phase = LogPhase(121, "Installation of devices")

    phase.op_ve[0] = DefPhase(1, 'Floating_TransportDeck_Lifted')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["LoadOut_Lift"],
                                  log_op["DeckTrans"],
                                  log_op["PosFLTdev"],
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



                                        
    phase.op_ve[1] = DefPhase(2, 'Floating_TransportDeck_Skidded')
    phase.op_ve[1].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["LoadOut_Skidded"],
                                  log_op["DeckTrans"],
                                  log_op["PosFLTdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['JUP Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Construction Support Vessel']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[4] = {'vessel': [(1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[5] = {'vessel': [(1, vessels['JUP Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}




    phase.op_ve[2] = DefPhase(3, 'Floating_TransportTowingQuay_Lifted')
    phase.op_ve[2].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["LoadOut_Lift"],
                                  log_op["TowTrans"],
                                  log_op["PosFLTdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]
                                  
    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}




    phase.op_ve[3] = DefPhase(4, 'Floating_TransportTowingQuay_Skidded')
    phase.op_ve[3].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["LoadOut_Skidded"],
                                  log_op["TowTrans"],
                                  log_op["PosFLTdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[3].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[3].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[3].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}





    phase.op_ve[4] = DefPhase(5, 'Floating_TransportTowingDryDock')
    phase.op_ve[4].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["DevAssPort"],
                                  log_op["TowTrans"],
                                  log_op["PosFLTdev"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]


    phase.op_ve[4].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[4].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[4].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}




    phase.op_ve[5] = DefPhase(6, 'BottomFixed_TransportDeck')
    phase.op_ve[5].op_sequence = [log_op["Mob"],
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

    phase.op_ve[5].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[5].ve_combination[1] = {'vessel': [(1, vessels['JUP Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[5].ve_combination[2] = {'vessel': [(1, vessels['Construction Support Vessel']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[5].ve_combination[3] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[5].ve_combination[4] = {'vessel': [(1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[5].ve_combination[5] = {'vessel': [(1, vessels['JUP Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}




    phase.op_ve[6] = DefPhase(7, 'BottomFixed_TransportTowingQuay')
    phase.op_ve[6].op_sequence = [log_op["Mob"],
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

    phase.op_ve[6].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[6].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[6].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}







    phase.op_ve[7] = DefPhase(8, 'BottomFixed_TransportTowingDryDock')
    phase.op_ve[7].op_sequence = [log_op["Mob"],
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


    phase.op_ve[7].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[7].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[7].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}







    return phase

