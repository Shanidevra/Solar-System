import turtle
import time
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=800)
screen.tracer(50)
screen.title("Solar System Simulation")

# Create the sun
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
sun.shapesize(3.5, 3.5)
sun.penup()

class Planet(turtle.Turtle):
    def __init__(self, name, radius, color, size, speed, eccentricity=0.0):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.color(color)
        self.shapesize(size, size)
        self.c = color
        self.angle = 0
        self.speed = speed
        self.eccentricity = eccentricity
        self.penup()
        
        # Draw orbital path
        self.draw_orbit()
        self.goto_start_position()
        self.pendown()
        
    def draw_orbit(self):
        orbit = turtle.Turtle()
        orbit.hideturtle()
        orbit.speed(0)
        orbit.color("gray")
        orbit.penup()
        orbit.width(0.5)
        
        a = self.radius
        b = a * math.sqrt(1 - self.eccentricity**2)
        
        orbit.penup()
        orbit.goto(sun.xcor() + a * (1 + self.eccentricity), sun.ycor())
        orbit.pendown()
        
        for angle in range(0, 361, 5):
            rad = math.radians(angle)
            x = a * math.cos(rad) * (1 - self.eccentricity * math.cos(rad))
            y = b * math.sin(rad)
            orbit.goto(sun.xcor() + x, sun.ycor() + y)
        
    def goto_start_position(self):
        x = self.radius * (1 - self.eccentricity)
        y = 0
        self.goto(sun.xcor() + x, sun.ycor() + y)
        
    def move(self):
        mean_anomaly = self.angle * self.speed
        eccentric_anomaly = mean_anomaly
        
        for _ in range(3):
            eccentric_anomaly = mean_anomaly + self.eccentricity * math.sin(eccentric_anomaly)
        
        x = self.radius * (math.cos(eccentric_anomaly) - self.eccentricity)
        y = self.radius * math.sqrt(1 - self.eccentricity**2) * math.sin(eccentric_anomaly)
        
        self.goto(sun.xcor() + x, sun.ycor() + y)

# Create planets
mercury = Planet("Mercury", 40, 'gray', 0.4, 4.15, 0.2056)
venus = Planet("Venus", 70, 'orange', 0.9, 1.63, 0.0067)
earth = Planet("Earth", 100, 'skyblue', 0.95, 1.0, 0.0167)
mars = Planet("Mars", 150, 'red', 0.5, 0.53, 0.0934)
jupiter = Planet("Jupiter", 220, 'beige', 1.8, 0.084, 0.0484)
saturn = Planet("Saturn", 280, 'goldenrod', 1.5, 0.034, 0.0542)
uranus = Planet("Uranus", 340, 'lightblue', 1.2, 0.012, 0.0472)
neptune = Planet("Neptune", 400, 'blue', 1.2, 0.006, 0.0086)

class Moon(turtle.Turtle):
    def __init__(self, planet, distance, color, size, speed):
        super().__init__(shape='circle')
        self.planet = planet
        self.distance = distance
        self.color(color)
        self.shapesize(size, size)
        self.speed = speed
        self.angle = 0
        self.penup()
        
    def move(self):
        x = self.planet.xcor() + self.distance * math.cos(self.angle)
        y = self.planet.ycor() + self.distance * math.sin(self.angle)
        self.goto(x, y)

# Create moons
moon = Moon(earth, 15, 'lightgray', 0.3, 0.2)
io = Moon(jupiter, 25, 'yellow', 0.25, 0.15)
europa = Moon(jupiter, 30, 'white', 0.2, 0.12)

# ============ ADD ASTEROID BELT HERE (after moons, before stars) ============
asteroids = []  # Create an empty list for asteroids

# Add asteroid belt between Mars (radius 150) and Jupiter (radius 220)
for i in range(80):  # Create 80 asteroids
    asteroid = turtle.Turtle()
    asteroid.shape('circle')
    
    # Vary asteroid colors (grays and browns)
    colors = ['gray', 'dark gray', 'brown', 'sienna', 'dim gray']
    asteroid.color(random.choice(colors))
    
    # Vary asteroid sizes (0.05 to 0.2)
    asteroid_size = 0.05 + random.random() * 0.15
    asteroid.shapesize(asteroid_size, asteroid_size)
    
    asteroid.penup()
    
    # Position asteroids in a belt between Mars and Jupiter
    # Radius between 165 and 215 (between Mars at 150 and Jupiter at 220)
    asteroid.radius = 165 + random.random() * 50
    
    # Random starting angle
    asteroid.angle = random.random() * 2 * math.pi
    
    # Vary speeds slightly
    asteroid.speed = 0.02 + random.random() * 0.01
    
    asteroids.append(asteroid)

# ============ END OF ASTEROID BELT CODE ============

# Add stars
for _ in range(150):
    star = turtle.Turtle()
    star.penup()
    star.color("white")
    star.shape("circle")
    star.shapesize(0.03 + random.random() * 0.04)
    star.goto(
        random.uniform(-450, 450),
        random.uniform(-350, 350)
    )

# Lists of objects
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
moons = [moon, io, europa]

# Animation control variables
running = True
time_scale = 0.005

def toggle_pause():
    global running
    running = not running

def increase_speed():
    global time_scale
    time_scale *= 1.5

def decrease_speed():
    global time_scale
    time_scale /= 1.5

def reset_simulation():
    global time_scale
    time_scale = 0.005
    for planet in planets:
        planet.angle = 0
        planet.goto_start_position()
    for moon_obj in moons:
        moon_obj.angle = 0
    # Also reset asteroids
    for asteroid in asteroids:
        asteroid.angle = random.random() * 2 * math.pi

# Keyboard controls
screen.listen()
screen.onkeypress(toggle_pause, "space")
screen.onkeypress(increase_speed, "Up")
screen.onkeypress(decrease_speed, "Down")
screen.onkeypress(reset_simulation, "r")
screen.onkeypress(screen.bye, "Escape")

# Add instruction display
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.color("white")
instructions.goto(-450, 350)
instructions.write("Solar System Simulation\nSpace: Pause/Resume\nUp/Down: Speed Control\nR: Reset\nEscape: Exit", 
                  align="left", font=("Arial", 12, "normal"))

# Add time display
time_display = turtle.Turtle()
time_display.hideturtle()
time_display.penup()
time_display.color("white")
time_display.goto(300, 350)

# Add planet counter display
counter_display = turtle.Turtle()
counter_display.hideturtle()
counter_display.penup()
counter_display.color("white")
counter_display.goto(300, 320)

frame_count = 0
simulation_time = 0

print("Simulation started! Press 'Space' to pause/resume, 'Up/Down' to control speed, 'R' to reset, 'Escape' to exit.")

# INFINITE LOOP
try:
    while True:
        if running:
            screen.update()
            frame_count += 1
            simulation_time += time_scale
            
            # Move planets
            for planet in planets:
                planet.move()
                planet.angle += planet.speed * time_scale
            
            # Move moons
            for moon_obj in moons:
                moon_obj.move()
                moon_obj.angle += moon_obj.speed * time_scale * 5
            
            # ============ MOVE ASTEROIDS ============
            for asteroid in asteroids:
                x = sun.xcor() + asteroid.radius * math.cos(asteroid.angle)
                y = sun.ycor() + asteroid.radius * math.sin(asteroid.angle)
                asteroid.goto(x, y)
                asteroid.angle += asteroid.speed * time_scale
            # ============ END ASTEROID MOVEMENT ============
            
            # Update displays every 30 frames
            if frame_count % 30 == 0:
                time_display.clear()
                counter_display.clear()
                
                earth_years = simulation_time / (2 * math.pi)
                time_display.write(f"Time: {earth_years:.1f} Earth Years", 
                                  align="center", font=("Arial", 12, "normal"))
                
                orbits_text = "Orbits Completed:\n"
                for planet in planets:
                    orbits = planet.angle / (2 * math.pi)
                    orbits_text += f"{planet.name[:3]}: {orbits:.1f}\n"
                counter_display.write(orbits_text, align="left", font=("Arial", 10, "normal"))
            
            time.sleep(0.001)
        else:
            screen.update()
            time.sleep(0.1)

except turtle.Terminator:
    print("Simulation ended.")
except KeyboardInterrupt:
    print("\nSimulation stopped by user.")
finally:
    turtle.bye()
    print("Goodbye!")
