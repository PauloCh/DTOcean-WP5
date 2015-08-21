"""
@author: WavEC Offshore Renewables 
email: boris.teillant@wavec.org; paulo@wavec.org

wp3.py is a function which determines the logistic requirement associated with 
one logistic phase dealing with the installation of the electrical 
infrastructure


Parameters
----------
log_phase : Class
 Class of the logistic phase under consideration for assessment
log_phase_id : str
 string describing the ID of the logistic phase under consideration
wp3_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP3

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


def wp3_feas(log_phase, log_phase_id, user_inputs):
    # TO-DO
    feasibility = {'equipment': [],
                   'vessel': []}
    return feasibility
