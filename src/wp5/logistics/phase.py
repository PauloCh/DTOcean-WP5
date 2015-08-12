
"""
phase.py is the file governing the definition of the logistic phases

"""

class LogPhase(object):

    def __init__(self, id, description, ops_sequence, ve_combination):
        self.id = id
        self.description = description
        self.ops_sequence = {}
        self.ve_combination = {}
#        self.feasibility = feasiblity
#        self.matching = matching
#        self.v&e&p_selected = {}
#        self.schedule = {}
#        self.time = {}
#        self.cost = {}
#        self.environmental = environment
#        self.risk = risk

    def set_sequence(self, key, ops_sequence):
        self.ops_sequence[key] = ops_sequence

    def set_combination(self, key, ve_combination):
        self.ve_combination[key] = ve_combination
        
class FeasiblityPhase(LogPhase):    
    
    def __init__(self, id, description, ops_sequence, ve_combination, feasibility):
        super(FeasiblityPhase, self).__init__(id, description,
                                                 ops_sequence, ve_combination)
        self.feasibility = feasibility
    
    def vessel_feasiblity(self, end_user_inputs, wp2_outputs, wp3_outputs,
                          wp4_outputs, wp6_output, vessels):
        if LogPhase.id == 100 or 101 or 102:                 
            deck_loading = 0
        elif LogPhase.id == 110 or 111 or 112:
            for dev in range(wp2_outpus['NumberOFnits']):
                for x in range(wp4_outputs['quantity'].ix[0]):
                    key1 = "diameter foundation " + str(x) + " [m]"
                    key2 = "length foundation " + str(x) + " [m]"
                    key3 = "weight foundation " + str(x) + " [kg]"
                    load_u_f[len(load_u_f):] = [wp4_outputs[key1].ix[0]*wp4_outputs[key2].ix[0]/wp4_outputs[key3].ix[0]]
                    area_u_f[len(area_u_f):] = [wp4_outputs[key1].ix[0]*wp4_outputs[key2].ix[0]]
                load_u[len(load_u):] = max(load_u_f[dev*x:(dev+1)*x])
                area_u[len(area_u):] = sum(area_u_f[dev*x:(dev+1)*x])
            deck_loading = max(load_u)
            deck_area = max(area_u)
                             
   
    
class op_sequence(object):

    def __init__(self, id, description, op_sequence):
        self.id = id
        self.description = description
        self.op_sequence = op_sequence

"""
#### Definition of the logistic pahase by invocaking the class LogPhase #######
# Invocation of the full list of logistic phases covered in WP5
# Explanation of the key ID numbering system implemented:
# 1st digit:  1 = Installation;
#             9 = O&M
# 2nd digit: 0 = Electrical infrastructure;
#            1 = Moorings and foundations;
#            2 = Wave and Tidal devices;
# 3rd digit: component/sub-system type - differ depending on the logistic phase
# 4th digit: method (level 1) - differ depending on the logistic phase
# 5th digit: sub-method (level 2) - differ depending on the logistic phase
####
"""

def logPhase_init(logOp, vessels, equipments):

    """
    Initialize the logistic phases through LogPhase classes
    """
    logPhase_install = {'E_export' : LogPhase(100, "Installation of static subsea export power cables", {}, {}),
                        'E_array'  : LogPhase(101, "Installation of static subsea inter-array power cables", {}, {}),
                        'E_cp'     : LogPhase(102, "Installation of offshore electrical collection point", {}, {}),

                        'F_driven'  : LogPhase(110, "Installation of driven piles foundations", {}, {}),
                        'F_suction' : LogPhase(111, "Installation of suction caissons for foundation systems", {}, {}),
                        'F_gravity' : LogPhase(112, "Installation of gravity based foundations", {}, {}),

                        'M_drag'   : LogPhase(113, "Installation of mooring systems with drag-embedment anchors", {}, {}),
                        'M_direct' : LogPhase(114, "Installation of mooring systems with direct-embedment anchors", {}, {}),

                        'D_fixed'    : LogPhase(120, "Installation of bottom fixed devices", {}, {}),
                        'D_floating' : LogPhase(121, "Installation of floating devices", {}, {})
                        }

    logPhase_OM = {'insp' : LogPhase(900, "O&M offshore intervention", {}, {})}

    """
    Define the diferent operations sequence for each logistic phase
    """

    logPhase_install['F_driven'].set_sequence('01', op_sequence(1,'Drilling',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F1"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_driven'].set_sequence('02', op_sequence(2,'Hammering',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F2"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_driven'].set_sequence('03', op_sequence(3,'Vibro-Pilling',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F3"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_suction'].set_sequence('01', op_sequence(1,'Suction',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F5"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['F_gravity'].set_sequence('01', op_sequence(1,'gravity',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_F4"],
                                                   logOp["op_F7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_drag'].set_sequence('01', op_sequence(1,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M6"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_direct'].set_sequence('01', op_sequence(1,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M7"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_direct'].set_sequence('02', op_sequence(2,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M8"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['M_direct'].set_sequence('03', op_sequence(3,'drag',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_M9"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['D_fixed'].set_sequence('01', op_sequence(1,'fixed',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_D1"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    logPhase_install['D_floating'].set_sequence('01', op_sequence(1,'floating',
                                                  [logOp["op1"],
                                                   logOp["op2"],
                                                   logOp["op3"],
                                                   logOp["op4"],
                                                   logOp["op5"],
                                                   logOp["op_D2"],
                                                   logOp["op6"],
                                                   logOp["op7"],
                                                   logOp["op8"]]
                                                   ))
    """
    Define the diferent vessel and equipment combination for each logistic phase
    """

    logPhase_install['F_driven'].set_combination(1, {'vessel': 
        {(1, vessels['Crane Barge']), (2, vessels['Tugboat'])},
                                                       'equipment': 
                                                           (1, equipments['Hammer'])})
    logPhase_install['F_driven'].set_combination(2, {'vessel': (1, vessels['Crane Vessel']),
                                                       'equipment': (1, equipments['Hammer'])})
    logPhase_install['F_driven'].set_combination(3, {'vessel': {(1, vessels['JUP Barge']), (2, vessels['Tugboat'])},
                                                       'equipment': (1, equipments['Hammer'])})
    logPhase_install['F_driven'].set_combination(4, {'vessel': (1, vessels['JUP Vessel']),
                                                       'equipment': (1, equipments['Hammer'])})
    logPhase_install['F_driven'].set_combination(5, {'vessel': {(1, vessels['Crane Barge']), (2, vessels['Tugboat'])},
                                                       'equipment': (1, equipments['Drill Rig'])})
    logPhase_install['F_driven'].set_combination(6, {'vessel': (1, vessels['Crane Vessel']),
                                                       'equipment': (1, equipments['Drill Rig'])})
    logPhase_install['F_driven'].set_combination(7, {'vessel': {(1, vessels['JUP Barge']), (2, vessels['Tugboat'])},
                                                       'equipment': (1, equipments['Drill Rig'])})
    logPhase_install['F_driven'].set_combination(8, {'vessel': (1, vessels['JUP Vessel']),
                                                       'equipment': (1, equipments['Drill Rig'])})

#    lg5.ve_combination[01] = {1: {(1, vt2.id), (2, vt1.id)}}
#    lg5.ve_combination[02] = {1: (1, vt3.id)}
#    lg5.ve_combination[03] = {1: {(1, vt4.id), (2, vt1.id)}}
#    lg5.ve_combination[04] = {1: (1, vt5.id)}
#    lg5.ve_combination[05] = {1: {(1, vt2.id), (2, vt1.id)}}
#    lg5.ve_combination[06] = {1: (1, vt3.id)}
#    lg5.ve_combination[07] = {1: {(1, vt4.id), (2, vt1.id))}
#    lg5.ve_combination[08] = {1: (1, vt5.id)}
#
#    lg6.ve_combination[01] = {1: {(1, vt2.id), (2, vt1.id)}}
#    lg6.ve_combination[02] = {1: (1, vt3.id)}
#    lg6.ve_combination[03] = {1: {(1, vt4.id), (2, vt1.id)}}
#    lg6.ve_combination[04] = {1: (1, vt5.id)}
#    lg6.ve_combination[05] = {1: {(1, vt2.id), (2, vt1.id)}}
#    lg6.ve_combination[06] = {1: (1, vt3.id)}
#    lg6.ve_combination[07] = {1: {(1, vt4.id), (2, vt1.id))}
#    lg6.ve_combination[08] = {1: (1, vt5.id)}

    return logPhase_install, logPhase_OM