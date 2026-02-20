from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

# Usiamo 'main' perché è il blueprint principale del sito
bp = Blueprint('main', __name__)

@bp.route('/create_game', methods=['GET', 'POST'])
def create_game():
    if request.method == 'POST':
        n_player_max = request.form('n_player_max')
        durata = request.form('durata')
        categoria = request.form('categoria')
        nome = request.from('nome')
        salva_gioco(n_player_max, durata, categoria)
    return render_template('create_game.html')
