def count_alpha_digits(s):
    d = {"alpha": 0, "num": 0}
    for i in range(len(s)):
        if s[i].isalpha():
            d["alpha"] += 1
        elif s[i].isnumeric():
            d["num"] += 1
    print(d)

count_alpha_digits("ab34cd")