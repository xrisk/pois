import mac
import random
import cpa


def gen_uniform(n):
    return "".join(random.choice("01") for _ in range(n))


def gen(n):
    k_e = gen_uniform(n)
    k_m = gen_uniform(n)
    return (k_e, k_m)


def enc(key, m):
    k_e, k_m = key
    c = cpa.enc(k_e, m)
    t = mac.mac(c, k_m)
    return c, t


def dec(key, ciphertext):
    k_e, k_m = key
    c, t = ciphertext
    if mac.verify(c, k_m, t):
        print("mac verification succeeded")
        return cpa.dec(c, k_e)
    else:
        print("decryption failed because of bad mac")


if __name__ == "__main__":
    message = "11011" * 3
    key = gen(len(message))

    ct = enc(key, message)

    print("key:", key)
    print("ciphertext:", ct)
    print("decrypted:", dec(key, ct))
