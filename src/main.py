"""
@author: WavEC Offshore Renewables
email: boris.teillant@wavec.org; paulo@wavec.org

main.py is the main file of the WP5 module within the suite of design tools
developped under the EU FP7 DTOcean project. main.py provides an estimation of
the predicted performance of feasible maritime infrastructure solutions
that can carry out marine operations pertaining to the installation of
wave and tidal energy arrays.

main.py can be described in five core sub-modules:
0- Loading input data
1- Initialising the logistic classes
2- Defining the installation plan
3- Selecting the installation port
4- Performing the assessment of all logistic phases sequencially, following
   six steps:
    (i) characterizartion of logistic requirements
    (ii) selection of the maritime infrastructure
    (iii) schedule assessment of the logistic phase
    (iv) cost assessment of the logistic phase
    (v) risk assessment of the logistic phase
    (vi) environmental impact assessment of the logistic phase

Parameters
----------
vessels : DataFrame
 Panda table containing the vessel database
equipments : DataFrame
 Panda table containing the equipment database
ports : DataFrame
 Panda table containing the ports database
user_inputs : dict
 dictionnary containing all required inputs to WP5 coming from WP1/end-user
wp2_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP2
wp3_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP3
wp4_outputs : DataFrame
 Panda table containing all required inputs to WP5 coming from WP4
wp6_outputs : dict
 dictionnary containing all required inputs to WP5 coming from WP6

Returns
-------
logOp : dict
 dictionnary containing all classes defining the individual logistic operations
logPhase_install : dict
 dictionnary containing all classes defining the logistic phases for installation
logPhase_OM : dict
 dictionnary containing all classes defining the logistic phases for O&M
install_plan : dict
 dictionnary containing the plan of the logistic phases for installation
install_port : dict
 dictionnary containing the results of the port selection
install : dict
 dictionnary compiling all key results obtained from the assessment of the
 logistic phases for installation
log_phase : Class
 Class of the logistic phase under consideration for assessment

Examples
--------
>>> WP5()


See also: ...

                       DTOcean project
                    http://www.dtocean.eu

                   WavEC Offshore Renewables
                    http://www.wavec.org/en


"""

from os import path

from wp5.load import load_vessel_data, load_equipment_data, load_port_data
from wp5.load.wp_bom import load_WP1_BoM, load_WP2_BoM
from wp5.load.wp_bom import load_WP3_BoM, load_WP4_BoM
from wp5.load.wp_bom import load_WP6_BoM
from wp5.logistics.operations import logOp_init
from wp5.logistics.phase import logPhase_install_init
from wp5.installation import planning, select_port
from wp5.feasibility.glob import glob_feas
from wp5.selection.select_ve import select_e, select_v
from wp5.selection.match import compatibility_ve
from wp5.performance.schedule.schedule import sched
from wp5.performance.economic.eco import cost

# # Set directory paths for loading inputs (@Tecanalia)
mod_path = path.dirname(path.realpath(__file__))


def database_file(file):
    """shortcut function to load files from the database folder
    """
    fpath = path.join('databases', '{0}'.format(file))
    db_path = path.join(mod_path, fpath)
    return db_path


#def run():
"""
Loading required inputs and database into panda dataframes
"""
vessels = load_vessel_data(database_file("Vessel_Database_python.xlsx"))
equipments = load_equipment_data(database_file("Equipment_Database_python.xlsx"))
ports = load_port_data(database_file("Ports_Database2_python.xlsx"))

user_inputs = load_WP1_BoM(database_file("WP1_BoM.xlsx"),
                           database_file("VianaCastelo.csv"))
wp2_outputs = load_WP2_BoM(database_file("WP2_BoM.xlsx"))
wp3_outputs = load_WP3_BoM(database_file("WP3_BoM.xlsx"))
wp4_outputs = load_WP4_BoM(database_file("WP4_BoM.csv"))
wp6_outputs = load_WP6_BoM(database_file("WP6_BoM.xlsx"))

# Initialise logistic operations and logistic phases
logOp = logOp_init()

logPhase_install = logPhase_install_init(logOp, vessels, equipments)
#logPhase_OM = logPhase_OM_init(logOp, vessels, equipments)

# Determine the adequate installation logistic phase plan
install_plan = planning.install_plan(user_inputs, wp3_outputs, wp4_outputs)

# DUMMY-TO BE ERASED, install plan is constrained to F_driven because
# we just have the F_driven characterized for now
install_plan = {0: ['F_driven']}

# Select the most appropriate base installation port
install_port = select_port.install_port(user_inputs, wp3_outputs, wp4_outputs, ports)

# Incremental assessment of all logistic phase forming the the installation process
install = {'plan': install_plan,
           'port': install_port,
           'requirement': {},
           'eq_select': {},
           've_select': {},
           'combi_select': {},
           'schedule': {},
           'cost': {},
           'risk': {},
           'envir': {},
           'status': "pending"}

if install['status'] == "pending":
    # loop over the number of layers of the installation plan
    for x in range(len(install['plan'])):
        for y in range(len(install['plan'][x])):
            # extract the LogPhase ID to be evaluated from the installation plan
            log_phase_id = install['plan'][x][y]
            log_phase = logPhase_install[log_phase_id]
            # characterize the logistic requirements
            install['requirement'] = glob_feas(log_phase, log_phase_id,
                                               user_inputs, wp2_outputs,
                                               wp3_outputs, wp4_outputs)

            # selection of the maritime infrastructure
            install['eq_select'], log_phase = select_e(install, log_phase)
            install['ve_select'], log_phase = select_v(install, log_phase)

            # matching requirements for combinations of port/vessel(s)/equipment
            # install['combi_select'] = compatibility_vp(install, log_phase)
            install['combi_select'], log_phase = compatibility_ve(install, log_phase)

            # schedule assessment of the different operation sequence
            install['schedule'], log_phase = sched(x, install, log_phase, user_inputs, wp2_outputs, wp3_outputs, wp4_outputs)

            # cost assessment of the different operation sequenc
            install['cost'], log_phase = cost(install, log_phase)

            # TO DO -> risk and enviromental impact

#
#if __name__ == "__main__":
#    run()
