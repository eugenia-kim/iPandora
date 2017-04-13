from z3 import *

class Z3Proof():

    def __init__(self):

        # given condition
        self.given = None

        # to Show condition
        self.toShow = None

        # step_map = [line number. z3 formula]
        self.step_map = dict()

'''
    Ask for the design choice
    Does Z3Proof use Z3StepBuilder? Or vice versa
'''