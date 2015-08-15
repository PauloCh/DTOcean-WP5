# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:49:56 2015

@author: BTeillant
"""

def compatibility(install, log_phase):
    combi_sel = 0
    return combi_sel
    
#    def compatibility_ve (install, log_phase):
#    
#    req_e = install['requirement'][0]
#    for typ in range(len(req_e)):
#        e_key_req = req_e.keys()[typ]
#        
#        for seq in range(len(log_phase.op_ve)):
#            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
#                for nr_eq in range(len(log_phase.op_ve[seq].ve_combination[combi]['equipment'])):
#                    
#                    e_key_phase = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].id
#                    
#                    if e_key_phase == e_key_req:
#                        
#                        for req in range(len(req_e[e_key_req][nr_eq])/3):
#                            e_para = req_e[e_key_req][nr_eq][0]
#                            e_meth = req_e[e_key_req][nr_eq][1]
#                            e_val = req_e[e_key_req][nr_eq][2]                           
#
#                            if e_meth == 'sup':
#                                pd = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda
#                                eq = pd[pd[e_para] >= e_val]  
#    return eq
