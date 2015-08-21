"""
@author: WavEC Offshore Renewables 
email: boris.teillant@wavec.org; paulo@wavec.org

glob.py contains a function that calls the appropriate sub-functions to 
determine the logistic requirement associated with one logistic phase


Parameters
----------
log_phase : Class
 Class of the logistic phase under consideration for assessment
log_phase_id : str
 string describing the ID of the logistic phase under consideration
user_inputs : dict
 dictionnary containing all required inputs to WP5 coming from WP1/end-user
wp2_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP2
wp3_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP3
wp4_outputs : DataFrame
 Panda table containing all required inputs to WP5 coming from WP4

Returns
-------
feasibility : typle
 tuple containing all logistic requirements associated with every vessel 
 and equipment type of the logistic phase under consideration

Examples
--------
>>> WP5()


See also: ...

                       DTOcean project
                    http://www.dtocean.eu

                   WavEC Offshore Renewables
                    http://www.wavsec.org/en


"""
from wp5.feasibility.wp1 import wp1_feas
from wp5.feasibility.wp4 import wp4_feas
from wp5.feasibility.wp3 import wp3_feas
# wp3_feas, wp4_feas


def glob_feas(log_phase, log_phase_id, user_inputs, wp2_outputs, wp3_outputs, wp4_outputs):
    if any(log_phase_id in s for s in ['E_export', 'E_array', 'E_cp']):
        feasibility = wp3_feas(log_phase, log_phase_id, wp3_outputs)
    elif any(log_phase_id in s for s in ['F_driven', 'F_suction', 'F_gravity', 'M_drag', 'M_direct']):
        feasibility = wp4_feas(log_phase, log_phase_id, wp2_outputs, wp4_outputs)
    elif any(log_phase_id in s for s in ['D_fixed', 'D_floating']):
        feasibility = wp1_feas(log_phase, log_phase_id, user_inputs)
    return feasibility
