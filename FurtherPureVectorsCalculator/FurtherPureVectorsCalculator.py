import numpy as np
import math
import re
import FPVCModule as fpvc
import sympy as sp



print("Note: Inputs for vectors should be given one at a time, decimals are accepted (for equation only, this is temporary)")
print("      Inputs for points should be given in the form 'x y z'")
print("      Inputs for planes should be given in the form, 'ax+by+cz=d'")
print("      Inputs for lines should be given in the form 'r=(x0 y0 z0)+t(x1 y1 z1)'")
print("      If there are no more inputs, press ENTER")
print("      Intersection calculations are slightly buggy, but will yield a correct result\n\n")

calculationType = input('''What would you like to calculate?
1 - Equation
2 - Distance
3 - Intersection
4 - Angle \n\n''')


if calculationType == "1":
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
        totalPoints = []
        for i in range(2):
            pointInputs = fpvc.get_point_input()
            while pointInputs is None:
                print("Error: Minimum of 2 points required")
                pointInputs = fpvc.get_point_input()
            totalPoints.append(pointInputs)
        dirVec = totalPoints[0]-totalPoints[1]
        print(f'''\nDirection vector
► {totalPoints[0]} - {totalPoints[1]}
► {dirVec}
''')
        print(f'''Equation of line : {totalPoints[0]} + t{dirVec}''')


elif calculationType == "2":
    
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
                

elif calculationType == "3":
    
    totalPoints = []
    pointInputs = fpvc.get_point_input()
    while pointInputs is not None:
        totalPoints.append(pointInputs)
        pointInputs = fpvc.get_point_input()
        
    totalLines = []
    lineInputs = fpvc.get_line_input()
    while lineInputs is not None:
        totalLines.append(lineInputs)
        lineInputs = fpvc.get_line_input()
        
    totalPlanes = []
    planeInputs = fpvc.get_plane_input()
    while planeInputs is not None:
        totalPlanes.append(planeInputs)
        planeInputs = fpvc.get_plane_input()   

    intersectionType = input('''\nWhich intersection do you want to calculate?
1 - Foot of point to plane
2 - Line and plane
3 - Plane and plane \n\n''')

    match intersectionType:
    
        case "1":
            try:
                posVec = totalPoints[0]
                normal = totalPlanes[0][0]
                planeTranslation = totalPlanes[0][1]
                parameter = ((planeTranslation - np.dot(posVec, normal)) / (fpvc.magnitude(normal)**2))
                parameter = round(parameter, 10)
                foot = posVec + (parameter*normal)
            
                print(f'''\nEquation of line to foot
► r = {posVec} + t{normal}

Equate the equation of the plane and line, solve for t
Plane: r • n = d
Line: r = a + tn

► (a + tn) • n = d
► ({posVec} + t{normal}) • {normal} = {planeTranslation}
► {normal[0]*posVec[0]} + {normal[0]**2}t + {normal[1]*posVec[1]} + {normal[1]**2}t + {normal[2]*posVec[2]} + {normal[2]**2}t = {planeTranslation}
► {normal[0]**2 + normal[1]**2 + normal[2]**2}t = {planeTranslation - normal[0]*posVec[0] - normal[1]*posVec[1] - normal[2]*posVec[2]}
► t = {parameter}

Foot 
► {posVec} + {parameter}{normal}
► {foot}''')

            except:
                print("Insufficient inputs")
                
        case "2":
            try:
                posVec = totalLines[0][0]
                dirVec = totalLines[0][1]
                normal = totalPlanes[0][0]
                planeTranslation = totalPlanes[0][1]
                parameter = ((planeTranslation - np.dot(posVec, normal)) / (np.dot(dirVec, normal)))
                parameter = round(parameter, 10)
                foot = posVec + (parameter*dirVec)
                
                print(f'''
Equate the equation of the plane and line, solve for t
Plane: r • n = d
Line: r = a + tn

► (a + tn) • n = d
► ({posVec} + t{dirVec}) • {normal} = {planeTranslation}
► {normal[0]*posVec[0]} + {normal[0]*dirVec[0]}t + {normal[1]*posVec[1]} + {normal[1]*dirVec[1]}t + {normal[2]*posVec[2]} + {normal[2]*dirVec[2]}t = {planeTranslation}
► {normal[0]*dirVec[0] + normal[1]*dirVec[1] + normal[2]*dirVec[2]}t = {planeTranslation - normal[0]*posVec[0] - normal[1]*posVec[1] - normal[2]*posVec[2]}
► t = {parameter}

Intersection 
► {posVec} + {parameter}{dirVec}
► {foot}''')
                
            except:
                print("Insufficient inputs")
                
        case "3":
            normal1 = totalPlanes[0][0]
            normal2 = totalPlanes[1][0]


            print("Direction vector of line", end="\n► ")
            dirVec = fpvc.cross(normal1, normal2)


            for index, value in enumerate(dirVec):
                if value != 0:   
                    break


            normal1[index] = 0
            normal2[index] = 0

            x,y,z = sp.symbols("x,y,z")
            equation1 = sp.Eq(normal1[0]*x + normal1[1]*y + normal1[2]*z, totalPlanes[0][1])
            equation2 = sp.Eq(normal2[0]*x + normal2[1]*y + normal2[2]*z, totalPlanes[1][1])
            solutions = sp.solve((equation1, equation2),x,y,z)
            if x not in solutions:
                print(f'''Set x to be 0
Solve simultaneous equations

► 0 + {normal1[1]}y + {normal1[2]}z = {totalPlanes[0][1]}      ---- (1)
► 0 + {normal2[1]}y + {normal2[2]}z = {totalPlanes[1][1]}      ---- (2)

y:{solutions[y]}, z:{solutions[z]}

Point on line: (0, {solutions[y]}, {solutions[z]})
''')
                solutions[x] = 0
            elif y not in solutions:
                print(f'''Set x to be 0
Solve simultaneous equations

► {normal1[0]}x + 0 + {normal1[2]}z = {totalPlanes[0][1]}      ---- (1)
► {normal2[0]}x + 0 + {normal2[2]}z = {totalPlanes[1][1]}      ---- (2)

x:{solutions[x]}, z:{solutions[z]}

Point on line: ({solutions[x]}, 0, {solutions[z]})
''')    
                solutions[y] = 0
            elif z not in solutions:
                print(f'''Set x to be 0
Solve simultaneous equations

► {normal1[0]}x + {normal1[1]}y + 0 = {totalPlanes[0][1]}      ---- (1)
► {normal2[0]}x + {normal2[1]}y + 0 = {totalPlanes[1][1]}      ---- (2)

x:{solutions[x]}, y:{solutions[y]}

Point on line: ({solutions[x]}, {solutions[y]}, 0)
''')   
                solutions[z] = 0
    

            xDir = solutions[x]
            yDir = solutions[y]
            zDir = solutions[z]

            solutionList = np.array([xDir, yDir, zDir])

            print(f'''Equation of line
► {solutionList} + t{dirVec}''')


elif calculationType == "4":
    
    totalLines = []
    lineInputs = fpvc.get_line_input()
    while lineInputs is not None:
        totalLines.append(lineInputs)
        lineInputs = fpvc.get_line_input()
        
    totalPlanes = []
    planeInputs = fpvc.get_plane_input()
    while planeInputs is not None:
        totalPlanes.append(planeInputs)
        planeInputs = fpvc.get_plane_input()
        
    angleType = input('''\nWhich angle do you want to calculate?
1 - Between line and plane
2 - Between plane and plane\n''')
    
    match angleType:
        
        case "1":
            try:
                normal = totalPlanes[0][0]
                dirVec = totalLines[0][1]
                
                print("\nDot product of normal and direction vector, n • b", end="\n► ")
                dotProduct = abs(fpvc.dot(normal, dirVec))
                
                normalMag = fpvc.magnitude(normal) 
                dirMag = fpvc.magnitude(dirVec)
                magValue = normalMag * dirMag
                angle = math.asin(dotProduct/magValue)
                
                print(f'''Magnitude of normal, |n|
► √({normal[0]}^2 + {normal[1]}^2 + {normal[2]}^2)
► {fpvc.magnitude(normal)}

Magnitude of direction vector, |b|
► √({dirVec[0]}^2 + {dirVec[1]}^2 + {dirVec[2]}^2)
► {fpvc.magnitude(dirVec)}

Angle between normal and line
► arcsin[ |({dotProduct})| / ({normalMag} * {dirMag}) ]
► {angle} rad      or       {angle*180/math.pi}
''')


            except:
                print("Insufficient inputs")

        case "2":
            try:
                normal1 = totalPlanes[0][0]
                normal2 = totalPlanes[1][0]
            
                print("\nDot product of normal vectors, n1 • n2", end="\n► ")
                dotProduct = abs(fpvc.dot(normal1, normal2))
            
                normalMag1 = fpvc.magnitude(normal1) 
                normalMag2 = fpvc.magnitude(normal2)
                magValue = normalMag1 * normalMag2
                angle = math.acos(dotProduct/magValue)
            
                print(f'''Magnitude of normal 1, |n1|
► √({normal1[0]}^2 + {normal1[1]}^2 + {normal1[2]}^2)
► {fpvc.magnitude(normal1)}

Magnitude of normal 2, |n2|
► √({normal2[0]}^2 + {normal2[1]}^2 + {normal2[2]}^2)
► {fpvc.magnitude(normal2)}

Angle between normal and line
► arccos[ |({dotProduct})| / ({normalMag1} * {normalMag2}) ]
► {angle} rad      or       {angle*180/math.pi}
''')
                
            except:
                print("Insufficient inputs")