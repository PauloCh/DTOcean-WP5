# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:51:10 2015

@author: BTeillant
"""


def select_e (install, log_phase):
    
    req_e = install['requirement'][0]
    for typ in range(len(req_e)):
        e_key_req = req_e.keys()[typ]
        for seq in range(len(log_phase.op_ve)):
            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                for nr_eq in range(len(log_phase.op_ve[seq].ve_combination[combi]['equipment'])):
                    e_key_phase = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].id
                    if e_key_phase == e_key_req:
                        for req in range(len(req_e[e_key_req][nr_eq])/3):
                            if req_e[req_e.keys()[typ]][req][1] == 'sup':
                                eq_para = req_e[e_key_req][nr_eq][0]
                                eq_val = req_e[e_key_req][nr_eq][2]
                                pd = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda
                                eq = pd[pd[req_e[e_key_req][nr_eq][0]] >= eq_pa]  
    return eq
                            
def select_v (install, log_phase_id):
    pass
#    req_v = install['requirement'][1]
#    for typ in range(len(req_v)):
#        if req_v[req_v.keys()[typ]][1] == 'sup':
