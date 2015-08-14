# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:39:42 2015

@author: BTeillant
"""

def wp1_feas(install, log_phase_id, user_inputs):
    deck_loading = user_inputs['device']['length [m]'].ix[0] *  user_inputs['device']['width [m]'].ix[0] / user_inputs['device']['drymass [kg]'].ix[0]
    deck_area = user_inputs['device']['length [m]'].ix[0] *  user_inputs['device']['width [m]'].ix[0]
    feasibility = {'equipment': [],
                   'vessel': {'Deck loading [m2/ton]': ['Sup', 'all', deck_loading],
                                  'Deck area [m2]': ['Sup', 'all', deck_area]}}
    return feasibility
    
