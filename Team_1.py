#imported libraries
from roboticstoolbox import Bicycle, RandomPath, VehicleIcon,RangeBearingSensor,LandmarkMap #roboticstoolbox library for the robot commands
from math import pi , atan2 #math library to carry out basic operations
import numpy as np #to use the arange function
import matplotlib.image as mpimg #to display the map
import matplotlib.pyplot as plt #to plot the graph

#obstacle points that are diagonally opposite to denote the area of the obstacle
obst1 = [(-50,50),(-45,-50)]
obst2 = [(-45,2),(20,8)]
obst3 = [(-45,-22),(-25,-17)]
obst4 = [(-25,50),(50,45)]
obst5 = [(40,45),(50,-50)]
obst6 = [(40,-50),(-5,-45)]
obst7 = [(-5,-45),(0,-17)]
obst8 = [(0,-17),(20,-22)]

#definition for the function that checks if the input point is outside of the grid range
def gridcheck(x):
    if x > 50 or x < -50:
        return(True)

#definiton for the function that checks the needed steer change according to the obstacles presented to it
def checkangle(angle):
    right = False
    middle = False
    left = False
    change = 0
    #determining the position of the obstacles present close to it
    for i in range(len(minangle)): #minangle is the list of angle that the function will run on
        if angle[i] < -pi/12 and angle[i] > -pi/4:
            right = True
        if angle[i] > pi/12 and angle[i] < pi/4:
            left = True
        if angle[i] >= -pi/12 and angle[i] <= pi/12:
            middle = True
    #determining the needed angle outcome to evade those obstacles through a truthtable
    if right == False and middle == False and left == True: 
        change = -pi/4
    elif right == True and middle == False and left == False:
        change = pi/4 
    elif right == False and middle == True and left == False:
        change = -pi/4
    elif right == True and middle == True and left == False: 
        change = pi/4 
    elif right == False and middle == True and left == True: 
        change = -pi/4 
    elif right == True and middle == True and left == True:
        change = pi
    else:
        change = 0 
    #returns the needed steer change
    return(change)

#definition for the functions that check the position of the inputted points compared to the preset obstacles
def error_pos(lx,a,b,c,d,e,f,g,h): #lx is list of input points(2), a is coordinates 1 of the obstacle and b is coordinates 2 of the obstacle
    if lx[0] in np.arange(a[0][0],a[1][0]+1) and lx[1] in np.arange(a[0][1],a[1][1]-1,-1):
        return(True)
    elif lx[0] in np.arange(b[0][0],b[1][0]+1) and lx[1] in np.arange(b[0][1],b[1][1]+1):
        return(True)
    elif lx[0] in np.arange(c[0][0],c[1][0]+1) and lx[1] in np.arange(c[0][1],c[1][1]+1):
        return(True)
    elif lx[0] in np.arange(d[0][0],d[1][0]+1) and lx[1] in np.arange(d[0][1],d[1][1]-1,-1):
        return(True)
    elif lx[0] in np.arange(e[0][0],e[1][0]+1) and lx[1] in np.arange(e[0][1],e[1][1]-1,-1):
        return(True)
    elif lx[0] in np.arange(f[0][0],f[1][0]-1,-1) and lx[1] in np.arange(f[0][1],f[1][1]+1):
        return(True)
    elif lx[0] in np.arange(g[0][0],g[1][0]+1) and lx[1] in np.arange(g[0][1],g[1][1]+1):
        return(True)
    elif lx[0] in np.arange(h[0][0],h[1][0]+1) and lx[1] in np.arange(h[0][1],h[1][1]-1,-1):
        return(True)
    else:
        return(False)

#customizing the goal marker
goal_marker_style = {
 'marker': 'D',
 'markersize': 6,
 'color': 'b',
}

#Main input while loop for checking similarity between the points
equalrun = True #flag
while(equalrun):
    goal_arr = [] #list of the points, empty for now and empty on reset\
    #input for number of obstacles in the map
    obstn = int(input("enter the number of obstacle(recommended up to 50): "))
    #creating a detailed grid to help the user see where to input the points
    plt.xticks(np.arange(-50,50, 5))
    plt.yticks(np.arange(-50,50, 5))
    map = LandmarkMap(obstn,50)

    #creating the sensor which reads the distance and angle relative to the robot, plotting the map and showing the image
    map.plot()
    image = mpimg.imread("projectmap.png")
    plt.imshow(image, extent = [-50,50,-50,50])
    #printing the sensor readings for increased transperancy
    plt.title("determine the start and end position of the car")
    plt.pause(5)

    startrun = True #flag
    while(startrun): #while loop for start position input
        init_pos = [] #empty start position list
        initx = float(input("please enter the x coordinate of the robot's initial position: "))
        inity = float(input("please enter the y coordinate of the robot's initial position: "))
        init_pos.append(initx)
        init_pos.append(inity)
        #error checks
        if error_pos(init_pos,obst1,obst2,obst3,obst4,obst5,obst6,obst7,obst8):
            startrun = True
            print("enter coordinates not in the obstacle")
        elif gridcheck(initx) or gridcheck(inity):
            startrun = True
            print("enter coordinates inside the 50 by 50 grid")
        else:
            startrun = False
    targetrun = True #flag
    while(targetrun): #while loop for target position input
        goal = [] #empty target position list
        targetx = float(input("please enter the x coordinate of the target's position: "))
        targety = float(input("please enter the y coordinate of the target's position: "))
        goal.append(targetx)
        goal.append(targety)
        #error checks
        if error_pos(goal,obst1,obst2,obst3,obst4,obst5,obst6,obst7,obst8):
            targetrun = True
            print("enter coordinates not in the obstacle")
        elif gridcheck(targetx) or gridcheck(targety):
            startrun = True
            print("enter coordinates inside the 50 by 50 grid")
        else:
            targetrun = False

    #creating a detailed grid to help the user see where to input the points
    
    
    #creating an object of the class bicycle and vehicleicon to initialise the robot
    anim = VehicleIcon('car', scale=4)
    veh = Bicycle(
    animation=anim,
    control=RandomPath,
    dim=500,
    x0 = [init_pos[0],init_pos[1],pi]
    )
    veh.init(plot=True)
    veh._animation.update(veh.x)
    plt.plot(goal[0], goal[1], **goal_marker_style)

    plt.xticks(np.arange(-50,50, 5))
    plt.yticks(np.arange(-50,50, 5))

    #creating the sensor which reads the distance and angle relative to the robot, plotting the map and showing the image
    map.plot()
    image = mpimg.imread("projectmap.png")
    plt.imshow(image, extent = [-50,50,-50,50])
    #printing the sensor readings for increased transperancy
    plt.title("determine the number of checkpoints(recommended 3 or 4 to avoid walls) and the position of them")
    plt.pause(10)

    

    no_check = int(input("enter how many checkpoints the car will pass through (recommended: at least 3 or 4 to avoid walls): ")) #number of needed inputs allowed by the user
    for i in range(no_check): #for loop to iterate on the number of needed checkpoints
        checkp_run = True #flag
        while(checkp_run): #while loop for checkpoints
            print("for checkpoint",i+1)
            temp1 = [] #empty list that clears on each for loop that contains the points which are added to the goal_arr at the end of each loop
            checkpx = float(input("please enter the x coordinate of the checkpoint's position: "))
            checkpy = float(input("please enter the y coordinate of the checkpoint's position: "))
            temp1.append(checkpx)
            temp1.append(checkpy)
            #error checks
            if error_pos(temp1,obst1,obst2,obst3,obst4,obst5,obst6,obst7,obst8):
                checkp_run = True
                print("enter coordinates not in the obstacle")
            elif gridcheck(checkpx) or gridcheck(checkpy):
                startrun = True
                print("enter coordinates inside the 50 by 50 grid")
            else:
                checkp_run = False
            
        goal_arr.append(tuple(temp1)) #appending of the checkpoints to the goal_arr, inside the for loop to append each different checkpoints
    goal_arr.insert(0,tuple(init_pos)) #inserting of the initial position at the beginning of the list
    goal_arr.append(tuple(goal)) #inserting of the goal at the end of the list
    print(goal_arr) #goal array for the user

    #set of functions for checking similiar points through converting the goal_arr into a list to get rid of duplicates, comparing them and seeing discrepency
    set_goal_arr = set(goal_arr)
    if len(goal_arr) != len(set_goal_arr):
        print("The checkpoints list contains duplicates, enter the points again without repeating points ")
        equalrun = True
    else:
        equalrun = False





#plotting the goal and the graphs and the map
plt.plot(goal[0], goal[1], **goal_marker_style)
#creating a detailed grid to help the user see where to input the points
plt.xticks(np.arange(-50,50, 5))
plt.yticks(np.arange(-50,50, 5))


#creating the sensor which reads the distance and angle relative to the robot, plotting the map and showing the image
sensor=RangeBearingSensor(robot=veh,map=map,animate=True)
map.plot()
image = mpimg.imread("projectmap.png")
plt.imshow(image, extent = [-50,50,-50,50])
print("Sensor readings: ", sensor.h(veh.x)) #printing the sensor readings for increased transperancy

#splitting the sensor list into distance and angle to facilitate operating on them
distance = [sensor.h(veh.x)[i][0] for i in range(len(sensor.h(veh.x)))]
angle = [sensor.h(veh.x)[i][1] for i in range(len(sensor.h(veh.x)))]
print(distance)
print(angle)

#for loop for iterating on the checkpoints provided
for i in range(len(goal_arr)):
    run = True
    #determining the goal
    goal = [goal_arr[i][0],goal_arr[i][1]]
    #main loop for movement
    while(run):
        #determining the angle of the goal according to the robot
        goal_heading = atan2((goal[1] - veh.x[1]),(goal[0] - veh.x[0]))
        #calculating the steer
        steer = goal_heading-veh.x[2]
        #making sure steer doesn't go out of the range of the atan function
        if steer>pi:
            steer = steer-2*pi
        #if condition to check wether it reached the goal or not
        if( (abs(goal[0]-veh.x[0]) >2) or (abs(goal[1]-veh.x[1]) > 2) ):
            run=True
        else:
            run=False
        #updating the distance and angle lists as the robot moves
        distance = [sensor.h(veh.x)[i][0] for i in range(len(sensor.h(veh.x)))]
        angle = [sensor.h(veh.x)[i][1] for i in range(len(sensor.h(veh.x)))]
        #creating empty list for the angles needed to dodge
        minangle = []
        #filling out the list using nested for and if loops
        for i in range(len(distance)):
            if distance[i] <= 7:
                if angle[i] >= -pi/4 and angle[i] <= pi/4:
                    minangle.append(angle[i])
        #adjusting the steer of the robot as such
        steer = steer + checkangle(minangle)
        veh.step(4,steer)
        veh._animation.update(veh.x)
        plt.pause(0.0005)
    
plt.pause(10)



