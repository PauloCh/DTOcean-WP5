from .classes import DefPhase, LogPhase

def initialize_e_cp_phase(log_op, vessels, equipments, electrical_outputs):

    # save outputs required inside short named variables
    cp_db = electrical_outputs['collection point']
    cp_db = cp_db[cp_db['type [-]'] != 'surface piercing']
    cp_db = cp_db[cp_db['downstream ei type [-]'] != 'hard-wired cable']

    # initialize logistic phase
    phase = LogPhase(102, "Installation of offshore electrical collection point")

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[0] = DefPhase(1, 'all seabed collection points')

    # define vessel and equipment combinations suited for this strategy
    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['Crane Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Crane Barge']), (2, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['JUP Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[3] = {'vessel': [(1, vessels['JUP Barge']), (2, vessels['Tugboat']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[4] = {'vessel': [(1, vessels['Construction Support Vessel']), (1, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    # iterate over the list of elements to be installed.
    # each element is associated with a customized operation sequence depending on it's characteristics,.
    for index, row in cp_db.iterrows():

        # initialize an empty operation sequence list for the 'index' element
        phase.op_ve[0].op_sequence_elem[index] = []

        if cp_db['type [-]'].ix[index] == 'seabed':

            if cp_db['upstream ei type [-]'].ix[index] == 'dry-mate':

                for x in range(cp_db['upstream ei number [-]'].ix[index]):
                    phase.op_ve[0].op_sequence_elem[index].extend([ log_op["LiftCable"] ])

            if cp_db['downstream ei type [-]'].ix[index] == 'dry-mate':

                for x in range(cp_db['upstream ei number [-]'].ix[index]):
                    phase.op_ve[0].op_sequence_elem[index].extend([ log_op["LiftCable"] ])

            if cp_db['upstream ei type [-]'].ix[index] == 'dry-mate' or cp_db['downstream ei type [-]'].ix[index] == 'dry-mate':
                phase.op_ve[0].op_sequence_elem[index].extend([ log_op["DryConnect"],
                                                           log_op["LowerCP"] ])

            else:  # meaning all electrical interfaces are wet-mate connected
                phase.op_ve[0].op_sequence_elem[index].extend([ log_op["LowerCP"] ])


        if cp_db['type [-]'].ix[index] == 'seabed with pigtails':

            if cp_db['downstream ei type [-]'].ix[index] == 'dry-mate':

                for x in range(cp_db['upstream ei number [-]'].ix[index]):
                    phase.op_ve[0].op_sequence_elem[index].extend([ log_op["LiftCable"] ])

                phase.op_ve[0].op_sequence_elem[index].extend([ log_op["DryConnect"],
                                                           log_op["LowerCP"] ])

            else:  # meaning all electrical interfaces are wet-mate connected
                phase.op_ve[0].op_sequence_elem[index].extend([ log_op["LowerCP"]] )

    return phase
