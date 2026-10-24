def custom_hash_modulo(password: str) -> int:
    MOD = 1000003
    base = 257
    h = 0
    for c in password:
        h = (h * base + ord(c)) % MOD

    for i in range(100):
        h = ((h << 5) ^ (h >> 3) ^ 12345) % MOD
    return h