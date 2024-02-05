import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

#plot the data w label and increase linewidth
plt.plot(backLegSensorValues, label = 'Back Leg', linewidth = 3)
plt.plot(frontLegSensorValues, label = 'Front Leg')
plt.legend()
plt.show()