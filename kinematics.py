# Program to figure out which kinematic variables are known and
# to solve for the unknown variables using the right kinematic equation

equations = [
    "x = x0 + v0*t + 0.5*a*t^2", 
    "v = v0 + a*t",
    "x = x0 + v*t",
    "v^2 = v0^2 + 2*a*(x - x0)"
]

v0 = input("Initial Velocity: ")
v = input("Final Velocity: ") 
a = input("Acceleration: ")
t = input("Time: ")
x = input("Position: ")

known = [v0, v, a, t, x]
unknown = [var for var in known if var == ""]

if len(unknown) > 2: # Is it two or three
    print("Not enough information")
    exit()
else:
    print(unknown)
    exit()

# TODO: finish