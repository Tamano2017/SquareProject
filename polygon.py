from Myro import * #should always be first line
init("sim") #should also always be there
side=float(input("How many sides should the shape have? Aim small so that you don't break poor Scribbly"))
angle=side 
while side > 0:
    penDown()
    forward(1,1)
    penUp()
    wait(1)
    turnBy(180-((180*(angle-2))/angle))
    wait(1)
    side = side - 1


