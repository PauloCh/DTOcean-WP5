def wp6_feas(log_phase, log_phase_id, wp6_outputs):

    if log_phase_id == 'insp':

        # Input collection
        lenght_SP = wp6_outputs['LogPhase1']['Length_SP [m]'].ix[0]
        width_SP = wp6_outputs['LogPhase1']['Width_SP [m]'].ix[0]
        height_SP = wp6_outputs['LogPhase1']['Height_SP [m]'].ix[0]
        total_mass_SP = wp6_outputs['LogPhase1']['Total_Mass_SP [t]'].ix[0]
        indiv_mass_SP = wp6_outputs['LogPhase1']['Indiv_Mass_SP [t]'].ix[0]

        # Feasibility functions
        deck_area = lenght_SP*width_SP
        deck_loading = total_mass_SP/area_SP
        lifting_req = indiv_mass_SP

        feas_e = {}
        feas_v = {'CTV': [['Deck loading [ton/m2]', 'sup', deck_loading],
                          ['Deck space [m2]', 'sup', deck_area],
                          ['Crane weight [t]', 'sup', lifting_req]],

                  'Multicat': [['Deck loading [ton/m2]', 'sup', deck_loading],
                               ['Deck space [m2]', 'sup', deck_area],
                               ['Crane weight [t]', 'sup', lifting_req]]
                    }

    return feas_e, feas_v