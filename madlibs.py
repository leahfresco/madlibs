"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

VERBY = ['run', 'walk', 'play', 'sleep', 'kick', 'jump', 'climb']


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """reroute to game pages."""
    response = request.args.get("game")
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    nouns = ["car", "apples", "mailman", "football", "water", "box"]
    adjectives = ["beautiful", "soupy", "delicious", "strong", "shiny"]
    if response == "yes":
        return render_template("game.html", color=colors, noun=nouns, adjective=adjectives)
    else:
        return render_template("goodbye.html", noun=nouns)


@app.route('/check')
def check_data():
    """checking output data."""
    nouns = request.args.getlist("noun")
    print nouns
    return render_template("check.html", noun=nouns)

@app.route('/madlib')
def show_madlib():
    """Greet user with compliment."""

    mad = choice(["madlib.html", "madlib2.html"])
    color = request.args.get("color")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    nouns = request.args.getlist("noun")
    verb = choice(VERBY)
    noun2 = choice(request.args.getlist("noun"))

    random_noun = ", and ".join(nouns)
    return render_template(mad,
                           person=person,
                           color=color,
                           adjective=adjective,
                           noun=nouns,
                           verb=verb,
                           noun2=noun2)
if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
