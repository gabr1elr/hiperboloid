from manim import *
import numpy as np

class HyperboloidConstruction(ThreeDScene):
    def construct(self):
        rx = 3.0       
        ry = 2.0       
        height = 5.0   # Total height
        num_lines = 48 
        
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)
        
        self.begin_ambient_camera_rotation(rate=0.15)
        
        axes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-4, 4])
        self.play(Create(axes))
        twist_tracker = ValueTracker(0) 
        
        waist_tracker = ValueTracker(1) 

        def get_surface_lines():
            """
            This function generates the VGroup of lines based on current 
            values of the twist and the waist factor.
            """
            lines = VGroup()
            twist = twist_tracker.get_value()
            w_factor = waist_tracker.get_value() # 1 for Hyperboloid, approaches 0 for Cone
            
            for i in range(num_lines):
                alpha = i * (TAU / num_lines) # Angle 0 to 2pi
                
                # Bottom Point (z = -height/2)
                p1 = np.array([
                    rx * np.cos(alpha),
                    ry * np.sin(alpha),
                    -height / 2
                ])
                
                # Top Point (z = +height/2)
                p2 = np.array([
                    rx * np.cos(alpha + twist),
                    ry * np.sin(alpha + twist),
                    height / 2
                ])
                
                if w_factor < 0.99:
                    cone_p2 = -p1 
                    p2 = interpolate(cone_p2, p2, w_factor)

                
                line = Line(p1, p2, stroke_width=2)
                
                
                line.set_color(interpolate_color(BLUE, TEAL, i/num_lines))
                lines.add(line)
            return lines

        surface_lines = always_redraw(get_surface_lines)
        
        title = Text("1. Cylinder (Twist = 0°)", font_size=36).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        
        self.play(Create(surface_lines), run_time=2)
        self.wait()

        target_twist = 110 * DEGREES
        
        self.play(
            title.animate.become(Text("2. Hyperboloid (Ruled Surface)", font_size=36).to_corner(UL)),
            twist_tracker.animate.set_value(target_twist),
            run_time=4
        )
        self.wait()
        
        top_ellipse = Ellipse(width=2*rx, height=2*ry, color=WHITE).shift(OUT * height/2)
        bot_ellipse = Ellipse(width=2*rx, height=2*ry, color=WHITE).shift(IN * height/2)
        self.play(Create(top_ellipse), Create(bot_ellipse))
        
        # Show Equation
        eq = MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1").to_corner(DL)
        self.add_fixed_in_frame_mobjects(eq)
        self.play(Write(eq))
        self.wait(2)

        self.play(
            title.animate.become(Text("3. Asymptotic Cone", font_size=36).to_corner(UL)),
            eq.animate.become(MathTex(r"\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 0").to_corner(DL)),
            waist_tracker.animate.set_value(0), 
            FadeOut(top_ellipse),
            FadeOut(bot_ellipse),
            run_time=3
        )
        
        self.wait(3)