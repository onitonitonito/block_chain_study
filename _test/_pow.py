"""
* 해쉬값의 마지막 자리가 '0'일 때까지 proof값을 1씩 증가 시키며 찾는다.
* 우연히 첫자리가 '0000'으로 시작하는 해쉬를 발견 했을 때,
* 작업 증명을 완성 한다. 작업증명(Proof of Work) 값은 proof=9675 이다.
"""

from hashlib import sha256

last_proof = 100
proof = 0

while sha256(str(last_proof * proof).encode()).hexdigest()[:4] != '0000':
    proof += 1

# proof = 21
print("The solution is ... proof = {0}".format(proof))
