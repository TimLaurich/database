from repositories.base_repository import BaseRepository

class SkladRepository(BaseRepository):

    def get(self, produkt_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM sklad WHERE produkt_id=%s", (produkt_id,))
        return cur.fetchone()

    def update(self, produkt_id, nove_mnozstvi):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE sklad SET mnozstvi=%s WHERE produkt_id=%s",
            (nove_mnozstvi, produkt_id)
        )
        self.conn.commit()
