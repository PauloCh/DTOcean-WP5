# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module is responsible for the interphase relation between the different 
logistic phases during installation. The inputs from the user and other DTOcean 
packages build up unique projects which require specific installation sequences. 
The functions in this module return the installation sequence required based on 
pre-defined cases (type of foundations, type of moorings, type of device, type 
of electrical infranstrucutres). 

BETA VERSION NOTES: Since 
"""

import warnings


def install_plan(user_inputs, wp3_outputs, wp4_outputs):
    """install_plan receives  function returns the id of the logistic phases required to
    conduct the installation of a particular case, plus the interphase relation
    between the 
    """
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
