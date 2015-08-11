# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 16:40:21 2015

@author: BTeillant
"""
import warnings

def install_port(end_user_inputs, wp3_outputs, wp4_outputs, port_data):
    # terminal bearing minimum requirement
    port = {"term_bearing_req": max(device_length*device_width/device_drymass,
                                    device_length*device_width/device_drymass)}
    port_list = port_data[port_data['termnal bearing'] == port["term_bearing_req"]]
    
    port{"terminal_area_req": max()}
    port_list = port_data[port_data['termnal area'] == port["term_area_req"]]
    
    port = {"short_list": port_list}
    return port