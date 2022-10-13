# https://www.codewars.com/kata/63306fdffa185d004a987b8e

import numpy as np

switchesLights = [
  [0, 1, 2],    # switch 0 controls light 0, 1, 2
  [1, 2],       # switch 1 controls light 1, 2
  [1, 2, 3, 4], # switch 2 controls light 1, 2, 3, 4
  [1, 4]        # switch 3 controls light 1, 4
]
allLights = []
for row in switchesLights:
    for item in row:
        allLights.append(item)
a = np.unique(allLights)

lights = [0 for x in a ]
while 0 in lights:
  print(lights)
  toggleSwitch = int(input())
  lightsToSwitch = switchesLights[toggleSwitch]
  for l in lightsToSwitch:
    lights[l] = 1
  print(lights)  

print(lights)

