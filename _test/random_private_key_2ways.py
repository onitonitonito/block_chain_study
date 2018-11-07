"""
# How to make Perfect Random Private key
# Private Key 소개 및 실습 -이동식, 이승현
# -------------------------
# https://www.facebook.com/etherstudy/videos/1155744144580081/
# Random Number Generation Site
#   - http://www.random.org = 숫자시드로 생성
#   - http://www.bitaddress.org = 마우스 이동으로 랜덤시드생성
#      * https://github.com/pointbiz/bitaddress.org 오픈소스 제공
#      * Bulk option, Paper wallet 등
#"""
print(__doc__)

import sys
import random
import secrets

def random_bits():
    """\n\n\n
    # random.getrandbits(256) ... import random
    # 자신이 고른언어로 난수를 발생시킴 = 현재시간 기반 시드발생
    # --> 이렇게 만든 난수는 암호화되지 않아 안전하지 않음
    """
    # this_func_name = sys._getframe().f_code.co_name
    print(random_bits.__doc__)

    bits = random.getrandbits(256)
    bits_hex = hex(bits)

    return str(bits), str(bits_hex)


def secret_random_bits():
    """\n\n\n
    # py3.6부터 지원, secrets.randbits(256) ... import secrets
    # Secrets 모듈은 암호, 인증, 보안과 같 데이터를 관리하기 적합
    # --> 암호화 작업을 위해 특별고안, 암호학 적으로 강력한 난수생성.
    """
    # this_func_name = sys._getframe().f_code.co_name
    print(secret_random_bits.__doc__)

    bits = secrets.randbits(256)
    bits_hex = hex(bits)

    return str(bits), str(bits_hex)


def show_bits_hex(str_bits, str_bits_hex):
    print("{} = {}".format(len(str_bits), str_bits[:50] + "...."))
    print("{} = {}".format(len(str_bits_hex), str_bits_hex[:50] + "...."))




if __name__ == '__main__':
    _as = random_bits()
    show_bits_hex(*_as)         # 튜플 _as를 풀어서 넣는다.

    _bs = secret_random_bits()
    show_bits_hex(*_bs)
