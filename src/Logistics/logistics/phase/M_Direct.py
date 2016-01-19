from .classes import DefPhase, LogPhase


def initialize_m_direct_phase(log_op, vessels, equipments, MF_outputs):
    phase = LogPhase(114, "Installation of mooring systems with direct-embedment anchors")

    if (MF_outputs['foundation']['subtype [-]'] == 'suction driven').any(): # ?????????????????????????????????????????????????

        phase.op_ve[0] = DefPhase(1, 'Deploy direct-embedment anchor by suction-embedment')
        phase.op_ve[0].op_seq_sea = [log_op["Mob"],
                                      log_op["AssPort"],
                                      log_op["VessPrep"],
                                      log_op["TranPortSite"],
                                      log_op["SeafloorEquipPrep"],
                                      log_op["DirecSuct"],
                                      log_op["Tensng"],
                                      log_op["PreLay"],
                                      log_op["TranSiteSite"],
                                      log_op["TranSitePort"],
                                      log_op["Demob"]]

        phase.op_ve[0].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                            'equipment': [(1, equipments['rov'], 0)]}

        phase.op_ve[0].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                            'equipment': [(1, equipments['rov'], 0)]}

        phase.op_ve[0].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                            'equipment': [(1, equipments['rov'], 0)]}



    if (MF_outputs['foundation']['subtype [-]'] == 'jetting driven').any(): # ?????????????????????????????????????????????????

        phase.op_ve[1] = DefPhase(2, 'Deploy direct-embedment anchor by jetting-embedment')
        phase.op_ve[1].op_seq_sea = [log_op["Mob"],
                                      log_op["AssPort"],
                                      log_op["VessPrep"],
                                      log_op["TranPortSite"],
                                      log_op["SeafloorEquipPrep"],
                                      log_op["DirecJet"],
                                      log_op["Tensng"],
                                      log_op["PreLay"],
                                      log_op["TranSiteSite"],
                                      log_op["TranSitePort"],
                                      log_op["Demob"]]

        phase.op_ve[1].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                            'equipment': [(1, equipments['rov'], 0)]}

        phase.op_ve[1].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                            'equipment': [(1, equipments['rov'], 0)]}

        phase.op_ve[1].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                            'equipment': [(1, equipments['rov'], 0)]}



    if (MF_outputs['foundation']['subtype [-]'] == 'hammer driven').any(): # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        phase.op_ve[2] = DefPhase(3, 'Deploy direct-embedment anchor by mechanical-embedment')
        phase.op_ve[2].op_seq_sea = [log_op["Mob"],
                                      log_op["AssPort"],
                                      log_op["VessPrep"],
                                      log_op["TranPortSite"],
                                      log_op["SeafloorEquipPrep"],
                                      log_op["DirecMech"],
                                      log_op["Tensng"],
                                      log_op["PreLay"],
                                      log_op["TranSiteSite"],
                                      log_op["TranSitePort"],
                                      log_op["Demob"]]

        phase.op_ve[2].ve_combination[0] = {'vessel': [(1, vessels['AHTS'])],
                                            'equipment': [(1, equipments['rov'], 0)]}

        phase.op_ve[2].ve_combination[1] = {'vessel': [(1, vessels['Multicat'])],
                                            'equipment': [(1, equipments['rov'], 0)]}

        phase.op_ve[2].ve_combination[2] = {'vessel': [(1, vessels['Tugboat'])],
                                            'equipment': [(1, equipments['rov'], 0)]}



    return phase
