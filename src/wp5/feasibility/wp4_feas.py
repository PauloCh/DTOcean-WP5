# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:51:31 2015

@author: BTeillant
"""

def wp4_feas(install, log_phase_id, wp2_outputs, wp4_outputs):

    if log_phase_id == 'F_driven':
       # Equipment feasiblity
       # Hammer sleeve diameter
        F_diam = []
        load_u_f = [] # list of loading due to each foundation per unit
        area_u_f = [] # list of area occupied by each foundation per unit
        load_u = [] # list of loading due to the set of foundation(s) per unit
        area_u = [] # list of loading occupied by the set of foundation(s) per unit
        for dev in range(wp2_outputs['numUnits'].ix[0]):
            for x in range(wp4_outputs['quantity'].ix[0]):
                key1 = "diameter foundation " + str(x) + " [m]"
                key2 = "length foundation " + str(x) + " [m]"
                key3 = "weight foundation " + str(x) + " [kg]"
                load_u_f[len(load_u_f):] = [wp4_outputs[key1].ix[0]*wp4_outputs[key2].ix[0]/wp4_outputs[key3].ix[0]]
                area_u_f[len(area_u_f):] = [wp4_outputs[key1].ix[0]*wp4_outputs[key2].ix[0]]
                F_diam[len(F_diam):] = wp4_outputs[key1].ix[0]
            load_u[len(load_u):] = max(load_u_f[dev*x:(dev+1)*x])
            area_u[len(area_u):] = sum(area_u_f[dev*x:(dev+1)*x])
        deck_loading = max(load_u)
        deck_area = max(area_u)
        sleeve_diam = max(F_diam)
        feasibility = {'equipment': {'Hammer': ['Sleeve diameter', 'sup', sleeve_diam]},
                        'vessel': {'Crane Barge': [['Deck loading', 'sup', deck_loading],
                                                   ['Deck area', 'sup', deck_area]],
                                   'Crane Vessel': [['Deck loading', 'sup', deck_loading],
                                                   ['Deck area', 'sup', deck_area]],
                                   'JUP barge': [['Deck loading', 'sup', deck_loading],
                                                   ['Deck area', 'sup', deck_area]],
                                   'JUP vessel': [['Deck loading', 'sup', deck_loading],
                                                   ['Deck area', 'sup', deck_area]]}}
    elif log_phase_id == 'F_suction':
        # TO-DO
    elif log_phase_id == 'F_gravity':
        # TO-DO
    
    feasibility = {'equipment': [],
                   'vessel': {'Crane Barge': ['Deck loading [m2/ton]','Sup', deck_loading],
                              ]}}
    return feasibility