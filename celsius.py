# Write a python program that converts temp from C to F and F to C using funcitons
# c=(f-32)*(5/9)
# (0°C × 9/5) + 32 = 32°F


def tempConvert(temp, isF=True):
    if isF:
        celsius_sum = (temp - 32) * (5 / 9)
        return celsius_sum
    else:
        farenheit_sum = (temp * 9 / 5) + 32
        return farenheit_sum


resultCel = tempConvert(95)
print(resultCel)

resultFar = tempConvert(30, False)
print(resultFar)
