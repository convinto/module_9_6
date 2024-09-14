def all_variants(text):
    n = len(text)
    for len_ in range(1, n + 1):
        for i in range(n - len_ + 1):
            yield text[i:i + len_]

a = all_variants("abc")
for i in a:
    print(i)