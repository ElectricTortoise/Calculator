import numpy as np
import math
import re

#Dot product function
def dot(vec1, vec2):
    dotProduct = np.dot(vec1, vec2)
    print(vec1, "•", vec2)
    print("►", vec1[0], "*", vec2[0], "+", vec1[1], "*", vec2[1], "+", vec1[2], "*", vec2[2]) 
    print("►", dotProduct, "\n")
    return dotProduct


#Cross product function
def cross(vec1, vec2):
    crossProduct = np.cross(vec1, vec2)
    print(vec1, "x", vec2)
    print("►", "[  (", vec1[1], "*", vec2[2], "-", vec1[2], "*", vec2[1], ")",
          "(",vec1[2], "*", vec2[0], "-", vec1[0], "*", vec2[2], ")",
           "(", vec1[0], "*", vec2[1], "-", vec1[1], "*", vec2[0], ")  ]")
    print("►", crossProduct, "\n")
    return crossProduct


#Gets vector inputs from user, returns the numpy array of the vectors inputted, specify direction or position.
def get_vector_input(numberOfVectors, vectorType):
    
    totalVectors = []
    i = 0
    
    for i in range(numberOfVectors):       
        print(f"Insert {vectorType} vector {i+1} : ")
        vector = np.array([])
        for i in range(3):
            vectorEntry = float(input())
            vector = np.append(vector, vectorEntry)
        totalVectors.append(vector)
    
    return totalVectors


#Should replace get_vector_input() soon
def get_point_input():
    while True:
        point = input("Input points: ")
        if point == "":
            return
        else:
            vector = np.array(point.split(), dtype="f")
            if vector.shape != (3,):
                print("Invalid Input! Try again")             
            else:
                return vector
        

#Gets plane inputs from user in the form ax+by+cz=d, returns tuple of numpy array and float, (ndarray[a b c], d), where the numpy array is the normal vector
def get_plane_input():
    while True:
        plane = input("Input plane: ")
        try:
            if plane == "":
                return
            else:
                planeCoefficients = re.split("x|y|z=", plane)
                normal = np.array([planeCoefficients[0], planeCoefficients[1], planeCoefficients[2]], dtype="f")
                return normal, float(planeCoefficients[3])
        except:
            print("Invalid input")
            continue


#Gets line inputs from the user in the form r=(x0 y0 z0)+t(x1 y1 z1), returns tuple of numpy arrays, (ndarray[x0 y0 z0], ndarray[x1 y1 z1])
def get_line_input():
    while True:
        line = input("Input line: ")
        try:
            if line == "":
                return
            else:
                lineVectors = re.split("\(|\)", line)
                fixedVector = np.array(re.split(" ", lineVectors[1]), dtype="f")
                directionVector = np.array(re.split(" ", lineVectors[3]), dtype="f")
                return fixedVector, directionVector
        except:
            print("Invalid input")
            continue
    

#Plane calculation function
def plane_calc(point, vec1, vec2):
    print("Normal vector of plane:")
    normal = cross(vec1, vec2)
    if (normal == 0).all():
        print("Error: Direction vectors are parallel")
    else:
        print("Dot product of fixed vector and normal vector:")
        d = dot(point, normal)
        a, b, c = normal
        print(f"Scalar equation of plane   : r • {normal} = {d}")
        print(f"Cartesian equation of plane: {a}x + {b}y + {c}z = {d}")
        print(f"Vector equation of plane   : r = {point} + λ{vec1} + μ{vec2} \n")
    return normal

#Normal calculation function
def normal_calc(vec1, vec2):
    print("Normal vector of plane:")
    normal = cross(vec1, vec2)
    if (normal == 0).all():
        print("Error: Direction vectors are parallel")
    else:
        return normal


#Length calculation function
def magnitude(x): 
    return math.sqrt(sum(i**2 for i in x))
