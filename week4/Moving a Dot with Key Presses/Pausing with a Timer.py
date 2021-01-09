from cmu_112_graphics import *


def appStarted(app):
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.r = 40
    app.paused = False


def timerFired(app):
    if (not app.paused):
        doStep(app)


def doStep(app):
    app.cx -= 10
    if (app.cx + app.r <= 0):
        app.cx = app.width + app.r


def keyPressed(app, event):
    if (event.key == 'p'):
        app.paused = not app.paused
    elif (event.key == 's') and app.paused:
        doStep(app)


def redrawAll(app, canvas):
    canvas.create_text(app.width / 2, 20, text='Watch the dot move!')
    canvas.create_text(app.width / 2, 40, text='Press p to pause or unpause')
    canvas.create_text(app.width / 2, 60, text='Press s to step while paused')
    canvas.create_oval(app.cx - app.r,
                       app.cy - app.r,
                       app.cx + app.r,
                       app.cy + app.r,
                       fill='darkGreen')


runApp(width=400, height=400)