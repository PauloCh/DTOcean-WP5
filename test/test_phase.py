# -*- coding: utf-8 -*-
"""py.test tests on main.py

.. moduleauthor:: Mathew Topper <mathew.topper@tecnalia.com>
"""

from dtocean-installation import main
from dtocean-installation.wp5.logistics.phase import FeasibilityPhase

def test_phase():
    '''Test the run method of main'''
    
    phase = FeasibilityPhase("id", "description", "ops_sequence", "v_sequence", "feasibility")
    assert phase.feasibility == "feasibility"
