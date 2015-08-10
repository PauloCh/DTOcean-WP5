# -*- coding: utf-8 -*-
"""py.test tests on main.py

.. moduleauthor:: Mathew Topper <mathew.topper@tecnalia.com>
"""

from dtocean_installation import main

def test_run():
    '''Test the run method of main'''
    
    (environment_data,
    technology_data,
    equipment_data,
    vessel_data,
    log_pre_sol,
    log_req,
    equipSol,
    vesselSol,
    portSol,
    log_sol,
    log_sched,
    log_cost) = main.run(0)
    
    print log_sol.keys()
    assert log_cost <= 0.
