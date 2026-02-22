from app.db import get_db

def salva_gioco(nome, numero_giocatori_massimo, durata_media, categoria):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO giochi (nome, numero_giocatori_massimo, durata_media, categoria) VALUES (?, ?, ?, ?)",
            (nome, numero_giocatori_massimo, durata_media, categoria),
        )
        db.commit() # Salviamo le modifiche
        return True
    except db.IntegrityError:

        return False
    
def prendi_giochi():
    db = get_db()
    query = """
    SELECT *
    FROM giochi;
    """

    giochi = db.execute(query).fetchall()
    return [dict(gioco) for gioco in giochi]