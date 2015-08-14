# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:25:21 2015

@author: BTeillant
"""
from wp5.feasibility.wp1 import wp1_feas
from wp5.feasibility.wp4 import wp4_feas
from wp5.feasibility.wp3 import wp3_feas
# wp3_feas, wp4_feas

def glob_feas(log_phase, log_phase_id, user_inputs, wp2_outputs, wp3_outputs, wp4_outputs):
    if log_phase_id == 'E_export' or 'E_array' or 'E_cp':
        feasibility = wp3_feas(log_phase, log_phase_id, wp3_outputs)
    elif log_phase_id == 'F_driven' or 'F_suction' or 'F_gravity' or 'M_drag' or 'M_direct':
        feasibility = wp4_feas(log_phase, log_phase_id, wp2_outputs, wp4_outputs)
    elif log_phase_id == 'D_fixed' or 'D_floating':
        feasibility = wp1_feas(log_phase, log_phase_id, user_inputs)
    return feasibility
