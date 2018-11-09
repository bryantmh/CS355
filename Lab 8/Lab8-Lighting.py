""" Modified code from Peter Colling Ridge 
	Original found at http://www.petercollingridge.co.uk/pygame-3d-graphics-tutorial
"""

import pygame, math
import numpy as np
import wireframe as wf
import basicShapes as shape

class WireframeViewer(wf.WireframeGroup):
    """ A group of wireframes which can be displayed on a Pygame screen """
    
    def __init__(self, width, height, name="Wireframe Viewer"):
        self.width = width
        self.height = height
        
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        
        self.wireframes = {}
        self.wireframe_colours = {}
        self.object_to_update = []
        
        self.displayNodes = False
        self.displayEdges = True
        self.displayFaces = True
        
        self.perspective = False
        self.eyeX = self.width/2
        self.eyeY = 100
        self.light_color = np.array([1,1,1])
        self.view_vector = np.array([0, 0, -1])        
        self.light_vector = np.array([0.0, 0.0, -1.0])  

        self.background = (10,10,50)
        self.nodeColour = (250,250,250)
        self.nodeRadius = 4
        
        self.control = 0
        self.rotx = 270.0
        self.roty = 270.0

    def addWireframe(self, name, wireframe):
        self.wireframes[name] = wireframe
        #   If colour is set to None, then wireframe is not displayed
        self.wireframe_colours[name] = (250,250,250)
    
    def addWireframeGroup(self, wireframe_group):
        # Potential danger of overwriting names
        for name, wireframe in wireframe_group.wireframes.items():
            self.addWireframe(name, wireframe)
    

    def display(self):
        self.screen.fill(self.background)

        for name, wireframe in self.wireframes.items():
            nodes = wireframe.nodes
            
            if self.displayFaces:
                for (face, colour) in wireframe.sortedFaces():
                    v1 = (nodes[face[1]] - nodes[face[0]])[:3]
                    v2 = (nodes[face[2]] - nodes[face[0]])[:3]

                    normal = np.cross(v1, v2)
                    normal /= np.linalg.norm(normal)
                    towards_us = np.dot(normal, self.view_vector)

                    # Only draw faces that face us
                    if towards_us > 0:
                        m_ambient = 0.1
                        ambient = self.light_color * (m_ambient * colour)

                        #Your lighting code here
                        #Make note of the self.view_vector and self.light_vector 
                        #Use the Phong model

                        # S = self.light_color
                        # M_amb = m_ambient * colour
                        # n = normal
                        # l = self.light_vector
                        # M_diff = m_diffuse * colour

                        # Compute Diffuse Reflection
                        # S ⊗ M_diff (n dot l)
                        # lightVector = self.light_vector
                        lightVector = self.light_vector / np.linalg.norm(self.light_vector)

                        # print(self.light_vector, lightVector)

                        m_diffuse = .4
                        diffuse = self.light_color * ((m_diffuse * colour) * (normal.dot(lightVector)))
                        diffuse[:] = np.clip(diffuse[:], 0, 255)

                        # Compute Reflection Vector
                        # r = 2(l · n)n − l
                        reflectionVector = 2 * (normal.dot(lightVector)) * normal - lightVector

                        # Compute Specular Reflection
                        # S ⊗ M_spec (v dot r) ^ Mgls
                        m_specular = .5
                        Mgls = 3
                        specular = (self.light_color * (m_specular * colour)) * ((reflectionVector.dot(self.view_vector)) ** Mgls)
                        specular[:] = np.clip(specular[:], 0, 255)
                        # print(diffuse, specular)



						#Once you have implemented diffuse and specular lighting, you will want to include them here
                        light_total = ambient + diffuse + specular
                        light_total[:] = np.clip(light_total[:], 0, 255)
 
                        pygame.draw.polygon(self.screen, light_total, [(nodes[node][0], nodes[node][1]) for node in face], 0)

                if self.displayEdges:
                    for (n1, n2) in wireframe.edges:
                        if self.perspective:
                            if wireframe.nodes[n1][2] > -self.perspective and nodes[n2][2] > -self.perspective:
                                z1 = self.perspective/ (self.perspective + nodes[n1][2])
                                x1 = self.width/2  + z1*(nodes[n1][0] - self.width/2)
                                y1 = self.height/2 + z1*(nodes[n1][1] - self.height/2)
                    
                                z2 = self.perspective/ (self.perspective + nodes[n2][2])
                                x2 = self.width/2  + z2*(nodes[n2][0] - self.width/2)
                                y2 = self.height/2 + z2*(nodes[n2][1] - self.height/2)
                                
                                pygame.draw.aaline(self.screen, colour, (x1, y1), (x2, y2), 1)
                        else:
                            pygame.draw.aaline(self.screen, colour, (nodes[n1][0], nodes[n1][1]), (nodes[n2][0], nodes[n2][1]), 1)

            if self.displayNodes:
                for node in nodes:
                    pygame.draw.circle(self.screen, colour, (int(node[0]), int(node[1])), self.nodeRadius, 0)
        
        pygame.display.flip()

    def keyEvent(self, key):
        # print(self.light_vector)
        if self.rotx < 0:
            self.rotx = 360
        elif self.rotx > 360:
            self.rotx = 0
        elif self.roty < 0:
            self.roty = 360
        elif self.roty > 360:
            self.roty = 0

        #Your code here
        if key == pygame.K_w:
            self.rotx -= 8
            self.light_vector[2] = math.sin(math.radians(self.rotx)) + math.sin(math.radians(self.roty))
            self.light_vector[1] = math.cos(math.radians(self.rotx))

        if key == pygame.K_s:
            self.rotx += 8
            self.light_vector[2] = math.sin(math.radians(self.rotx)) + math.sin(math.radians(self.roty))
            self.light_vector[1] = math.cos(math.radians(self.rotx))

        if key == pygame.K_a:
            self.roty -= 8
            self.light_vector[2] = math.sin(math.radians(self.roty)) + math.sin(math.radians(self.rotx))
            self.light_vector[0] = math.cos(math.radians(self.roty))

        if key == pygame.K_d:
            self.roty += 8
            self.light_vector[2] = math.sin(math.radians(self.roty)) + math.sin(math.radians(self.rotx))
            self.light_vector[0] = math.cos(math.radians(self.roty))

        if key == pygame.K_q:
            self.roty -= 8
            self.rotx -= 8
            self.light_vector[1] = math.sin(math.radians(self.rotx))
            self.light_vector[0] = math.cos(math.radians(self.roty))
            self.light_vector[2] = math.sin(math.radians(self.roty)) + math.sin(math.radians(self.rotx))

        if key == pygame.K_e:
            self.roty += 8
            self.roty += 8
            self.light_vector[1] = math.sin(math.radians(self.rotx))
            self.light_vector[0] = math.cos(math.radians(self.roty))
            self.light_vector[2] = math.sin(math.radians(self.roty)) + math.sin(math.radians(self.rotx))


        return

    def run(self):
        """ Display wireframe on screen and respond to keydown events """
        
        running = True
        key_down = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    key_down = event.key
                elif event.type == pygame.KEYUP:
                    key_down = None
            
            if key_down:
                self.keyEvent(key_down)
            
            self.display()
            self.update()
            
        pygame.quit()

		
resolution = 52
viewer = WireframeViewer(600, 400)
viewer.addWireframe('sphere', shape.Spheroid((300,200, 20), (160,160,160), resolution=resolution))

# Colour ball
faces = viewer.wireframes['sphere'].faces
for i in range(int(resolution/4)):
	for j in range(resolution*2-4):
		f = i*(resolution*4-8) +j
		faces[f][1][1] = 0
		faces[f][1][2] = 0
	
viewer.displayEdges = False
viewer.run()
