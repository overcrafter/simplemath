import math
print("Enter the angle in degrees to find its cosine, sine, and tangent values:")
print("Enter the ratio between the adjacent and hypotenuse")
# Get user input for cosine calculation
cosnum = float(input())
cosans = math.cos(math.radians(cosnum))
print(cosans)
print("Enter the ratio between the opposite and hypotenuse")
# Get user input for sine calculation
sinnum = float(input())
sinans = math.sin(math.radians(sinnum))
print(sinans)
# Get user input for tangent calculation
print("Enter the ratio between the opposite and adjacent")
tannum = float(input())
tanans = math.tan(math.radians(tannum))
print(tanans)