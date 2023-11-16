import turtle
from oop2 import Ball

class Simulation:
    def __init__(self, num_balls):
        self.num_balls = num_balls
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width

        self.balls = [Ball(self.canvas_width, self.canvas_height, self.ball_radius) for _ in range(num_balls)]

    def run(self):
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        turtle.colormode(255)

        while True:
            turtle.clear()
            for ball in self.balls:
                ball.draw()
                ball.move(self.canvas_width, self.canvas_height, self.ball_radius)
            turtle.update()

# Example Usage:
num_balls = int(input("Number of balls to simulate: "))
simulation = Simulation(num_balls)
simulation.run()

# Hold the window; close it by clicking the window close 'x' mark
turtle.done()
