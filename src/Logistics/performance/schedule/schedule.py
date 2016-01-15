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
import utm
import transit_algorithm

def distance(UTM_ini, UTM_fin):
    """
    distance returns the calculated distance (in kms) between two points
    defined in the UTM coordinate system
    """
# point_i = (lat_i, long_i)
#point_if= (lat_f, long_f)
#        length = great_circle(point_i, point_f).kilometers
# gives you a distance between two coordinate in dd.dd in kms
# to get dd.dd from utm you can use:
# utm.to_latlon(ini_x_utm, ini_y_utm, ini_zone_utm[1], ini_zone_utm[2])
    return 20.0


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


def sched(x, install, log_phase, user_inputs, hydrodynamic_outputs, electrical_outputs, MF_outputs, log_phase_id):

    for seq in range(len(log_phase.op_ve)): # loop over the number of operation
    # sequencing options

        for ind_sol in range(len(log_phase.op_ve[seq].sol)): # loop over the
        # number of feasible combinations of port/vessel(s)/equipment(s)
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
            if log_phase_id == 'Devices': # check the nature of the logistic phase
                if log_phase.op_ve[seq].description == 'On-deck transportation': # check the transportation method
                    assemb_method = user_inputs['device']['assembly strategy [-]'].ix[0]
                    if assemb_method == '([A,B,C,D])':
        elem_area[elem_id] = user_inputs['device']['length [m]'].ix[0] * user_inputs['device']['width [m]'].ix[0]
        elem_cargo[elem_id] = user_inputs['device']['dry mass [kg]'].ix[0]/1000
        deck_loading = user_inputs['device']['dry mass [kg]'].ix[0] / (user_inputs['device']['length [m]'].ix[0] * user_inputs['device']['width [m]'].ix[0])

                    elif assemb_method == '([A,B,C],D)':
        deck_area = max(user_inputs['sub_device']['length [m]']['A':'C'] * user_inputs['sub_device']['width [m]']['A':'C'])
        deck_cargo = user_inputs['sub_device']['dry mass [kg]']['A':'C'].sum()/1000
        deck_loading = max(user_inputs['sub_device']['dry mass [kg]']['A':'C'] / (1000 * user_inputs['sub_device']['length [m]']['A':'C'] * user_inputs['sub_device']['width [m]']['A':'C']))
                    
                # determine t
            log_phase.op_ve[seq].op_sequence_mob[2].description # access id of mobilisation 

            for op in range(len(log_phase.op_ve[seq].op_sequence)):
                log_op = log_phase.op_ve[seq].op_sequence
                if log_op[op].description == "Transportation from port to site":
                    coordinates = 'none'
                    map_land = 'none'
                    dist_p2s = distance(coordinates, map_land)  # [km]
                    sailing_speed = 3.6 * log_phase.op_ve[seq].sol[ind_sol]['Transit speed [m/s]']  # [km/h]
                    # sailing_speed = 20.0  # [km/h]
                    log_op[op].time = dist_p2s / sailing_speed  # [h]
                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
                    olc_sea_Hs[len(olc_sea_Hs):] = [1.5]
                    # olc_sea_Hs[len(olc_sea_Hs):] =  log_phase.op_ve[seq].ve_combination[combi].solution[2]
                elif log_op[op].description == "Mobilisation":
                    log_op[op].time = 48
                    op_dur_prep[len(op_dur_prep):] = [log_op[op].time]
                elif log_op[op].description == "Assembly at port":
                    log_op[op].time = 0
                    op_dur_prep[len(op_dur_prep):] = [log_op[op].time]
                elif log_op[op].description == "Vessel preparation and loading":
                    log_op[op].time = 24
                    op_dur_prep[len(op_dur_prep):] = [log_op[op].time]
                elif log_op[op].description == "Seafloor and equipment preparation on-site":
                    log_op[op].time = 0.5
                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
                elif log_op[op].description == "Driven pile foundation seafloor penetration through drilling rig + positioning":
                    log_op[op].time = 3
                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
                    olc_sea_Ws[op] = 20  # [m/s]
                elif log_op[op].description == "Driven pile foundation seafloor penetration through hammering + positioning":
                    log_op[op].time = 5
                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
                elif log_op[op].description == "Driven pile foundation seafloor penetration through vibro-driving + positioning":
                    log_op[op].time = 6
                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]
                elif log_op[op].description == "Transportation from site to port":
                    coordinates = 'none'
                    map_land = 'none'
                    dist_p2s = distance(coordinates, map_land)  # [km]
                    sailing_speed = 3.6 * log_phase.op_ve[seq].sol[ind_sol].sol_ves[0]['Transit speed [m/s]']  # [km/h]
                    log_op[op].time = dist_p2s / sailing_speed  # [h]
                    op_dur_sea[len(op_dur_sea):] = [log_op[op].time]

            if olc_sea_Hs:
                olc['maxHs'] = min(olc_sea_Hs)
            if olc_sea_Tp:
                olc['maxTp'] = min(olc_sea_Tp)
            if olc_sea_Ws:
                olc['maxWs'] = min(olc_sea_Ws)
            if olc_sea_Cs:
                olc['maxCs'] = min(olc_sea_Cs)

            weather_wind = weatherWindow(user_inputs, olc)

            dur_total_sea = sum(op_dur_sea)
            if x == 0:  # find layer of installation plan
                start_proj = user_inputs['device']['Project starting date [-]'].ix[0]
                starting_time = start_proj + sum(op_dur_prep)
            elif x > 0:  # to be implemented (dummy not functional at the moment)
                last_end_time = max(install['schedule'][end_time])
                starting_time = last_end_time + sum(op_dur_prep)

            index_ww_start = indices(weather_wind['start'], lambda x: x > starting_time)
            # and weatherWind['duration'] >= duration_total)/
            index_ww_dur = indices(weather_wind['duration'], lambda x: x >= dur_total_sea)
            index_ww = index_ww_start or index_ww_dur
            waiting_time = weather_wind['start'][index_ww[0]] - starting_time
            log_phase.op_ve[seq].sol[ind_sol].schedule = {'olc': olc,
                                                      'log_op_dur_all': op_dur_prep + op_dur_sea,
                                                      'preparation': sum(op_dur_prep),
                                                      'sea time': dur_total_sea,
                                                      'weather windows': weather_wind,
                                                      'waiting time': waiting_time}

    sol = {}
#    sol[0] = log_phase.op_ve[1].sol[0].schedule
#    sol[1] = log_phase.op_ve[1].sol[1].schedule

    return sol, log_phase
