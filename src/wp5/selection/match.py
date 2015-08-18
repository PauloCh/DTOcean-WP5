from ..logistics.phase import VE_solutions

def compatibility_ve(install, log_phase):

    log_phase.op_ve[1].sol[0] = VE_solutions(0)
    log_phase.op_ve[1].sol[1] = VE_solutions(1)

    pd_ves0 = log_phase.op_ve[1].ve_combination[0]['vessel'][0][1].panda
    pd_ves0_index = pd_ves0.index

    pd_ves1 = log_phase.op_ve[1].ve_combination[0]['vessel'][1][1].panda
    pd_ves1_index = pd_ves1.index

    pd_eq = log_phase.op_ve[1].ve_combination[0]['equipment'][0][1].panda
    pd_eq_index = pd_eq.index

    log_phase.op_ve[1].sol[0].sol_ves[0] = pd_ves0.ix[pd_ves0_index[0]]
    log_phase.op_ve[1].sol[0].sol_ves[1] = pd_ves1.ix[pd_ves1_index[0]]
    log_phase.op_ve[1].sol[0].sol_eq[0] = pd_eq.ix[pd_eq_index[0]]

    log_phase.op_ve[1].sol[1].sol_ves[0] = pd_ves0.ix[pd_ves0_index[1]]
    log_phase.op_ve[1].sol[1].sol_ves[1] = pd_ves1.ix[pd_ves1_index[1]]
    log_phase.op_ve[1].sol[1].sol_eq[0] = pd_eq.ix[pd_eq_index[0]]

    return log_phase

def compatibility_ve_om(install, log_phase):

    log_phase.op_ve[0].sol[0] = VE_solutions(0)
    log_phase.op_ve[0].sol[1] = VE_solutions(1)

    pd_ves0 = log_phase.op_ve[0].ve_combination[0]['vessel'][0][1].panda
    pd_ves0_index = pd_ves0.index

    pd_ves1 = log_phase.op_ve[0].ve_combination[1]['vessel'][0][1].panda
    pd_ves1_index = pd_ves1.index

    log_phase.op_ve[0].sol[0].sol_ves[0] = pd_ves0.ix[pd_ves0_index[0]]

    log_phase.op_ve[0].sol[1].sol_ves[0] = pd_ves1.ix[pd_ves1_index[1]]

    return log_phase

#    for seq in log_phase.op_ve.keys():
#        for combi in log_phase.op_ve[seq].ve_combination.keys():
#
##            log_phase.op_ve[seq].ve_combination[combi]['vessel']
##            log_phase.op_ve[seq].ve_combination[combi]['equipment']
#
#            for nr_ves in range(len(log_phase.op_ve[seq].ve_combination[combi]['vessel'])):
#                pd_ves = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda
#                pd_ves_index = pd_ves.index
#
#                for nr_ves in range(len(pd_ves_index))
#
#                log_phase.op_ve[seq].sol[0] =
#
#            for nr_eq in log_phase.op_ve[seq].ve_combination[combi]['equipment'].keys():
#                pd_eq = log_phase.op_ve[seq].ve_combination[combi]['equipment'][nr_eq][1].panda
#                pd_eq_index = pd_eq.index
#
##                for ves in len(pd_index):
##
##                    sol[0] =
##
##                    log_phase.op_ve[seq].ve_combination[combi].sol[ves] = VE_solutions(ves)
##
##                    log_phase.op_ve[seq].ve_combination[combi].sol[ves].sol_ve[ = pd.ix[pd_index[ves]]
##
##                    sol[0] = {'sol_ve': 0: panda
##                                        1: panda
##                              'sol_eq': 0: panda}
##
#                pass



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
