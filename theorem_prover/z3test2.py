from z3 import *
s = Solver()
p = Bool('p')
q = Bool('q')
r = Bool('r')
s.add(Not(Implies(p, q)))
print(s.check())

if s.check() == sat:
    print("Not Valid")
else:
    print("Valid")

#, r == Not(q), Or(Not(p), r))
