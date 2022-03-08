generator = 5
prime = 63337


def stretch(seed: int, n: int) -> str:
    ret = []
    for i in range(n):
        seed = pow(generator, seed, prime)
        ret.append(1 if seed <= (prime - 1) // 2 else 0)
    return "".join(map(str, ret))


if __name__ == "__main__":
    seed = 1234
    print(bin(seed)[2:])
    print("".join(map(str, stretch(seed, 20))))
