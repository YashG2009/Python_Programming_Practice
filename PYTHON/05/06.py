# Convert list of temperatures in fahrenheit degrees to equivalent celsius degrees.

fahrenheit = [31, 41, 59, 77, 93]
celsius = []

for i in fahrenheit:
    c = round(((i-32)*5)/9)
    celsius.append(c)

print(f"In fahrenheit: {fahrenheit}",f"In celsius: {celsius}",sep="\n")