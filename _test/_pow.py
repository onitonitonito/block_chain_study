"""
* 해쉬값의 마지막 자리가 '0'일 때까지 y값을 1씩 증가 시키며 찾는다.
* 우연히 마지막 자리가 0 일때 작업 증명을 완성 한다.
* 작업증명(Proof of Work) 값은 y=21 이다.
"""

from hashlib import sha256

x = 5
y = 0

while sha256(str(x * y).encode()).hexdigest()[-1] != '0':
    y += 1

print("The solution is y = {0}".format(y))      # y = 21
