from turtle import*
width(4)
ht()
bgcolor('misty rose')
#основа фотоапарату
pencolor('gray')
up()
goto(-95,-5)
fillcolor('gray')
begin_fill()
down()
goto(-95,195)
goto(305,195)
goto(305,-5)
goto(-95,-5)
end_fill()
up()

pencolor('plum')
up()
goto(-100,0)
fillcolor('thistle')
begin_fill()
down()
goto(-100,200)
goto(300,200)
goto(300,0)
goto(-100,0)
end_fill()
up()

pencolor('plum')
up()
goto(-85,200)
fillcolor('thistle')
begin_fill()
down()
goto(-85,230)
goto(-30,230)
goto(-30,200)
goto(-85,200)
end_fill()
up()


#об'єктив
color('gray')
goto(100,20)
down()
fillcolor('dark gray')
begin_fill()
circle(80)
end_fill()
up()

width(2)
speed(1000)
color('gray')
circle(38)
goto(100,100)
down()
for i in range(25):
    circle(38)
    right(15)
up()


#вспишка


pencolor('black')
goto(230,160)
down()
fillcolor('white')
begin_fill()
goto(230,190)
goto(290,190)
goto(290,160)
goto(230,160)
end_fill()
up()


color('black')
up()
goto(-100,-50)
down()
write('Малова Валерія <3<3<3',font=('Times New Roman',14,'italic'))

