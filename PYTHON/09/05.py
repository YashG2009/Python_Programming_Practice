def ispangram(s):
    alpha = set([chr(x) for x in range(97,123)])
    s = s.replace(" ",'')
    s = set(s.lower())
    return True if alpha == s else False

print(ispangram("The quick brown fox jumps over the lazy dog"))