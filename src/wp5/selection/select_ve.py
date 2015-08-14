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
                            e_para = req_e[e_key_req][nr_eq][0]
                            e_meth = req_e[e_key_req][nr_eq][1]
                            e_val = req_e[e_key_req][nr_eq][2]                           

                            if e_meth == 'sup':
                                pd = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda
                                eq = pd[pd[e_para] >= e_val]  
    return eq

                        
def select_v (install, log_phase):
#    ves = 0
    req_v = install['requirement'][1]
    for typ in range(len(req_v)):
        v_key_req = req_v.keys()[typ]
        
        for seq in range(len(log_phase.op_ve)):
            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                for nr_eq in range(len(log_phase.op_ve[seq].ve_combination[combi]['vessel'])):
                    
                    v_key_phase = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_eq][1].id
                    
                    if v_key_phase == v_key_req:
                        
                        for req in range(len(req_v[v_key_req][nr_eq])/3):
                            v_para = req_v[v_key_req][nr_eq][0]
                            v_meth =req_v[v_key_req][nr_eq][1]
                            v_val = req_v[v_key_req][nr_eq][2]                           

                            if v_meth == 'sup':
                                pd = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_eq][1].panda
                                ves = pd[pd[v_para] >= v_val]  
    return ves