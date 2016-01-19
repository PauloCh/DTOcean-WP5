from .classes import DefPhase, LogPhase


def initialize_m_suction_phase(log_op, vessels, equipments, MF_outputs):

    # save outputs required inside short named variables
    found_db = MF_outputs['foundation']
    drag_db = found_db[found_db['type [-]'] == 'drag-embedment anchor']

    # initialize logistic phase
    phase = LogPhase(115, "Installation of mooring systems with suction-embedment anchors")

    ''' Deploy drag-embedment anchor installation strategy'''

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[0] = DefPhase(1, 'Installation of suction caissons')

    # define vessel and equipment combinations suited for this strategy

    phase.op_ve[0].op_seq_sea = [log_op["Mob"],
                                       log_op["AssPort"],
                                       log_op["VessPrep"],
                                       log_op["TranPortSite"],
                                       log_op["SeafloorEquipPrep"],
                                       log_op["SuctCais"],
                                       log_op["TranSiteSite"],
                                       log_op["TranSitePort"],
                                       log_op["Demob"]]


    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Vessel'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['drilling rigs'], 0)]}

    # phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Vessel'])],
    #                                     'equipment': [(1, equipments['drilling rigs'], 0)]} # STILL NOT IN DB!!!!!!!!!


    return phase
