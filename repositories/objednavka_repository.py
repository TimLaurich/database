from repositories.base_repository import BaseRepository

class ObjednavkaRepository(BaseRepository):

    def create(self, zakaznik_id):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO objednavka (zakaznik_id) VALUES (%s)",
            (zakaznik_id,)
        )
        return cur.lastrowid
