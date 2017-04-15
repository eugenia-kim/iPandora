from z3 import *
import argparse
import sys
from Z3StepBuilder import Z3StepBuilder
from Z3TypeBuilder import Z3TypeBuilder
from antlr4 import *

class Z3Proof():

    def __init__(self):

        # given condition in z3 formula
        self.given = None

        # to Show condition in z3 formula
        self.toShow = None

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
        '-s', '--step', type=str, help='Step file path', required=True
    )

    return parser.parse_args()


def main(argv):
    args = get_args()

    type_builder = Z3TypeBuilder()

    if args.declaration:
        type_input = FileStream(args.declaration)
        type_builder.visitInputFile(type_input)

    step_input = FileStream(args.step)
    step_builder = Z3StepBuilder(type_builder)
    step_builder.visitInputFile(step_input)

if __name__ == '__main__':
    main(sys.argv)
'''
    Ask for the design choice
    Does Z3Proof use Z3StepBuilder? Or vice versa
'''