# Description: This script calculates the distance on the ruler that corresponds
#  to a given angle for the phys 1241 microwave optics experiment
import math

# define constants
ORIGIN = 68.5
RECIEVER_DIST = 100

def calculate_distances(angle, distance_marking_at_180):
    # compute angels
    if angle <= 180:
        theta = 180 - angle
    else:
        theta = angle - 180
    
    # compute change in distance
    D = distance_marking_at_180 - ORIGIN
    final_marking = D / math.cos(math.radians(theta))
    
    # return final distance on the marking that corresponds to given angle
    return final_marking + ORIGIN

# print out the distances for angles from 100 to 240
for i in range(100, 240, 10):
    print("angle is: " + str(i))
    print("distance is: " + str(calculate_distances(i, RECIEVER_DIST)))
    print("--------------------")
