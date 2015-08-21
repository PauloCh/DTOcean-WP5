"""
@author: WavEC Offshore Renewables 
email: boris.teillant@wavec.org; paulo@wavec.org

wp1.py is a function which determines the logistic requirement associated with 
one logistic phase dealing with the installation of devices


Parameters
----------
log_phase : Class
 Class of the logistic phase under consideration for assessment
log_phase_id : str
 string describing the ID of the logistic phase under consideration
user_inputs : dict
 dictionnary containing all required inputs to WP5 coming from WP1/end-user

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


def wp1_feas(log_phase, log_phase_id, user_inputs):
    deck_loading = user_inputs['device']['length [m]'].ix[0] * user_inputs['device']['width [m]'].ix[0] / user_inputs['device']['drymass [kg]'].ix[0]
    deck_area = user_inputs['device']['length [m]'].ix[0] * user_inputs['device']['width [m]'].ix[0]
    feasibility = {'equipment': [],
                   'vessel': {'Deck loading [m2/ton]': ['Sup', 'all', deck_loading],
                              'Deck area [m2]': ['Sup', 'all', deck_area]}}
    return feasibility
