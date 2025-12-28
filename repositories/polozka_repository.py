from repositories.base_repository import BaseRepository

class PolozkaRepository(BaseRepository):

    def add(self, objednavka_id, produkt_id, mnozstvi):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO polozka (objednavka_id, produkt_id, mnozstvi) VALUES (%s,%s,%s)",
            (objednavka_id, produkt_id, mnozstvi)
        )
