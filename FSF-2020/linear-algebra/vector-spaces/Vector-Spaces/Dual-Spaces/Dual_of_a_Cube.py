from manimlib.imports import *
class Duality(ThreeDScene):


    def construct(self):
        axes = ThreeDAxes()  
        self.set_camera_orientation(phi = 65*DEGREES,theta =80*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.09)     
        cube = Cube(stroke_width=5,color=WHITE).scale(2)      
        cube.set_opacity(0.2) 
        self.play(ShowCreation(cube))        
        dot1= Dot(color=RED).scale(0.85).shift([2,0,0])        
        self.play(ShowCreation(dot1))
        dot2= Dot(color=YELLOW).scale(0.85).shift([-2,0,0])        
        self.play(ShowCreation(dot2))
        dot3= Dot(color=BLUE).scale(0.85).shift([0,-2,0])        
        self.play(ShowCreation(dot3))
        dot4= Dot(color=GREEN).scale(0.85).shift([0,2,0])       
        self.play(ShowCreation(dot4))
        dot5= Dot(color=ORANGE).scale(0.85).shift([0,0,2])        
        self.play(ShowCreation(dot5))
        dot6= Dot(color=PINK).scale(0.85).shift([0,0,-2])       
        self.play(ShowCreation(dot6))
        line1 = Line(start=[0,0,2],end=[2,0,0],stroke_width=2.5,color=BLACK)        
        line2 = Line(start=[0,0,2],end=[-2,0,0],stroke_width=2.5,color=BLACK)        
        line3 = Line(start=[0,0,2],end=[0,-2,0],stroke_width=2.5,color=BLACK)        
        line4 = Line(start=[0,0,2],end=[0,2,0],stroke_width=2.5,color=BLACK)        
        line5 = Line(start=[2,0,0],end=[0,0,-2],stroke_width=2.5,color=BLACK)        
        line6 = Line(start=[-2,0,0],end=[0,0,-2],stroke_width=2.5,color=BLACK)        
        line7 = Line(start=[0,-2,0],end=[0,0,-2],stroke_width=2.5,color=BLACK)        
        line8 = Line(start=[0,2,0],end=[0,0,-2],stroke_width=2.5,color=BLACK)        
        line9 = Line(start=[0,2,0],end=[-2,0,0],stroke_width=2.5,color=BLACK)        
        line10 = Line(start=[-2,0,0],end=[0,-2,0],stroke_width=2.5,color=BLACK)        
        line11 = Line(start=[0,-2,0],end=[2,0,0],stroke_width=2.5,color=BLACK)        
        line12 = Line(start=[2,0,0],end=[0,2,0],stroke_width=2.5,color=BLACK)        
        self.play(ShowCreation(line1),ShowCreation(line2),ShowCreation(line3),ShowCreation(line4),ShowCreation(line5),ShowCreation(line6),ShowCreation(line7),ShowCreation(line8),ShowCreation(line9),ShowCreation(line10),ShowCreation(line11),ShowCreation(line12))
        self.wait(10)
       
