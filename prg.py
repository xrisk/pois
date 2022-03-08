prime = 63337
generator = 5


def f(x):
    return pow(generator, x, prime)


def g(x, r):
    return (f(x), r)


def gl(x, r):
    ret = 0
    for i in range(32):
        ret ^= (x & (1 << i) != 0) * (r & (1 << i) != 0)
    return ret


def G(s):
    print("input bit string", bin(s)[2:])
    binary = bin(s)[2:]
    fs = int(binary[: len(binary) // 2])
    snd = int(binary[len(binary) // 2 + 1 :])
    output = g(fs, snd)
    hc = gl(fs, snd)
    return bin(output[0])[2:] + bin(snd)[2:] + str(hc)


if __name__ == "__main__":
    print(G(123212121))
