import numpy as np
import math
import FPVCModule as fpvc




print("Note: Vectors are given in the form [x y z], and should be inputted in the form 'x y z', with spaces in between")
print("      Planes should ONLY be given in Cartesian form, 'ax + by + cz = d' \n")

goAgain = True

while goAgain == True:
    whatToCalculate = input("What would you like to calculate today? (Intersection, Angle, Foot, Distance, Equation) \n").upper()


    if whatToCalculate == "EQUATION":
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
        
            goAgain = fpvc.again(goAgain)


        elif lineOrPlane == "LINE":
            print("")
        
    elif whatToCalculate == "DISTANCE":
        pointOrSkew = input("\nFrom point to plane or between skew lines? (Plane/Skew)\n").upper()
        if pointOrSkew == "PLANE":
            isCartesian = input("\nIs your plane in cartesian form? (Yes/No)\n").upper()
            notCartesian = True
            while notCartesian == True:
                if isCartesian == "YES":
                    print()
                elif isCartesian == "NO":
                    directions = fpvc.get_vector_input(2)
                    fpvc.normal_calc(directions[0], directions[1])
                    isCartesian = "YES"
                else:
                    print("Invalid Input!")