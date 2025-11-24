import math
print("Enter your desired operation: sine, cosine, or tangent")
# Get user input on operation choice
operation = input().strip().lower()
if operation == "cosine":
    print("Enter the ratio between the adjacent and hypotenuse")
    # Get user input for cosine calculation
    cosnum = float(input())
    cosans = math.cos(math.radians(cosnum))
    print(cosans)
if operation == "sine":
    print("Enter the ratio between the opposite and hypotenuse")
    # Get user input for sine calculation
    sinnum = float(input())
    sinans = math.sin(math.radians(sinnum))
    print(sinans)
if operation == "tangent":
    print("Enter the ratio between the opposite and adjacent")
    tannum = float(input())
    tanans = math.tan(math.radians(tannum))
    print(tanans)
 # Functon for cosine calculation
def esin(cosnum):
    cosnum = float(input())
    cosans = math.cos(math.radians(cosnum))
    print(cosans)