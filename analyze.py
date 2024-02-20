import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
#targetAngleValues = numpy.load("data/targetAngles.npy")
backLegJointValues = numpy.load("data/backLegJointValues.npy")
frontLegJointValues = numpy.load("data/frontLegJointValues.npy")

#plot the data w label and increase linewidth
#plt.plot(backLegSensorValues, label = 'Back Leg', linewidth = 3)
#plt.plot(frontLegSensorValues, label = 'Front Leg')
#plt.plot(targetAngleValues, label = "Target Angles")
plt.plot(frontLegJointValues, label = "Front Leg Values")
plt.plot(backLegJointValues, label = "Back Leg Values")
plt.legend()
plt.show()