# This version bounds the dot to remain entirely on the canvas

from cmu_112_graphics import *


def appStarted(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.r = 40


def keyPressed(app, event):
    if (event.key == 'Left'):
        app.cx -= 10
        if (app.cx - app.r < 0):
            app.cx = app.r
    elif (event.key == 'Right'):
        app.cx += 10
        if (app.cx + app.r > app.width):
            app.cx = app.width - app.r


def redrawAll(app, canvas):
    canvas.create_text(app.width / 2,
                       20,
                       text='Move dot with left and right arrows')
    canvas.create_text(app.width / 2,
                       40,
                       text='See how it is bounded by the canvas edges')
    canvas.create_oval(app.cx - app.r,
                       app.cy - app.r,
                       app.cx + app.r,
                       app.cy + app.r,
                       fill='darkGreen')


runApp(width=400, height=400)