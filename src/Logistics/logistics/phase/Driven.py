from .classes import DefPhase, LogPhase


def initialize_drive_phase(log_op, vessels, equipments):
    phase = LogPhase(110, "Installation of driven piles foundations")

    phase.op_ve[0] = DefPhase(1, 'Drilling')
    phase.op_ve[0].op_sequence = [log_op["Mob"],
                                 log_op["AssPort"],
                                 log_op["VessPrep"],
                                 log_op["TranPortSite"],
                                 log_op["SeafloorEquipPrep"],
                                 log_op["PileDrill"],
                                 log_op["Grout"],
                                 log_op["GroutRemov"],
                                 log_op["TranSiteSite"],
                                 log_op["TranSitePort"],
                                 log_op["Demob"]]

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                       'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                       'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                       'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                       'equipment': [(1, equipments['drilling rigs'], 0)]}


#-------------------------------------------------------------------------------------------------


    phase.op_ve[1] = DefPhase(2, 'Hammering')
    phase.op_ve[1].op_sequence = [log_op["Mob"],
                                  log_op["AssPort"],
                                  log_op["VessPrep"],
                                  log_op["TranPortSite"],
                                  log_op["SeafloorEquipPrep"],
                                  log_op["PileHamm"],
                                  log_op["Grout"],
                                  log_op["GroutRemov"],
                                  log_op["TranSiteSite"],
                                  log_op["TranSitePort"],
                                  log_op["Demob"]]

    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['hammer'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                        'equipment': [(1, equipments['hammer'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['hammer'], 0)]}

    phase.op_ve[1].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                        'equipment': [(1, equipments['hammer'], 0)]}


#-------------------------------------------------------------------------------------------------


    phase.op_ve[2] = DefPhase(3, 'Vibro Pilling')
    phase.op_ve[2].op_sequence = [log_op["Mob"],
                                 log_op["AssPort"],
                                 log_op["VessPrep"],
                                 log_op["TranPortSite"],
                                 log_op["SeafloorEquipPrep"],
                                 log_op["PileVibro"],
                                 log_op["Grout"],
                                 log_op["GroutRemov"],
                                 log_op["TranSiteSite"],
                                 log_op["TranSitePort"],
                                 log_op["Demob"]]


    phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                       'equipment': [(1, equipments['vibro driver'], 0)]}

    phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                       'equipment': [(1, equipments['vibro driver'], 0)]}

    phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                       'equipment': [(1, equipments['vibro driver'], 0)]}

    phase.op_ve[2].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
                                       'equipment': [(1, equipments['vibro driver'], 0)]}



    return phase
