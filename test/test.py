import FPVCModule as fpvc
import numpy as np
import re

while True:
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
        

    print(totalPoints, totalLines, totalPlanes)