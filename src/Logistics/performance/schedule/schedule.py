# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module is responsible for the schedule step in the WP5 methodology. It
contains functions to calculate the time required to perform certain operations
such as transit to site, always taking into account the weather windows through
the operation limit conditions defined for each operation.

BETA VERSION NOTES: The module will suffer major changes in the next version of
the code.
"""

import numpy
#import utm
#from geopy.distance import great_circle
from transit_algorithm import transit_algorithm
#import itertools
from Logistics.installation.select_port import distance



def indices(a, func):
    """
    indices returns the indices of a vector "a" that satisfy the
    conditional function "func"
    """
    return [i for (i, val) in enumerate(a) if func(val)]


def differences(a):
    """
    differences returns a vector containing the difference
    """
    return [j - i for i, j in zip(a[:-1], a[1:])]


def weatherWindow(user_inputs, olc):
    """
    this functions returns the starting times and the durations of all weather
    windows found in the met-ocean data for the given operational limit
    conditions (olc)
    """
    # Initialisation
    met_ocean = user_inputs['metocean']
    ww = {'start': 0,
          'duration': 0}
    # Operational limit conditions (consdiered static over the entire duration of the marine operation fro the moment)
    timeStep = met_ocean['hour [-]'].ix[1] - met_ocean['hour [-]'].ix[0]
    # resourceDataPointNb = len(met_ocean.waveHs)
    # Build the binary weather windows: 1=authorized access, 0=denied access
    Hs_bin = map(float, met_ocean['Hs [m]'] > olc['maxHs'])
    Ws_bin = map(float, met_ocean['Ws [m/s]'] > olc['maxWs'])

    WW_bin = Hs_bin or Ws_bin

    # Determine the durations and the starting times of the weather windows
    # Look for all indexes permitting access
    WW_authorized = indices(WW_bin, lambda x: x == 1)
    if not WW_authorized:
        print'Not a single permitting weather window was found with the criteria specified for one vessel with these met-ocean data!'
    else:
        # Return the number of consecutive time steps where marine operations are not permitted ("Gap") or 0 otherwise
        WW_authorized = numpy.array(WW_authorized)
        index = numpy.array(range(len(WW_authorized)))
        WW_authorized_0 = WW_authorized - index
        WW_Gap1 = differences(WW_authorized_0)
        # Find position of consecutive permitting weather window among Gap
        WW_posConsecutiveGap1 = indices([1] + WW_Gap1, lambda x: x == 1)
        # Give the number of consecutive permitting weather conditions without
        # interuption, i.e the durations of all weather windows
        # except the last one!
        WW_findConsecutive1 = differences(WW_posConsecutiveGap1)
        WW_findConsecutive1_2 = [1] + WW_findConsecutive1
        WW_findConsecutive1_2 = numpy.cumsum(WW_findConsecutive1_2)
        # Locate the starting times of each weather windows
        WW_posConsecutive1 = WW_authorized[WW_findConsecutive1_2]
        # assign starting times and durations of all weather windows to output
        # tt = numpy.multiply(timeStep,range(WW_posConsecutive1))
        # WW_posConsecutive1 * timeStep
        ww['start'] = WW_posConsecutive1 * timeStep
        # [x*timeStep for x in WW_posConsecutive1]
        duration = numpy.array(WW_findConsecutive1)
        ww['duration'] = duration * timeStep
    return ww


def sched(x, install, log_phase, log_phase_id,
          user_inputs, hydrodynamic_outputs, electrical_outputs, MF_outputs):

    for seq in range(len(log_phase.op_ve)): # loop over the number of operation
    # sequencing options

        for ind_sol in range(len(log_phase.op_ve[seq].sol)): # loop over the
        # number of solutions, i.e feasible combinations of
        # port/vessel(s)/equipment(s)

            op_dur_prep = []
            op_dur_sea = []
            olc_sea_Hs = []
            olc_sea_Tp = []
            olc_sea_Ws = []
            olc_sea_Cs = []
            olc = {'maxHs': 0,
                   'maxTp': 0,
                   'maxWs': 0,
                   'maxCs': 0}
            # check the nature of the logistic phase
            if log_phase_id == 'Devices':
#                sched = sched_dev(install, log_phase, user_inputs, hydrodynamic_outputs)
                # check the transportation method
                # (1st branch in the decision making tree)
                if log_phase.op_ve[seq].description == 'On-deck transportation':
                    # check the device assembly strategy
                    # (2nd and FINAL branch in the decision making tree)
                    assemb_method = user_inputs['device']['assembly strategy [-]'].ix[0]
                    if assemb_method == '([A,B,C,D])':
                        # calculate the number of devices
                        nb_dev = len(hydrodynamic_outputs['device [-]'])
                        elem_area = [0]*nb_dev
                        elem_mass = [0]*nb_dev
                        for dev in range(nb_dev): # loop over the number of devices
                            # calculate the area and dry mass of all elements
<<<<<<< HEAD
                            elem_area[dev] = user_inputs['device']['length [m]'].ix[0]*user_inputs['device']['width [m]'].ix[0]
                            elem_mass[dev] = user_inputs['device']['dry mass [kg]'].ix[0]/1000
=======
                            elem_area[dev] = user_inputs['device']['length [m]'].ix[0]*user_inputs['device']['width [m]'].ix[0] # [m^2]
                            elem_mass[dev] = user_inputs['device']['dry mass [kg]'].ix[0]/1000 # [ton]
                            
>>>>>>> 589bf62a3545f9674767c94075da855a0179e66d
                        nb_elem_port = nb_dev # initialise the number of elements to be transported that are initially at port
                        nb_journey = 0 # initialise the number of vessel journeys
                        nb_el_journey = [] # initialise the list of number of elements per journey
                        while nb_elem_port > 0:
                            # extract the panda series of the tranporting vessel
                            # assumption: the first vessel is always the transporting vessel 
                            sol_pd_series = log_phase.op_ve[seq].sol[ind_sol]['VEs'][0][2]
                            # extract the deck area and cargo
                            deck_area = sol_pd_series.ix['Deck space [m^2]']
                            deck_cargo = sol_pd_series.ix['Max. cargo [t]']
                            # determine the cumulative vector of element areas and dry masses
                            elem_area_accum = list(numpy.cumsum(elem_area))
                            elem_mass_accum = list(numpy.cumsum(elem_mass))
                            # determine the maximum number of elements that can fit on-deck due to max deck area or max deck cargo limitations
                            nb_dev_area = indices(elem_area_accum, lambda x: x>deck_area)
                            if not nb_dev_area:
                                nb_dev_area = len(elem_area_accum)
                            else:
                                nb_dev_area = min(nb_dev_area)
                            nb_dev_mass = indices(elem_mass_accum, lambda x: x>deck_cargo)
                            if not nb_dev_mass:
                                nb_dev_mass = len(elem_mass_accum)
                            else:
                                nb_dev_mass = min(nb_dev_mass)
                            nb_el_journey.append(min([nb_dev_area,nb_dev_mass]))
                            # update the number of elements remaining at port and their areas/masses lists
                            if nb_el_journey[nb_journey] == nb_elem_port:
                                nb_elem_port = 0
                            elif nb_el_journey[nb_journey] == 0:
                                # error that means not a single element can fit!
                                print 'not a single device can fit in the deck!' 
                            else:
                                nb_elem_port = nb_elem_port - nb_el_journey[nb_journey]
                                elem_area = elem_area[nb_el_journey[-1]:]
                                elem_mass = elem_mass[nb_el_journey[-1]:]
                            # update the number of vessel journeys
                            nb_journey = nb_journey + 1
                            
                            ind_el = 0
                        for jour in range(nb_journey):
                            # number of operation sequence in the preparation phase
                            nb_op_prep = len(log_phase.op_ve[seq].op_seq_prep)                            
                            # determine the duration of the logistic phase preparation before departure of the vessel(s)
                            for op_prep in range(nb_op_prep): # loop over the nb of onshore logistic operations
                                log_op_prep = log_phase.op_ve[seq].op_seq_prep[op_prep]
                                # discriminate between the time assessment methods
                                if log_op_prep.time_value: # direct value
                                    op_dur_prep.append(log_op_prep.time_value)
                                elif log_op_prep.time_function: # function
                                    # type of function
                                    if log_op_prep.time_function == "transit_algorithm":
                                        port_pd = log_phase.op_ve[seq].sol[ind_sol]['port']
                                        UTM_port = [port_pd.ix['UTM x [m]'],
                                                    port_pd.ix['UTM y [m]'],
                                                    port_pd.ix['UTM zone [-]']]
                                        site = user_inputs['site']
                                        UTM_site = [site['x coord [m]'].ix[0],
                                                    site['y coord [m]'].ix[0],
                                                    site['zone [-]'].ix[0]]
                                        port_2_site_dist = transit_algorithm(UTM_port, UTM_site)
                                        nb_ves_type = range(len(log_phase.op_ve[seq].sol[ind_sol]['VEs']))
                                        # loop over the nb of vessel types                                        
                                        for vt in nb_ves_type:
                                            ves_speed[vt] = log_phase.op_ve[seq].sol[ind_sol]['VEs'][vt][2].ix['Transit speed [m/s]']
                                        ves_slow = 3.6*min(ves_speed) # [km/h]
                                        port_2_site_time = port_2_site_dist/ves_slow
                                        # append transit time to the preparation time
                                        op_dur_prep.append(port_2_site_time)
                                    elif log_op_prep.time_function == "distance":
                                        dist_tot = 0
                                        dist_el = []
                                        for el in range(nb_el_journey[jour]):
                                            UTM_el_i = [hydrodynamic_outputs['x coord [m]'].ix[el],
                                                        hydrodynamic_outputs['y coord [m]'].ix[el],
                                                        hydrodynamic_outputs['zone [-]'].ix[el]]
                                            UTM_el_f = [hydrodynamic_outputs['x coord [m]'].ix[el+1],
                                                        hydrodynamic_outputs['y coord [m]'].ix[el+1],
                                                        hydrodynamic_outputs['zone [-]'].ix[el+1]]
                                            dist_el[el] = distance(UTM_el_i,UTM_el_f)
                                            dist_tot = dist_tot + dist_el[el]  
                                        
                                elif log_op_prep.time_other:
                                    if log_op_prep.time_other == "vesselDB['Mob time [h]']":
                                        mob_time = 0
                                        op_dur_prep.append(mob_time)  
                                    elif log_op_prep.time_other == "device['assembly duration [h]']":
                                        assemb_time = 0
                                        op_dur_prep.append(assemb_time)  
                                    elif log_op_prep.time_other == "device['connect duration [h]']":
                                        dev_connect_time = 0
                                        op_dur_prep.append(dev_connect_time)  
                                    elif log_op_prep.time_other == "device['disconnect duration [h]']":
                                        dev_disconnect_time = 0
                                        op_dur_prep.append(dev_disconnect_time)
                                        
                            ind_el = ind_el + nb_el_journey[jour]
                            # determine the sea duration
                            
                        # add demobilisation time to finalise the logistic phase

#                    elif assemb_method == '([A,B,C],D)':
#
#
#                # determine t
#            log_phase.op_ve[seq].op_seq_prep[2].description # access id of mobilisation

#            for op in range(len(log_phase.op_ve[seq].op_sequence)):
#                log_op = log_phase.op_ve[seq].op_sequence
#                if log_op[op].description == "Transportation from port to site":
#                    coordinates = 'none'
#                    map_land = 'none'
#                    dist_p2s = distance(coordinates, map_land)  # [km]
#                    sailing_speed = 3.6 * log_phase.op_ve[seq].sol[ind_sol]['Transit speed [m/s]']  # [km/h]
#                    # sailing_speed = 20.0  # [km/h]
#                    log_op[op].time = dist_p2s / sailing_speed  # [h]
#                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
#                    olc_sea_Hs[len(olc_sea_Hs):] = [1.5]
#                    # olc_sea_Hs[len(olc_sea_Hs):] =  log_phase.op_ve[seq].ve_combination[combi].solution[2]
#                elif log_op[op].description == "Mobilisation":
#                    log_op[op].time = 48
#                    op_dur_prep[len(op_dur_prep):] = [log_op[op].time]
#                elif log_op[op].description == "Assembly at port":
#                    log_op[op].time = 0
#                    op_dur_prep[len(op_dur_prep):] = [log_op[op].time]
#                elif log_op[op].description == "Vessel preparation and loading":
#                    log_op[op].time = 24
#                    op_dur_prep[len(op_dur_prep):] = [log_op[op].time]
#                elif log_op[op].description == "Seafloor and equipment preparation on-site":
#                    log_op[op].time = 0.5
#                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
#                elif log_op[op].description == "Driven pile foundation seafloor penetration through drilling rig + positioning":
#                    log_op[op].time = 3
#                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
#                    olc_sea_Ws[op] = 20  # [m/s]
#                elif log_op[op].description == "Driven pile foundation seafloor penetration through hammering + positioning":
#                    log_op[op].time = 5
#                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
#                elif log_op[op].description == "Driven pile foundation seafloor penetration through vibro-driving + positioning":
#                    log_op[op].time = 6
#                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
#                elif log_op[op].description == "Transportation from site to port":
#                    coordinates = 'none'
#                    map_land = 'none'
#                    dist_p2s = distance(coordinates, map_land)  # [km]
#                    sailing_speed = 3.6 * log_phase.op_ve[seq].sol[ind_sol].sol_ves[0]['Transit speed [m/s]']  # [km/h]
#                    log_op[op].time = dist_p2s / sailing_speed  # [h]
#                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
#
#            if olc_sea_Hs:
#                olc['maxHs'] = min(olc_sea_Hs)
#            if olc_sea_Tp:
#                olc['maxTp'] = min(olc_sea_Tp)
#            if olc_sea_Ws:
#                olc['maxWs'] = min(olc_sea_Ws)
#            if olc_sea_Cs:
#                olc['maxCs'] = min(olc_sea_Cs)
#
#            weather_wind = weatherWindow(user_inputs, olc)
#
#            dur_total_sea = sum(op_dur_sea)
#            if x == 0:  # find layer of installation plan
#                start_proj = user_inputs['device']['Project starting date [-]'].ix[0]
#                starting_time = start_proj + sum(op_dur_prep)
#            elif x > 0:  # to be implemented (dummy not functional at the moment)
#                last_end_time = max(install['schedule'][end_time])
#                starting_time = last_end_time + sum(op_dur_prep)
#
#            index_ww_start = indices(weather_wind['start'], lambda x: x > starting_time)
#            # and weatherWind['duration'] >= duration_total)/
#            index_ww_dur = indices(weather_wind['duration'], lambda x: x >= dur_total_sea)
#            index_ww = index_ww_start or index_ww_dur
#            waiting_time = weather_wind['start'][index_ww[0]] - starting_time
#            log_phase.op_ve[seq].sol[ind_sol].schedule = {'olc': olc,
#                                                      'log_op_dur_all': op_dur_prep + op_dur_sea,
#                                                      'preparation': sum(op_dur_prep),
#                                                      'sea time': dur_total_sea,
#                                                      'weather windows': weather_wind,
#                                                      'waiting time': waiting_time}

    sol = {}
#    sol[0] = log_phase.op_ve[1].sol[0].schedule
#    sol[1] = log_phase.op_ve[1].sol[1].schedule

    return sol, log_phase
