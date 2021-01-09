#################################################
# hw4.py
#
# Your name:
# Your andrew id:
#################################################

import cs112_f20_week4_linter
from cmu_112_graphics import *


def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 5
    app.section = (-1, -1)


def mousePressed(app, event):
    pass


def keyPressed(app, event):
    app.keyPressed = {event.key}


def explosionIntersectsDot(app):
    pass


def moveDot(app):
    pass


def growExplosion(app):
    pass


def timerFired(app):
    pass


def doStep(app):
    pass


def drawTitleAndScore(app, canvas):
    pass


def drawGrid(app, canvas):
    pass


def drawDot(app, canvas):
    pass


def drawExplosion(app, canvas):
    pass


def redrawAll(app, canvas):
    drawTitleAndScore(app, canvas)
    drawGrid(app, canvas)
    drawDot(app, canvas)
    drawExplosion(app, canvas)


def main():
    cs112_f20_week4_linter.lint()
    runApp(width=510, height=540)


if __name__ == '__main__':
    main()