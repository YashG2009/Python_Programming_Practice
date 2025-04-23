class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

# Test code
weather = Weather(['temperature', 'humidity', 'pressure', 'wind'])

print("temperature" in weather)  # True
print("rainfall" in weather)     # False
print("wind" in weather)         # True
print("clouds" in weather)       # False
