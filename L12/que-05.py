class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def add(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def subtract(self, other):
        total_seconds1 = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds2 = other.hours * 3600 + other.minutes * 60 + other.seconds
        diff = total_seconds1 - total_seconds2
        if diff < 0:
            diff = 0
        h = diff // 3600
        diff %= 3600
        m = diff // 60
        s = diff % 60
        return Time(h, m, s)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Test code
t1 = Time(2, 45, 30)
t2 = Time(1, 20, 50)

print("Time 1:", t1)
print("Time 2:", t2)
print("Addition:", t1.add(t2))
print("Subtraction:", t1.subtract(t2))
