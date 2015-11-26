

import itertools


arrays_test = [(-1,+1), (-2,+2, -20), (-3,+3), (-4, +4)];
sol_test = list(itertools.product(*arrays_test))



ves_A = (-1, +1)
ves_B = (-2,+2,-20)
arrays_ves = (ves_A, ves_B);
comb_ves = list(itertools.product(*arrays_ves))


eq_1 = (-3,+3)
eq_2 = (-4,+4)
arrays_eq = (eq_1, eq_2);
comb_eq = list(itertools.product(*arrays_eq))


arrays_sol = (comb_ves, comb_eq);
combA = list(itertools.product(*arrays_sol))






combA








