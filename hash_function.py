generator = 5
order = 63337

import random


def is_prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def gen():
    return random.randint(0, order)


def fixed_hash(h, x1, x2):
    assert x1 <= order and x2 <= order
    return (pow(generator, x1) * pow(h, x2)) % order


if __name__ == "__main__":
    h = gen()
    a, b = "11111", "101011"
    print("hashing", a + b)
    hashed = fixed_hash(h, int(a, 2), int(b, 2))
    print("hashed", bin(hashed)[2:])
