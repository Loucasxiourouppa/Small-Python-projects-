fahrenheit = float(input("Temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature is", celsius, "Celsius")

if celsius <= 0:
    print("It's very cold")
elif celsius >= 35:
    print("It's hot!")
else:
    print("It's neither very cold nor hot.")
