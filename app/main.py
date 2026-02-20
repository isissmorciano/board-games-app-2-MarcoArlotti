from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.repository.repo import salva_gioco
# from app.repository.repo import salva_gioco

bp = Blueprint('main', __name__)

@bp.route('/create_game', methods=['GET', 'POST'])
def create_game():
    if request.method == 'GET':
        return render_template('create_game.html')
    if request.method == 'POST':
        nome = request.form['nome']
        n_max_player = request.form['n_max_player']
        durata = request.form['durata']
        categoria = request.form['categoria']

        salva_gioco(nome, n_max_player, durata, categoria)

        return render_template('create_game.html')