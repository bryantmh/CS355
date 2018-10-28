import sys

try:
	from OpenGL.GLUT import *
	from OpenGL.GL import *
	from OpenGL.GLU import *
	from OpenGL.GL import glOrtho
	from OpenGL.GLU import gluPerspective
	from OpenGL.GL import glRotated
	from OpenGL.GL import glTranslated
	from OpenGL.GL import glLoadIdentity
	from OpenGL.GL import glMatrixMode
	from OpenGL.GL import GL_MODELVIEW
	from OpenGL.GL import GL_PROJECTION
except:
	print("ERROR: PyOpenGL not installed properly. ")
import math

DISPLAY_WIDTH = 700.0
DISPLAY_HEIGHT = 700.0

def init():
	glClearColor (0.0, 0.0, 0.0, 0.0)
	glShadeModel (GL_FLAT)

def drawCar():
	glLineWidth(2.5)
	glColor3f(0.0, 1.0, 0.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-3, 2, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 2, 2)
	#Back Side
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 1, -2)
	glVertex3f(-3, 2, -2)
	#Connectors
	glVertex3f(-3, 2, 2)
	glVertex3f(-3, 2, -2)
	glVertex3f(-2, 3, 2)
	glVertex3f(-2, 3, -2)
	glVertex3f(2, 3, 2)
	glVertex3f(2, 3, -2)
	glVertex3f(3, 2, 2)
	glVertex3f(3, 2, -2)
	glVertex3f(3, 1, 2)
	glVertex3f(3, 1, -2)
	glVertex3f(-3, 1, 2)
	glVertex3f(-3, 1, -2)
	glEnd()
	
def drawTire():
	glLineWidth(2.5)
	glColor3f(0.0, 0.0, 1.0)
	glBegin(GL_LINES)
	#Front Side
	glVertex3f(-1, .5, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, .5, .5)
	#Back Side
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, -.5, -.5)
	glVertex3f(-1, .5, -.5)
	#Connectors
	glVertex3f(-1, .5, .5)
	glVertex3f(-1, .5, -.5)
	glVertex3f(-.5, 1, .5)
	glVertex3f(-.5, 1, -.5)
	glVertex3f(.5, 1, .5)
	glVertex3f(.5, 1, -.5)
	glVertex3f(1, .5, .5)
	glVertex3f(1, .5, -.5)
	glVertex3f(1, -.5, .5)
	glVertex3f(1, -.5, -.5)
	glVertex3f(.5, -1, .5)
	glVertex3f(.5, -1, -.5)
	glVertex3f(-.5, -1, .5)
	glVertex3f(-.5, -1, -.5)
	glVertex3f(-1, -.5, .5)
	glVertex3f(-1, -.5, -.5)
	glEnd()

def drawHouse ():
	glLineWidth(2.5)
	glColor3f(1.0, 0.0, 0.0)
	#Floor
	glBegin(GL_LINES)
	glVertex3f(-5.0, 0.0, -5.0)
	glVertex3f(5, 0, -5)
	glVertex3f(5, 0, -5)
	glVertex3f(5, 0, 5)
	glVertex3f(5, 0, 5)
	glVertex3f(-5, 0, 5)
	glVertex3f(-5, 0, 5)
	glVertex3f(-5, 0, -5)
	#Ceiling
	glVertex3f(-5, 5, -5)
	glVertex3f(5, 5, -5)
	glVertex3f(5, 5, -5)
	glVertex3f(5, 5, 5)
	glVertex3f(5, 5, 5)
	glVertex3f(-5, 5, 5)
	glVertex3f(-5, 5, 5)
	glVertex3f(-5, 5, -5)
	#Walls
	glVertex3f(-5, 0, -5)
	glVertex3f(-5, 5, -5)
	glVertex3f(5, 0, -5)
	glVertex3f(5, 5, -5)
	glVertex3f(5, 0, 5)
	glVertex3f(5, 5, 5)
	glVertex3f(-5, 0, 5)
	glVertex3f(-5, 5, 5)
	#Door
	glVertex3f(-1, 0, 5)
	glVertex3f(-1, 3, 5)
	glVertex3f(-1, 3, 5)
	glVertex3f(1, 3, 5)
	glVertex3f(1, 3, 5)
	glVertex3f(1, 0, 5)
	#Roof
	glVertex3f(-5, 5, -5)
	glVertex3f(0, 8, -5)
	glVertex3f(0, 8, -5)
	glVertex3f(5, 5, -5)
	glVertex3f(-5, 5, 5)
	glVertex3f(0, 8, 5)
	glVertex3f(0, 8, 5)
	glVertex3f(5, 5, 5)
	glVertex3f(0, 8, 5)
	glVertex3f(0, 8, -5)
	glEnd()

def display():
	glClear (GL_COLOR_BUFFER_BIT)
	glColor3f (1.0, 1.0, 1.0)	

	global project
	global wheelTranslate
	global wheelRotate
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if project is 'p':		
		gluPerspective(90, 1, 0, 100)
	elif project is 'o':
		glOrtho(-10, 10, -10, 10, 1, 100)

	glMatrixMode(GL_MODELVIEW)

	# House 1
	drawHouse()

	# House 2
	glPushMatrix()
	glTranslate(-20,0,0)
	drawHouse()
	glPopMatrix()

	# House 3
	glPushMatrix()
	glTranslate(-40,0,0)
	drawHouse()
	glPopMatrix()

	# House 4
	glPushMatrix()
	glTranslate(-60,0,0)
	drawHouse()
	glPopMatrix()

	## House 5
	glPushMatrix()
	glTranslate(-80,0,20)
	glRotate(90,0,1,0)
	drawHouse()
	glPopMatrix()

	## House 6
	glPushMatrix()
	glTranslate(-80,0,40)
	glRotate(90,0,1,0)
	drawHouse()
	glPopMatrix()

	# House 7
	glPushMatrix()
	glTranslate(-60,0,60)
	glRotate(180,0,1,0)
	drawHouse()
	glPopMatrix()

	# House 8
	glPushMatrix()
	glTranslate(-40,0,60)
	glRotate(180,0,1,0)
	drawHouse()
	glPopMatrix()

	# House 9
	glPushMatrix()
	glTranslate(-20,0,60)
	glRotate(180,0,1,0)
	drawHouse()
	glPopMatrix()

	# House 10
	glPushMatrix()
	glTranslate(0,0,60)
	glRotate(180,0,1,0)
	drawHouse()
	glPopMatrix()

	### Car
	glPushMatrix()
	glTranslate(-60 + wheelTranslate,0,20)
	drawCar()

	# Tire - Back Right
	glPushMatrix()
	glTranslate(-2,0,2)
	glRotate(wheelRotate,0,0,1)
	drawTire()
	glPopMatrix()

	# Tire - Back Left
	glPushMatrix()
	glTranslate(-2,0,-2)
	glRotate(wheelRotate,0,0,1)
	drawTire()
	glPopMatrix()
	
	# Tire - Front Left
	glPushMatrix()
	glTranslate(2,0,-2)
	glRotate(wheelRotate,0,0,1)
	drawTire()
	glPopMatrix()

	# Tire - Front Right
	glPushMatrix()
	glTranslate(2,0,2)
	glRotate(wheelRotate,0,0,1)
	drawTire()
	glPopMatrix()

	glPopMatrix()


	glFlush()

def timer(dist):
	global wheelTranslate
	global wheelRotate
	wheelTranslate += .2
	wheelRotate -= 300
	glutPostRedisplay()
	glutTimerFunc(50, timer, 0)
	
def start():
	global rot
	global xdisp
	global ydisp
	global zdisp
	global project
	global wheelTranslate
	global wheelRotate

	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	glRotate(-90,0,1,0)
	glTranslate(0, -10, -20)
	rot = 90.0
	xdisp = 0.0
	ydisp = -10.0
	zdisp = -30.0
	project = 'p'
	wheelTranslate = 0.0
	wheelRotate = 0.0

def keyboard(key, x, y):

	global rot
	global xdisp
	global ydisp
	global zdisp
	global project
	glMatrixMode(GL_MODELVIEW)

	if key == chr(27):
		import sys
		sys.exit(0)

	if key == b'w':
		z = 1.0 * math.cos(math.radians(rot))
		x = 1.0 * math.sin(math.radians(rot))
		zdisp += z
		xdisp += x
		glTranslated(x, 0.0, z)

	if key == b's':
		z = -1.0 * math.cos(math.radians(rot))
		x = -1.0 * math.sin(math.radians(rot))
		zdisp += z
		xdisp += x
		glTranslated(x, 0.0, z)

	if key == b'a':
		z = -1.0 * math.sin(math.radians(rot))
		x = 1.0 * math.cos(math.radians(rot))
		zdisp += z
		xdisp += x
		glTranslated(x, 0.0, z)

	if key == b'd':
		z = 1.0 * math.sin(math.radians(rot))
		x = -1.0 * math.cos(math.radians(rot))
		zdisp += z
		xdisp += x
		glTranslated(x, 0.0, z)
		
	if key == b'r':
		ydisp += 1
		glTranslated(0.0, -1.0, 0.0)

	if key == b'f':
		ydisp -= 1
		glTranslated(0.0, 1.0, 0.0)

	if key == b'q':
		rot += 1
		if rot > 360:
			rot = 0
		glTranslated(-xdisp, -ydisp, -zdisp)
		glRotated(-1.0, 0.0, 1.0, 0.0)
		glTranslated(xdisp, ydisp, zdisp)

	if key == b'e':
		rot -= 1
		if rot < 0:
			rot = 360
		glTranslated(-xdisp, -ydisp, -zdisp)
		glRotated(1.0, 0.0, 1.0, 0.0)
		glTranslated(xdisp, ydisp, zdisp)

	if key == b'h':
		start()

	if key == b'o':
		project = 'o'

	if key == b'p':
		project = 'p'

	glutPostRedisplay()

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init()
start()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(50, timer, 0)
glutMainLoop()
