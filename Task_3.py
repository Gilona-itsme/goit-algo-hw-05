import timeit

# -----------------------------
# 1) KMP
# -----------------------------
def compute_lps(pattern):
    lps = [0] * len(pattern)
    i = 1
    length = 0

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


# -----------------------------
# 2) BM
# -----------------------------
def build_shift_table(pattern):
    table = {}
    length = len(pattern)

    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1

    table.setdefault(pattern[-1], length)
    return table

def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i

        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1


# -----------------------------
# 3) RK
# -----------------------------
def polynomial_hash(s, base=256, modulus=101):
    h = 0
    for char in s:
        h = (h * base + ord(char)) % modulus
    return h

def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return -1

    base = 256
    modulus = 101

    pattern_hash = polynomial_hash(pattern, base, modulus)
    current_hash = polynomial_hash(text[:m], base, modulus)

    base_power = pow(base, m - 1, modulus)

    for i in range(n - m + 1):
        if current_hash == pattern_hash:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            current_hash = (
                (current_hash - ord(text[i]) * base_power) * base + ord(text[i + m])
            ) % modulus

    return -1


# -----------------------------
# Read files
# -----------------------------
with open("article1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("article2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

real_substring = "the"            
fake_substring = "abcdefghijk"    


# -----------------------------
# Timing
# -----------------------------
def measure(algorithm, text, pattern):
    return timeit.timeit(
        lambda: algorithm(text, pattern),
        number=100
    )

algorithms = {
    "KMP": kmp_search,
    "Boyer–Moore": boyer_moore_search,
    "Rabin–Karp": rabin_karp
}

for name, func in algorithms.items():
    print(f"\n=== {name} ===")
    print("Article 1 (real):", measure(func, text1, real_substring))
    print("Article 1 (fake):", measure(func, text1, fake_substring))
    print("Article 2 (real):", measure(func, text2, real_substring))
    print("Article 2 (fake):", measure(func, text2, fake_substring))



"""У більшості випадків найшвидшим є Боєр–Мур, бо він пропускає великі фрагменти тексту.
КМП дає стабільний результат і не робить зайвих перевірок. Рабін–Карп може бути швидким, але залежить від хешування."""