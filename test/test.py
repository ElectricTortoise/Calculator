import FPVCModule as fpvc
import numpy as np
import re
import sympy as sp


totalPlanes = [(np.array([1, 3, -1]), 12), (np.array([2, -1, 1]), 10)]

normal1 = totalPlanes[0][0]
normal2 = totalPlanes[1][0]


print("Direction vector of line", end="\n► ")
dirVec = fpvc.cross(normal1, normal2)


for index, value in enumerate(dirVec):
    if value != 0:   
        break


normal1[2] = 0
normal2[2] = 0

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
