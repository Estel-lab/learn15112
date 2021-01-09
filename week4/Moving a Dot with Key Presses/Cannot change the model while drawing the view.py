from cmu_112_graphics import *


def appStarted(app):
    app.x = 0


def redrawAll(app, canvas):
    canvas.create_text(app.width / 2, 20, text='This has an MVC Violation!')

    app.x = 10  # This is an MVC Violation!
    # We cannot change the model from the view (redrawAll)


runApp(width=400, height=400)