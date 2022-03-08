import prf
import random


def mac(message, key):
    return prf.prf(message, key)


def verify(message, key, tag):
    return tag == prf.prf(message, key)


if __name__ == "__main__":
    message = "010101010101"
    key = "".join(random.choice("01") for _ in range(len(message)))
    print("generaeted key", key)
    tag = mac(message, key)
    print("generated tag", tag)
    print("verification status", verify(message, key, tag))
