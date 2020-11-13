import turtle
import time
wn = turtle.Screen()
red = "#ff0000"   #צבעים
grey = "#808080"
green = "#00ff00"
yellow = "#ffff00"

turtle.width(4) #רמזור
turtle.fillcolor('#000000')
turtle.begin_fill()
turtle.up()
turtle.goto(-25, -50)
turtle.down()
turtle.goto(-25, 50)
turtle.goto(25, 50)
turtle.goto(25, -50)
turtle.goto(-25, -50)
turtle.end_fill()
turtle.ht()

red_light = turtle.Turtle() #אדום
red_light.color(grey)
red_light.shape("circle")
red_light.up()
red_light.setposition(0, 30)

yellow_light = turtle.Turtle() #צהוב
yellow_light.color(grey)
yellow_light.shape("circle")
yellow_light.up()
yellow_light.setposition(0, 0)

green_light = turtle.Turtle() #ירוק
green_light.color(grey)
green_light.shape("circle")
green_light.up()
green_light.setposition(0, -30)

while True: #שינוי צבע
	green_light.color(grey)
	red_light.color(red)
	time.sleep(1)
	red_light.color(grey)
	yellow_light.color(yellow)
	time.sleep(1)
	yellow_light.color(grey)
	green_light.color(green)
	time.sleep(1)

turtle.mainloop()