from Logistics.feasibility.user_inputs import user_inputs_feas
from Logistics.feasibility.electrical import electrical_feas
from Logistics.feasibility.MF import MF_feas


def glob_feas(log_phase, log_phase_id, user_inputs, hydrodynamic_outputs, electrical_outputs, MF_outputs):
    """glob.py contains a function that calls the appropriate sub-functions to
    determine the logistic requirements associated with one logistic phase
    
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
    feasibility : tuple
     tuple containing all logistic requirements associated with every vessel
     and equipment type of the logistic phase under consideration
    """
    
    if any(log_phase_id in s for s in ['E_export', 'E_array', 'E_cp']):
        feasibility = electrical_feas(log_phase, log_phase_id, electrical_outputs)
    elif any(log_phase_id in s for s in ['F_driven', 'F_gravity', 'Moorings']):
        feasibility = MF_feas(log_phase, log_phase_id, hydrodynamic_outputs, MF_outputs)
    elif any(log_phase_id in s for s in ['Devices']):
        feasibility = user_inputs_feas(log_phase, log_phase_id, user_inputs)
    return feasibility
