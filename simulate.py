import pybullet as p
import time

physicsClient = p.connect(p.GUI)

simulationTime = 1000
for i in range(simulationTime):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()
