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
    if any(log_phase_id in s for s in ['E_export', 'E_array', 'E_cp']):
        feasibility = wp3_feas(log_phase, log_phase_id, wp3_outputs)
    elif any(log_phase_id in s for s in ['F_driven', 'F_suction', 'F_gravity', 'M_drag', 'M_direct']):
        feasibility = wp4_feas(log_phase, log_phase_id, wp2_outputs, wp4_outputs)
    elif any(log_phase_id in s for s in ['D_fixed', 'D_floating']):
        feasibility = wp1_feas(log_phase, log_phase_id, user_inputs)
    return feasibility
