
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
