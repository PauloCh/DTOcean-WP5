# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:53:24 2015

@author: BTeillant
"""

def sched(install, log_phase):
    for seq in range(len(log_phase.op_ve)):
            for op in range(len(log_phase.op_ve[seq].op_sequence)):
                log_op = log_phase.op_ve[seq].op_sequence
                if log_op[op].description == "Transportation from port to site":
                    coordinates = 'none'
                    map_land = 'none'
                    dist_p2s = distance(coordinates, map_land) # [km]
                    sailing_speed = 20.0 # [km/h]
                    log_op[op].time = dist_p2s/sailing_speed
                    
                    
    def distance(coordinates, map_land)
        '''
        distance returns the calculated distance between two points
        TO BE PROVIDED BY UEDIN (WP3)
        '''
        return 20.0s
    def indices(a, func):
        '''
        indices returns the indices of a vector "a" that satisfy the 
        conditional function "func"
        '''
        return [i for (i, val) in enumerate(a) if func(val)]
    def differences(a):
        '''
        differences returns a vector containing the difference 
        '''
        return [j-i for i, j in zip(a[:-1], a[1:])] 
        
    def weatherWindow(user_inputs, olc):
        '''
        this functions returns the starting times and the durations of all weather
        windows found in the met-ocean data for the given operational limit
        conditions (olc)
        '''
        # Initialisation
        met_ocean = user_inputs['metocean']
        
        # Operational limit conditions (consdiered static over the entire duration of the marine operation fro the moment)
        timeStep = met_ocean.hour.ix[1]-met_ocean.hour.ix[0]
        resourceDataPointNb = len(met_ocean.waveHs)
        # Build the binary weather windows: 1=authorized access, 0=denied access
        Hs_bin = map(float, met_ocean.waveHs > olc['maxHs'])
        Ws_bin = map(float, met_ocean.windSpeed > olc['maxWs'])

        WW_bin = Hs_bin or Ws_bin

        ## Determine the durations and the starting times of the weather windows
        # Look for all indexes permitting access
        WW_authorized = indices(WW_bin,lambda x: x==1)
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
            #tt = numpy.multiply(timeStep,range(WW_posConsecutive1))
            #WW_posConsecutive1 * timeStep
            ww['start'] = WW_posConsecutive1 * timeStep
            #[x*timeStep for x in WW_posConsecutive1]
            duration = numpy.array(WW_findConsecutive1)
            ww['duration'] = duration * timeStep
        return  ww
    durations = 
    olc['maxHs'] = min(log_sol['vesselSol'].ix['Max. Hs'],log_sol['equipmentSol'].ix[17]) # [1.5, 1.5, 1.5, 1.5, 1.5]
    olc['maxWs'] = min(log_sol['vesselSol'].ix['Max. Us'],log_sol['equipmentSol'].ix[20]) #
    ww = {'start': 'none',
         'duration': 'one'}
    weather_wind = weatherWindow(metOcean, owl, ww)
    #durations.pop(0)
    duration_total = sum(durations) - durations[0]
    starting_time = 0
    index_ww_start = indices(weather_wind['start'], lambda x: x>starting_time)
                             #and weatherWind['duration']>=duration_total)/
    index_ww_dur = indices(weather_wind['duration'], lambda x: x>=duration_total)
    index_ww = index_ww_start or index_ww_dur
    waiting_time = weather_wind['start'][index_ww[0]] - starting_time