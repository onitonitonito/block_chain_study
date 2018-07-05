import hashlib


def test_00():
    """HASH TEST & COMPARISON of DIFFERNT STINGS RESULTS"""
    hs1 = hashlib.sha256()
    hs2 = hashlib.sha256()

    # 해쉬는 바이너리로 진행해야 한다
    hs1.update(b"Nobody inspects")
    hs2.update(b"the spammish repetition")

    # 결과는 바이너리로 출력된다
    print(hs1.digest())
    print(hs2.digest(), "\n\n")

    """바이너리 스트링 길이 체크 (테스트)"""
    ss1 = str(hs1.digest()).split("\\")
    ss2 = str(hs2.digest()).split("\\")

    # 리스트 스트링의 갯수 체크
    print(ss1)
    print(ss2)

    print(len(ss1))
    print(len(ss2), "\n\n")

    # 바이너리를 핵사로 변경하여 출력 ... 당연히 길이는 동일함!
    print("hs1=", hs1.hexdigest())
    print("hs1.digest_siz=", hs1.digest_size)
    print("hs1.digest_siz=", hs2.digest_size, "\n\n")

    print("hs2=", hs2.hexdigest())
    print("hs1.block_size=", hs1.block_size)
    # hash comparison
    print("hs2.block_size=", hs2.block_size)


def test_01():
    import datetime
    date_fields = (2015, 6, 12)
    date = datetime.date(*date_fields)
    print(date)


def test_02():
    from functools import reduce

    def product(*numbers):
        return reduce(lambda x, y: x * y, numbers)

    print(product(1, 2, 3, 4))


def test_03():
    from math import sqrt

    class SmartPoint(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @property
        def hypotenuse(self):
            return sqrt(self.x ** 2 + self.y ** 2)

        @hypotenuse.setter
        def hypotenuse(self, z):
            # Sily setter example .. 값을 정(set)해주면 self.y를 변경
            self.y = sqrt(z ** 2 - self.x ** 2)

    point = SmartPoint(3, 4)

    # Callable 함수는 없다. 속성 값만 있다.
    # print(dir(point.hypotenuse))
    print(point.hypotenuse)

    point.hypotenuse = 6
    print(point.x, point.y)

# test_01()               # 2015-06-12
# test_02()               # 24
# test_03()               # 5.0 / 3 5.196152422706632


# HASH FUNCTION TEST
print(test_00.__doc__.join([" ********** "] * 2))
test_00()


def turn_hash(bin_string, hex=0):
    """ to turn binary strint to SHA256 Crypted string(bin) """
    hs = hashlib.sha256()
    hs.update(bin_string)

    if hex is not 0:
        return hs.hexdigest()
    else:
        return hs.digest()


def show_count_str(sort_of_string):
    print(sort_of_string)
    print("= %s bits\n" % len(sort_of_string))


def main(bin_str):
    _ = """
    t2 = %s

    sha256(t2).digest() = 32 bit
    sha256(t2).hexdigest() = 64 bit
    bin(int(sha256(t2).hexdigest(), 16)) = 256 bit
    """ % bin_str
    print(_, end="\n\n")

    # b"7\xea\x99\xe0'L-\x1fr\xc3]\xc2\x91W\x87\x17\xb4=1\xa7k\x17\xe2`\x97zlj\xc9\xfbWU"
    msl_string = turn_hash(bin_str, hex=0)
    show_count_str(msl_string)

    # 37ea99e0274c2d1f72c35dc291578717b43d31a76b17e260977a6c6ac9fb5755
    hex_string = turn_hash(bin_str, hex=1)
    show_count_str(hex_string)

    # 핵사스트링을 16스케일에 자릿수 256바이트 규격에 맞춰 이진수 스트링으로 반환한다
    scale = 16              # equals to hexadecimal
    num_of_bits = 256
    bin_string = bin(int(hex_string, scale))[2:].zfill(num_of_bits)
    show_count_str(bin_string)


if __name__ == '__main__':
    MSL_STRING = b'Hello SHA-256 World!'

    main(MSL_STRING)
