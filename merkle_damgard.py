import hash_function

from random import randint

n = 63337


def merkle_damgard_hash(h, x):
    x += "1"
    iv = bin(randint(0, 2**15))[2:]
    z_0 = iv
    while len(x) % 15 != 0:
        x += "0"
    for i in range(len(x) // 15):
        block = x[i * 15 : (i + 1) : 15]
        z_0 = bin(hash_function.fixed_hash(h, int(z_0, 2), int(block, 2)))[2:]
    return z_0


if __name__ == "__main__":
    h = hash_function.gen()
    x = "1010101111111"
    print("hashed value", merkle_damgard_hash(h, x))
