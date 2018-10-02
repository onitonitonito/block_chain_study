"""
# Set CWD and other general configuration
"""
# print(__doc__)

import os
import sys


# '루트'와 '작업'디렉토리 설정 - for 스크립트런
HOME = "block_chain_study"
WORK_DIR = "_static/"
DIRS = os.path.dirname(__file__).partition(HOME)
ROOT = DIRS[0] + DIRS[1] + "/"
WORK_DIR = ROOT + WORK_DIR

# 스크립트런 '한글' 표시를 위한 커스텀 모듈 실행
sys.path.append(ROOT)
import _stat





if __name__ == '__main__':
    print(__doc__)
    print("HOME=", HOME)
    print("DIRS=", DIRS)
    print("ROOT=", ROOT)
