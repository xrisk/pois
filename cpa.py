import random
import prf


def gen(n):
    k = [random.choice("01") for _ in range(n)]
    return "".join(k)


def enc(k, m):
    assert len(k) == len(m)
    n = len(k)
    r = "".join([random.choice("01") for _ in range(n)])
    ciphertext = (r, bin(int(prf.prf(r, k), 2) ^ int(m, 2))[2:])
    return ciphertext


def dec(ciphertext, k):
    r, s = ciphertext
    message = bin(int(prf.prf(r, k), 2) ^ int(s, 2))[2:]
    return message


if __name__ == "__main__":
    message = "1010101011111"
    n = len(message)
    key = gen(n)
    print("generated key:", key)
    ciphertext = enc(key, message)
    print("original message:", message)
    print("ciphertext: ", ciphertext)
    print("decrypted message:", dec(ciphertext, key))
