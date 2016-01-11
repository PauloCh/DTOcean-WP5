from .classes import DefPhase, LogPhase


def initialize_gravity_phase(log_op, vessels, equipments, MF_outputs):

    # save outputs required inside short named variables
    found_db = MF_outputs['foundation']
    gravity_db = found_db[found_db['type [-]'] == 'gravity']

    # initialize logistic phase
    phase = LogPhase(112, "Installation of gravity based foundations")

    '''On-deck Transportation Strategy'''

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[0] = DefPhase(1, 'Gravity based anchor installation with on deck transportation')

    # define vessel and equipment combinations suited for this strategy
    phase.op_ve[0].ve_combination[0] = {'vessel': [ (1, vessels['Crane Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0) ]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [ (1, vessels['Construction Support Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0) ]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [ (1, vessels['Fit for Purpose']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0) ]}

    phase.op_ve[0].ve_combination[3] = {'vessel': [ (1, vessels['Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['divers'], 0), (1, equipments['rov'], 0) ]}

    phase.op_ve[0].ve_combination[4] = {'vessel': [ (1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [ (1, equipments['rov'], 0) ]}

    phase.op_ve[0].ve_combination[5] = {'vessel': [ (1, vessels['Platform Support Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0) ]}

    # iterate over the list of elements to be installed.
    # each element is associated with a customized operation sequence depending on it's characteristics,
    for index, row in gravity_db.iterrows():

        gravity_id = gravity_db['foundations [-]'].ix[index]

        # initialize an empty operation sequence list for the 'index' element
        phase.op_ve[0].op_sequence_elem[gravity_id] = []

        phase.op_ve[0].op_sequence_elem[gravity_id].extend([ log_op["GBS_deck_pos"] ])

    '''Tow Transportation Strategy'''

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[1] = DefPhase(2, 'Gravity based anchor installation with towing transportation')

    # define vessel and equipment combinations suited for this strategy
    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['Anchor Handling']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (2, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(3, vessels['Tugboat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    # iterate over the list of elements to be installed.
    # each element is associated with a customized operation sequence depending on it's characteristics,
    for index, row in gravity_db.iterrows():

        gravity_id = gravity_db['foundations [-]'].ix[index]

        # initialize an empty operation sequence list for the 'index' element
        phase.op_ve[0].op_sequence_elem[gravity_id] = []

        phase.op_ve[0].op_sequence_elem[gravity_id].extend([ log_op["GBS_tow_pos"] ])


    return phase
