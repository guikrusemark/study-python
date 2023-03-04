from flask import Flask, render_template, request, redirect
from werkzeug import Response

from src.game import Game

app: Flask = Flask(__name__)

games: list = [
    Game('Super Mario Bros', 'Platformer', 'A plumber rescues a princess.', 5),
    Game('God of War', 'Action-Adventure', 'A Spartan warrior slays gods.', 9),
    Game('The Last of Us', 'Survival Horror', 'A post-apocalyptic survival game.', 9),
    Game('Batman Arkham Asylum', 'Action-Adventure', 'A dark and gritty Batman game.', 8),
    Game('The Elder Scrolls V: Skyrim', 'Action-Adventure', 'A fantasy open world game.', 9)
]


@app.route('/')
def index() -> str:
    games.sort(key=lambda game: game.name)
    return render_template('index.html', title='Meus jogos', games=games)


@app.route('/add-game')
def add_game() -> str:
    return render_template('add_game.html', title='Add game', games=games)


@app.route('/save-game', methods=['POST'])
def save_game() -> Response:
    name = request.form['name']
    category = request.form['category']
    description = request.form['description']

    game = Game(name, category, description)
    games.append(game)
    return redirect('/')


@app.route('/remove-game')
def remove_game() -> str:
    return render_template('remove_game.html', title='Remove game', games=games)


@app.route('/delete-game', methods=['POST'])
def delete_game() -> Response:
    index = request.form['index']
    if index.isnumeric():
        i = int(index) - 1
        if 0 <= i < len(games):
            del games[i]
    return redirect('/')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
