# Solar-System
This project simulates the motion of planets around the Sun using Python's `turtle` graphics module. The simulation creates a simple representation of the solar system with eight planets orbiting the Sun.
## Features
- Visual representation of the solar system with planets orbiting the Sun.
- Eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.
- Each planet moves at a different speed to simulate the varying orbits of planets around the Sun.
## Prerequisites
- Python 3.x
- Turtle Graphics (`turtle` module comes pre-installed with Python)

# Code Explanation
## Sun
The Sun is represented as a large yellow circle in the center of the screen.
## Planet Class
Each planet is an instance of the Planet class, which inherits from turtle.Turtle.
Each planet has:
  name: The name of the planet.
  radius: The distance from the Sun (center of the screen).
  color: The color of the planet.
The move() function updates the position of each planet to simulate orbit.
## Orbit Simulation
Each planet moves around the Sun at a different angular speed, reflecting their varying orbital periods.
mercury.angle += 0.05
venus.angle += 0.03
earth.angle += 0.01
mars.angle += 0.007
jupiter.angle += 0.02
saturn.angle += 0.018
uranus.angle += 0.016
neptune.angle += 0.005
## Infinite Loop
The planets continuously orbit the Sun in an infinite while True loop, and the screen is updated in each iteration.
