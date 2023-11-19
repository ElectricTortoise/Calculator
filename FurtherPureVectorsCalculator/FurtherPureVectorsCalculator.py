import numpy as np
import math
import re
import FPVCModule as fpvc




print("Note: Inputs for vectors should be given one at a time, decimals are accepted (for equation only, this is temporary)")
print("      Inputs for points should be given in the form 'x y z'")
print("      Inputs for planes should be given in the form, 'ax+by+cz=d'")
print("      Inputs for lines should be given in the form 'r=(x0 y0 z0)+t(x1 y1 z1)'")
print("      If there are no more inputs, press ENTER  \n")


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
1 - Point-Line
2 - Point-Plane
3 - Line-Line \n\n''')
    
    match distanceType:
        case "1":
            try:
                totalPoints[0], totalLines[0][0], totalLines[0][1]

                AB = totalPoints[0] - totalLines[0][0]
            
                print(f''' \n\n\n
Let OA be {totalPoints[0]}
Let OB be {totalLines[0][0]}
Let b1 be the direction vector {totalLines[0][1]}

BA
► OA - OB
► {totalPoints[0]} - {totalLines[0][0]}
► {AB}

Area vector
► BA x b1
► ''', end="")
                areaVector =  fpvc.cross(AB, totalLines[0][1])
                area = fpvc.magnitude(areaVector)
                height = fpvc.magnitude(totalLines[0][1])
                print(f'''Area
► |BA x b1|                  
► √({areaVector[0]}^2 + {areaVector[1]}^2 + {areaVector[2]}^2)    
► {area}

Height
► |b1|
► √({totalLines[0][1][0]}^2 + {totalLines[0][1][1]}^2 + {totalLines[0][1][2]}^2)
► {height}''')
                finalDistance = area/height
                print(f'''
Distance
► Area / Height
► {area} / {height}                  
► {finalDistance}
''')
            except:
                print("Insufficient inputs")
                
        case "2":
            try:
                totalPoints[0], totalPlanes[0][1]
                above = np.dot(totalPlanes[0][0], totalPoints[0])-totalPlanes[0][1]
                below = fpvc.magnitude(totalPlanes[0][0])
                print(f'''ax+by+cz-d
► {totalPoints[0][0]} * {totalPlanes[0][0][0]} + {totalPoints[0][1]} * {totalPlanes[0][0][1]} + {totalPoints[0][2]} * {totalPlanes[0][0][2]} - {totalPlanes[0][1]}
► {above}

√(a^2 + b^2 + c^2)
► √({totalPlanes[0][0][0]}^2 + {totalPlanes[0][0][1]}^2 + {totalPlanes[0][0][2]}^2)
► {below}

Distance
► |{above}/{below}|
► {abs(above/below)}''') 
            except:
                 print("Insufficient inputs")
                 
        case "3":
            try:
                totalLines[1][1]
                A1 = totalLines[0][0]
                A2 = totalLines[1][0]
                b1 = totalLines[0][1]
                b2 = totalLines[1][1]
                A1A2 = totalLines[0][0] - totalLines[1][0]
                print(f'''Let OA1 be {A1} and b1 be {b1}
Let OA2 be {A2} and b2 be {b2}

A1A2
► {A1} - {A2}
► {A1 - A2}
''')
                print('''Normal direction, n
► ''', end="")
                n = fpvc.cross(b1, b2)
                print('''A1A2 • n
► ''', end="")
                projection = fpvc.dot(A1A2, n)
                nMag = fpvc.magnitude(n)
                print(f'''Magnitude of normal
► √({n[0]}^2 + {n[1]}^2 + {n[2]}^2)
► {nMag}
''')
                finalDistance = abs(projection/nMag)
                print(f'''Distance
► |{projection} / {nMag}|
► {finalDistance}''')
            except:
                print("Insufficient inputs")