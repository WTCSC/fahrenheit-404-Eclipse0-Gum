def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 0.5555

print("Welcome! This is the Temperature Convertion ")

print("What would you like to do?")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = input("Enter 1 for F or 2 for C: ")
if choice == '1':
    celsius = float(input("Enter the temperature number in Celsius: "))
    fahrenhiet = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.1f} C is equal to {fahrenhiet:.1f} F")
    
elif choice == '2':
    fahrenhiet = float(input("Enter the tempertaure number in Fahrenhiet: "))
    celsius = fahrenheit_to_celsius(fahrenhiet)
    print(f"{fahrenhiet:.1f} F is equal to {celsius:.1f} C")
    
else:
    print("Okay we restarting, I ain't here to waste time, choose 1 or 2 next time")
    
print("Thanks for using the converter user!")