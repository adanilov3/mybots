import numpy
import pyrosim.pyrosim as pyrosim
import constants as c
class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.simulationTime)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if t == c.simulationTime - 1:
            print(self.values)

    def Save_Values(self):
        numpy.save('data/SensorValues.npy', self.values)