Documentation 

Introduction
	This is  a code developed by Marwan Hatem and Seif Magdy for their Computer engineering course. The aim from this project is to develop a code that simulates a car
  that moves from a starting point to a target point while dodging randomly generated obstacles. 
	The code will run as follows. Firstly it will take inputs from the user for the desired starting point, goal point, and desired checkpoint to move along them in
  order for it to reach the desired target smoothly.  
	The python version used to execute and run the code is 3.7.9
	

Required Libraries 
	There are several libraries that we will need that will help us in developing our code. The first and most important is the “roboticstoolbox” which includes 
 pre-defined classes and instances of vehicles. Its version was 0.10.0. This library includes several classes such as “Unicycle” and “Bicycle”. It also includes 
 predefined functions that control the speed, steering, distance from obstacles in the map, etc. The “math” library is needed so we can calculate certain angles 
 using the tan inverse function. The “Numpy” and “matplotlib” libraries are used to create specific arrays and to display the map respectively. 

Defined Functions 
	In our code we will have three functions that are defined by us which will be helpful and make the code more efficient and runs smoothly. The first function is 
  called “checkangle” and it takes a list of the angles of the nearest obstacles to the car that are measured by the function “SensorReading”. The objective of this 
  function is to determine the needed angle of steer according to the obstacles in front of it so it could dodge the obstacles. It then assesses which region, left, 
  right or middle has an obstacle in it using “if” statements. Afterwards it goes through a “Truth Table” using “if” statements to determine the change in the angle 
  that will make the car avoid hitting the obstacles. 
The second function defined is called “error_pos”. The aim of this function is to check whether the inputs from the user for the starting position, goal, or 
checkpoints are in the walls of the map. The walls in the map are defined as an area in a range of values between diagonally opposite points of each obstacle. 
This can be seen in figure 1 for further clarification. This function has an input of a coordinate and the list of the obstacles that are defined in the beginning 
of the code. Then using “if” statements it check if the inputted point is in the range of the list that represents the obstacles. It then returns “True” if the 
point is in fact in the list that represents one of the obstacles. 
The third function is called “gridcheck” and its functionality is very simple and has only one input. It is used to check whether the inputted x-coordinates and 
y-coordinates are outside the grid of the map. Since this check will run multiple times when checking for the initial position, target location, and checkpoints, 
it is better to define it as a function and call it further in the code. 

Input Loops 
	The next part of the code revolves around having certain loops that check whether the inputs from the user are valid and could be used or not. Starting line 85 
  we will have a big while loop which under it will take all required inputs from the user. The user will be required to enter several points which lie on the map 
  and correspond to specific x and y coordinates. These points include the initial position of the car, the target position, and the check points which the car will 
  follow to reach the target. Other inputs include how many obstacles does the user want to be there in the map. There are several important aspects in this while 
  loop. Firstly, an empty list will be created named “goal_arr.” This empty list will be used as the path for the car from its initial position to its goal. Saying 
  that this list will be appended multiple times to add the inputted points from the user. The first point on this list will be the initial position, the last point 
  will be the target point, and all the points in the middle will be the check points. Secondly, from lines 95 to 100, this is a setup for showing the map and the 
  grid. Thirdly, from lines 102 to 117, we have another while loop to take the inputs for the initial position of the car and check for any invalid inputs using 
  the defined function we explained previously. The user will input the x coordinate and y coordinate of each point separately so each one of them could be appended 
  to an empty list created at the beginning of the loop. This is done so we can check using our defined function “error_pos” if the inputted values are in the 
  obstacles. The same will be applied for the target position which could be seen from lines 119 to 133. Of course all of this is inside a loop which is originally 
  set to be “True” so if any input is to be invalid the loop is repeated and the user is requested to enter the values again.  

Vehicle Setup 
	This part of the code is related to initializing the vehicle setup which is found from lines 139 to 159. The initialization includes choosing the class 
  “Bicycle” to create an instance “vehicle”. Also, marking the goal target, the grid lines, and choosing which map to be displayed. Then from lines 207 to 
  lines 218, the sensor which reads the distance and the angle from the vehicle to all obstacles is created. Then a separate list is created for all the distances 
  and all the angles. 
 
Vehicle Run 
	Finally, this is the last part of the code where there is a “for” loop which makes the car move from its initial position to the checkpoints and to the goal 
  while dodging the obstacles ahead. At the beginning, the for loop will run as many times as the length of the goal array which includes the initial point, check 
  points, and target. And then the goal will be updated to be the next point in the goal array so it could move from the initial point to the first check point and 
  from the first check point to the second and so on and so forth. Then in line 226 a “while” loop will be created and under it there will be many updates and “if ” 
  conditions. In line 228 the angle is calculated so the steer could be adjusted. Then there is an “if” condition to check whether the car reached the goal or not. 
  Then in line 240 and 241 the distance and angle lists are updated each time it moves is could readjust its path. Finally, an empty list is created called “minangle” 
  in line 243. This list will only take values of angles of obstacles that are at a distance of 7 units from the car so it could determine whether the change in angle 
  will be positive pi/4 or negative pi/4 so it could dodge the obstacle ahead. 

