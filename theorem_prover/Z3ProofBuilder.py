from z3 import *
import argparse
import sys
from Z3StepBuilder import Z3StepBuilder
from Z3TypeBuilder import Z3TypeBuilder
from antlr4 import *

class Z3ProofBuilder():

    def __init__(self, type_builder, step_builder):

        # given condition in z3 formulas
        self.givens= []

        # toShow condition in z3 formula
        self.toShow = None

        self.type_builder = type_builder

        self.step_builder = step_builder

    def setTypes(self, declaration):
        self.type_builder.visitInputFile(FileStream(declaration))

    def setGiven(self, given):
        z3_given = self.step_builder.visitInputFile(FileStream(given))
        self.givens.append(z3_given)

    def setToShow(self, toShow):
        self.toShow = self.step_builder.visitInputFile(toShow)

    def build(self):
        return Z3Proof(self.givens, self.toShow, self.step_builder)

class Z3Proof():

    def __init__(self, given, toShow, step_builder):

        # given condition in z3 formula
        self.given = given

        # toShow condition in z3 formula
        self.toShow = toShow

        self.step_builder = step_builder

        # step_map = [line number. z3 formula]
        self.step_map = dict()

    def __isValid(self, f):
        s = Solver()
        s.add(Not(f))
        return s.check() == unsat

    def __isSat(self, f):
        s = Solver()
        s.add(f)
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
    step_builder.visitInputFile(step_input)

if __name__ == '__main__':
    main(sys.argv)
'''
    Ask for the design choice
    Does Z3Proof use Z3StepBuilder? Or vice versa
'''
