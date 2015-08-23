# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module is responsible for returning the plan and the logistic phases 
required to be run the required logistic phases during installation
interphase sequencing of all logistic phases
during installation. 

BETA VERSION NOTES: This current version is limited to the feasibility functions 
of two logistic phases (one for the installation module and one for the O&M), 
this will be upgraded for the beta version due to october.
"""

import warnings


def install_plan(user_inputs, wp3_outputs, wp4_outputs):
    if user_inputs['device']['technology type'].ix[0] == "seabed fixed":
        if wp3_outputs['layout']['Electrical Layout'].ix[0] == "type 1":
            if wp4_outputs['foundation type'].ix[0] == "shallow foundation":
                # Explanation of the distionnary install_seq
                # install_seq = {0: [100, 101, 112],
                #                1: [{120: 112}],
                #                2: [{102: (120, 100)}]}
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "pile":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "suction caisson":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "gravity based":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "drag-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "direct-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            else:
                warnings.warn("unknown electrical layout type")

        elif wp3_outputs['electrical layout'] == "type 2":
            if wp4_outputs['foundation type'].ix[0] == "shallow foundation":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "pile":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "suction caisson":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "gravity based":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "drag-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "direct-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

        elif wp3_outputs['electrical layout'] == "type 3":
            if wp4_outputs['foundation type'].ix[0] == "shallow foundation":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "pile":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "suction caisson":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "gravity based":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "drag-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "direct-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

    elif user_inputs['device_type'] == "floating":
        if wp3_outputs['electrical layout'] == "type 1":
            if wp4_outputs['foundation type'].ix[0] == "shallow foundation":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "pile":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "suction caisson":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "gravity based":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "drag-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "direct-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            else:
                warnings.warn("unknown electrical layout type")

        elif wp3_outputs['electrical layout'] == "type 2":
            if wp4_outputs['foundation type'].ix[0] == "shallow foundation":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "pile":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "suction caisson":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "gravity based":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "drag-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "direct-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

        elif wp3_outputs['electrical layout'] == "type 3":
            if wp4_outputs['foundation type'].ix[0] == "shallow foundation":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "pile":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "suction caisson":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "gravity based":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "drag-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

            elif wp4_outputs['foundation type'].ix[0] == "direct-embedment":
                install_seq = {0: ['E_export', 'E_array', 'E_cp', 'F_driven', 'D_fixed']}

    else:
        warnings.warn("unknown vessel type")

    return install_seq

# see = selectSeq(end_user_inputs, WP3_outputs, WP4_outputs)
