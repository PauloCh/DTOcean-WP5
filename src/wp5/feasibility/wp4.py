"""
@author: WavEC Offshore Renewables 
email: boris.teillant@wavec.org; paulo@wavec.org

wp1.py is a function which determines the logistic requirement associated with 
one logistic phase dealing with the installation of moorings and
foundation systems


Parameters
----------
log_phase : Class
 Class of the logistic phase under consideration for assessment
log_phase_id : str
 string describing the ID of the logistic phase under consideration
wp2_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP2
wp4_outputs : DataFrame
 Panda table containing all required inputs to WP5 coming from WP4

Returns
-------
feas_e : dict
 dictionnary containing all logistic requirements associated with every 
 equipment type of the logistic phase under consideration
feas_v : dict
 dictionnary containing all logistic requirements associated with every 
 vessel type of the logistic phase under consideration

Examples
--------
>>> WP5()


See also: ...

                       DTOcean project
                    http://www.dtocean.eu

                   WavEC Offshore Renewables
                    http://www.wavsec.org/en


"""


def wp4_feas(log_phase, log_phase_id, wp2_outputs, wp4_outputs):

    if log_phase_id == 'F_driven':
        # Equipment feasiblity
        # Hammer sleeve diameter
        diam_u_f = []  # list of diameter of each foundation per unit
        load_u_f = []  # list of loading due to each foundation per unit
        area_u_f = []  # list of area occupied by each foundation per unit
        diam_u = []  # list of max diameter per unit
        load_u = []  # list of loading due to the set of foundation(s) per unit
        area_u = []  # list of loading occupied by the set of foundation(s) per unit
        for dev in range(wp2_outputs['NumOFunits'].ix[0]):
            for x in range(wp4_outputs['quantity'].ix[0]):
                key1 = "diameter foundation " + str(x) + " [m]"
                key2 = "length foundation " + str(x) + " [m]"
                key3 = "weight foundation " + str(x) + " [kg]"
                load_u_f[len(load_u_f):] = [wp4_outputs[key1].ix[0] * wp4_outputs[key2].ix[0] / wp4_outputs[key3].ix[0]]
                area_u_f[len(area_u_f):] = [wp4_outputs[key1].ix[0] * wp4_outputs[key2].ix[0]]
                diam_u_f[len(diam_u_f):] = [wp4_outputs[key1].ix[0]]
            load_u[len(load_u):] = [max(load_u_f[dev * x:(dev + 1) * x])]
            area_u[len(area_u):] = [sum(area_u_f[dev * x:(dev + 1) * x])]
            diam_u[len(diam_u):] = [max(diam_u_f[dev * x:(dev + 1) * x])]
        deck_loading = max(load_u)
        deck_area = max(area_u)
        sleeve_diam = max(diam_u)

        feas_e = {'Hammer': [['Sleeve diameter [m]', 'sup', sleeve_diam]]}
        feas_v = {'Crane Barge': [['Deck loading [ton/m2]', 'sup', deck_loading],
                                  ['Deck space [m2]', 'sup', deck_area]],
                  'Crane Vessel': [['Deck loading [ton/m2]', 'sup', deck_loading],
                                   ['Deck space [m2]', 'sup', deck_area]],
                  'JUP Barge': [['Deck loading [ton/m2]', 'sup', deck_loading],
                                ['Deck space [m2]', 'sup', deck_area]],
                  'JUP Vessel': [['Deck loading [ton/m2]', 'sup', deck_loading],
                                 ['Deck space [m2]', 'sup', deck_area]]}
    elif log_phase_id == 'F_suction':
        pass
    elif log_phase_id == 'F_gravity':
        pass
    return feas_e, feas_v
