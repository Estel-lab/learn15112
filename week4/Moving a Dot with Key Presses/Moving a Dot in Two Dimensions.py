# This version moves in both x and y dimensions.

from cmu_112_graphics import *


def appStarted(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.r = 40


def keyPressed(app, event):
    if (event.key == 'Left'): app.cx -= 10
    elif (event.key == 'Right'): app.cx += 10
    elif (event.key == 'Up'): app.cy -= 10
    elif (event.key == 'Down'): app.cy += 10


def redrawAll(app, canvas):
    canvas.create_text(app.width / 2,
                       20,
                       text='Move dot with up, down, left, and right arrows')
    canvas.create_oval(app.cx - app.r,
                       app.cy - app.r,
                       app.cx + app.r,
                       app.cy + app.r,
                       fill='darkGreen')


runApp(width=400, height=400)