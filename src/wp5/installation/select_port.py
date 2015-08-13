# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 16:40:21 2015

@author: BTeillant
"""


def install_port(end_user_inputs, wp3_outputs, wp4_outputs, port_data):
    # initialisation
    port = {'Terminal Load Bearing [ton/m2]': 0,
            'Terminal area [m2]': 0,
            'Port list satisfying the minimum requirements': 0,
            'Distance port-site': 0,
            'Selected base port for installation': 0}
    # calculate loading and projeted area of foundations/anchors
    load = []
    area = []
    if end_user_inputs['device']['technology type'].ix[0] == "seabed fixed":
        for x in range(wp4_outputs['quantity'].ix[0]):
            key1 = "diameter foundation " + str(x) + " [m]"
            key2 = "length foundation " + str(x) + " [m]"
            key3 = "weight foundation " + str(x) + " [kg]"
            load[len(load):] = [wp4_outputs[key1].ix[0] * wp4_outputs[key2].ix[0] / wp4_outputs[key3].ix[0]]
            area[len(area):] = [wp4_outputs[key1].ix[0] * wp4_outputs[key2].ix[0]]
    # terminal load bearing minimum requirement
    port['Terminal Load Bearing [ton / m2]'] = max(end_user_inputs['device']['length [m]'].ix[0] * end_user_inputs['device']['width [m]'].ix[0] / end_user_inputs['device']['drymass [kg]'].ix[0],
                                                   max(load))
    port_list = port_data[port_data['Terminal Load Bearing [ton/m2]'] >= port['Terminal Load Bearing [ton/m2]']]
    port['Terminal area [m2]'] = max(end_user_inputs['device']['length [m]'].ix[0] * end_user_inputs['device']['width [m]'].ix[0], sum(area))
    port_list = port_list[port_list['Terminal area [m2]'] >= port['Terminal area [m2]']]

    port['Port list satisfying the minimum requirements'] = port_list

    # Distance ports-site calculation
    # to be implemented once the transit distance algorithm is available
    # by making use of the grid coordinate position of the site and the ports

    # Nearest port selection
    # to be modified by making use of port['Distance port-site'] will be
    # implemented

    port['Selected base port for installation'] = port_list.ix[0]

    return port
