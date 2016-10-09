from Myro import *
init("sim")
penDown()
turnTo(90)
forward(2.5,1)
turnTo(0)
move(.5,-1)
wait(5)
turnTo(-65)
forward(1,1)

#To me, writing code for letters and shapes in
#Calico isn't all that different. Both require
#about the same number of steps--especially with
#how fickle the robot simulator is with angles--
#and both involve the robot turning and moving.
#In the case of the letter I chose to draw, there
#is especially little difference; with that,
#the only difference between drawing letters and
#shapes is that shapes can always be drawn in one
#fluid movement, whereas letters often require the
#robot to pick up the pen and move back to a certain
#point (in the case of a T, for example, the robot has to
#make the horizontal line and then go back to make 
#the vertical line). 