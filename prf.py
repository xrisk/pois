import blum


def prf(value, key):
    ret = []
    for i in value:
        key = blum.stretch(int(key, 2), len(key) * 2)
        if i == "0":
            key = key[: len(key) // 2]
        else:
            key = key[len(key) // 2 :]
    return key


if __name__ == "__main__":
    print(prf("1010010111", "111010101"))
