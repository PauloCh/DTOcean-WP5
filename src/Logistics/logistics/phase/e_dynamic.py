from .classes import DefPhase, LogPhase

def initialize_e_dynamic_phase(log_op, vessels, equipments, electrical_outputs):

    phase = LogPhase(102, "Installation of offshore electrical collection point")

    dynamic_db = electrical_outputs['dynamic cable']
    dynamic_db = dynamic_db[dynamic_db['upstream ei type [-]'] != 'hard-wired']
    cp_db = electrical_outputs['collection point']

    phase.op_ve[0] = DefPhase(1, 'all dynamic cables')

    phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['CLV']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['CLB']), (2, vessels['Tugboat']), (2, vessels['Multicat'])],
                                        'equipment': [(1, equipments['rov'], 0)]}

    for index, row in dynamic_db.iterrows():

        # initialize an empty operation sequence list for the 'index' collection point
        phase.op_ve[0].op_sequence[index] = []

        if dynamic_db['downstream termination type [-]'].ix[index] == 'Device':
            phase.op_ve[0].op_sequence[index].extend([ log_op["LowerCable"] ])

        elif dynamic_db['downstream termination type [-]'].ix[index] == 'Static Cable':

            if dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate connector':
                phase.op_ve[0].op_sequence[index].extend([ log_op["Term_Static_Wet"] ])

            elif dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate connector':
                phase.op_ve[0].op_sequence[index].extend([ log_op["Term_Static_Dry"] ])

            elif dynamic_db['downstream ei type [-]'].ix[index] == 'splice':
                phase.op_ve[0].op_sequence[index].extend([ log_op["Term_Static_Splice"] ])

        elif dynamic_db['downstream termination type [-]'].ix[index] == 'Collection Point':

            if cp_db['type [-]'].ix[index] == 'Seabed':

                if dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate connector':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["LowerCable"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate connector':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["Term_CP_Wet"] ])

            elif cp_db['type [-]'].ix[index] == 'Seabed with pigtails':

                if dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate connector':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["Term_Static_Dry"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'splice':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["Term_Static_Splice"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate connector':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["Term_Static_Wet"] ])

            elif cp_db['type [-]'].ix[index] == 'Surface Piercing':
                phase.op_ve[0].op_sequence[index].extend([ log_op["Term_CP_Jtube"] ])



        phase.op_ve[0].op_sequence[index].extend([ log_op["DynCableLay"] ])



        if dynamic_db['upstream termination type [-]'].ix[index] == 'Device':
            phase.op_ve[0].op_sequence[index].extend([ log_op["LowerCable"] ])

        elif dynamic_db['upstream termination type [-]'].ix[index] == 'Collection Point':

            if cp_db['type [-]'].ix[index] == 'Seabed' or 'Seabed with pigtails':

                if dynamic_db['downstream ei type [-]'].ix[index] == 'dry-mate connector':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["LowerCable"] ])

                elif dynamic_db['downstream ei type [-]'].ix[index] == 'wet-mate connector':
                    phase.op_ve[0].op_sequence[index].extend([ log_op["Term_CP_Wet"] ])

            elif cp_db['type [-]'].ix[index] == 'Surface Piercing':
                phase.op_ve[0].op_sequence[index].extend([ log_op["Term_CP_Jtube"] ])

    return phase
