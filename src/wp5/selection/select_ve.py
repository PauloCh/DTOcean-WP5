# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 12:51:10 2015

@author: BTeillant
"""


def select_e (install, log_phase):

    req_e = install['requirement'][0]
    eq = dict.fromkeys(req_e.keys()) #Initialize an empty dic with the name of the equip to be evaluated

    for typ in range(len(req_e)):
        e_key_req = req_e.keys()[typ]

        for seq in range(len(log_phase.op_ve)):
            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                for nr_eq in range(len(log_phase.op_ve[seq].ve_combination[combi]['equipment'])):

                    e_key_phase = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].id
                    e_pd = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda

                    if e_key_phase == e_key_req:

                        for req in range(len(req_e[e_key_req])):
                            e_para = req_e[e_key_req][req][0]
                            e_meth = req_e[e_key_req][req][1]
                            e_val = req_e[e_key_req][req][2]

                            if e_meth == 'sup':
                                e_pd = e_pd[e_pd[e_para] >= e_val]

                        # Check if no vessel is feasible within the req for this particular ve_combination
                        if e_pd.empty:
                            del log_phase.op_ve[seq].ve_combination[combi]   # If so, force the combination to be 0
                            break
                        else:
                            eq[e_key_req] = e_pd
                            log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda = e_pd

    return eq, log_phase


def select_v (install, log_phase):

    req_v = install['requirement'][1]
    ves = dict.fromkeys(req_v.keys()) #Initialize an empty dic with the name of the vessels to be evaluated

    for typ in range(len(req_v)):
        v_key_req = req_v.keys()[typ]

        for seq in range(len(log_phase.op_ve)):
            for combi in range(len(log_phase.op_ve[seq].ve_combination)):
                for nr_ves in range(len(log_phase.op_ve[seq].ve_combination[combi]['vessel'])):

                    v_key_phase = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].id
                    v_pd = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda

                    if v_key_phase == v_key_req:

                       for req in range(len(req_v[v_key_req])):
                           v_para = req_v[v_key_req][req][0]
                           v_meth = req_v[v_key_req][req][1]
                           v_val = req_v[v_key_req][req][2]

                           if v_meth == 'sup':
                               v_pd = v_pd[v_pd[v_para] >= v_val]

                       # Check if no vessel is feasible within the req for this particular ve_combination
                       if v_pd.empty:
                           del log_phase.op_ve[seq].ve_combination[combi]   # If so, force the combination to be 0
                           break
                       else:
                           ves[v_key_req] = v_pd
                           log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda = v_pd

    return ves, log_phase