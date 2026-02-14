print("Hello, World!") 
# Program to calculate Moment (Torque)

# Input force and distance
force = float(input("Enter the force (in Newtons): "))
distance = float(input("Enter the distance from pivot (in meters): "))

# Calculate moment
moment = force * distance

# Display result
print("The moment (torque) is:", moment, "Newton-meters (Nm)")
