"""
# Set CWD and other general configuration
"""
# print(__doc__)

import os
import sys


HOME = "block_chain_study"
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "\\"




if __name__ == '__main__':
    print(__doc__)
    print("HOME=", HOME)
    print("DIRS=", DIRS)
    print("ROOT=", ROOT)
