# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:45:03 2015

@author: BTeillant
"""

def cost(install, log_phase):
    for seq in range(len(log_phase.op_ve)):
#        
        for sol in range(len(log_phase.op_ve[seq].sol)):
            sched = log_phase.op_ve[seq].sol[sol].schedule
            dur_sea_wait = sched['sea time'] + sched['waiting time']
            log_phase.op_ve[seq].sol[sol].schedule= {'olc': olc,
                                                     'log_op_dur_all': op_dur_prep + op_dur_sea,
                                                     'preparation': sum(op_dur_prep),
                                                     'sea time': dur_total_sea,
                                                     'weather windows': weather_wind,
                                                     'waiting time': waiting_time}