# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module is the second and last part of the selection step in the WP5 methodology.
It contains functions to make the compatibility check between the characteristics
of port/vessel, port/equipment and vessel/equipment, returning only the feasible
and compatible solutions of vessels and equipments to perform the operations
sequence of the logistic phase.

BETA VERSION DETAILS: up to date, the functionalities explained previously have
not been implemented, this module should suffer major changes for the beta version
"""

from ..logistics.phase.classes import VE_solutions
import itertools
import  numpy

def compatibility_ve(install, log_phase):
    """This function is currently limited to the selection of the first two
    feasible solutions for the installation logistic phase in analysis.

    Parameters
    ----------
    install : dict
     not used
    log_phase : class
     class of the logistic phase under consideration for assessment, contains
     data refered to the feasible vessel and equipment combinations specific of
     each operation sequence of the logistic phase

    Returns
    -------
    sol : dict
     A dict of panda dataframes with unique feasible solutions
    log_phase : class
     An updated version of the log_phase argument containing only the feasible
     equipments within each vessel and equipment combinations dataframes
    """


    sol = {}

    # Go through different sequence options
    for seq in log_phase.op_ve:

        sols_ve_indxs_combs_inseq = []
        nr_sol = 0

        # Go through different possible combination
        for combi in range(len(log_phase.op_ve[seq].ve_combination)):

            # initialise solution variables
            ves = {}
            ves_sol = {}
            ves_indexs = {}
            eq = {}
            eq_sol = {}
            eq_indexs = {}


            #  Go through vessels
            nr_diff_ves = len(log_phase.op_ve[seq].ve_combination[combi]['vessel'])
            for ves_type in range(nr_diff_ves):

                ves_quant = log_phase.op_ve[seq].ve_combination[combi]['vessel'][ves_type][0]  # Quantity of vessels in the solution
                ves_class = log_phase.op_ve[seq].ve_combination[combi]['vessel'][ves_type][1]  # Vessel class

                ves_index_vec = ves_class.panda.index  # Get indexs that correspond to vessel class
                nr_feas_vess_i = len(ves_index_vec)  # Number of feasible vessels within vessel type

                # Quantify number of total feasible vessels regardless of type
                if ves_type == 0:
                    nr_feas_vess_T = nr_feas_vess_i
                else:
                    nr_feas_vess_T = nr_feas_vess_T * nr_feas_vess_i

                for indx_vec in range(nr_feas_vess_i):
                  ves[indx_vec] = ves_class.panda.ix[indx_vec]  # Get info of the feasible vessels

                ves_sol[ves_type] = {'quantity': ves_quant,
                                   'Series': ves, 'indexs': ves_index_vec}  # Store info of the vessels
                ves_indexs[ves_type] = list(ves_index_vec)  # Vector of indexs of feasible vessels per type


            #  Go through equips
            nr_diff_equi = len(log_phase.op_ve[seq].ve_combination[combi]['equipment'])
            for eq_type in range(nr_diff_equi):

                eq_quant = log_phase.op_ve[seq].ve_combination[combi]['equipment'][eq_type][0]  # Quantity of vessels in the solution
                eq_class = log_phase.op_ve[seq].ve_combination[combi]['equipment'][eq_type][1]  # Equipment class

                eq_index_vec = eq_class.panda.index
                nr_feas_eq_i = len(eq_index_vec)

                # Quantify number of total feasible equipments regardless of type
                if eq_type == 0:
                    nr_feas_eq_T = nr_feas_eq_i
                else:
                    nr_feas_eq_T = nr_feas_eq_T * nr_feas_eq_i

                for indx_vec in range(nr_feas_eq_i):
                  eq[indx_vec] = eq_class.panda.ix[indx_vec]  # Get info of the feasible equipments

                eq_sol[eq_type] = {'quantity': eq_quant,
                                 'Series': eq, 'indexs': eq_index_vec}  # Store info of the equipments
                eq_indexs[eq_type] = list(eq_index_vec)  # Vector of indexs of feasible equipments per type



            nr_sol_T = nr_feas_vess_T * nr_feas_eq_T  # Total number of solutions per combination




            # Build solutions
            # sols_ve_indxs = []

            sols_ves = []
            for ves_type in range(nr_diff_ves):  # Agregatte vessel type solutions
                sols_ves.append(tuple(ves_indexs[ves_type]))
                # sols_ve_indxs.append(tuple(ves_indexs[ves_type]))

            sols_v_indxs_combs = list(itertools.product(*sols_ves))  # Combine vessel solutions

            sols_eq = []
            for eq_type in range(nr_diff_equi):  # Agregatte equipment type solutions
                sols_eq.append(tuple(eq_indexs[eq_type]))
                # sols_ve_indxs.append(tuple(eq_indexs[eq_type]))

            sols_e_indxs_combs = list(itertools.product(*sols_eq))  # Combine vessel solutions

            # sols_ve_indxs_combs_incombi = list(itertools.product(*sols_ve_indxs))

            sols_ve_indxs_sprt = (sols_v_indxs_combs, sols_e_indxs_combs)  # Agregatte vessel and equipment solutions
            sols_ve_indxs_comb = list(itertools.product(*sols_ve_indxs_sprt))  # Combine solutions


            # sols_ve_indxs_combs_inseq.append(sols_ve_indxs_combs_incombi)
            sols_ve_indxs_combs_inseq.append(sols_ve_indxs_comb)  # Store solution per combination


        log_phase.op_ve[seq].sol_combi = sols_ve_indxs_combs_inseq  # Store solution per sequence
        log_phase.op_ve[seq].sol_ves = ves_sol
        log_phase.op_ve[seq].sol_eq = eq_sol


        # Store final solution
        sol = VE_solutions(nr_sol) # ??????????????!
        sol.sol_combi[seq] = sols_ve_indxs_combs_inseq
        sol.sol_ves[seq] = ves_sol
        sol.sol_eq[seq] = eq_sol
        nr_sol = nr_sol + 1





    # Apply feasibility functions between vessel and equipment ??????????????????????????????????????????!

    # req_m = install['requirement'][2]
    # #Initialize an empty dic with the name of the vessels to be evaluated
    # match = dict.fromkeys(req_m.keys())
    #
    # for typ in range(len(req_m)):
    #     m_key_req = req_m.keys()[typ]
    #
    #     for seq in range(len(log_phase.op_ve)):
    #         for combi in range(len(log_phase.op_ve[seq].ve_combination)):
    #             for nr_ves in range(len(log_phase.op_ve[seq].ve_combination[combi]['vessel'])):
    #
    #                 v_key_phase = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].id
    #                 v_pd = log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda
    #
    #                 if v_key_phase == v_key_req:
    #
    #                    for req in range(len(req_v[v_key_req])):
    #                        v_para = req_v[v_key_req][req][0]
    #                        v_meth = req_v[v_key_req][req][1]
    #                        v_val = req_v[v_key_req][req][2]
    #
    #                        if v_meth == 'sup':
    #                            v_pd = v_pd[v_pd[v_para] >= v_val]
    #
    #                    # Check if no vessel is feasible within the req for this particular ve_combination
    #                    if v_pd.empty:
    #                        del log_phase.op_ve[seq].ve_combination[combi]   # If so, force the combination to be 0
    #                        break
    #                    else:
    #                        ves[v_key_req] = v_pd
    #                        log_phase.op_ve[seq].ve_combination[combi]['vessel'][nr_ves][1].panda = v_pd



            # # Build solutions
            # for ves_type in range(nr_diff_ves):
            #     nr_feas_ves_i = len(ves_sol[ves_type]['Series'])
            #     for ind_vel_sol in range(nr_feas_ves_i):
            #
            #         for eq_type in range(nr_diff_equi):
            #             nr_feas_eq_i = len(eq_sol[eq_type]['Series'])
            #             for ind_eq_sol in range(nr_feas_eq_i):
            #
            #                 sol = VE_solutions(nr_sol_inseq)
            #
            #                 sol.sol_ves[ves_type] = ves_sol[ves_type]['Series'][ind_vel_sol]
            #                 sol.sol_eq[eq_type] = eq_sol[eq_type]['Series'][ind_eq_sol]
            #
            #                 log_phase.op_ve[seq].sol[nr_sol_inseq] = sol # MOVE ?!?!?!?!?!?!!?
            #
            #                 nr_sol_inseq = nr_sol_inseq + 1
            #                 nr_sol_incombi = nr_sol_incombi + 1
            #
            # ERROR_check = nr_sol_T - nr_sol_incombi


#    log_phase.op_ve[1].sol[0] = VE_solutions(0)
#    log_phase.op_ve[1].sol[1] = VE_solutions(1)
#
#    pd_ves0 = log_phase.op_ve[1].ve_combination[0]['vessel'][0][1].panda
#    pd_ves0_index = pd_ves0.index
#
#    pd_ves1 = log_phase.op_ve[1].ve_combination[0]['vessel'][1][1].panda
#    pd_ves1_index = pd_ves1.index
#
#    pd_eq = log_phase.op_ve[1].ve_combination[0]['equipment'][0][1].panda
#    pd_eq_index = pd_eq.index
#
#    log_phase.op_ve[1].sol[0].sol_ves[0] = pd_ves0.ix[pd_ves0_index[0]]
#    log_phase.op_ve[1].sol[0].sol_ves[1] = pd_ves1.ix[pd_ves1_index[0]]
#    log_phase.op_ve[1].sol[0].sol_eq[0] = pd_eq.ix[pd_eq_index[0]]
#
#    log_phase.op_ve[1].sol[1].sol_ves[0] = pd_ves0.ix[pd_ves0_index[1]]
#    log_phase.op_ve[1].sol[1].sol_ves[1] = pd_ves1.ix[pd_ves1_index[1]]
#    log_phase.op_ve[1].sol[1].sol_eq[0] = pd_eq.ix[pd_eq_index[0]]
#
#    sol = {}
#    sol[0] = log_phase.op_ve[1].sol[0]
#    sol[1] = log_phase.op_ve[1].sol[1]

    return sol, log_phase


def compatibility_ve_om(install, log_phase):
    """This function is currently limited to the selection of the first two
    feasible solutions for the O&M logistic phase in analisys.

    Parameters
    ----------
    install : dict
     not used
    log_phase : class
     class of the logistic phase under consideration for assessment, contains
     data refered to the feasible vessel and equipment combinations specific of
     each operation sequence of the logistic phase

    Returns
    -------
    sol : dict
     A dict of panda dataframes with unique feasible solutions
    log_phase : class
     An updated version of the log_phase argument containing only the feasible
     equipments within each vessel and equipment combinations dataframes
    """

    log_phase.op_ve[0].sol[0] = VE_solutions(0)
    log_phase.op_ve[0].sol[1] = VE_solutions(1)

    pd_ves0 = log_phase.op_ve[0].ve_combination[0]['vessel'][0][1].panda
    pd_ves0_index = pd_ves0.index

    pd_ves1 = log_phase.op_ve[0].ve_combination[1]['vessel'][0][1].panda
    pd_ves1_index = pd_ves1.index

    log_phase.op_ve[0].sol[0].sol_ves[0] = pd_ves0.ix[pd_ves0_index[0]]

    log_phase.op_ve[0].sol[1].sol_ves[0] = pd_ves1.ix[pd_ves1_index[1]]

    sol = {}
    sol[0] = log_phase.op_ve[0].sol[0]
    sol[1] = log_phase.op_ve[0].sol[1]

    return sol, log_phase

#    for seq in log_phase.op_ve.keys():
#        for combi in log_phase.op_ve[seq].ve_combination.keys():
#
# log_phase.op_ve[seq].ve_combination[combi]['vessel']
           # log_phase.op_ve[seq].ve_combination[combi]['equipment']
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
