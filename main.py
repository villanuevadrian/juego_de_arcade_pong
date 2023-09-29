import turtle

import turtle

# Configuración de la ventana
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)

paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("white")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

# Paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("blue")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(10)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.15
pelota.dy = -0.15

# Funciones para mover las paletas
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    y += 20
    paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    y -= 20
    paleta_izquierda.sety(y)

def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    y += 20
    paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    y -= 20
    paleta_derecha.sety(y)

# Teclado
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")

# Bucle principal del juego
while True:
    ventana.update()

    # Mover la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Revisar colisiones con los bordes
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1

    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1

    # Revisar colisiones con las paletas
    if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_derecha.ycor() + 50 and pelota.ycor() > paleta_derecha.ycor() - 50):
        pelota.setx(340)
        pelota.dx *= -1

    if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_izquierda.ycor() + 50 and pelota.ycor() > paleta_izquierda.ycor() - 50):
        pelota.setx(-340)
        pelota.dx *= -1
