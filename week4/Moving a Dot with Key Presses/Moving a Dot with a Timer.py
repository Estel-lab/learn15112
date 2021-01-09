from cmu_112_graphics import *


def appStarted(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.r = 40


def timerFired(app):
    app.cx -= 10
    if (app.cx + app.r <= 0):
        app.cx = app.width + app.r


def redrawAll(app, canvas):
    canvas.create_text(app.width / 2, 20, text='Watch the dot move!')
    canvas.create_oval(app.cx - app.r,
                       app.cy - app.r,
                       app.cx + app.r,
                       app.cy + app.r,
                       fill='darkGreen')


runApp(width=400, height=400)