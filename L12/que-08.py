class String:
    def __init__(self, content=""):
        self.content = content

    def __iadd__(self, other):
        self.content += other
        return self

    def toLower(self):
        self.content = self.content.lower()

    def toUpper(self):
        self.content = self.content.upper()

    def __str__(self):
        return self.content

# Test code
s = String("Hello")
print("Original:", s)
s += " World"
print("After += :", s)
s.toLower()
print("toLower():", s)
s.toUpper()
print("toUpper():", s)
