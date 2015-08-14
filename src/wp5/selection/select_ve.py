# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:51:10 2015

@author: BTeillant
"""


def select_e (install, log_phase):
    
    req_e = install['requirement'][0]
    for typ in range(len(req_e)):
        if req_e[req_e.keys()[typ]][1] == 'sup':
            for seq in range(len(log_phase.op_ve)):
                for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                    if log_phase.op_ve[seq].ve_combination[combi]['equipment'][typ][1].id == req_e.keys()[typ]:
                        eq_pa = req_e[req_e.keys()[typ]][2]

                        pd_vessel[pd_vessel['Vessel Type'] >= eq_pa
]
                
def select_v (install, log_phase_id):
    
    req_v = install['requirement'][1]
    for typ in range(len(req_v)):
        if req_v[req_v.keys()[typ]][1] == 'sup':
                       
            
            
        
#    for seq in range(len(log_phase.op_ve)):
#            if log_phase.op_ve[seq].ve_combination[1]['equipment'][1].id == 'Hammer':
elec