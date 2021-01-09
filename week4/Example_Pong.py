# 112_pong.py

# This is a simplified version of Pong, one of the earliest
# arcade games.  We have kept it simple for learning purposes.

from cmu_112_graphics import *


def appStarted(app):
    # This is a Controller
    app.waitingForKeyPress = True
    resetApp(app)


def resetApp(app):
    # This is a helper function for Controllers
    # This initializes most of our model (stored in app.xyz)
    # This is called when they start the app, and also after
    # the game is over when we restart the app.
    app.timerDelay = 50  # milliseconds
    app.dotsLeft = 2
    app.score = 0
    app.paddleX0 = 20
    app.paddleX1 = 40
    app.paddleY0 = 20
    app.paddleY1 = 80
    app.margin = 5
    app.paddleSpeed = 10
    app.dotR = 15
    app.gameOver = False
    app.paused = False
    resetDot(app)


def resetDot(app):
    # This is a helper function for Controllers
    # Get the dot ready for the next round.  Move the dot to
    # the center of the screen and give it an initial velocity.
    app.dotCx = app.width // 2
    app.dotCy = app.height // 2
    app.dotDx = -10
    app.dotDy = -3


def movePaddleDown(app):
    # This is a helper function for Controllers
    # Move the paddle down while keeping it inside the play area
    dy = min(app.paddleSpeed, app.height - app.margin - app.paddleY1)
    app.paddleY0 += dy
    app.paddleY1 += dy


def movePaddleUp(app):
    # This is a helper function for Controllers
    # Move the paddle up while keeping it inside the play area
    dy = min(app.paddleSpeed, app.paddleY0 - app.margin)
    app.paddleY0 -= dy
    app.paddleY1 -= dy


def keyPressed(app, event):
    # This is a Controller
    if app.gameOver:
        resetApp(app)
    elif app.waitingForKeyPress:
        app.waitingForKeyPress = False
        app.dotsLeft -= 1
    elif (event.key == 'Down'):
        movePaddleDown(app)
    elif (event.key == 'Up'):
        movePaddleUp(app)
    elif (event.key == 'p'):
        app.paused = not app.paused
    elif (event.key == 's') and app.paused:
        doStep(app)


def timerFired(app):
    # This is a Controller
    if (not app.paused):
        doStep(app)


def doStep(app):
    # This is a helper function for Controllers
    # The dot should move only when we are not waiting for
    # a key press or in the game-over state
    if not app.waitingForKeyPress and not app.gameOver:
        moveDot(app)


def dotWentOffLeftSide(app):
    # This is a helper function for Controllers
    # Called when the dot went off the left side of the screen,
    # so the round is over.  If there are no dots left, then
    # the game is over.
    if app.dotsLeft == 0:
        app.gameOver = True
    else:
        app.waitingForKeyPress = True
        resetDot(app)


def dotIntersectsPaddle(app):
    # This is a helper function for Controllers
    # Check if the dot intersects the paddle.  To keep this
    # simple here, we will only test that the center of the dot
    # is inside the paddle.  We could be more precise here
    # (that's an interesting exercise!).
    return ((app.paddleX0 <= app.dotCx <= app.paddleX1)
            and (app.paddleY0 <= app.dotCy <= app.paddleY1))


def moveDot(app):
    # This is a helper function for Controllers
    # Move the dot by the current velocity (dotDx and dotDy).
    # Then handle all the special cases:
    #  * bounce the dot if it went off the top, right, or bottom
    #  * bounce the dot if it went off the paddle
    #  * lose the round (or the game) if it went off the left side
    app.dotCx += app.dotDx
    app.dotCy += app.dotDy
    if (app.dotCy + app.dotR >= app.height):
        # The dot went off the bottom!
        app.dotCy = app.height - app.dotR
        app.dotDy = -app.dotDy
    elif (app.dotCy - app.dotR <= 0):
        # The dot went off the top!
        app.dotCy = app.dotR
        app.dotDy = -app.dotDy
    if (app.dotCx + app.dotR >= app.width):
        # The dot went off the right!
        app.dotCx = app.width - app.dotR
        app.dotDx = -app.dotDx
    elif dotIntersectsPaddle(app):
        # The dot hit the paddle!
        app.score += 1  # hurray!
        app.dotDx = -app.dotDx
        app.dotCx = app.paddleX1
        dToMiddleY = app.dotCy - (app.paddleY0 + app.paddleY1) / 2
        dampeningFactor = 3  # smaller = more extreme bounces
        app.dotDy = dToMiddleY / dampeningFactor
    elif (app.dotCx - app.dotR <= 0):
        # The dot went off the left side
        dotWentOffLeftSide(app)


def drawAppInfo(app, canvas):
    # This is a helper function for the View
    # This draws the title, the score, and the dots left
    font = 'Arial 18 bold'
    title = '112 Pong!'
    canvas.create_text(app.width / 2, 20, text=title, font=font)
    canvas.create_text(app.width - 70,
                       20,
                       text=f'Score: {app.score}',
                       font=font)
    canvas.create_text(app.width - 70,
                       app.height - 20,
                       text=f'Dots Left: {app.dotsLeft}',
                       font=font)


def drawPaddle(app, canvas):
    # This is a helper function for the View
    canvas.create_rectangle(app.paddleX0,
                            app.paddleY0,
                            app.paddleX1,
                            app.paddleY1,
                            fill='black')


def drawDot(app, canvas):
    # This is a helper function for the View
    cx, cy, r = app.dotCx, app.dotCy, app.dotR
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill='black')


def drawGameOver(app, canvas):
    # This is a helper function for the View
    canvas.create_text(app.width / 2,
                       app.height / 2,
                       text='Game Over!',
                       font='Arial 18 bold')
    canvas.create_text(app.width / 2,
                       app.height / 2 + 50,
                       text='Press any key to restart',
                       font='Arial 16 bold')


def drawPressAnyKey(app, canvas):
    # This is a helper function for the View
    canvas.create_text(app.width / 2,
                       app.height / 2,
                       text='Press any key to start!',
                       font='Arial 18 bold')


def redrawAll(app, canvas):
    # This is the View
    drawAppInfo(app, canvas)
    drawPaddle(app, canvas)
    if app.gameOver:
        drawGameOver(app, canvas)
    elif app.waitingForKeyPress:
        drawPressAnyKey(app, canvas)
    else:
        drawDot(app, canvas)


def main():
    # This runs the app
    runApp(width=400, height=300)


if __name__ == '__main__':
    main()