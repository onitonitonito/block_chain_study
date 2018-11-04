"""
# Test 5 Hashes from `Crypto` library
# another way, using `hashlib` library
# !pip install Crypto
#
#    - MD5    = 128 bit, Rivest (1991)
#    - SHA-1  = 160 bit, NIST standards in 1995
#    - RIPEMD = 160 bit, Hans Dobbertin et.al
#    - SHA256 = 256 bit, NIST standards in 2002
#    - MD5, SHA-1 = deprecated due to low collision resistancy
#    - more than SHA-256, 384, 512 have became Nat'l standards
#    - RIPEMD = scholatic use, developed on open-source project.
#\n\n"""
print(__doc__)

from Crypto.Hash import MD5, RIPEMD, SHA, SHA256


def show_various_hash(message):
    message = message.encode()
    print("\n\nMessage = {} \n".format(message.decode()))

    #MD5
    h = MD5.new()
    h.update(message)
    hv_md5 = h.hexdigest()

    #RIPEMD
    h = RIPEMD.new()
    h.update(message)
    hv_ripemd = h.hexdigest()

    #SHA
    h = SHA.new()
    h.update(message)
    hv_sha = h.hexdigest()

    #SHA256
    h1 = SHA256.new()
    h1.update(message)
    hv_sha256 = h1.hexdigest()

    #double SHA256
    h2 = SHA256.new()
    h2.update(hv_sha256.encode())
    hv_double = h2.hexdigest()


    #Base64


    #Base58_check



    print("{2:>7} ({1:2}) :{0:}".format(hv_md5, len(hv_md5), 'MD5'))
    print("{2:>7} ({1:2}) :{0:}".format(hv_ripemd,  len(hv_ripemd), 'RIPEMD'))
    print("{2:>7} ({1:2}) :{0:}".format(hv_sha, len(hv_sha), 'SHA-1'))
    print("{2:>7} ({1:2}) :{0:}".format(hv_sha256, len(hv_sha256), 'SHA-256'))
    print("{2:>7} ({1:2}) :{0:}".format(hv_double, len(hv_double), 'DOUBLE'))




show_various_hash('Hello World! this is Alice speaking')
show_various_hash('Hello World! this is Alice speaking.')
show_various_hash('ec7abe0b76b023b9c10adcf302c2b1232677951e035efe8e4a64b0d5fa05755b')
