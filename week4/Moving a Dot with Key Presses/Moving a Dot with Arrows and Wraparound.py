# This version wraps around, so leaving one side enters the opposite side

from cmu_112_graphics import *


def appStarted(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.r = 40


def keyPressed(app, event):
    if (event.key == 'Left'):
        app.cx -= 10
        if (app.cx + app.r <= 0):
            app.cx = app.width + app.r
    elif (event.key == 'Right'):
        app.cx += 10
        if (app.cx - app.r >= app.width):
            app.cx = 0 - app.r


def redrawAll(app, canvas):
    canvas.create_text(app.width / 2,
                       20,
                       text='Move dot with left and right arrows')
    canvas.create_text(app.width / 2,
                       40,
                       text='See how it uses wraparound on the edges')
    canvas.create_oval(app.cx - app.r,
                       app.cy - app.r,
                       app.cx + app.r,
                       app.cy + app.r,
                       fill='darkGreen')


runApp(width=400, height=400)