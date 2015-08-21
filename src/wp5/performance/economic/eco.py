# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:45:03 2015

@author: BTeillant
"""
import numpy


def cost(install, log_phase):
    for seq in range(len(log_phase.op_ve)):

        for sol in range(len(log_phase.op_ve[seq].sol)):
            sched = log_phase.op_ve[seq].sol[sol].schedule
            dur_sea_wait = sched['sea time'] + sched['waiting time']
            op_cost_max = log_phase.op_ve[seq].sol[sol].sol_ves[0]['Op max Day Rate']
            op_cost_min = log_phase.op_ve[seq].sol[sol].sol_ves[0]['Op min Day Rate']
            vessel_cost = numpy.mean([op_cost_max, op_cost_min]) / 24  # [€/hour]
            log_phase.op_ve[seq].sol[sol].cost = {'vessel': vessel_cost * dur_sea_wait,
                                                  'equipment': 0,
                                                  'port cost': 0}

    sol = {}
    sol[0] = log_phase.op_ve[1].sol[0].cost
    sol[1] = log_phase.op_ve[1].sol[1].cost

    return sol, log_phase
