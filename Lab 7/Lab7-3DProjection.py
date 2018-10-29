# Import a library of functions called 'pygame'
import pygame
from math import pi
import math as m
import numpy as np

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Point3D:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		
class Line3D():
	def __init__(self, start, end):
		self.start = start
		self.end = end

class Line():
	def __init__(self, start, end):
		self.start = start
		self.end = end

class HomogenousPoint3D:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.w = 1

def loadOBJ(filename):
	
	vertices = []
	indices = []
	lines = []
	
	f = open(filename, "r")
	for line in f:
		t = str.split(line)
		if not t:
			continue
		if t[0] == "v":
			vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))
			
		if t[0] == "f":
			for i in range(1,len(t) - 1):
				index1 = int(str.split(t[i],"/")[0])
				index2 = int(str.split(t[i+1],"/")[0])
				indices.append((index1,index2))
			
	f.close()
	
	#Add faces as lines
	for index_pair in indices:
		index1 = index_pair[0]
		index2 = index_pair[1]
		lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))
		
	#Find duplicates
	duplicates = []
	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			line1 = lines[i]
			line2 = lines[j]
			
			# Case 1 -> Starts match
			if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
				if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
					duplicates.append(j)
			# Case 2 -> Start matches end
			if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
				if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
					duplicates.append(j)
					
	duplicates = list(set(duplicates))
	duplicates.sort()
	duplicates = duplicates[::-1]
	
	#Remove duplicates
	for j in range(len(duplicates)):
		del lines[duplicates[j]]
	
	return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))
	
    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire

def begin():
	global rot
	global xdisp
	global ydisp
	global zdisp
	global wheelTranslate

	rot = 0.0
	xdisp = 0.0
	ydisp = 0.0
	zdisp = 20.0
	wheelTranslate = 0.0

def keyboard(pressed):
	global rot
	global xdisp
	global ydisp
	global zdisp

	if pressed[pygame.K_w]:
		z = -1.0 * m.cos(m.radians(rot))
		x = 1.0 * m.sin(m.radians(rot))
		zdisp += z
		xdisp += x
	if pressed[pygame.K_s]:
		z = 1.0 * m.cos(m.radians(rot))
		x = -1.0 * m.sin(m.radians(rot))
		zdisp += z
		xdisp += x
	if pressed[pygame.K_a]:
		z = -1.0 * m.sin(m.radians(rot))
		x = -1.0 * m.cos(m.radians(rot))
		zdisp += z
		xdisp += x
	if pressed[pygame.K_d]:
		z = 1.0 * m.sin(m.radians(rot))
		x = 1.0 * m.cos(m.radians(rot))
		zdisp += z
		xdisp += x

	if pressed[pygame.K_r]:
		ydisp -= 1
	if pressed[pygame.K_f]:
		ydisp += 1

	if pressed[pygame.K_q]:
		rot -= 1
		if rot < 0:
			rot = 360
	if pressed[pygame.K_e]:
		rot += 1
		if rot > 360:
			rot = 0

	if pressed[pygame.K_h]:
		begin()

def getHomogenousPoints(linelist):
	homogenousPoints = []
	for line in linelist:
		homogenousPoints.append(Line3D([line.start.x, line.start.y, line.start.z, 1], [line.end.x, line.end.y, line.end.z, 1]))
	return homogenousPoints

def constructWorld(linelist, kind):
	homogenousPoints = getHomogenousPoints(linelist)
	worldPoints = []
	for toWorldMatrix in kind:
		for line in homogenousPoints:
			startOut = toWorldMatrix.dot(line.start)
			endOut = toWorldMatrix.dot(line.end)
			worldPoints.append(Line3D(startOut, endOut))
	return worldPoints

def constructCar():

	car = loadCar();
	tire = loadTire();
	homogenousCarPoints = getHomogenousPoints(car)
	homogenousTirePoints = getHomogenousPoints(tire)

	#Construct World Points
	worldCarPoints = []
	worldTirePoints = []

	for toWorldMatrix in cars:
		for carLine in homogenousCarPoints:
			startOutCar = toWorldMatrix.dot(carLine.start)
			endOutCar = toWorldMatrix.dot(carLine.end)
			worldCarPoints.append(Line3D(startOutCar, endOutCar))

		#Transformation Heirarchy
		for toCarMatrix in tires:
			for tireLine in homogenousTirePoints:
				newMatrix = toWorldMatrix.dot(toCarMatrix)
				startOutTire = newMatrix.dot(tireLine.start)
				endOutTire = newMatrix.dot(tireLine.end)
				worldTirePoints.append(Line3D(startOutTire, endOutTire))


	return worldCarPoints, worldTirePoints

def constructScreen(worldPoints):
	toCameraMatrix = np.array([[m.cos(m.radians(rot)), 0, -m.sin(m.radians(rot)), -xdisp * m.cos(m.radians(rot)) - zdisp * m.sin(m.radians(rot))],
					 	   [0, 1, 0, ydisp],
					 	   [m.sin(m.radians(rot)), 0, m.cos(m.radians(rot)), -xdisp * m.sin(m.radians(rot)) + zdisp * m.cos(m.radians(rot))],
					 	   [0, 0, 0, 1]])
	#Construct Camera Points
	cameraPoints = []
	for line in worldPoints:
		startOut = toCameraMatrix.dot(line.start)
		endOut = toCameraMatrix.dot(line.end)
		cameraPoints.append(Line3D(startOut, endOut))

	#Construct Clipped Points
	clipPoints = []
	for line in cameraPoints:
		startOut = clipMatrix.dot(line.start)
		endOut = clipMatrix.dot(line.end)
		clipPoints.append(Line3D(startOut, endOut))
	
	#Construct Canonical Points
	canonicalPoints = []
	for line in clipPoints:
		#Start Points
		xs = line.start[0]
		ys = line.start[1]
		zs = line.start[2]
		ws = line.start[3]

		#End Points
		xe = line.end[0]
		ye = line.end[1]
		ze = line.end[2]
		we = line.end[3]
		if not (
				 ((xs > ws or xs < -ws) and (ys > ws or ys < -ws)) or 
				 ((xe > we or xe < -we) and (ye > we or ye < -we)) or
				 ((zs > ws or zs < -ws) or (ze > we or ze < -we))
			   ):
			canonicalPoints.append(Line([xs/ws, ys/ws, 1], [xe/we, ye/we, 1]))
		#Else clip the line

	#Convert to Screen Space
	screenPoints = []
	for line in canonicalPoints:
		startOut = screenMatrix.dot(line.start)
		endOut = screenMatrix.dot(line.end)
		screenPoints.append(Line(startOut, endOut))
	return screenPoints

def drawObjects(screenPoints, color):
	#Draw Lines on Screen
	for line in screenPoints:
		pygame.draw.line(screen, color, (line.start[0], line.start[1]), (line.end[0], line.end[1]))

# Initialize the game engine
begin()
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [1024, 1024]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")

#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
global rot
global xdisp
global ydisp
global zdisp

clipMatrix = np.array([[1.73, 0, 0, 0], 
					   [0, 1.73, 0, 0],
					   [0, 0, 1.02, -20.20],
					   [0, 0, 1, 0]])

screenMatrix = np.array([[size[0]/2, 0, size[0]/2],
						 [0, -size[1]/2, size[1]/2],
						 [0, 0, 1]])

houses = np.array([
					[[1, 0, 0, 0],
				    [0, 1, 0, 0],
				    [0, 0, 1, 0],
				    [0, 0, 0, 1]],

				    [[1, 0, 0, -20],
				    [0, 1, 0, 0],
				    [0, 0, 1, 0],
				    [0, 0, 0, 1]],

				    [[1, 0, 0, -40],
				    [0, 1, 0, 0],
				    [0, 0, 1, 0],
				    [0, 0, 0, 1]],

				    [[1, 0, 0, -60],
				    [0, 1, 0, 0],
				    [0, 0, 1, 0],
				    [0, 0, 0, 1]],

				    [[m.cos(m.radians(-90)), 0, -m.sin(m.radians(-90)), -80],
				    [0, 1, 0, 0],
				    [m.sin(m.radians(-90)), 0, m.cos(m.radians(-90)), 20],
				    [0, 0, 0, 1]],

				    [[m.cos(m.radians(-90)), 0, -m.sin(m.radians(-90)), -80],
				    [0, 1, 0, 0],
				    [m.sin(m.radians(-90)), 0, m.cos(m.radians(-90)), 40],
				    [0, 0, 0, 1]],

					[[m.cos(m.radians(180)), 0, -m.sin(m.radians(180)), -60],
				    [0, 1, 0, 0],
				    [m.sin(m.radians(180)), 0, m.cos(m.radians(180)), 60],
				    [0, 0, 0, 1]],

				    [[m.cos(m.radians(180)), 0, -m.sin(m.radians(180)), -40],
				    [0, 1, 0, 0],
				    [m.sin(m.radians(180)), 0, m.cos(m.radians(180)), 60],
				    [0, 0, 0, 1]],

				    [[m.cos(m.radians(180)), 0, -m.sin(m.radians(180)), -20],
				    [0, 1, 0, 0],
				    [m.sin(m.radians(180)), 0, m.cos(m.radians(180)), 60],
				    [0, 0, 0, 1]],

				    [[m.cos(m.radians(180)), 0, -m.sin(m.radians(180)), 0],
				    [0, 1, 0, 0],
				    [m.sin(m.radians(180)), 0, m.cos(m.radians(180)), 60],
				    [0, 0, 0, 1]]
				  ])

cars = np.array([
					[[1, 0, 0, -60],
				    [0, 1, 0, 0],
				    [0, 0, 1, 20],
				    [0, 0, 0, 1]],
				])

tires = np.array([
					[[1, 0, 0, -2],
				    [0, 1, 0, 0],
				    [0, 0, 1, 2],
				    [0, 0, 0, 1]],

				    [[1, 0, 0, -2],
				    [0, 1, 0, 0],
				    [0, 0, 1, -2],
				    [0, 0, 0, 1]],

				    [[1, 0, 0, 2],
				    [0, 1, 0, 0],
				    [0, 0, 1, -2],
				    [0, 0, 0, 1]],

				    [[1, 0, 0, 2],
				    [0, 1, 0, 0],
				    [0, 0, 1, 2],
				    [0, 0, 0, 1]],
				])

#Loop until the user clicks the close button.
while not done:
 
	# This limits the while loop to a max of 100 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(100)

	# Clear the screen and set the screen background
	screen.fill(BLACK)

	#Controller Code#
	#####################################################################

	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If user clicked close
			done=True
			
	pressed = pygame.key.get_pressed()

	keyboard(pressed);
	

	#Viewer Code#
	#####################################################################

	houseWorldPoints = constructWorld(loadHouse(), houses)
	carWorldPoints, tireWorldPoints = constructCar()

	houseScreenPoints = constructScreen(houseWorldPoints)
	carScreenPoints = constructScreen(carWorldPoints)
	tireScreenPoints = constructScreen(tireWorldPoints)

	drawObjects(carScreenPoints, GREEN)
	drawObjects(houseScreenPoints, RED)
	drawObjects(tireScreenPoints, BLUE)

	# Go ahead and update the screen with what we've drawn.
	# This MUST happen after all the other drawing commands.
	pygame.display.flip()

# Be IDLE friendly
pygame.quit()
