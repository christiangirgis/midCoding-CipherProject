import turtle as t
t.speed(5000)
t.pensize(10)
t.fillcolor('yellow')
t.hideturtle()
t.bgcolor('blue')

radius=180
t.penup()
t.setposition(0,-radius)
t.setheading(0)
t.pendown()
t.begin_fill()
t.circle(radius)
t.end_fill()

mouth_radius=radius*0.6
mouth_angle=100
t.penup()
t.setposition(0, -mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius,mouth_angle)
t.penup()
t.setposition(0,-mouth_radius)
t.setheading(0)
t.pendown()
t.circle(mouth_radius,-mouth_angle)

x=50
y=50
eye_size=60
t.penup()
t.setposition(x,y)

t.pendown()
t.dot(eye_size)
t.penup()
t.setposition(-x,y)
t.dot(eye_size)

def tri(left,top):
    t.color("black")
    
    t.pensize(2)
    t.penup()
    t.setposition(left,top)
    t.pendown()
    t.begin_fill()
    for i in range (3):
        t.left(120)
        t.forward(10)
        t.forward(10)
    t.end_fill()


tri(-110,145)
tri(-140,125)
tri(-80,165)
tri(-40,176)
tri(-2,180)
tri(40,175)
tri(70,160)
tri(100,145)


size = 100
t.color("red")
t.width("2")

angle = 120
t.begin_fill()
t.fillcolor("black")
t.penup()
t.goto(350,400)
t.pendown()

for size in  range(5):
    t.speed(5)
    t.forward(100)
    t.right(144)

t.end_fill()

#t.hideturtle()

t.done()
    