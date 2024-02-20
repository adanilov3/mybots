import pybullet as p
import pybullet_data
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

simulationTime = 1000
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(simulationTime)
frontLegSensorValues = numpy.zeros(simulationTime)

backLegJointValues = numpy.zeros(1000)
frontLegJointValues = numpy.zeros(1000)

amplitudeBackLeg = numpy.pi/4
frequencyBackLeg = 1/20
phaseOffsetBackLeg = 0

amplitudeFrontLeg = -numpy.pi/4
frequencyFrontLeg = 1/10
phaseOffsetFrontLeg = numpy.pi/16

for i in range(simulationTime):
    time.sleep(1/120)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    backLegPosition = amplitudeBackLeg * numpy.sin(frequencyBackLeg * i + phaseOffsetBackLeg)
    frontLegPosition = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * i + phaseOffsetFrontLeg)
    backLegJointValues[i] = backLegPosition
    frontLegJointValues[i] = frontLegPosition

    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_BackLeg', controlMode=p.POSITION_CONTROL,
                                targetPosition=backLegPosition, maxForce=200)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_FrontLeg', controlMode=p.POSITION_CONTROL,
                                targetPosition=frontLegPosition, maxForce=200)
    #print(i)

#numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
#numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/backLegJointValues.npy", backLegJointValues)
numpy.save("data/frontLegJointValues.npy", frontLegJointValues)

p.disconnect()
