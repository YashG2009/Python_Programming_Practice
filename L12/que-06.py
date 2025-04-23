class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return (self.day == other.day and
                self.month == other.month and
                self.year == other.year)

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

# Test code
date1 = Date(15, 8, 2023)
date2 = Date(15, 8, 2023)
date3 = Date(16, 8, 2023)

print("Date1:", date1)
print("Date2:", date2)
print("Date3:", date3)
print("Date1 == Date2:", date1 == date2)
print("Date1 == Date3:", date1 == date3)
