class LogPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.op_ve = {}
        # self.op_ve.sol_ves = {}
        # self.op_ve.sol_eq = {}
#        self.feasibility = feasiblity
#        self.matching = matching
#        self.v&e&p_selected = {}
#        self.schedule = {}
#        self.time = {}
#        self.cost = {}
#        self.environmental = environment
#        self.risk = risk


class DefPhase(object):

    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.op_sequence = {}
        self.ve_combination = {}
        self.sol = {}


class VE_solutions(object):

    def __init__(self, id):
        self.id = id
        self.sol_combi = {}
        self.sol_ves = {}
        self.sol_eq = {}
        self.schedule = {}
        self.cost = {}
