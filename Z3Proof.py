from z3 import *

class Z3Proof():

    def __init__(self):

        # given condition
        self.given = None

        # to Show condition
        self.toShow = None

        # step_map = [line number. z3 formula]
        self.step_map = dict()

    def setGiven(self, given):
        self.given = given

    def setToShow(self, toShow):
        self.toShow = toShow

    def __isValid(self, f):
        s = Solver()
        s.add(Not(f))
        return s.check() == unsat

    def __isSat(self, f):
        s = Solver()
        s.add(f)
        return s.check() == sat

'''
    Ask for the design choice
    Does Z3Proof use Z3StepBuilder? Or vice versa
'''