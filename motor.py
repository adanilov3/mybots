import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c
class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset

        if self.jointName == 'Torso_BackLeg':
            self.frequency = c.frequency
        else:
            self.frequency = c.frequency / 2

        value = self.frequency * numpy.linspace(0, 2 * c.pi, c.simulationTime) + self.offset
        self.motorValues = self.amplitude * numpy.sin(value)

    def Set_Value(self, t, robot):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot.robotId, jointName=self.jointName, controlMode=p.POSITION_CONTROL,
                                    targetPosition=self.motorValues[t], maxForce=100)

    def Save_Values(self):
        numpy.save('data\MotorValues.npy', self.MotorValues)
