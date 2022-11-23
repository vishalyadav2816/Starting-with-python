#The angles in degrees has been provided to you.
#Your task is to find the tangent of the given angle and print the value upto 2 decimal places.

import math
a=int(input())
radians=math.pi/180*a

print(f"{math.tan(radians):.2f}")