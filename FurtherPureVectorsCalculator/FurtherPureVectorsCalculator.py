import numpy as np
import math
import re
import FPVCModule as fpvc




print("Note: Inputs for vectors/points should be given one at a time, decimals are accepted")
print("      Inputs for planes should be given in the form, 'ax+by+cz=d'")
print("      Inputs for lines should be given in the form 'r=(x0 y0 z0)+t(x1 y1 z1)'")
print("      If there are no inputs, enter '-' \n")


calculationType = input("What would you like to calculate today? (Intersection, Angle, Foot, Distance, Equation) \n").upper()


if calculationType == "EQUATION":
    lineOrPlane = input("\nLine or plane? \n").upper()
    if lineOrPlane == "PLANE":
        #Plane calculation
        numberOfPoints = int(input("\nNumber of points:"))
        numberOfVectors = int(input("Number of direction vectors:"))

        pointInputs = fpvc.get_vector_input(numberOfPoints, "position")
        vectorInputs = fpvc.get_vector_input(numberOfVectors, "direction")

        if numberOfPoints == 1 and numberOfVectors == 2 :
            normal = fpvc.plane_calc(pointInputs[0], vectorInputs[0], vectorInputs[1])
        
        elif numberOfPoints == 2 and numberOfVectors == 1: 
            vector1 = vectorInputs[0]
            vector2 = pointInputs[0] - pointInputs[1]
        
            print(f"Direction vector 1: {vector1} \n")
        
            print("Direction vector 2:")
            print(pointInputs[0], "-", pointInputs[1])
            print(f"► {vector2} \n")
        
            normal = fpvc.plane_calc(pointInputs[0], vector1, vector2)
        
        elif numberOfPoints == 3:
            vector1 = pointInputs[0] - pointInputs[1]
            vector2 = pointInputs[1] - pointInputs[2]
        
            print("Direction vector 1:")
            print(pointInputs[0], "-", pointInputs[1])
            print(f"► {vector1} \n")
        
            print("Direction vector 2:")
            print(pointInputs[1], "-", pointInputs[2])
            print(f"► {vector2} \n")
        
            normal = fpvc.plane_calc(pointInputs[0], vector1, vector2)
        
        else:
            print("Insufficient information")
        

    elif lineOrPlane == "LINE":
        print("")
        
elif calculationType == "DISTANCE":
    
    #Getting inputs
    totalPoints = []
    pointInputs = fpvc.get_point_input()
    while pointInputs is not None:
        totalPoints.append(pointInputs)
        pointInputs = fpvc.get_point_input()
    
    totalPlanes = []
    planeInputs = fpvc.get_plane_input()
    while planeInputs is not None:
        totalPlanes.append(planeInputs)
        planeInputs = fpvc.get_plane_input()
        
    totalLines = []
    lineInputs = fpvc.get_line_input()
    while lineInputs is not None:
        totalLines.append(lineInputs)
        lineInputs = fpvc.get_line_input()
        
    distanceType = input('''\nWhich distance do you want to calculate?
1 - Line-PLane
2 - Line-Line
3 - Point-Line \n\n''')