from z3 import *

class Propositional():
    premiseList = []
    stepList = []
    goal = ''

    def __init__(self, premiseList, goal):
        self.premiseList = premiseList
        self.goal = goal

    def newStep(self, assPList, assSList, intermediate):
        # assPList and assSList contains the index of premiseList and stepList respectively
        assPLength = len(assPList)
        assSLength = len(assSList)
        LHS = BoolVector('ass', assPLength + assSLength)
        for i in range(assPLength):
            LHS[i] = eval(premiseList[assPList[i]])
        for j in range(assSLength):
            LHS[i + assPLength] = eval(stepList[assSList[i]])

        f = Implies(And(LHS), eval(intermediate))

        if(self.__isValid(f)):
            self.stepList.append(intermediate)
            return True
        return False

    def __isValid(self, f):
        s = Solver()
        s.add(Not(f))
        return s.check() == unsat

p = Bool('p')
q = Bool('q')
r = Bool('r')

premiseList = ["And(p, q)"]
goal = "Not(p)"

Prop = Propositional(premiseList, goal)
print(Prop.newStep([0], [],"Or(p, r)"))
