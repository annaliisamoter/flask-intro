"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<br><a href='http://localhost:5000/hello'>Hello</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <br>
             <label>Choose a diss!</label>
             <br>
             <select name="diss">
              <option name ="diss" value="boring">boooooring
              <option name ="diss" value="smelly">smelly
              <option name ="diss" value="lame">laaaaame
              </select>
            <br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/diss')
def say_diss():
    """Insults the user. Great idea"""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return """
      <!doctype html>
      <html>
        <head>
          <title>An Insult. I bite my thumb at thee.</title>
        </head>
        <body>
          Hi, {player}! I think you're {diss}!
        </body>
      </html>
      """.format(player=player, diss=diss)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
