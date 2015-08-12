# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 10:34:21 2015

@author: BTeillant
"""
import warnings


def install_plan(end_user_inputs, wp3_outputs, wp4_outputs):
    if end_user_inputs['device_type'] == "bottom fixed":
        if wp3_outputs['electrical layout'] == "type 1":
            if wp4_outputs['foundation_type'] == "shallow foundation":
                # Explanation of the distionnary install_seq
#                install_seq = {0: [100, 101], 
#                               1: [{120: 112}],
#                               2: [{102: (120,100)}] }
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "pile":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "suction caisson":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "gravity based":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "drag-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "direct-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            else:
                warnings.warn("unknown electrical layout type")
        elif wp3_outputs['electrical layout'] == "type 2":
            if wp4_outputs['foundation_type'] == "shallow foundation":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "pile":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "suction caisson":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "gravity based":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "drag-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "direct-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
        elif wp3_outputs['electrical layout'] == "type 3":
            if wp4_outputs['foundation_type'] == "shallow foundation":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "pile":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "suction caisson":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "gravity based":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "drag-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "direct-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}

    elif end_user_inputs['device_type'] == "floating":
        if wp3_outputs['electrical layout'] == "type 1":
            if wp4_outputs['foundation_type'] == "shallow foundation":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "pile":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "suction caisson":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "gravity based":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "drag-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "direct-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            else:
                warnings.warn("unknown electrical layout type")
        elif wp3_outputs['electrical layout'] == "type 2":
            if wp4_outputs['foundation_type'] == "shallow foundation":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "pile":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "suction caisson":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "gravity based":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "drag-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "direct-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
        elif wp3_outputs['electrical layout'] == "type 3":
            if wp4_outputs['foundation_type'] == "shallow foundation":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "pile":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "suction caisson":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "gravity based":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "drag-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
            elif wp4_outputs['foundation_type'] == "direct-embedment":
                install_seq = {0: [100, 101, 102, 112, 120]}
    else:
        warnings.warn("unknown vessel type")

    return install_seq

# see = selectSeq(end_user_inputs, WP3_outputs, WP4_outputs)