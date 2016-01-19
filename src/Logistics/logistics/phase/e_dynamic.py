from .classes import DefPhase, LogPhase

def initialize_e_dynamic_phase(log_op, vessels, equipments, electrical_outputs):

    # save outputs required inside short named variables
    dynamic_db = electrical_outputs['dynamic cable']
    dynamic_db = dynamic_db[dynamic_db['upstream ei type [-]'] != 'hard-wired']
    cp_db = electrical_outputs['collection point']

    # initialize logistic phase
    phase = LogPhase(102, "Installation of offshore electrical collection point")

    # initialize strategy (all strategies will be individually assessed by the
    # performance functions, with the lowest costs on being choosen)
    phase.op_ve[0] = DefPhase(1, 'all dynamic cables')

    # define vessel and equipment combinations suited for this strategy
    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['CLV']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['CLB']), (2, vessels['Tugboat']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    # iterate over the list of elements to be installed.
    # each element is associated with a customized operation sequence depending on it's characteristics,.
    for index, row in dynamic_db.iterrows():

        # initialize an empty operation sequence list for the 'index' element
        phase.op_ve[0].op_seq_sea[index] = []

        if dynamic_db['downstream termination type [-]'].ix[index] == 'device':
            phase.op_ve[0].op_seq_sea[index].extend([ log_op["LowerCable"] ])

        elif dynamic_db['downstream termination type [-]'].ix[index] == 'static cable':

            if dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate':
                phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_Static_Wet"] ])

            elif dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate':
                phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_Static_Dry"] ])

            elif dynamic_db['downstream ei type [-]'].ix[index] == 'splice':
                phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_Static_Splice"] ])

        elif dynamic_db['downstream termination type [-]'].ix[index] == 'Collection Point':

            if cp_db['type [-]'].ix[ dynamic_db['downstream termination id [-]'].ix[index] ] == 'seabed':

                if dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["LowerCable"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_CP_Wet"] ])

            elif cp_db['type [-]'].ix[ dynamic_db['downstream termination id [-]'].ix[index] ] == 'seabed with pigtails':

                if dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_Static_Dry"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'splice':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_Static_Splice"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_Static_Wet"] ])

            elif cp_db['type [-]'].ix[ dynamic_db['downstream termination id [-]'].ix[index] ] == 'surface piercing':
                phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_CP_Jtube"] ])


        phase.op_ve[0].op_seq_sea[index].extend([ log_op["DynCableLay"] ])


        if dynamic_db['upstream termination type [-]'].ix[index] == 'device':
            phase.op_ve[0].op_seq_sea[index].extend([ log_op["LowerCable"] ])

        elif dynamic_db['upstream termination type [-]'].ix[index] == 'collection point':

            if cp_db['type [-]'].ix[ dynamic_db['downstream termination id [-]'].ix[index] ] == 'seabed' or 'seabed with pigtails':

                if dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["LowerCable"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate':
                    phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_CP_Wet"] ])

            elif cp_db['type [-]'].ix[index] == 'surface piercing':
                phase.op_ve[0].op_seq_sea[index].extend([ log_op["Term_CP_Jtube"] ])

    return phase
