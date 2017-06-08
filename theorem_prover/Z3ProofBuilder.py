import logging
from z3 import *
import argparse
import sys
from Z3StepBuilder import Z3StepBuilder
from Z3TypeBuilder import Z3TypeBuilder
from antlr4 import *



class Z3ProofBuilder():

    def __init__(self, step_builder, step, given_just, step_just):

        self.step_builder = step_builder

        self.step = step
        self.given_just = given_just
        self.step_just = step_just

    def __paran(self, str):
       return "(" + str + ")"

    def __joinAnd(self, array):
        return " & ".join(map((lambda l: self.__paran(l)), array))

    def __joinImplies(self, array):
        return  " -> ".join(map((lambda l: self.__paran(l)), array))

    def __build(self):
        lhs = ""
        if len(self.given_just) != 0:
            lhs += self.__joinAnd(self.given_just)
        if len(self.step_just) != 0:
            if len(lhs) !=0:
                lhs += " & "
            lhs += self.__joinAnd(self.step_just)

        if(len(lhs) > 0):
            formula = self.__joinImplies([lhs, self.step])
        else :
            formula = self.step

        valid, z3 = self.step_builder.visitInput(formula)
        print(str(z3))
        return z3

    def isValid(self):
        s = Solver()
        s.add(Not(self.__build()))
        return s.check() == unsat

    def isSat(self):
        s = Solver()
        s.add(self.__build())
        return s.check() == sat

def get_args():
    parser = argparse.ArgumentParser(
        description='Script builds z3 command from given proof steps and optional type declarations'
    )

    parser.add_argument(
        '-d', '--declaration', type=str, help='Declaration file path', required=False
    )

    parser.add_argument(
        '-s', '--step', type=str, help='Step file path', required=False
    )

    return parser.parse_args()


def main(argv):

    args = get_args()

    type_builder = Z3TypeBuilder()

    if args.declaration:
        type_input = FileStream(args.declaration)
        type_builder.visitInputFile(type_input)

    step_input = FileStream(args.step)
    step_builder = Z3StepBuilder(type_builder.param_map, type_builder.predicate_map)

    proof_builder = Z3ProofBuilder()
    step = step_builder.visitInputFile(step_input)

if __name__ == '__main__':
    main(sys.argv)
'''
    Ask for the design choice
    Does Z3Proof use Z3StepBuilder? Or vice versa
'''
