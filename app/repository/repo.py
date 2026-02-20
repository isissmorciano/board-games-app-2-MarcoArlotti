from app.db import get_db

def salva_gioco(nome, n_player_max, durata, categoria):
    db = get_db()
    db.execute(
        'INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES (?, ?, ?, ?)',
        (nome, n_player_max, durata, categoria)
    )
    db.commit()