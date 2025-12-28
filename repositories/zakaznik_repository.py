from repositories.base_repository import BaseRepository

class ZakaznikRepository(BaseRepository):

    def create(self, jmeno, email, kredit):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO zakaznik (jmeno, email, kredit) VALUES (%s,%s,%s)",
            (jmeno, email, kredit)
        )
        self.conn.commit()
        return cur.lastrowid

    def get(self, zakaznik_id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM zakaznik WHERE id=%s", (zakaznik_id,))
        return cur.fetchone()

    def update_kredit(self, zakaznik_id, novy_kredit):
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE zakaznik SET kredit=%s WHERE id=%s",
            (novy_kredit, zakaznik_id)
        )
        self.conn.commit()
