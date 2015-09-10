# -*- coding: utf-8 -*-
"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

This module governs the definition of the logistic phases. The functions included
are responsible to initialize and characterize the logistic phases both of the
installation and O&M modules. The functions return a class of each logistic phase
characterized in terms of operations sequence and vessel & equipment combination.

BETA VERSION NOTES: In this version, only two logistic phases were characterized,
one related to Moorings and Foundation Installation: Driven Pile, and another
related to Operation and Maintenance: Offshore Inspection.
"""

from .classes import LogPhase, DefPhase

from .e_export import initialize_e_export_phase
from .e_array import initialize_e_array_phase
from .e_cp import initialize_e_cp_phase

from .f_driven import initialize_f_drive_phase
from .f_suction import initialize_f_suction_phase
from .f_gravity import initialize_f_gravity_phase

from .m_drag import initialize_m_drag_phase
from .m_direct import initialize_m_direct_phase

from .d_fixed import initialize_d_fixed_phase
from .d_floating import initialize_d_floating_phase


def logPhase_install_init(log_op, vessels, equipments):
    """This function initializes and characterizes all logistic phases associated
    with the installation module. The first step uses LogPhase class to initialize
    each class with a key ID and description, the second step uses the DefPhase
    class to characterize each phase with a set of operation sequences and vessel
    and equipment combinations.
    Explanation of the key ID numbering system implemented:
     1st digit: 1 = Installation;
                9 = O&M
     2nd digit: 0 = Electrical infrastructure;
                1 = Moorings and foundations;
                2 = Wave and Tidal devices;
     3rd digit: component/sub-system type - differ depending on the logistic phase
     4th digit: method (level 1) - differ depending on the logistic phase
     5th digit: sub-method (level 2) - differ depending on the logistic phase

    Parameters
    ----------
    log_op : dict
     dictionnary containing all classes defining the individual logistic operations
    vessels : DataFrame
     Panda table containing the vessel database
    equipments : DataFrame
     Panda table containing the equipment database

    Returns
    -------
    logPhase_install : dict
     dictionnary containing all classes defining the logistic phases for installation
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_install = {'E_export': initialize_e_export_phase(log_op, vessels, equipments),
                        'E_array': initialize_e_array_phase(log_op, vessels, equipments),
                        'E_cp': initialize_e_cp_phase(log_op, vessels, equipments),

                        'F_driven': initialize_f_drive_phase(log_op, vessels, equipments),
                        'F_suction': initialize_f_suction_phase(log_op, vessels, equipments), 
                        'F_gravity': initialize_f_gravity_phase(log_op, vessels, equipments), 

                        'M_drag': initialize_m_drag_phase(log_op, vessels, equipments),
                        'M_direct': initialize_m_direct_phase(log_op, vessels, equipments),

                        'D_fixed': initialize_d_fixed_phase(log_op, vessels, equipments),
                        'D_floating': initialize_d_floating_phase(log_op, vessels, equipments)
                        }


    # 2nd Level - Define the diferent operations sequence and corresponding V&E combination for each Phase



    return logPhase_install






from om_topside import initialize_om_topside_phase 
                   
from om_underwater_divers import initialize_om_underwater_divers_phase 
from om_underwater_rov import initialize_om_underwater_rov_phase

from om_moorings import initialize_om_moorings_phase 
from om_electrical import initialize_om_electrical_phase 

from rt_ondeck import initialize_rt_ondeck_phase 
from rt_towing import initialize_rt_towing_phase

from rt_mooring import initialize_rt_mooring_phase 
from rt_umbilical import initialize_rt_umbilical_phase 



def logPhase_OM_init(log_op, vessels, equipments):
    """This function initializes and characterizes all logistic phases associated
    with the O&M module. The first step uses LogPhase class to initialize
    each class with a key ID and description, the second step uses the DefPhase
    class to characterize each phase with a set of operation sequences and vessel
    and equipment combinations.
    Explanation of the key ID numbering system implemented:
     1st digit: 1 = Installation;
                9 = O&M
     2nd digit: 0 = Electrical infrastructure;
                1 = Moorings and foundations;
                2 = Wave and Tidal devices;
     3rd digit: component/sub-system type - differ depending on the logistic phase
     4th digit: method (level 1) - differ depending on the logistic phase
     5th digit: sub-method (level 2) - differ depending on the logistic phase

    Parameters
    ----------
    log_op : dict
     dictionnary containing all classes defining the individual logistic operations
    vessels : DataFrame
     Panda table containing the vessel database
    equipments : DataFrame
     Panda table containing the equipment database

    Returns
    -------
    logPhase_OM : dict
     dictionnary containing all classes defining the logistic phases for O&M
    """

    # 1st Level - Initialize the logistic phases through LogPhase classes

    logPhase_OM = {'Om_topside': initialize_om_topside_phase(log_op, vessels, equipments), 
                   
                   'Om_underwater_divers': initialize_om_underwater_divers_phase(log_op, vessels, equipments), 
                    'Om_underwater_rov': initialize_om_underwater_rov_phase(log_op, vessels, equipments), 

                    'Om_moorings': initialize_om_moorings_phase(log_op, vessels, equipments), 
                    'Om_electrical': initialize_om_electrical_phase(log_op, vessels, equipments), 

                    'Rt_ondeck': initialize_rt_ondeck_phase(log_op, vessels, equipments), 
                    'Rt_towing': initialize_rt_towing_phase(log_op, vessels, equipments), 

                    'Rt_mooring': initialize_rt_mooring_phase(log_op, vessels, equipments), 
                    'Rt_umbilical': initialize_rt_umbilical_phase(log_op, vessels, equipments) 
                    }    
                    
                        

    # 2nd Level - Define the diferent operations sequence and corresponding v&e combination for each Phase


    return logPhase_OM
