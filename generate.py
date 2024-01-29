import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = height / 2

pyrosim.Start_SDF("boxes.sdf")

#pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
#pyrosim.Send_Cube(name="Box2", pos=[x+1, y, z+1], size=[length, width, height])

for g in range(5):
    length = 1
    width = 1
    height = 1
    for h in range(5):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            pyrosim.Send_Cube(name=f"Box{i}", pos=[x+g, y+h, z+i], size=[length,width,height])
            length *= .9
            width *= .9
            height *= .9


pyrosim.End()
