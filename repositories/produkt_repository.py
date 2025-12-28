from repositories.base_repository import BaseRepository

class ProduktRepository(BaseRepository):

    def get(self, produkt_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM produkt WHERE id=%s", (produkt_id,))
        return cur.fetchone()
