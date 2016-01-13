
from .classes import DefPhase, LogPhase


def initialize_devices_phase(log_op, vessels, equipments, user_inputs, hydrodynamic_outputs):

    # save outputs required inside short named variables
    dev_type = user_inputs['device']['type [-]'].ix[0]
    assmbly_stratg = user_inputs['device']['assembly strategy [-]'].ix[0]
    trans_methd = user_inputs['device']['transportation method [-]'].ix[0]
    loadout_methd = user_inputs['device']['load out [-]'].ix[0]
    hydro_db = hydrodynamic_outputs

    # initialize logistic phase
    phase = LogPhase(121, "Installation of devices")

    ''' On-deck Transportation Strategy '''

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[0] = DefPhase(1, 'On-deck transportation')

    # define vessel and equipment combinations suited for this strategy
    phase.op_ve[0].ve_combination[0] = {'vessel': [ (1, vessels['Crane Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0), (1, equipments['divers'], 0) ]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [ (1, vessels['JUP Vessel']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0), (1, equipments['divers'], 0) ]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [ (1, vessels['Construction Support Vessel']), (2, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0), (1, equipments['divers'], 0) ]}

    phase.op_ve[0].ve_combination[3] = {'vessel': [ (1, vessels['Fit for Purpose']), (2, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0), (1, equipments['divers'], 0) ]}

    phase.op_ve[0].ve_combination[4] = {'vessel': [ (1, vessels['Crane Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0), (1, equipments['divers'], 0) ]}

    phase.op_ve[0].ve_combination[5] = {'vessel': [ (1, vessels['JUP Barge']), (1, vessels['Tugboat']), (1, vessels['Multicat']) ],
                                        'equipment': [ (1, equipments['rov'], 0), (1, equipments['divers'], 0) ]}

    # define initial mobilization and onshore tasks
    phase.op_ve[0].op_sequence_mob = [ log_op["Mob"],
                                       log_op["DevAssPort"] ]
    if trans_methd == 'deck':

        if loadout_methd == 'lift away':
            phase.op_ve[0].op_sequence_mob.extend([ log_op["LoadOut_Lift"],
                                                    log_op["Seafast"] ])
        elif loadout_methd == 'skidded':
            phase.op_ve[0].op_sequence_mob.extend([ log_op["LoadOut_Skidded"],
                                                    log_op["Seafast"] ])
    elif trans_methd == 'tow':

        if loadout_methd == 'lift away':
            phase.op_ve[0].op_sequence_mob.extend([ log_op["LoadOut_Lift"] ])

        elif loadout_methd == 'skidded' or 'trailer':
            phase.op_ve[0].op_sequence_mob.extend([ log_op["LoadOut_Skidded"] ])

        elif loadout_methd == 'float away':
            phase.op_ve[0].op_sequence_mob.extend([ log_op["LoadOut_Float"] ])

    # iterate over the list of elements to be installed.
    # each element is associated with a customized operation sequence depending on it's characteristics,.
    for index, row in hydro_db.iterrows():

        device_id = hydro_db['device [-]'].ix[index]

        # initialize an empty operation sequence list for the 'index' element
        phase.op_ve[0].op_sequence_elem[device_id] = []

        if dev_type == 'float WEC' or 'float TEC':

            phase.op_ve[0].op_sequence_elem[device_id].extend([ log_op["PosFLTdev"] ])

        elif dev_type == 'fixed WEC' or 'fixed TEC':

             phase.op_ve[0].op_sequence_elem[device_id].extend([ log_op["PosBFdev"] ])

    # define final demobilization tasks
    phase.op_ve[0].op_sequence_demob = [ log_op["Demob"] ]

    ''' Tow Transportation Strategy '''

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[1] = DefPhase(1, 'Towing transportation')

    # define vessel and equipment combinations suited for this strategy
    phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['AHTS']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Fit for Purpose']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0), (1, equipments['divers'], 0)]}

    # define initial mobilization and onshore tasks
    phase.op_ve[1].op_sequence_mob = [ log_op["Mob"],
                                       log_op["DevAssPort"] ]
    if trans_methd == 'deck':

        if loadout_methd == 'lift away':
            phase.op_ve[1].op_sequence_mob.extend([ log_op["LoadOut_Lift"],
                                                    log_op["Seafast"] ])
        elif loadout_methd == 'skidded':
            phase.op_ve[1].op_sequence_mob.extend([ log_op["LoadOut_Skidded"],
                                                    log_op["Seafast"] ])
    elif trans_methd == 'tow':

        if loadout_methd == 'lift away':
            phase.op_ve[1].op_sequence_mob.extend([ log_op["LoadOut_Lift"] ])

        elif loadout_methd == 'skidded' or 'trailer':
            phase.op_ve[1].op_sequence_mob.extend([ log_op["LoadOut_Skidded"] ])

        elif loadout_methd == 'float away':
            phase.op_ve[1].op_sequence_mob.extend([ log_op["LoadOut_Float"] ])

    # iterate over the list of elements to be installed.
    # each element is associated with a customized operation sequence depending on it's characteristics,.
    for index, row in hydro_db.iterrows():

        device_id = hydro_db['device [-]'].ix[index]

        # initialize an empty operation sequence list for the 'index' element
        phase.op_ve[1].op_sequence_elem[device_id] = []

        if dev_type == 'float WEC' or 'float TEC':
            phase.op_ve[1].op_sequence_elem[device_id].extend([ log_op["PosFLTdev"] ])

        elif dev_type == 'fixed WEC' or 'fixed TEC':
             phase.op_ve[1].op_sequence_elem[device_id].extend([ log_op["PosBFdev"] ])


    # define final demobilization tasks
    phase.op_ve[0].op_sequence_demob = [ log_op["Demob"] ]

    ''' Selection of suitable strategies '''

    # delete the strategies that are not applicable for the scenario
    # so they're not tested in the performance functions
    if trans_methd == 'tow':
        del phase.op_ve[0]
    elif trans_methd == 'deck':
        del phase.op_ve[1]

    return phase

