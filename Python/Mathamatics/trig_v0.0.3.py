import math
print("Enter your desired operation: sine, cosine, tangent, arcsine, arccosine, or arctangent")
# Get user input on operation choice
operation = input().strip().lower()
if operation == "cosine":
    print("Enter the angle")
    # Get user input for cosine calculation
    cosnum = float(input())
    cosans = math.cos(math.radians(cosnum))
    print("The ratio between the adjacent and hypotenuse is", cosans)
if operation == "sine":
    print("Enter the angle")
    # Get user input for sine calculation
    sinnum = float(input())
    sinans = math.sin(math.radians(sinnum))
    print("The ratio between the opposite and hypotenuse is", sinans)
if operation == "tangent":
    print("Enter the angle")
    # Get user input for tangent calculation
    tannum = float(input())
    tanans = math.tan(math.radians(tannum))
    print("The ratio between the opposite and adjacent is", tanans)
if operation == "arcsine":
    print("""Enter the legnth of the opposite, or type "Ratio" and that ratio""")
    arcsine_opposite = float(input())
    print("Enter the legnth of the hypotenuse")
    arcsine_hypotenuse = float(input())
    print("Your angle is", math.degrees(math.asin(arcsine_opposite / arcsine_hypotenuse)))
if operation == "arccossine":
    print("""Enter the legnth of the adjacent, or type "Ratio" and that ratio""")
    arccossine_adjacent = float(input())
    print("Enter the legnth of the hypotenuse")
    arccossine_hypotenuse = float(input())
    print("Your angle is", math.degrees(math.acos(arccossine_adjacent / arccossine_hypotenuse)))
if operation == "arctangent":
    print("""Enter the legnth of the opposite, or type "Ratio" and that ratio""")
    arctangent_opposite = float(input())
    print("Enter the legnth of the adjacent")
    arctangent_adjacent = float(input())
    print("Your angle is", math.degrees(math.atan(arctangent_opposite / arctangent_adjacent)))
 # Functon for cosine calculation
 # Not needed in production, shell avalible in debug console (VS Code)
def esin(cosnum):
    cosnum = float(input())
    cosans = math.cos(math.radians(cosnum))
    print(cosans)