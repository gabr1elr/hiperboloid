# manim -pqm hiperboloid.py hiperboloid

from manim import *
import numpy as np

class cerc(Scene):
    def construct(self):
        cerc = Circle(color=BLUE)
        self.add(cerc)


class elipsa(Scene):
    def construct(self):
        x = float(input("width = "))
        y = float(input("height = "))
        elipsa = Ellipse(width=x, height=y, color=BLUE)
        self.add(elipsa)
        self.wait(2)


class hiperboloid(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi = 55* DEGREES, theta = 45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        axe = ThreeDAxes()

        self.play(Create(axe))

        x = float(input("lungime = "))
        y = float(input("latime = "))

        e = Ellipse(width=x, height=y, color=BLUE)
        cext = Circle(radius=max(x, y) / 2, color=BLUE)
        cint = Circle(radius=min(x, y) / 2, color=BLUE)
        self.play(Create(e))
        self.play(Create(cint))
        self.play(Create(cext))
        u1 = float(input("unghi1 = ")) * DEGREES
        u2 = float(input("unghi2 = ")) * DEGREES

        h = float(input("inaltime = "))
##P si D
        P = np.array([
            (max(x, y) / 2) * np.cos(u1),
            (max(x, y) / 2) * np.sin(u1),
            0
        ])

        D = np.array([
            (max(x, y) / 2) * np.cos(u1),
            (min(x, y) / 2) * np.sin(u1),
            0
        ])

        linie1 = Line(ORIGIN, P, color=RED)
        self.play(Create(linie1))
        self.wait(1)

        self.play(Create(Dot(P, color=WHITE)))
        self.wait(1)

        pPx = np.array([P[0], 0, 0])
        self.play(Create(Line(P, pPx, color = RED)))
        self.wait(1)

        self.play(Create(Dot(D, color=WHITE)))
        self.wait(1)

## Q si E
        Q = np.array([
            (max(x, y) / 2) * np.cos(u2),
            (max(x, y) / 2) * np.sin(u2),
            0
        ])
        self.wait(1)
        E = np.array([
            (max(x, y) / 2) * np.cos(u2),
            (min(x, y) / 2) * np.sin(u2),
            0
        ])

        linie2 = Line(ORIGIN, Q, color=RED)
        self.play(Create(linie2))
        self.wait(2)
        self.play(Create(Dot(Q, color=WHITE)))

        pQx = np.array([Q[0], 0, 0])
        self.play(Create(Line(Q, pQx, color=RED)))
        self.play(Create(Dot(E, color=WHITE)))

        self.wait(1)

        H = np.array([
            max(x, y) / 2 * np.cos(u1),
            min(x, y) / 2 * np.sin(u1),
            h
        ])
        self.play(Create(Dot(H)))
        self.wait(1)
        self.play(Create(Line(H, D, color = YELLOW)))
        self.wait(2)

        theta = u2 - u1
        S = VGroup()
        dist = 2 * DEGREES
        rx = x / 2
        ry = y / 2

        for unghi in np.arange(0, TAU, dist):
            p_jos = np.array([
                rx * np.cos(unghi),
                ry * np.sin(unghi),
                0
            ])

            p_sus = np.array([
                rx * np.cos(unghi + theta),
                ry * np.sin(unghi + theta),
                h
            ])

            linie = Line(p_jos, p_sus, stroke_width=1, stroke_opacity=0.5)
            linie.set_color(interpolate_color(RED, BLUE, unghi / TAU))
            S.add(linie)

        self.play(Create(S), run_time=4)
        self.wait(2)