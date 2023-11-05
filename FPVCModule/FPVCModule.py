import numpy as np
import math

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
    print("►", "[ [", vec1[1], "*", vec2[2], "-", vec1[2], "*", vec2[1], "]",
          "[", vec1[2], "*", vec2[0], "-", vec1[0], "*", vec2[2], "]",
           "[", vec1[0], "*", vec2[1], "-", vec1[1], "*", vec2[0], "] ]")
    print("►", crossProduct, "\n")
    return crossProduct


#Gets vector inputs from user, returns the numpy array of the vectors inputted, specify direction or position.
def get_vector_input(numberOfVectors, vectorType):
    
    totalVectors = []
    i = 0
    
    while i < numberOfVectors:
        vectorInput = input(f"Insert {vectorType} vector {i+1} : ")
        vector = np.array([])
        vector.append(vectorInput)
        if vector.shape != (3,):
            print("Invalid Input! Try again")
        else:
            totalVectors.append(vector)
            i = i + 1
    
    totalVectors = np.array(totalVectors)
    print()
    
    return totalVectors


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
