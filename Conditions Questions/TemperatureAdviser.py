temperature = int(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's hot. Let's go swimming!")
elif 20 <= temperature <= 30:
    print("Perfect for a picnic.")
elif 10 <= temperature < 20:
    print("Maybe wear a jacket?")
else:
    print("Too cold! Best to stay indoors.")
