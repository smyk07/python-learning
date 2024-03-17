temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30: 
    print("The temmperature is good today, go outside.")
elif temp <0 or temp > 30: 
    print("The temperature is bad today, stay inside.")