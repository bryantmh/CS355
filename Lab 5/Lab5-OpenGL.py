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
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if project is 'p':		
		gluPerspective(90, 1, 0, 100)
	elif project is 'o':
		glOrtho(-10, 10, -10, 10, 1, 100)

	glMatrixMode(GL_MODELVIEW)
	drawHouse()
	glFlush()
	
def start():
	global rot
	global xdisp
	global ydisp
	global zdisp
	global project
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
	rot = 0.0
	xdisp = 0.0
	ydisp = 0.0
	zdisp = -10.0
	project = 'p'

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
glutMainLoop()
